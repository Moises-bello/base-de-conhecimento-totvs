---
content_hash: c15ef4ff00bd1ed9ba0a05cab10e82a5133f778eced5a9069ecd275c979bf9ff
fetched_at: '2026-06-29T00:06:10.630676+00:00'
page_id: '203765746'
product: rm
source: tdn-rm
title: TTDQB7_DT_ERRO_Filtro_Assistente_Associacao_Unica
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDQB7_DT_ERRO_Filtro_Assistente_Associacao_Unica
version: 1
---

# ASSISTENTE ASSOCIAÇÃO ÚNICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Avaliação e Pesquisa* |
| **Função:** | *Assistente de associação única* |
| **Situação/Requisito:** | *O sistema exibe a seguinte mensagem de erro Ambiguous column name 'NOME', quando passamos o valor "%" para o Cód. Prova no filtro de Associação única de inscrições.* |
| **Solução/Implementação:** | *Ajustar a consulta realizada para pesquisar os registros de BPROVA, para impedir que o filtro seja executado utilizando uma coluna que possa existir em mais de uma tabela.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
