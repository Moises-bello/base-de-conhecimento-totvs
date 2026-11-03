---
content_hash: a1619a467a4ed913965eb288fa66592529cbb26ec7885390f2c166b42480970e
fetched_at: '2026-06-29T00:12:14.031822+00:00'
page_id: '963024382'
product: rm
source: tdn-rm
title: Cálculo da Rescisão com provisionamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963024382
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Rescisão com provisionamento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

No cadastro de empréstimos existe o seguinte cadastro

No período 2 foi lançado o provisionamento no lançamento do adiantamento - perceba que foi lançado o valor proporcionalizando o valor do empréstimo no provisionamento porque o adiantamento no cadastro do funcionário está com o valor de 40%.

IMPORTANTE:

Esse evento de provisionamento não poderá ter a natureza de rubrica 9253 - Empréstimo eConsignado - Desconto.

Ao lançar a rescisão deve marcar para lançar o empréstimo - nesse caso o teste foi com o parâmetro informado manualmente, observe que foi selecionado para descontar apenas a parcela atual

Foram inseridos os eventos no movimento da rescisão

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
