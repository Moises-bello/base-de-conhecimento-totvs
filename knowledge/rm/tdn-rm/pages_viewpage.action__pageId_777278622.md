---
content_hash: a1b1fe7e325f33c127494aa58053743dc584356c3a37ab89579746e23a236209
fetched_at: '2026-06-29T00:11:37.429257+00:00'
page_id: '777278622'
product: rm
source: tdn-rm
title: DT - Código de cálculo 466 - ADIANTAMENTO PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS
  (Desconto)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777278622
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Eventos - Códigos de Cálculos |
| País: | Brasil |
| Story | [DRHCALCRM-2840](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2840) |

## **01.** **VERSÕES**

**Versões:**

* + **12.1.2209.249**
  + **12.1.2302.176**
  + **12.1.2306.119**

## **02. SITUAÇÃO/REQUISITO**

Discriminar na folha de pagamento o valor provisionado no recibo de férias para pagamento da parcela do empréstimo consignado, quando o cliente parametrizar o sistema para realizar o desconto do empréstimo consignado nas férias.

## **03. SOLUÇÃO**

Criado o código de cálculo [466 - ADIANTAMENTO PROVISÃO EMPRÉSTIMO CONSIGNADO FÉRIAS (Desconto)](https://tdn.totvs.com.br/pages/editpage.action?pageId=777277297), para que possa ser criado um evento que poderá ser utilizado para desconto do empréstimo provisionado não acumulando o valor do desconto do empréstimo de férias no evento com [CC 43 - Adiantamento Conforme Recibo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719758). 

## **05. ASSUNTOS RELACIONADOS**

* [Exemplo de lançamento do Adiantamento Provisão Empréstimo Consignado Férias (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=777277575)
