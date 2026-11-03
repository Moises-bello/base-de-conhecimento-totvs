---
content_hash: feac92ceb7a2f0c47447f5f0ce9143a3e79b07161ab095bc3608b25c649f91df
fetched_at: '2026-06-29T00:10:21.664172+00:00'
page_id: '490990838'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1328 DT Radar duplicado quando aluno está matriculado em 2 cursos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490990838
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Detalhes do Aluno |
| Ticket: | N/A |
| Requisito/Story/Issue | DEDUANALYTICS-1328 |

## **02. SITUAÇÃO/REQUISITO**

Quando o aluno estava cursando mais de 1 curso, os eixos do radar nos detalhes deste aluno eram exibidos repetidos.

## **03. SOLUÇÃO**

Ajuste realizado na chamada da API que retorna os dados do radar, para filtrar as informações de acordo com o curso selecionado.
