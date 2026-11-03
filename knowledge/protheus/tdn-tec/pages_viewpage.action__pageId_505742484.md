---
content_hash: 935a68fd4a8ab3f668fa0bdb3455a42ebc4e39bb71a9ecded88daf12c9bf19c0
fetched_at: '2026-07-02T19:24:25.713439+00:00'
page_id: '505742484'
product: protheus
source: tdn-tec
title: Correção - Problemas na pintura do TComboBox no MacOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=505742484
version: 1
---

|  |  |
| --- | --- |
| Situação | O componente TComboBox apresenta problemas de tamanho/pintura no MacOS |
| Ocorrência | Problema acontece ao ativar o estilo de tema *plastique.* Após a atualização para o Qt5 (SmartClient Lobo Guara) começou a ocorrer esse problema |
| Correção | Correção efetuada para não utilizar o tema *plastique* no TComboBox do MacOS. |
| Informações adicionais | * Referente ao chamado: [6071625](https://totvssuporte.zendesk.com/agent/tickets/6071625 "View ticket on the Zendesk portal") * Referente à ocorrência: MTEC-2803 * Disponível em builds superiores a 7.00.170117A - 17.3.0.9 |
