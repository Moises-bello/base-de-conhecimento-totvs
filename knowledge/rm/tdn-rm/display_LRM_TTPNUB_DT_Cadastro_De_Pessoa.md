---
content_hash: 992a6654b7ab5780053fb64f5f6220ff9d6a91982827a9c2204f2b01cc11b3cc
fetched_at: '2026-06-29T00:06:16.956623+00:00'
page_id: '212902426'
product: rm
source: tdn-rm
title: TTPNUB_DT_Cadastro_De_Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPNUB_DT_Cadastro_De_Pessoa
version: 1
---

# CADASTRO DE PESSOAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Pessoas* |
| **Função:** | *Cadastro de Pessoas* |
| **Situação/Requisito:** | Ao editar um registro antigo com o campo ORGEMISSORRNE da PPESSOA com mais de 15 caracteres, era exibida uma mensagem de erro de violação de constraints. |
| **Solução/Implementação:** | Foi retornado o MaxLength do campo ORGEMISSORRNE para 20, conforme era no passado e conforme é no banco de dados. |
| **Chamados relacionados:** | TTPNUB |
| **Versões/Release:** | *12.1.8* |

divs
