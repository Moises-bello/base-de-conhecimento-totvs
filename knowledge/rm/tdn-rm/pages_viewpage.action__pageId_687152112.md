---
content_hash: b9afa238736682ab483e7ccc737c3a127111abb71fe09707937113c2508eadd7
fetched_at: '2026-06-29T00:11:20.561925+00:00'
page_id: '687152112'
product: rm
source: tdn-rm
title: 14134331 FISCAL01-18044 - DT - DMA Bahia - Não são gerados os registros 14
  e 15
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687152112
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | [14134331](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2214134331%22 "14134331") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18044 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a Rotina DMA-BA na nova MDI não foram gerados os registros (quadros) 14 e 15, quando não há lançamentos de ajuste (outros débitos e créditos).

## **03. SOLUÇÃO**

Ajustado o Layout DMA BA. Os registros 14 e 15 passam a ser gerados mesmo quando não há lançamentos de ajuste (outros débitos e créditos).
