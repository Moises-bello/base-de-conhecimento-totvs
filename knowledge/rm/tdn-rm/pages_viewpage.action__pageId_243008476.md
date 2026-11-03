---
content_hash: a4388fb336978cbcf1b3ec8e74eee5130afe189b6ffcebbed7acf4263c55d486
fetched_at: '2026-06-29T00:08:11.435757+00:00'
page_id: '243008476'
product: rm
source: tdn-rm
title: TVDLE8_DT_Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243008476
version: 113
---

# Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Lançamento |
| **Situação/Requisito:** | Erro ao executar filtro na visão de lançamentos pelo campo Dias de Atraso: Invalid column name  DIASATRASO . |
| **Solução/Implementação:** | O campo Dias em Atraso não é um campo apto a filtro na tela de filtros do Lançamento, por ser um campo calculado e não um campo de tabela. Desta forma o mesmo foi removido para filtro.  Para utilizar o campo Dias em Atraso como filtro, deve-se utilizar o filtro personalizado por coluna da grid de lançamentos.  Para utilizar este filtro, clique no "funil" que se encontra em cada coluna da grid de lançamentos e informe o filtro desejado, desta forma os lançamentos exibidos na tela, serão filtrados conforme dias em atraso. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000254 |

divs
