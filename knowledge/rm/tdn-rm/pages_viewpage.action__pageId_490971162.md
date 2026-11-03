---
content_hash: ac347dcd58935078a8db3a389d129921a9c4abc0a3b860d198d086223b2d2f03
fetched_at: '2026-06-29T00:10:21.252906+00:00'
page_id: '490971162'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1323 - Valores dos Filtros da última lista gerada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490971162
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Filtros |
| Ticket: | N/A |
| Requisito/Story/Issue | DEDUANALYTICS-1323 |

## **02. SITUAÇÃO/REQUISITO**

Os filtros das telas estavam exibindo valores de cursos que não faziam mais parte da lista de evasores atual.

## **03. SOLUÇÃO**

Ajuste na chamada da API que retorna os valores dos filtros para retornar os itens de acordo com a última lista de evasores disponível.
