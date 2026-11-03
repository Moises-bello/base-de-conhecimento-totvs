---
content_hash: 699b936a99518315d07d0a7cdf4844622d9e8fdb1eba214034d6e472794e3e8b
fetched_at: '2026-06-29T00:05:47.163875+00:00'
page_id: '1008223899'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Diferença Férias (Dissidio)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008223899
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculos |
| País: | Brasil |
| Ticket: | [23678073](https://totvssuporte.zendesk.com/agent/tickets/23678073 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-8855](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8855) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.225
  + 12.1.2506.175
  + 12.1.2510.106
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao lançar a diferença de férias por dissidio o sistema calculou e lançou na aba Verbas Geradas por Diferença o evento de código de cálculo [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652).

## **04. SOLUÇÃO**

Tratamento para não calcular o evento de código de cálculo [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652) no cálculo da diferença de férias.

## **05.** **ASSUNTOS RELACIONADOS**

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
