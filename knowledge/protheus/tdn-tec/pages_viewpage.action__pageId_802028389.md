---
content_hash: 01a694792ba56fea1796a8a863089f8e5e93b288746a9d82fefd0bfa29101748
fetched_at: '2026-07-02T19:24:28.630910+00:00'
page_id: '802028389'
product: protheus
source: tdn-tec
title: Correção - Ajuste com linhas guia na TTree
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802028389
version: 1
---

|  |  |
| --- | --- |
| Situação | Dependendo do estilo deveria mostrar as linhas guia da TTree |
| Ocorrência | Em algumas telas o TTree mostrava uma linha guia e na última atualização do Smartclient (Qt6) parou de mostrar |
| Correção | No Qt6 não existe mais o estilo "Plastique" que era o responsável por essa linha guia de estilo. Para resolver o caso foi implementado manualmente a linha via CSS caso seja o estilo relacionado ao plastique |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4329 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.2.1 |
