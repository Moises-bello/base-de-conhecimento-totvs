---
content_hash: c5481c5a25832981023893b8cfbac4e4c134ac80fef458fea776a844a895a03c
fetched_at: '2026-06-29T00:08:10.619774+00:00'
page_id: '240309472'
product: rm
source: tdn-rm
title: TVCKTM_DT_Editar_Usuario_Taxa_Cadastro_Situacao_Pendente_Lancamento_CancExclu
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCKTM_DT_Editar_Usuario_Taxa_Cadastro_Situacao_Pendente_Lancamento_CancExclu
version: 118
---

# USUÁRIOS - TAXA DE CADASTRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Cadastro de usuários* |
| **Situação/Requisito:** | *Quando um cadastro de usuário cobra taxa de inscrição porém com o lançamento cancelado ou excluído, o candidato fica com a situação pendente e o campo bloqueado para alteração.* |
| **Solução/Implementação:** | *Foi feito o ajuste na validação da situação do usuário, que verifica se o mesmo tem taxa de inscrição pendente, se tiver, mantêm bloqueado e somente após a baixa que será habilitado (manualmente ou por atualização da biblioteca), se não tiver, o campo permanecerá pendente porém desbloqueado para edição.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVCOWE* |
| **Requisito (ISSUE):** | *N/A* |

divs
