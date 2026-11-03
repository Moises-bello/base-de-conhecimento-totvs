---
content_hash: 4ea55f96ba685d09de625fc085f5ff4bcf3d65a77f754c521b12723a7e722110
fetched_at: '2026-06-29T00:09:11.523497+00:00'
page_id: '407114598'
product: rm
source: tdn-rm
title: 3850318 EDUCACIONAL01-6482 DT Enturmação em Turma Mista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=407114598
version: 81
---

# ENTURMAÇÃO EM TURMA MISTA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Enturmação em Turma Mista* |
| **Situação/Requisito:** | *Ao acessar a tela de Enturmação em Turma Mista o sistema está apresentando erro de inconsistência na base de forma errônea onde impede de continuar o processo de enturmação na turma mista.* |
| **Solução/Implementação:** | *Ajuste no método que valida a inconsistência na base de dados quando monta os alunos a serem enturmados em turma mista. Sendo que esta validação deverá respeitar os parâmetros da situação de matrícula. Ou seja, o sistema enxergará uma inconsistência quando o aluno possuir matrícula em uma mesma disciplina porém em turmas diferentes com a mesma situação de matrícula com o item "conta com aluno matriculado" e "disciplina" marcado na aba Disciplina da situação de matrícula.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
