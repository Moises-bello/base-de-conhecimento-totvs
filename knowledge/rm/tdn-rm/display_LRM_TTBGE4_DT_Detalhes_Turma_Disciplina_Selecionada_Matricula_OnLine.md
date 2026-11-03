---
content_hash: 89216db3bfe034c1d7a4b27439ba81147181d65a53d6cf66f48b2bdd3d7e292b
fetched_at: '2026-06-29T00:06:07.583956+00:00'
page_id: '201736515'
product: rm
source: tdn-rm
title: TTBGE4_DT_Detalhes_Turma_Disciplina_Selecionada_Matricula_OnLine
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBGE4_DT_Detalhes_Turma_Disciplina_Selecionada_Matricula_OnLine
version: 2
---

# Matrícula OnLine

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Seleção de disciplinas na matrícula online.* |
| **Situação/Requisito:** | *Na matrícula online, ao selecionar uma turma/disciplina que não seja da matriz aplicada do curso do aluno, os detalhes dessa turma estão vindo em*  *branco.* *Isto ocorre devido a existência de um filtro na query correspondente ao identificador da matriz aplicada do curso do aluno, fazendo com que*  *os detalhes de turmas/disciplinas que não são do curso do aluno não sejam exibidos.* |
| **Solução/Implementação:** | *Remoção de filtros que identificam a matriz aplicada do curso do aluno na query que recupera os detalhes da turma/disciplina e inclusão de filtro no join*  *com a tabela de matriz aplicada do curso do aluno.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.41.* |
