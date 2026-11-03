---
content_hash: a4c149f030268f5bf7344e13ffc0161e36e5b8cd024465f80a74b8b4672da816
fetched_at: '2026-06-29T00:12:14.021240+00:00'
page_id: '963023764'
product: rm
source: tdn-rm
title: Cálculo da Folha - Provisionamento no adiantamento salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963023764
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Folha com Provisionamento no adiantamento salarial.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

No cadastro de empréstimos existe o seguinte cadastro

Ao lançar o grupo de eventos com o adiantamento e marcando o parâmetro de provisionamento

Será lançado no movimento de adiantamento verificando o cadastro do funcionário

IMPORTANTE:

Esse evento  de provisionamento não poderá ter a natureza de rubrica 9253 - Empréstimo eConsignado - Desconto.

IMPORTANTE:

O provisionamento somente lançará para a modalidade de empréstimo "Crédito do trabalhador eSocial" considerando o percentual do cadastro do funcionário aplicado na parcela devedora. Não será feita nenhuma tratativa para lançar dentro da margem consignável, mesmo se estiver parametrizado.

Se não tiver líquido suficiente para desconto será lançado até o líquido disponível, não gerando evento de arredondamento/insuficiência de saldo.

Ao lançar a folha de pagamento foi inserido o evento de provento com o valor do provisionamento feito no adiantamento

Dica:

Quando não provisiona no desconto do adiantamento pode gerar saldo insuficiente lançado no movimento do funcionário devido adiantar salário. porque lança o desconto do adiantamento mais o desconto do empréstimo em um movimento onde uma parte já foi paga adiantadamente.

Quando provisiona desconta antecipadamente no adiantamento guardando o valor e quando chegar no pagamento mensal, tem o valor para descontar o empréstimo.

Quando não houver valor no percentual de adiantamento no cadastro do funcionário será apresentada a mensagem no log

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
