---
content_hash: 14ecc464f98a4ac9ed1c606ece77c48d84482857e6d89277875dd59b56290341
fetched_at: '2026-06-29T00:12:14.016564+00:00'
page_id: '963023701'
product: rm
source: tdn-rm
title: Cálculo da Folha - Insuficiência de saldo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963023701
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Folha com Insuficiência de saldo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

No anexo Eventos Remuneração Crédito do Trabalhador do cadastro de funcionários não foram inseridos os eventos que deveriam ser considerados para o cálculo da margem consignável do empréstimo, então será considerado o líquido do movimento do funcionário

No empréstimo foi informado

No movimento do funcionário foi lançado o valor do empréstimo, a base usada para o cálculo e o valor da insuficiência de saldo

E no anexo Desconto de Empréstimo do cadastro de Empréstimos armazena esses valores discriminados

Caso o parâmetro do relatório LAB04 seja selecionado no Parametrizador , no caminho **Parametrizador | RM Portal | Demonstrativo de Pagamento**

E houver insuficiência de saldo (CC 483) no envelope do funcionário

Tanto no Portal RM, quanto no MeuRH, haverá a inclusão da mensagem "ATENÇÃO TRABALHADOR! Não foi possível realizar o desconto total ou parcial do seu empréstimo consignado, por exceder o percentual (35%) da remuneração disponível prevista na lei nº10.820/2003 e Portaria MTE nº 435/2025. Procure sua instituição financeira para regularizar o pagamento desse empréstimo.", quando da emissão do relatório LAB04, conforme exemplo abaixo.

## **03.****TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
