---
content_hash: 54edd5c1ebdf5f5c2c5fa041e930ede110665c1fa1858a3e98138215fe6f695e
fetched_at: '2026-06-29T00:12:09.189342+00:00'
page_id: '942050432'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS Patronal - Tratativa para Agroindústria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=942050432
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência INSS Patronal - Tratativa para Agroindústria |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13428](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13428 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.275
* 12.1.2410.226
* 12.1.2502.142 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adequar a geração do **Relatório de Conferência INSS Patrona**l para que, quando a classificação tributária for "06 - Agroindústria" e o FPAS for 604 com código de terceiros 0003, ou o FPAS for 833 com código de terceiros 0079, o valor do GILRAT não seja calculado.

**04. SOLUÇÃO**

Foi implementada uma tratativa no produto para que, na geração do **Relatório de Conferência INSS Patronal**, quando a classificação tributária for "06 - Agroindústria" e o FPAS for 604 com código de terceiros 0003, ou o FPAS for 833 com código de terceiros 0079, o valor do GILRAT não seja calculado, conforme demonstrado abaixo:

## **05. DOCUMENTAÇÃO**
