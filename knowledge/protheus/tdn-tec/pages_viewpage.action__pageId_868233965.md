---
content_hash: 24d202a57a42963e05e75a419237628f696130922568beb97a14e5d62eb42ff2
fetched_at: '2026-07-02T19:24:29.409089+00:00'
page_id: '868233965'
product: protheus
source: tdn-tec
title: 1 - @skip()
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868233965
version: 3
---

Pulando Funções, Classes e Métodos - @Skip()

Esse recurso causa o "pulo" da função, classe inteira ou somente o método de testes, independentemente de quantas funções de asserts existem implementados em seu escopo.

Portanto, mesmo que hajam muitos asserts implementados, quando houver @skip() o **PROBAT** irá registrar somente 1 (um) salto no resultado de testes, pois ele irá fazer referência à função, classe ou ao método e não ao seu conteúdo.

Exemplos:

## @Skip() para função:

cpptrue

## @Skip() para classe:

cpptrue

## @Skip() para método:

cpptrue
