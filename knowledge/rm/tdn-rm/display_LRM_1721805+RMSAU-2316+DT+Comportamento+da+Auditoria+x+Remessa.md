---
content_hash: efb6d92a53c3614d5a83430d3dd74063bf0a8d4514f05e0626277f63bbf58cdd
fetched_at: '2026-06-29T00:08:50.077503+00:00'
page_id: '331861856'
product: rm
source: tdn-rm
title: 1721805 RMSAU-2316 DT Comportamento da Auditoria x Remessa
type: documentation
url: https://tdn.totvs.com/display/LRM/1721805+RMSAU-2316+DT+Comportamento+da+Auditoria+x+Remessa
version: 1
---

# COMPORTAMENTO DA AUDITORIA X REMESSA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Auditoria Interna/Pré-Glosa |
| **Situação/Requisito:** | O sistema está permitindo retornar o status da auditoria interna para iniciada quando a conta foi Refaturada. Ocorre quando o usuário permanece com a tela da Auditoria Interna aberta e faz o refaturamento da remessa. |
| **Solução/Implementação:** | Foi incluída uma validação para verificar se o status da parcial está como faturada antes de retornar a parcial para auditoria iniciada. Caso esteja faturada, será emitida uma mensagem. |
| **Tickets relacionados:** | 1721805 |
| **Requisito:** | RMSAU-2316 |
