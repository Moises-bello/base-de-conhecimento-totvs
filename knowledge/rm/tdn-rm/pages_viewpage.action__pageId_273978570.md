---
content_hash: beda3017eaa9c84ae127a2c8a65c8bfb89c97e546f77e161cb569e67f495a6ab
fetched_at: '2026-06-29T00:08:31.954052+00:00'
page_id: '273978570'
product: rm
source: tdn-rm
title: 572325 MRH-8318 Erro de seleção de Cidade e Estado e de salvamento das alterações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273978570
version: 109
---

# Edição das Formas De Contato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Banco de Talentos |
| **Função:** | Edição de Perfil |
| **Situação/Requisito:** | Ao realizar seleção de Cidade e Estado e tentar clicar para gravar o dado, em Formas de Contato, é apresentado uma mensagem de erro. |
| **Solução/Implementação:** | No back-end e front-end a coluna CODMUNICIPIO não estava sendo setada pelo banco de talentos, gerando excessão de chave estrangeira no banco de dados.  Corrigdo essa situação. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** | 572325 |

divs
