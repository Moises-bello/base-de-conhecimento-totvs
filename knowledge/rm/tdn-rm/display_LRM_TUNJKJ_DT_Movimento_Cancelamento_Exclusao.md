---
content_hash: 0c2d3bbed7dc712a28ae4fcc78c46ea1ca5a6fa621ce8bbbc8df620e8c7ffbe1
fetched_at: '2026-06-29T00:08:05.290910+00:00'
page_id: '235593329'
product: rm
source: tdn-rm
title: TUNJKJ_DT_Movimento_Cancelamento_Exclusao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNJKJ_DT_Movimento_Cancelamento_Exclusao
version: 124
---

# TUNJKJ\_DT\_Movimento\_Cancelamento\_Exclusao

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e projetos.* |
| **Módulo:** | *Gestão de estoque compras e faturamento.* |
| **Função:** | *Cancelamento e exclusão de movimento e cancelamento financeiro vinculado ao movimento.* |
| **Situação/Requisito:** | *Ao cancelar o movimento ou os lançamentos financeiros vinculado ao movimento deve atualizar o valor do campo NUMEROLCTABERTO da tabela TMOV. Ao excluir um movimento a exclusão deve ser realizada mesmo que tenha registro vinculados ao mesmo na TMOVLAN.* |
| **Solução/Implementação:** | *O valor do campo NUMEROLCTABERTO da tabela TMOV é atualizado com a quantidade de lançamentos em aberto. A exclusão do movimento remove os vínculos com TMOVLAN e é realizada com sucesso.* |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | *NA.* |
| **Requisito (ISSUE):** | NA*.* |

divs
