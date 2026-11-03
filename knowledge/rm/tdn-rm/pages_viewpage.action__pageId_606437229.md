---
content_hash: c924690c8bda581f2cfdc99c1aede7ff140bb620fd14ea8e3b00597895306ae1
fetched_at: '2026-06-29T00:10:58.759117+00:00'
page_id: '606437229'
product: rm
source: tdn-rm
title: 10850665 FISCAL01-15127 - DT Cálculo de retenção de ISS (alíquota incorreta)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606437229
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cálculo alíquota tributo |
| Ticket: | 10850665 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15127 |

## **02. SITUAÇÃO/REQUISITO**

A retenção do tributo ISS RF está sendo calculada para tributos que não estão parametrizados para cálculo.

No cenário do cliente, o cálculo do ISS deve ser realizado apenas para os tributos que estão parametrizados na Natureza de operação e que possuam alíquota.

## **03. SOLUÇÃO**

Realizado ajuste para que seja levado em conta o código do tributo ao se calcular a alíquota dos tributos conforme requisito informado.
