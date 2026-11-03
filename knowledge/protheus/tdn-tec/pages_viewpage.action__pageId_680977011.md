---
content_hash: 8fb576f38c36d7d01cf74686b4907f811d72a9b9db9a37b82f7fd6aeab3493f1
fetched_at: '2026-07-02T19:24:27.786058+00:00'
page_id: '680977011'
product: protheus
source: tdn-tec
title: Correção - A tela de downloads do TWebEngine não limita o "href" apresentado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680977011
version: 1
---

Foi limitada a informação apresentada na tela de downloads do TWebEngine da tag "href", evitando q ocorra uma "overflow" na interface.

|  |  |
| --- | --- |
| Situação | A informação contida na tag "href" aparece inteira na interface de downloads do TWebEngine. |
| Ocorrência | Nenhuma limitação foi desenvolvida para esta informação, e em casos em que ela é muito grande, ocorre uma quebra da interface. |
| Correção | Foi estipulado um limite da informação, sendo que quando ela extrapola o permitido pela interface, é terminada com reticências (...) apenas na sua apresentação. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-3266 * Disponível em builds superiores a 20.3.0.3 |
