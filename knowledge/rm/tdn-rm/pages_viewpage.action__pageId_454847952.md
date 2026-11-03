---
content_hash: fd3adacbc3c443002917791ffb8b601394ffab69d878edb6c8f690c852b018fb
fetched_at: '2026-06-29T00:10:13.259410+00:00'
page_id: '454847952'
product: rm
source: tdn-rm
title: 4870173 FINANCEIRO01-10874 DT Baixa de lançamentos com cheque emitidos ou recebidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454847952
version: 1
---

# Baixa de cheques emitidos ou recebidos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Baixa de cheques emitidos ou recebidos. |
| **Situação/Requisito:** | Ao emitir um cheque para mais de um lançamento, onde todos os lançamentos possuem vinculo, o cálculo do valor líquido está ficando incorreto. Este problema acontece após selecionar apenas um dos lançamentos que está relacionado ao cheque e baixar parcialmente este lançamento. |
| **Solução/Implementação:** | Melhoria na baixa de cheques vinculados. Nos casos onde houver mais de um lançamento relacionado ao cheque emitido ou recebido, os vínculos passam a ser considerados para todos os lançamentos relacionados ao cheque no momento de sua baixa.Dessa forma todos os vínculos ficam atualizados após a baixa. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [4870173](https://totvssuporte.zendesk.com/agent/tickets/4870173 "View ticket on the Zendesk portal"). |
| **Requisito:** | FIN000040 |
| **Documento de Referência:** |  |
| **Pacote:** | N/A. |
