---
content_hash: 05971f0dd2832b7a647bcc4afeed2d1b81f36b0e4c501c2616ca0e1ae5fe86e4
fetched_at: '2026-06-29T00:12:14.185704+00:00'
page_id: '967085381'
product: rm
source: tdn-rm
title: 'Recibo de Pagamento : Incluir Mensagem Insuficiência de Saldo - RM Reports'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967085381
version: 1
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

* 12.1.2406 e Superiores

## **02. V****ISÃO GERAL**

Foi implementada, no relatório FOPREL00178 - Envelope de Pagamento do Portal SQL, uma verificação que exibe mensagem de insuficiência de saldo para empréstimos feitos através do Crédito do Trabalhador.

## **03. EXEMPLO DE UTILIZAÇÃO**

Quando houver insuficiência de saldo no envelope de pagamento do funcionário

E o relatório FOPREL00178 - Envelope de Pagamento do Portal SQL for emitido, aparecerá no campo "Mensagem" (ao final do relatório): "ATENÇÃO TRABALHADOR: não foi possível realizar o desconto total ou parcial do seu empréstimo consignado, por exceder o percentual (35%) da remuneração disponível prevista na lei nº10.820/2003 e Portaria MTE nº 435/2025. Procure sua instituição financeira para regularizar o pagamento desse empréstimo."

## **04.** **TABELAS UTILIZADAS**

* GFILIAL
* PSECAO
* PFUNC
* PFFINANC
* PEVENTO
* PFPERFF
