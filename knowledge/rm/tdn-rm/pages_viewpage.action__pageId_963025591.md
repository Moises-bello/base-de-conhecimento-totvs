---
content_hash: 03646bd9493a8e16ae2ef3a5d6a314f614a5aefdd621ad33ccd75b829c34cfcc
fetched_at: '2026-06-29T00:12:14.044014+00:00'
page_id: '963025591'
product: rm
source: tdn-rm
title: Cancelamento de movimento do empréstimo Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963025591
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cancelamento de movimento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

No cadastro de empréstimos existe o seguinte cadastro

Foi lançado no movimento do funcionário através do lançamento de grupo de eventos

No cadastro de empréstimos foi atualizado para os seguintes valores

Executando o cancelamento de movimento marcando "Atualiza cadastro de empréstimos"

O cadastro de empréstimos foi atualizado

IMPORTANTE:

Os campos "Nro de Parcelas Pagas" e "Saldo Devedor" não serão alterados pelo cálculo e não serão alterados pelo cancelamento de movimento também porque esses campos serão atualizados pelo valor informado no arquivo de importação do crédito do trabalhador.

Os valores que estavam no anexo Descontos de Empréstimos retornaram para o Valor da Parcela, caso haja informação no campo "Valor da Insuficiência de Saldo" então o retorno para o Valor da Parcela será a soma desse campo "Valor da Insuficiência de Saldo"  com o campo "Valor" do mesmo anexo.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
