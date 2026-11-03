---
content_hash: 7b39a632fcd7a0b83d480269c4fc1bda24fa945bebacd2fd9bf8dc29a6cababc
fetched_at: '2026-06-29T00:11:37.421163+00:00'
page_id: '777277297'
product: rm
source: tdn-rm
title: Código de cálculo 466 - ADIANTAMENTO PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS
  (Desconto)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777277297
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Desconto do tipo valor.

Este evento será utilizado para desconto do adiantamento de férias armazenando o valor do empréstimo provisionado e não acumulando o valor do desconto do empréstimo de férias no [CC 43 - Adiantamento Conforme Recibo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719758). Desta forma será discriminado na folha, o valor provisionado no recibo de férias para pagamento da parcela do empréstimo consignado.

O valor descontado nas férias, a título de provisão para quitação do empréstimo consignado, deverá passar a ser discriminado como provento na folha de pagamento, e o valor do código de cálculo 43 - Adiantamento conforme recibo apresentará exatamente o valor recebido pelo funcionários à título de férias.

## **02. EXEMPLO DE UTILIZAÇÃO**

[Exemplo de lançamento do Adiantamento Provisão Empréstimo Consignado Férias (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=777277575)

## **03. TABELAS UTILIZADAS**

* PCODCALCULO
* PFMOVTEMP
* PFMOVTEMPCONSIG
