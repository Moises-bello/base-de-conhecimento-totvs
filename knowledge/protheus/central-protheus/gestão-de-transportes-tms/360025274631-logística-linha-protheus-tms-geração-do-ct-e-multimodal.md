---
article_id: 360025274631
category: Gestão de Transportes (TMS)
content_hash: 51fdd2e6ec047130f44b3dfea73d0b26cd4e9af04898b203bc4e83ddd7216ddd
fetched_at: '2026-06-28T22:45:29.237879+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Geração do CT-e Multimodal
type: support-article
updated_at: '2025-03-20T19:55:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025274631-Log%C3%ADstica-Linha-Protheus-TMS-Gera%C3%A7%C3%A3o-do-CT-e-Multimodal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16872972829719)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais os procedimentos para geração do **CTe - Conhecimento de Transporte Eletrônico** Multimodal?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**O CTe multimodal é um documento fiscal eletrônico obrigatório para cobrir operações de transporte que utilizam mais de um tipo de transporte.  
  
Para emiti-lo, a transportadora deve ser credenciada como **OTM** - **Operadora de Transporte Multimodal** pela **ANTT - Agência Nacional de Transportes Terrestres**. O **CT-e** Multimodal não substitui os **CTes** de cada modal envolvido, sendo necessário emitir um **CTe** específico para cada etapa do transporte. Esses documentos são chamados de **CTe** vinculados ao multimodal e podem ser emitidos pela mesma transportadora ou empresas contratadas.  
  
Para emissão do **CT-e** Multimodal, efetuar os procedimentos abaixo:

1. Criação de campos no arquivo**SX3,** através do **SIGACFG - Configurador,** tabela**DTC:**  
     

   |  |  |
   | --- | --- |
   | **Campo** | DTC\_INDNEG |
   | **Tipo** | Carácter |
   | **Tamanho** | 1 |
   | **Decimal** | 0 |
   | **Formato** | @! |
   | **Título** | Ind. Negocia |
   | **Descrição** | Indicador Negociável |
   | **Nível** |  |
   | **Usado** | Sim |
   | **Obrigatório** | Não |
   | ***Browse*** |  |
   | **Opções** | 0=Não Negociável;1=Negociável |
   | ***When*** |  |
   | **Relação** |  |
   | **Val. Sistema** |  |
   | **Help** | Indicador Negociável Preencher com: 0 - Não Negociável; 1 - Negociável; Este campo é utilizado para o modal igual a Multimodal. |
2. Criação e configuração de parâmetro no arquivo **SX6 – Parâmetros:**  
     

   |  |  |
   | --- | --- |
   | **Nome da Variável** | MV\_TMSCOTM |
   | **Tipo** | Carácter |
   | **Descrição** | Número do Certificado do Operador de Transporte Multimodal |
   | **Valor Padrão** |  |

     
   Após a criação do parâmetro em questão, configurar ele informando o número do **OTM - Operador de Transporte Multimodal**.

Exemplo de utilização:

1. Em **Gestão de Transportes** - **SIGATMS**, acessar **Atualizações**/**Recebimento**/**Entrada Documentos** - **TMSA050.**O Sistema apresentará a tela de Entrada de Nota Fiscal do Cliente;
2. No campo **Tipo de Transporte** - **DTC\_TIPTRA**, informar a opção **6** -**Multimodal**;
3. No campo **Indicador Negociável** - **DTC\_INDNEG**, informar a opção desejada conforme a regra de negócio do cliente;
4. Calcule o **CT-e** e realize a transmissão.
5. Imprima a **DACTE - Documento Auxiliar do Conhecimento de Transporte Eletrônico**.

**Saiba mais**Consultoria de segmentos - CT-e Multimodal: [MG - CT-e Multimodal](https://tdn.totvs.com.br/display/public/ConSeg/MG+-+CT-e+Multimodal)  
Documentação para emissão de CTe vinculado a multimodal: [Entrada Documentos de Clientes – DT CTe Vinculado a Multimodal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=593970923)
