---
content_hash: e81f2fe4f4b66bb951be912af8faaeb90da7b9420fbba95173fde7062e297023
fetched_at: '2026-06-29T00:10:21.904073+00:00'
page_id: '494807831'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1381 DT Radar do perfil evasor quando aluno possui vários scores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494807831
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Detalhes do Alunos - Radar do perfil evasor |
| Ticket: |  |
| Requisito/Story/Issue | DEDUANALYTICS-1381 |

## **02. SITUAÇÃO/REQUISITO**

Quando aluno possuía vários scores, os detalhes do aluno não exibiam o radar do perfil evasor com as informações mais recentes.

## **03. SOLUÇÃO**

Ajuste na chamada do serviço que retorna as informações do radar para retornar os dados do último score do aluno.
