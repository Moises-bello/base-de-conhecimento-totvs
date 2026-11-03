---
content_hash: d967b29338168c58b7428ecbffea1965f3ca605e9ee232e82fa6c209e3de2dbb
fetched_at: '2026-06-29T00:10:42.894507+00:00'
page_id: '547872816'
product: rm
source: tdn-rm
title: DEDUMOBILE 2989 - Ao acessar o gráfico de enquetes é apresentado erro de time
  out
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547872816
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Educacional |
| Segmento: | Totvs Gestão Educacional |
| Módulo: | Central de comunicação |
| Função: | Gestão de Mensagens |
| Ticket: | 8536454 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2989](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2989) |

## **02. SITUAÇÃO/REQUISITO**

A acessar um gráfico de enquete na Central de Comunicações > eduCONNECT> Gestão de mensagem > anexo> gráfico é apresentado o seguinte erro:Execution Timeout Expired. The timeout period elapsed prior to completion of the operation or the server is not responding. [InternalServerError].

## **03. SOLUÇÃO**

Otimizado a performance no gráfico de enquetes, anexo de mensagem individual e painel de utilização de usuários, pois caso a API do eduCONNECT esteja com processamento ocupado serão realizadas novas tentativas de conexão.
