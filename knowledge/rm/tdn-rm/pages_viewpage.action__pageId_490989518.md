---
content_hash: 4f75be5bdb21f91d152692413a1be9ba2b31f62f12f2794dd344e22b51dd1d42
fetched_at: '2026-06-29T00:10:21.658759+00:00'
page_id: '490989518'
product: rm
source: tdn-rm
title: DEDUANALYTICS-586 DT Valor de bolsas dos lançamentos a receber
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490989518
version: 2
---

Fato A Receber

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Fast Analytics |
| Função: | Fato A Receber |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUANALYTICS-586 Indicadores Financeiros](http://jiraproducao.totvs.com.br/browse/DEDUANALYTICS-586 "Indicadores Financeiros - Valores Bolsa (fato A Receber)") |

## **02. SITUAÇÃO/REQUISITO**

Cliente precisa subtrair dos valores que tem a receber o valor de bolsas relacionadas aos lançamentos a receber.

## **03. SOLUÇÃO**

Extrair para o GoodData o valor das bolsas que estão relacionadas aos lançamentos a receber. Para isso foi criado o campo Valor Bolsa na fato A Receber.

As consultas de extração foram modificadas para retornar o valor sitado anteriormente

Novas métricas e relatórios foram criados considerando esse novo cenário.
