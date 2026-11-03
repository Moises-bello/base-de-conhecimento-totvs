---
content_hash: c79a506045d4adfba008b5dc2f18d22eed4dd8beb38cb223497b56479e2a5026
fetched_at: '2026-06-29T00:11:55.974161+00:00'
page_id: '865001008'
product: rm
source: tdn-rm
title: DT - Retificação - Médias duplicando na segunda retificação de rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865001008
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão Complementar |
| País: | Brasil |
| Ticket: | [19991263](https://totvssuporte.zendesk.com/agent/tickets/19991263) |
| Issue: | [DRHCALCRM-6475](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6475) |

## **02. VERSÕES**

* 12.1.2310.248
* 12.1.2402.211
* 12.1.2406.142
* 12.1.2410 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Ao realizar a segunda retificação de uma rescisão, o RM está ignorando que as médias já foram pagas e calculando novamente, o que está dobrando o pagamento de médias.

## **04.****SOLUÇÃO**

Ao calcular a primeira retificação será inserido os valores das diferenças na tabela PFVERBASDIS para que em cálculos posteriores sejam utilizados como abatimento de diferenças.

## **05. ASSUNTOS RELACIONADOS**

* [Rescisão Complementar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718921)
