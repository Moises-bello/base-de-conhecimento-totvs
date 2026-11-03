---
content_hash: 926a05086714ed7214630aa9459f1509a9a531b4687f3dd7fda052c6879daee9
fetched_at: '2026-06-29T00:08:09.969107+00:00'
page_id: '240297393'
product: rm
source: tdn-rm
title: TVBOK5_DT_Criar_Excluir_Usuario_Erros
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBOK5_DT_Criar_Excluir_Usuario_Erros
version: 117
---

# USUÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Cadastro de usuários* |
| **Situação/Requisito:** | *Ao tentar cadastrar um usuário por meio da ordem de leitura do cadastro de publicação, o sistema cadastra o usuário porém retorna um erro impedindo sua busca no campo de usuários da ordem de leitura, foi identificado também que na tela de edição de usuários, o sistema retorna um erro não tratado ao tentar excluir um usuário.* |
| **Solução/Implementação:** | *Foi identificado que após o cadastro do usuário pelo campo de ordem de leitura no cadastro de publicação, o sistema tentava fazer o filtro de busca por um campo diferente do existente nas opções da busca do usuário, foi feito o ajuste para que busque pelo código correto do usuário, e foi feito o ajuste para que a exclusão do usuário seja feita sem erros.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVBYGI* |
| **Requisito (ISSUE):** | *N/A* |

divs
