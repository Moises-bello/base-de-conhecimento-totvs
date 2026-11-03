---
content_hash: 36fcbe5b4d7197d63a76d93513a7add04bcd38e8dac8f8a0c5c3d16cd4911b12
fetched_at: '2026-06-29T00:06:04.036411+00:00'
page_id: '200904860'
product: rm
source: tdn-rm
title: TSOBZY_DT_Cadastro_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TSOBZY_DT_Cadastro_Aluno
version: 2
---

# CADASTRO DE ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Cadastro de Aluno* |
| **Situação/Requisito:** | *Os telefones nos cadastros de alguns dos alunos estão sendo exibidos incorretamente. Pode-se observar que está faltando um dígito. Segue a consulta executada na base que mostra que os números corretamente cadastrados, apenas visualização na tela do sistema é que esta incorreta. Quando visualizamos a tela dentro de gestão de pessoas, os números estão corretos. Este erro se dá, pois o sistema permitiu cadastrar os telefones em questão com a máscara. Com isso, ao alterar a máscara do sistema por meio de uma parametrização e entrar no cadastro do aluno, os telefones em questão não são exibidos corretamente.* |
| **Solução/Implementação:** | **Utilização de um script sql para efetuar a remoção dos caracteres pertencentes as máscaras ( "(", ")", " ", "-" ) nos campos TELEFONE1, TELEFONE2, TELEFONE3 e FAX da tabela PPESSOA.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
