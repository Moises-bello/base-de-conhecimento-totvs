---
content_hash: 0435eae7f8ceb5c662ae7da4ee3bf7cffd59207f0306a5215d4e5c3b9720eb9c
fetched_at: '2026-06-29T00:11:16.136908+00:00'
page_id: '662421685'
product: rm
source: tdn-rm
title: Consulta Autorização de evento REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662421685
version: 8
---

Ao consultar a autorização ou cancelamento de um evento REINF é realizada uma integração com o TSS através do  através do retorno do TSS para o RM, o evento pode ser autorizada, cancelada ou rejeitada.

Para múltiplos eventos, a consulta é feita fracionada, com lotes de 50 eventos consultados. Isso permite realizar consulta de qualquer quantidade de eventos.

Ex: *Se eu consultar 500 eventos de uma só vez, internamente irá fracionar com 10 lotes de 50 eventos, para consultar tudo.*

*Se eu consultar 103 eventos de uma só vez, internamente irá fracionar com 2 lotes de 50 eventos e 1 lote de 3 eventos.*
