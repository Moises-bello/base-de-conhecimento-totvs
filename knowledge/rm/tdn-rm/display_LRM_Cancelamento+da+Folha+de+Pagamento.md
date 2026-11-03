---
content_hash: 6bebefadfcbfa49f2aa5647d5af2e81bee02ada9bd73a5aa59c7f135b699534b
fetched_at: '2026-06-29T00:11:12.526090+00:00'
page_id: '654108236'
product: rm
source: tdn-rm
title: Cancelamento da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+da+Folha+de+Pagamento
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

SumárioVisão Geral

## **01. VISÃO GERAL**

Este processo consiste em retornar os itens para o status de liberado para pagamento e caso esteja integrado com o BackOffice, o movimento é excluído. Se existir um movimento do BackOffice associado à folha, só será possível cancelá-la se o lançamento financeiro não estiver sido recebido.

As vezes é necessário cancelar uma folha quando algum repasse não foi incluído ou algum débito não foi computado.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Vá até **Faturamento > Gestão de Repasse > Folha de Pagamento de Prestadores,**ao acessar, informe o prestador e vá até pagamento. Clique em **Processos> Cancelar a folha de pagamento.**

Sumário 2Mudança de status

Ao cancelar uma folha, os itens voltam para o status de liberado.

Itens disponíveis para a geração de uma nova folha para o prestador.

Quantidade de itens pertencentes a uma folha

Após o cancelamento da folha que tinha 15 itens, ao se gerar a folha novamente, os itens farão parte da nova folha.

## **03.****TABELAS UTILIZADA**

* SZFOLHAPRODPREST
* SZFOLHAPAGTOPREST
