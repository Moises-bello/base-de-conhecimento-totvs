---
content_hash: 15dec277e47b851b60b3f530a67a6fa35e34bf8b157af0040383051ced495a56
fetched_at: '2026-06-29T00:11:32.007571+00:00'
page_id: '743673313'
product: rm
source: tdn-rm
title: DT - Indenização adicional na dispensa antes da Data Base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=743673313
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão | Cálculo |
| País: | Brasil |
| Ticket: | [#13907935](https://totvssuporte.zendesk.com/agent/tickets/13907935 "View ticket on the Zendesk portal") |
| Issue | [DRHCALCRM-2463](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2463) |

## **02. SITUAÇÃO/REQUISITO**

Sistema está pagando a indenização adicional antes da data base (evento com Código de Cálculo 344) de forma incorreta para um funcionário que tem a projeção do aviso prévio caindo no dia e mês da data base informada no cadastro de sindicato. Conforme orientação da nossa consultoria de segmentos: 'Saliento que se o funcionário foi dispensado na data base (mês do dissídio), deverá ser pago somente a diferença do dissídio".

## **03. SOLUÇÃO**

Adequado o lançamento do evento de Código de Cálculo 344 - Indenização adicional na dispensa antes da Data Base, quando a projeção do aviso prévio indenizado termina no mesmo dia da Data base informada no Sindicato. 

## **04. DEMAIS INFORMAÇÕES**

[Código de Cálculo 344 - Indenização Adicional na Dispensa Antes Data Base](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718308)
