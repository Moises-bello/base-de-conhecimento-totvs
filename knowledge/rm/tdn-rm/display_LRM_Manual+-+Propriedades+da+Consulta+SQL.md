---
content_hash: 4c26312ad60ddd72c657776e907d51f94daa310e6746c02c9c6f9726a5bfaad5
fetched_at: '2026-06-29T00:08:47.307178+00:00'
page_id: '319787296'
product: rm
source: tdn-rm
title: Manual - Propriedades da Consulta SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Propriedades+da+Consulta+SQL
version: 3
---

Na janela de propriedades da consulta SQL, pode ser informada uma sentença SQL que será executada para fazer a leitura dos dados no banco de dados. A sentença deverá obedecer a sintaxe de cada banco de dados e poderá conter somente cláusulas SELECT.

![](/download/attachments/319787296/propriedades_da_consulta_sql.png?version=1&modificationDate=1512921905000&api=v2)

1Nome

Informe o nome da tabela no conjunto de dados, este nome não pode ser repetido para mais de uma tabela/consulta do conjunto de dados.

2Tempo Limite

Informe um tempo máximo para leitura dos dados da tabela no banco de dados (em segundos). Caso o tempo de leitura seja ultrapassado, ocorrerá um erro de timeout no momento da geração.

3SQL

Informe a sentença SQL que deverá ser executada.  É possível a utilização de parâmetros através do prefixo : (dois pontos). Este parâmetro será criado no contexto e poderá ser informado no momento da geração. Conforme o exemplo acima. Também é possível a passagem de um Filtro do Usuário, para isso a sentença deverá ter uma marcação onde o filtro será inserido na sentença. Coloque um comentário /\*WHERE\*/, /\*AND\*/ ou /\*OR\*/ que serão substituídos pelo valor do filtro do filtro informado juntamente com a cláusula respectiva WHERE, AND ou OR.

4OK

Clique para salvar as alterações da Consulta SQL e fechar a tela.

5Cancelar

Clique para cancelar as alterações da Consulta SQL e fechar a tela.
