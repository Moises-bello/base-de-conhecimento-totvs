---
content_hash: d130065e9acf64385037963fd6f5318ba6c486fb6ab992128ff9c539367a2164
fetched_at: '2026-06-29T00:06:12.000872+00:00'
page_id: '204967088'
product: rm
source: tdn-rm
title: ER_PCREQ-7858_Conversão de perfis de tela Delphi x .NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=204967088
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Folha de Pagamento | **Módulo** | Conversão de perfis de tela (Delphi x .NET) |
| **Segmento Executor** |  | | |
| **Projeto1** | PDR\_RH\_FOP007 | **IRM1** | PCREQ-7828 |
| **Requisito1** | PCREQ-7858 | **Subtarefa1** | PDR\_RH\_FOP128-129 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 

Converter os perfis de tela gravados na versão delphi para o formato da versão .net.

O conversor estará disponível para os perfis: RAIS, DIRF, Lançamentos Financeiros e Geração de Encargos.

## Definição da Regra de Negócio

 

**Mapeamento dos campos**:

DIRF:

RAIS:

**Acesso**:

Para acessar o conversor de perfil de tela, o usuário deve acessar o menu que se encontra no seguinte caminho:

Folha de Pagamento -> Configurações -> Conversão -> Conversão de perfis (Delphi x .NET)

**Roteiro de uso**:

Na tela do processo o usuário deve informar o processo de onde ele deseja converter os perfis. Após informar o processo, devem ser selecionados os perfis que serão convertidos.

Após a execução do processo é exibida uma tela com os arquivos de log gerados durante a conversão, o novo perfil é gravado com o sufixo \_convertido no nome

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
