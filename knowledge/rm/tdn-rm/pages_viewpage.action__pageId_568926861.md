---
content_hash: e8bf767d472f7e7f5bef511f4da4558371e8017a450360657fb5c8bc5a426899
fetched_at: '2026-06-29T00:10:51.521812+00:00'
page_id: '568926861'
product: rm
source: tdn-rm
title: 9789196 FISCAL01-14010 - DT Lançamento Fiscal Saída e Escrituração Fiscal -
  DIFAL devido na UF de entrega
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568926861
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Ticket: | [9789196](https://totvssuporte.zendesk.com/agent/tickets/9789196 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14010 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que possui uma venda para o estado de SP, porém a mercadoria será entregue no estado do RJ. Foi enviado pelo cliente legislação referente ao DIFAL devido para o estado que está recebendo a mercadoria, que por sua vez é o cenário do cliente.

## **03. SOLUÇÃO**

Foi criada uma regra para que ao se realizar os procedimentos de Escrituração do Lote Fiscal, inclusão manual do Lançamento Fiscal de Saída, edição do Lançamento Fiscal de Saída e cópia do Lançamento Fiscal de Saída a UF do Lançamento Fiscal de Saída seja obtida de acordo com a seguinte premissa: Quando o tipo de emitente não for empresa e o tipo de documento for NFe a UF de entrega for diferente da UF do CliFor, será retornado a UF de entrega.
