---
content_hash: 77d4b67faa9f2da8fe926da481ef9e8552bc05fe790834cc2b85192ac38e445a
fetched_at: '2026-06-29T00:06:07.681075+00:00'
page_id: '201737062'
product: rm
source: tdn-rm
title: TTEK89_DT_Detalhes_Turma_Disciplina_Selecionada_Matricula_OnLine
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEK89_DT_Detalhes_Turma_Disciplina_Selecionada_Matricula_OnLine
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
| **Versões/Release:** | *12.1.8.* |
