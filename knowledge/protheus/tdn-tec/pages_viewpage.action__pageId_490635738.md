---
content_hash: d2d28879605daf7bb5d5c023f05c640451b3541b27776cddde1bdcca168be8ba
fetched_at: '2026-07-02T19:24:24.849890+00:00'
page_id: '490635738'
product: protheus
source: tdn-tec
title: Errorlog quando pressionado PageDown várias vezes no componente TGrid
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490635738
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao manter pressionado o botão do teclado Page Down, após alguns instantes era apresentado erro no WebApp, encerrando a conexão. |
| Correção | Implementação de controle de tempo para o evento (keyCode) PAGEDOWN. |
| Informações adicionais | * Referente ao chamado:  Não há chamado associado * Referente à ocorrência: SCHTML-920 * Disponível a partir da build 7.00.131227A - 4.3.0 |
