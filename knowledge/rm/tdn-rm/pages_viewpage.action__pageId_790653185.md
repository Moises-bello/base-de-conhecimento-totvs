---
content_hash: 1fa51bf94e4cbff907ccb89152b2ae78ef9ba465b87b38691a35638db2b6c6fc
fetched_at: '2026-06-29T00:11:39.904945+00:00'
page_id: '790653185'
product: rm
source: tdn-rm
title: API - Comissões para migrar vendas da antiga comissão para a nova comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790653185
version: 2
---

Para tratar as comissões ainda não sincronizadas e pendentes no Portal de Imóveis, no sincronismo devem ser utilizadas as APIs abaixo para realizar a conversão dessa comissão.

* Para migrar a comissão de uma venda antiga para a nova comissão utilize a API abaixo, com os seguintes argumentos, onde 1 é a Coligada e 2579 é a venda:

API: <http://localhost:8051/api/imb/v1/sales/1_2579/commission/migration>

Verbo: POST

* Para excluir uma comissão já migrada, utilize a API abaixo, com os seguintes argumentos, onde 1 é a Coligada e 2579 é a venda:

API: <http://localhost:8051/api/imb/v1/sales/1_2579/commission> 

Verbo: DELETE
