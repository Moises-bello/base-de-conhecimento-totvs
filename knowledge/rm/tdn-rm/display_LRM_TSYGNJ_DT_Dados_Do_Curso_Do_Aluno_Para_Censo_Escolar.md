---
content_hash: 6fa65cc48d43b7d227e2972e40af0ac96f676a8f57ac43b0edd082ff3b3d3ad1
fetched_at: '2026-06-29T00:06:02.842499+00:00'
page_id: '198949214'
product: rm
source: tdn-rm
title: TSYGNJ_DT_Dados_Do_Curso_Do_Aluno_Para_Censo_Escolar
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYGNJ_DT_Dados_Do_Curso_Do_Aluno_Para_Censo_Escolar
version: 4
---

# DADOS DO CURSO DO ALUNO PARA O CENSO ESCOLAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Dados do curso do aluno para o censo escolar* |
| **Situação/Requisito:** | *Ao selecionar na visão do lookup Código do INEP do curso de origem e preencher o campo habilitação com "%" , ocorre a seguinte não conformidade: "Ocorreu um erro ao efetuar a leitura da visão de lookup: ORA-00934: a função de grupo não é permitida aqui". O fato acontece apenas em base de dados oracle.* |
| **Solução/Implementação:** | *Ajuste na consulta sql que faz o filtro por "%" ao selecionar a visão do lookup Código do INEP do curso de origem, para uma subquery..* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.40 / 11.82.41* |
