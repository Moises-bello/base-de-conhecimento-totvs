---
content_hash: 627fe2fb14b51f6c8ca60a39301c453576c841911c344ae7b77a832f48d3b5ba
fetched_at: '2026-06-29T00:06:27.453902+00:00'
page_id: '232822265'
product: rm
source: tdn-rm
title: TTZANA_DT_Geração_De_Lançamentos_Em_Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232822265
version: 120
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Geração de lançamentos* |
| **Situação/Requisito:** | *Ao processar a geração de lançamentos financeiros para um grande volume de alunos, o sistema monta uma consulta SQL com um filtro muito extensão e isso causa uma mensagem de erro no SGBD, pois o este não consegue montar um plano de execução devido a complexidade da consulta SQL.* |
| **Solução/Implementação:** | *Foi realizado ajuste no sistema para que sejam realizadas mais consultas ao banco, durante a geração de lançamentos, de forma a limitar a quantidade de alunos aplicados ao filtro da consulta por vez.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | TUJJYQ e TUIVUH |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
