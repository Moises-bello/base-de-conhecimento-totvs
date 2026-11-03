---
content_hash: bd510e10cabd7872c631d7ea335d8610dcc86c1a1b2b7aac71ad0816a38019c5
fetched_at: '2026-06-29T00:11:54.602921+00:00'
page_id: '856437064'
product: rm
source: tdn-rm
title: DT - Retificação da Folha - Funcionário Reintegrado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856437064
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Ratificação da Folha |
| País: | Brasil |
| Ticket: | [19115148](https://totvssuporte.zendesk.com/agent/tickets/19115148) |
| Issue: | [DRHCALCRM-6216](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6216) |

## **02. SITUAÇÃO/REQUISITO**

Quando o colaborador era reintegrado e há necessidade de calcular um retificação da folha pagamento os dias de direito em que o colaborador esteve desligado, o processo estava considerando para a Base de Cálculo de INSS o valor do aviso prévio indenizado pago na rescisão. 

## **03. SOLUÇÃO**

Adequado o calculo de retificação da Folha para não considerar o valor de aviso prévio indenizado (evento de código de cálculo 62) na base de INSS, quando o mesmo não possuir incidência em INSS.

## **04.** **ASSUNTOS RELACIONADOS**

* [Retificação da Folha de Pagamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719911)
