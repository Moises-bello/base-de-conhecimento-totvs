---
content_hash: 4085d3f939e06fd3c3292c59a09627942b29f955647893100e2d96d15ca73a5d
fetched_at: '2026-06-29T00:11:46.493690+00:00'
page_id: '822687841'
product: rm
source: tdn-rm
title: serv/atvEvento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687841
version: 8
---

## 1. Visão Geral

Esta rotina visa permitir a identificação detalhada de atividades de eventos (artísticos, culturais, esportivos, etc.) dentro do processo de emissão da NFS-e. Foi criado um novo grupo de tags (`atvEvento`) que permite identificar o evento por um código único (ID) ou pelo detalhamento do endereço (nacional ou exterior).

## 2. Estrutura Hierárquica (Schema)

Abaixo está a representação da árvore de dados do grupo `atvEvento`. Note que a tag `xCidade` é exclusiva do grupo de endereço no exterior (`endExt`).

infNFSe  
 └── DPS  
      └── infDPS  
           └── serv  
                └── atvEvento (Grupo Raiz)  
                     ├── xNome (Nome do evento)  
                     ├── dtIni (Data Início)  
                     ├── dtFim (Data Fim)  
                     ├── idAtvEv (ID do Evento - Excludente com 'end')  
                     └── end (Grupo Endereço)  
                          ├── CEP (CEP Nacional - Excludente com 'endExt')  
                          ├── endExt (Grupo Endereço Exterior)  
                          │    ├── cEndPost (Código Postal Exterior)  
                          │    ├── xCidade  (Cidade no Exterior)  
                          │    └── xEstProvReg (Estado/Província Exterior)  
                          ├── xLgr (Logradouro)  
                          ├── nro (Número)  
                          ├── xCpl (Complemento)  
                          └── xBairro (Bairro)

## 3. Dicionário de Dados

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| xNome | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/ | Sim |  | Nome do evento Artístico, Cultural, Esportivo. |
| dtIni | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/ | Sim |  | Data de início da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD) |
| dtFim | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/ | Sim |  | Data de fim da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD) |
| idAtvEv | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/ | Sim |  | Identificação da Atividade de Evento  (código identificador de evento determinado pela Administração Tributária Municipal) |
| end | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/ | Sim |  | Grupo de informações do endereço da atividade de evento. |

## 4. Regras de Validação e Negócio

Para garantir a integridade dos dados, as seguintes regras devem ser aplicadas pelo sistema:

1. **Exclusão Mútua de Identificação vs. Endereço:**

   * **Regra:** Se o campo `idAtvEv` for preenchido, o grupo `end` (e todos os seus filhos) **NÃO** deve ser informado.
   * *Lógica:* Ou o evento é identificado pelo código pré-cadastrado, ou descreve-se o local.
2. **Exclusão Mútua de Endereço Nacional vs. Exterior:**

   * **Regra:** Se o campo `CEP` for informado, o grupo `endExt` **NÃO** deve ser informado.
   * *Lógica:* O `CEP` denota endereço no Brasil. `endExt` denota endereço fora do Brasil.
3. **Localização do Campo Cidade:**

   * Para endereços nacionais (`CEP` informado), o nome da cidade **não** é enviado explicitamente no XML (deduzido pelo sistema via CEP/Município de incidência).
   * O campo `xCidade` deve ser enviado **apenas** quando se tratar de endereço no exterior (dentro de `endExt`).

## 5. Estrutura do grupo endereço:
