---
content_hash: 8d907318ad74e2b7bd8857dc7b2b4ff0a57899cfaf741a4e8e4e484460e550c0
fetched_at: '2026-07-02T19:24:22.199607+00:00'
page_id: '269060362'
product: protheus
source: tdn-tec
title: Alteração do comportamento do método IsConnected.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269060362
version: 2
---

O comportamento do método IsConnected da classe tSocketConnClass retornada pela função GetTCPObj.

|  |  |
| --- | --- |
| Situação | Quando o método IsConnected era chamado após o encerramento (close) do socket era gerado um erro no Aplication Server. |
| Ocorrência | Erro no Aplication Server após a execução do método IsConnected. |
| Correção | Quando o método IsConnected é chamado será exibido uma mensagem de warning e retornado falso (.F.). |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - 1.0.9 |
