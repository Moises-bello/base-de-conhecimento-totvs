---
content_hash: 04c0470933710a1d33b81af7dee98df5c13a319c50e8156ac6509aacf2d21aa1
fetched_at: '2026-06-29T00:09:07.573487+00:00'
page_id: '384578845'
product: rm
source: tdn-rm
title: DEDUANALYTICS-353 DT Fast Analytics - Lançamentos gerados por bolsa de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384578845
version: 1
---

# TOTVS Fast Analytics - Fato de Faturamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração Fato Faturamento. | N/A. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parametrização do Business Analytics no RM Integração. | N/A. | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A. |
| **País(es):** | Todos. |
| **Banco(s) de Dados:** | Sql Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS    SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

## Descrição

Modificação na consulta da fato Faturamento para não considerar como valor faturado o valor original de lançamentos gerados a partir de bolsa de crédito.
