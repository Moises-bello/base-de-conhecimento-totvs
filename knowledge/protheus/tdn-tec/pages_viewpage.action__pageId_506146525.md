---
content_hash: 5feb3fd9f8c2592c4188e4d73ed99af95913a13012b182a589b504b02b872f25
fetched_at: '2026-07-02T19:24:25.756677+00:00'
page_id: '506146525'
product: protheus
source: tdn-tec
title: Correção - Utilização de item de menu como popup em um botão.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506146525
version: 1
---

|  |  |
| --- | --- |
| Situação | Queda da aplicação quando um item de menu utilizado em um botão não foi definido como popup. |
| Ocorrência | Quando um item de menu não era definido como popup e existia uma tentativa de uso como popup o SmartClient era fechado. |
| Correção | Foi implementado apenas uma proteção para evitar o fechamento do SmartClient. O erro de sintaxe deve ser corrigido na camada ADVPL. |
| Informações adicionais | * Referente à ocorrência: MTEC-2933 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.10 |
