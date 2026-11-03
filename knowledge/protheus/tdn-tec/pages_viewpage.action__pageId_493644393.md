---
content_hash: 9d3dfcb655b97efb698e59eec26f70d60b33aa82a06550b63186d0feaea16ff9
fetched_at: '2026-07-02T19:24:24.987691+00:00'
page_id: '493644393'
product: protheus
source: tdn-tec
title: Correção - Alguns links não abrem no TWebEngine
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493644393
version: 1
---

Links que deveriam ser abertos em uma nova janela agora são abertos corretamente.

|  |  |
| --- | --- |
| Situação | Alguns links não abrem no TWebEngine, o click neles não provoca ação nenhuma. |
| Ocorrência | O problema ocorre pois o tratamento destes links é diferente. |
| Correção | Feita a implementação pra tratar estes links que agora são abertos corretamente no mesmo TWebEngine. |
| Informações adicionais | * Referente à ocorrência: MTEC-2350 * Disponível em builds superiores a 17.3.0.8 |
