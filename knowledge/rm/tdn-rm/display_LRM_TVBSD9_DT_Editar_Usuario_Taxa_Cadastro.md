---
content_hash: c65a49e33b651fe87452b161f01cf34b8ca345e7c2e2f01eccb3a528aecd967f
fetched_at: '2026-06-29T00:08:09.873673+00:00'
page_id: '240293551'
product: rm
source: tdn-rm
title: TVBSD9_DT_Editar_Usuario_Taxa_Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBSD9_DT_Editar_Usuario_Taxa_Cadastro
version: 115
---

# USUÁRIOS - TAXA DE CADASTRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Cadastro de usuários* |
| **Situação/Requisito:** | *Ao editar um usuário após ativar o parâmetro que cobra taxa de cadastro, o sistema não gera o lançamento e define o status do usuário como pendente.* |
| **Solução/Implementação:** | *Foi identificado que como o usuário já está cadastrado, a cobrança de taxa deve ser feita somente para novos cadastros, não para existentes, sendo assim, foi inserido uma validação no cadastro para que identifique se é um novo usuário, caso sim, se parametrizado, será feito a cobrança da taxa de inscrição.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVBYEV* |
| **Requisito (ISSUE):** | *N/A* |

divs
