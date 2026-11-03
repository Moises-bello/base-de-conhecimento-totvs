---
content_hash: ddb23a492e196697c171ba9eb754e2bc940787617329d998b65ded98ac1bfe0e
fetched_at: '2026-06-29T00:09:07.632008+00:00'
page_id: '384583623'
product: rm
source: tdn-rm
title: 3398055 FINANCEIRO01-8253 DT  Ajuste de transação de cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384583623
version: 2
---

# Ajuste de Transação de cartão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Ajuste de transação de cartão |
| **Situação/Requisito:** | Caso o boleto tenha uma transação de pagamento cancelado o posteriormente a uma de pagamento concluído, o ajuste de transação não respeita a ordem das transações, cancelado assim a baixa do lançamento/boleto. |
| **Solução/Implementação:** | Feito tratamento para considerar apenas a ultima transação com cartão e assim evitar que as transações passadas modifiquem o status do boleto |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 3398055 |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-8253> |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
