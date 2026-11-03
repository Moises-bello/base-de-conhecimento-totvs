---
content_hash: 03864befbcfd61485b8e50b9775c8cc68a3725f2838370ae2cca2e4649094ed8
fetched_at: '2026-06-29T00:10:30.314149+00:00'
page_id: '519718934'
product: rm
source: tdn-rm
title: DEDUMOBILE-2353 DT Não é disparado o push das mensagens trocadas entre professores
  e alunos pelo aplicativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519718934
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS eduCONNECT |
| Função: | Recebimento de *Push* das mensagens pessoais |
| Ticket: | [6649831](https://totvssuporte.zendesk.com/agent/tickets/6649831 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2353](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2353) |

## **02. SITUAÇÃO/REQUISITO**

Não é disparado o *Push* das mensagens trocadas entre professores e alunos pelo aplicativo.

## **03. SOLUÇÃO**

Otimizado a rotina de envio de Push de notificação para mensagens pessoais, pois o sistema estava carregando o contexto incorreto ao buscar a parametrização de conexão com eduCONNECT para enviar as notificações de Push ao salvar uma mensagem pessoal.
