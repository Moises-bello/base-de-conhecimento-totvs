---
content_hash: 07b02e94ab1b98336e6ab5a457ad64b517ad91b3f11bda59f8a224f670bf363f
fetched_at: '2026-06-29T00:11:48.874628+00:00'
page_id: '828438994'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência de INSS Patronal - Terceiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828438994
version: 18
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência de INSS Patronal - Terceiros |
| País: | Brasil |
| Ticket: | [18495766](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2218495766%22 "18495766") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8081](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8081) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.234
* 12.1.2310.175
* 12.1.2402.113 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

O Relatório INSS Patronal está sendo gerado com uma diferença no campo "Total Folha"  quando existe o código de receita "1170-01 - CP TERCEIROS - SALÁRIO EDUCAÇÃO".

## **04. SOLUÇÃO**

Implementado tratativa correspondente ao campo "Total Folha" onde o valor de terceiros passou a considerar o valor (SEST/SENAT).

Além disso, uma segunda melhoria foi realizada, que diz respeito à aplicação da regra de arredondamento para os terceiros de cada seção. Anteriormente, o arredondamento era realizado após a soma de todas as seções. Agora, essa regra é aplicada individualmente a cada seção, assegurando uma maior precisão nos cálculos.

## **05. DEMAIS INFORMAÇÕES**

**[Relatório INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)**
