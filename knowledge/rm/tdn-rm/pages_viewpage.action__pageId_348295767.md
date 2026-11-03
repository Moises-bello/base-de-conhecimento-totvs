---
content_hash: 80d15b0b631d9f76244c61244266c181f82fcb84271d404d4642470045cf865d
fetched_at: '2026-06-29T00:08:54.965901+00:00'
page_id: '348295767'
product: rm
source: tdn-rm
title: 1548402 RMSAU-1452 DT Agenda Atendimento - número máximo de encaixes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=348295767
version: 1
---

# Agenda Atendimento - número máximo de encaixes

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Agenda de Atendimento |
| **Situação/Requisito:** | O RM Saúde não permite que o usuário altere os dados do agendamento, pois o número de encaixes não excedeu ao permitido na agenda. A mensagem só deveria ser apresentada caso o número de encaixes seja excedido, ou seja, no caso acima, não tinha necessidade de apresentar nenhuma mensagem. |
| **Solução/Implementação:** | Ajustado para permitir inserir o número de encaixes conforme previamente cadastrado, a mensagem agora só é apresentada caso a quantidade de encaixes exceda o número de encaixes cadastrados. |
| **Documento de Referência:** | [Ticket #1548402](https://totvssuporte.zendesk.com/agent/tickets/1548402 "Open ticket in Zendesk Support") |
