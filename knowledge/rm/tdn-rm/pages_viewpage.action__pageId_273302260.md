---
content_hash: cf18af27fe3bb5297e8f853d365de64253e216d280765b59741c19dcf5f71257
fetched_at: '2026-06-29T00:08:31.628005+00:00'
page_id: '273302260'
product: rm
source: tdn-rm
title: 413929 FINANCEIRO01-93 Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273302260
version: 107
---

# Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Lançamentos. |
| **Situação/Requisito:** | Lançamentos com valor opcional negativo na base de dados. |
| **Solução/Implementação:** | Feito validação para valores negativos no lançamento, no serviço de geração de itens de baixa, alteração e inclusão de lançamentos e no formulário de baixa. Dessa forma, caso algum lançamento tenha algum valor negativo será exibido mensagem de erro.   Obs: Exceção apenas para os valores de integração de lançamentos do TIN que podem ter valores negativos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000254 |

divs
