---
content_hash: 696f12c36c7c8873aa4f2726af3267fd23d647145bfc7a90a1f926111c39fc8d
fetched_at: '2026-06-29T00:11:50.687307+00:00'
page_id: '844984056'
product: rm
source: tdn-rm
title: DT - FGTS Digital - Lançamento Financeiro - Tipo de demissão "T - Término de
  contrato de trabalho"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844984056
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | FGTS Digital - Lançamento Financeiro - Tipo de demissão "T - Término de contrato de trabalho" |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-10381](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10381) |

## **02.****VERSÕES**

**A partir das Versões:**

* 12.1.2306.264
* 12.1.2310.213
* 12.1.2402.154 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Ao realizar o lançamento financeiro para um funcionário com rescisão do Tipo "T - Término de contrato de trabalho", o sistema não está gerando o FGTS para o tipo "24 - Total Guia FGTS Digital" nas guias do tipo Rescisório ou Rescisório + Mensal (somente demitido).

## **03. SOLUÇÃO**

Foi realizado o ajuste no lançamento financeiro do tipo "24 - Total Guia FGTS Digital" para que considere o tipo de demissão "T - Término de contrato de trabalho" ao gerar a guia do FGTS nos formatos Rescisório ou Rescisório + Mensal (somente demitido).

## **04. DEMAIS INFORMAÇÕES**
