---
content_hash: 9466e2d9b6ba5a63648b702244e8e7cb608793d3b761a54e8e8c0dfc9dc55d5d
fetched_at: '2026-06-29T00:08:38.386065+00:00'
page_id: '285650256'
product: rm
source: tdn-rm
title: 1086298 EDUCACIONAL01-1724 DT Turmas do Censo Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285650256
version: 101
---

# TURMAS DO CENSO BÁSICO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | T*****otvs Educacional***** |
| **Função:** | Censo da Educação Básica |
| **Situação/Requisito:** | O sistema está gerando dados no registro 20, no arquivo do Educacenso, para a turma código: 51190, no período letivo 20172 código 899, porém essa turma não possui nenhuma turma/disciplina, portanto não possui alunos matriculados, nem professores. Dessa forma, não deveria ser considerada, para envio no arquivo. |
| **Solução/Implementação:** | O sistema foi alterado para verificar a existência de alunos na turma na hora de gerar a lista de turmas para o Censo. Serão desconsideradas as turmas que não possuírem alunos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
