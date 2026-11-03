---
content_hash: 097a6d3550cd7bca7e42702493ef841b76564462fa67a49dcdc5d5eb8f27b5eb
fetched_at: '2026-06-29T00:05:47.358302+00:00'
page_id: '1010820140'
product: rm
source: tdn-rm
title: Cálculo da Folha - Cálculo da margem consignado considerando IRRF conforme
  mês caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010820140
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O valor de IRRF retido no adiantamento salarial não deve ser incluído na base de cálculo da provisão do Crédito do Trabalhador na folha mensal.

*Consultoria: Diante do exposto, considerando que o fato gerador do IRRF ocorre na data do pagamento (regime de caixa) e não na competência da folha, concluímos que o imposto retido no adiantamento deve ser considerado apenas para a base de cálculo do próprio adiantamento, não compondo novamente a base da folha de pagamento.*

Para ver em quais patches foi liberada a alteração consulte [DT - Crédito do Trabalhador - Margem consignado considerar IRRF conforme mês caixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1010813118)

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios:

Cálculo do adiantamento no dia 15/03/2025 com desconto de provisão para o empréstimo consignado e do IRRF

Cálculo da folha de pagamento com o desconto do empréstimo consignado com a data de pagamento é 05/04/2025. No print abaixo demonstra os dois IRRFs com datas distintas na seleção de todos os períodos do envelope de pagamento.

 No log de cálculo o valor considerado foi apenas no mês caixa com data igual ao desconto

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
