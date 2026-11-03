---
content_hash: a1af55ed89b0d7882ea50fcd6c67c6ca016cfff72c426a00a74be1662bd52ab3
fetched_at: '2026-06-29T00:12:00.047361+00:00'
page_id: '878928866'
product: rm
source: tdn-rm
title: DT - Folha Analítica por Dissidio - Tratativa do INSS Exclusivo do Segurado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=878928866
version: 10
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Folha Analítica por Dissidio - Tratativa do INSS Exclusivo do Segurado |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11323](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11323 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.239
* 12.1.2406.173
* 12.1.2410.108 e superiores

## **03. SITUAÇÃO/REQUISITO**

Na Folha Analítica por Dissídio, o campo '**Base de INSS do Dissídio**' não deve considerar eventos/verbas com incidência de 'INSS Exclusiva do Segurado'.

## **04. SOLUÇÃO**

Foi implementada uma tratativa no produto para que, no campo '**Base de INSS do Dissídio**' da Folha Analítica por Dissídio, não seja considerado eventos com 'INSS Exclusiva do Segurado'.

Em Cadastros | Eventos | Eventos

Em Folha Mensal | Relatórios da Folha | Folha Analítica por Dissídio

## **05. DEMAIS INFORMAÇÕES**
