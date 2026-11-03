---
content_hash: 71b388b368e6414a326888bd8d0e6e45ee35a2168bd93fff40527b9550a0f09f
fetched_at: '2026-06-29T00:08:19.976016+00:00'
page_id: '267803006'
product: rm
source: tdn-rm
title: TVZJ29_DT_Cadastro_De_Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZJ29_DT_Cadastro_De_Pessoa
version: 111
---

# CADASTRO DE PESSOA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Cadastro de Pessoa |
| **Situação/Requisito:** | Ao incluir uma pessoa através do cadastro de pessoa quando o código da tabela GAutoInc está desatualizado o registro é atualizado e não adicionado. |
| **Solução/Implementação:** | Realizado ajuste no cadastro de pessoa de forma a não permitir a inclusão caso a tabela GAUTOINC esteja inconsistente. O sistema irá emitir a seguinte mensagem:  "Não será possível criar uma nova Pessoa pois existem inconsistências na tabela GAutoInc. Favor procurar o administrador do sistema." |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVZJ29 |
| **Requisito (ISSUE):** |  |

divs
