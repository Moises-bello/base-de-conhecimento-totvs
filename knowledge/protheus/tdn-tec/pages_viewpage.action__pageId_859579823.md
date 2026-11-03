---
content_hash: 56844e7ab40e6e226468162e15accfcadf93c1d6e92ec6c78fc0303087ebdb85
fetched_at: '2026-07-02T19:24:28.819363+00:00'
page_id: '859579823'
product: protheus
source: tdn-tec
title: Correção - Scroll to zoom twebengine
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859579823
version: 1
---

|  |  |
| --- | --- |
| Situação | Control + Scroll do mouse não ajusta o zoom do TWebEngine |
| Ocorrência | Situação percebida na versão 20.3.2.0 ou superior, não estava implementado no CEF |
| Correção | Implementando suporte a Control + scroll e Control + (mais/menos) para mudar o zoom dentro do TWebEngine |
| Informações adicionais | * Referente ao chamado: [#20233440](https://totvssuporte.zendesk.com/agent/tickets/20233440 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4817 * Disponível em builds iguais ou superiores a 20.3.2.8 |
