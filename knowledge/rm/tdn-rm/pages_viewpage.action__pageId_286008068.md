---
content_hash: 66cbcfc366ea5e4ddec17e5dd9e58b2ae97bf153530b7d25d6bf71625d67c823
fetched_at: '2026-06-29T00:08:39.066985+00:00'
page_id: '286008068'
product: rm
source: tdn-rm
title: 1128496 EDUCACIONAL01-1774 DT Choque de Horário - Alteração de Situação de
  Matrícula da Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286008068
version: 102
---

# CHOQUE DE HORÁRIO - ALTERAÇÃO DE SITUAÇÃO DE MATRÍCULA DA DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Choque de Horário - Alteração de Situação de Matrícula da Disciplina* |
| **Situação/Requisito:** | *Ao se alterar a situação de matrícula da disciplina de cancelado para matriculado o sistema não está validando choque de horário.* |
| **Solução/Implementação:** | *Ajuste no processo de alteração de situação de matrícula da disciplina para efetuar validação de choque de horário ao executar o processo, sendo que será validado o choque para o Ensino Superior se a situação antiga não for "É uma disciplina em curso" e a situação nova for "É uma disciplina em curso" e para o Ensino Básico se a situação antiga não for "Conta como aluno matriculado na turma" e a situação nova for "Conta como aluno matriculado na turma". Os demais casos não será feita validação de choque de horário.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
