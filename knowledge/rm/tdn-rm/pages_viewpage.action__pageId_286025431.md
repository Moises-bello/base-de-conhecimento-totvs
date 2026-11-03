---
content_hash: 65af81b437302f87e74366d722e26b663f1be84c7588ad8a547ab684fbdd1ef2
fetched_at: '2026-06-29T00:08:39.922242+00:00'
page_id: '286025431'
product: rm
source: tdn-rm
title: 1152113 PORTALMOBILE01-1222 DT Professores da turma/disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286025431
version: 102
---

# QUADRO DE HORÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Função:** | Quadro de horários. |
| **Situação/Requisito:** | Mesmo o sistema estando parametrizado para utilizar horários independentes na turma e subturma, a lista de professores da turma/disciplina sempre retornava todos os professores cadastrados na turma/disciplina e não os professores que o aluno terá aula(professores associados aos horários da subturma matriculada pelo aluno). |
| **Solução/Implementação:** | Quando o sistema estiver parametrizado para utilizar horários independentes, somente será retornados os professores dos horários que o aluno tiver matriculado. Seja horário da turma/disciplina ou subturma. Se a turma/disciplina tiver vários professores e apenas um professor associado a subturma matriculada pelo aluno, somente este professor será listado como professor da turma no quadro de horário(Portal do aluno). |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
