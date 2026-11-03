---
content_hash: bd1a7fdcc9e097deb1876c1a273edc3dbd0640b48f6019db84abc606e2daeab7
fetched_at: '2026-06-29T00:12:14.120797+00:00'
page_id: '965458808'
product: rm
source: tdn-rm
title: Cálculo da Folha - Provisionamento no adiantamento salarial quando tem mais
  de um empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965458808
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador calculando provisão de adiantamento quando o funcionário tem mais de um empréstimo.

Veja também dicas e observações importantes no exemplo [Cálculo da Folha - Provisionamento no adiantamento salarial](https://tdn.totvs.com/pages/viewpage.action?pageId=963023764).

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Existindo 6 empréstimos no cadastro de empréstimo

Lançamento do grupo de eventos marcando o parâmetro "Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial"

IMPORTANTE:

Se no adiantamento do funcionário não pode descontar valores então não deve marcar o parâmetro.

Marcando o parâmetro será descontado o percentual de adiantamento cadastrado nos parâmetros do cadastro de funcionários referente a cada um dos empréstimos até chegar no valor do provento de adiantamento. Então pode ocorrer de não ter valor a receber de adiantamento e também de não provisionar para todos os empréstimos devido a falta de saldo.

No envelope de pagamento será lançado apenas um evento de desconto da provisão com os valores acumulados referentes ao percentual de cada empréstimo 

No log de cálculo será discriminado o cálculo da provisão de cada um dos empréstimos

IMPORTANTE:

Veja que o valor do desconto é maior que o valor do provento de adiantamento menos o desconto do arredondamento do mês anterior então a provisão assume o valor do líquido que seria pago no envelope de adiantamento, informando que o provisionamento só poderá ser de acordo com o líquido.

1800 - 0,07 = 1799,93 = que foi o valor do evento 9481 - PROVISÃO EMPRÉSTIMO CRÉDITO DO TRABALHADOR FOLHA

Valor calculado do provento de adiantamento

Valor calculado do desconto de arredondamento

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
