---
content_hash: e5c6c8c0f9028b5c7896bc7bc3c55972dc0c1e5c42df7cc1eeda96aeba3727b7
fetched_at: '2026-07-02T19:24:23.402534+00:00'
page_id: '448600333'
product: protheus
source: tdn-tec
title: Correção - Menu popup aparece desposicionado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448600333
version: 1
---

Quando um menu tipo popup é chamado usando coordenadas de uma tela que não seja a principal, ele não mais aparece desposicionado.

|  |  |
| --- | --- |
| Situação | Menu tipo popup aparece desposicionado |
| Ocorrência | Quando são utilizadas coordenadas de uma tela que não seja a principal pra ativar o menu, ele aparece desposicionado. |
| Correção | É feito um reajuste da coordenada pra que funcione corretamente independente da tela que esteja. |
| Informações adicionais | * Referente à ocorrência: ITEC-384 * Disponível em builds superiores a 17.3.0.5 |
