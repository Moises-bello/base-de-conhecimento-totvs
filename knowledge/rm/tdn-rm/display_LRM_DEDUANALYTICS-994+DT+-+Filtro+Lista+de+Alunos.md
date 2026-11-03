---
content_hash: 08edd84f1229f5da987902524520766226896664e57018fe38c16906d62b56cb
fetched_at: '2026-06-29T00:10:15.818396+00:00'
page_id: '465182923'
product: rm
source: tdn-rm
title: DEDUANALYTICS-994 DT - Filtro Lista de Alunos
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUANALYTICS-994+DT+-+Filtro+Lista+de+Alunos
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Lista de Alunos |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-994 |

## **02. SITUAÇÃO/REQUISITO**

Quando usuário filtra a lista de alunos pelo RA de um aluno específico, é exibido a mensagem "Nenhum dado encontrado" antes de exibir o resultado da busca.

## **03. SOLUÇÃO**

O ícone "Carregando alunos" será exibido na tela durante a busca pelo RA. Apenas no final da busca, caso não seja encontrado nenhum registro, a mensagem "Nenhum dado encontrado" será exibida. O mesmo comportamento é válido para a busca pelo RA do aluno.
