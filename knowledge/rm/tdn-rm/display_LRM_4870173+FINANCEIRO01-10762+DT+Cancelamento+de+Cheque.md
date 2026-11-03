---
content_hash: 7f419c2f1cb2cd5d3d5386b76816d6207a6eae90025e0a288ed82845f2bb4b3f
fetched_at: '2026-06-29T00:10:11.829410+00:00'
page_id: '453288495'
product: rm
source: tdn-rm
title: 4870173 FINANCEIRO01-10762 DT Cancelamento de Cheque
type: documentation
url: https://tdn.totvs.com/display/LRM/4870173+FINANCEIRO01-10762+DT+Cancelamento+de+Cheque
version: 1
---

# Cancelamento de Cheque

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Cancelamento de cheque |
| **Situação/Requisito:** | Após realizar o cancelamento do cheque (item baixa) o sistema mantem o valor do cheque no calculo do valor líquido |
| **Solução/Implementação:** | Otimização no cancelamento de cheques emitidos para mais de um lançamento, o campo VALORCHEQUE da tabala FLAN, de todos os lançamentos relacionados ao cheque cancelado, está sendo atualizado com o saldo restante de cheque emitidos, ou zero, caso não tenha mais cheques relacionados ao lançamento. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [4870173](https://totvssuporte.zendesk.com/agent/tickets/4870173 "Open ticket in Zendesk Support") |
| **Requisito:** | FIN000041. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
