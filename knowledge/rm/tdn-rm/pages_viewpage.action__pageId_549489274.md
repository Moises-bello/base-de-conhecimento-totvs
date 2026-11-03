---
content_hash: bba2793f13e0dbe31e9ad695f65c0c4021daa77dad1f31c7303e44ca47dae0c3
fetched_at: '2026-06-29T00:10:43.001657+00:00'
page_id: '549489274'
product: rm
source: tdn-rm
title: Cancelamento de transação com cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549489274
version: 12
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Para realizar o cancelamento de uma transação com cartão, deve ser executado o processo ***Solicitar o cancelamento de transação***na visão de transações com cartão de crédito/débito.

Este processo realiza o cancelamento das transações para os modelos IFrame Getnet, eRede, CyberSource e Adyen.

Este processo somente solicitará o cancelamento da transação com cartão onde o status da transação for ***Pagamento Confirmado*** ou ***Pagamento Concluído***. Ao solicitar o cancelamento da transação o status da transação no TOTVS Gestão Financeira será alterada para ***Cancelamento Pendente.***Após 6hrs da solicitação do cancelamento deve ser executado o processo de ***Ajustar transação***, que verificará se o cancelamento foi processado com sucesso e realizará a baixa do título no RM e a transação ficará com status ***Pagamento Cancelado***. 

OBS: Para a solução IFrame Getnet e eRede, caso a solicitação do cancelamento seja feito no mesmo dia da transação (D+0), a transação será cancelada imediatamente.

## **02. EXEMPLO DE UTILIZAÇÃO**

Posteriormente deverá ser executado o processo <b>Ajustar transação</b> para ser atualizado para <b>Pagamento Cancelado</b> e seja executado o processo de cancelamento da baixa do boleto.IMPORTANTE!

]]>
