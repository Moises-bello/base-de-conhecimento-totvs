---
content_hash: 47e1d61ad5283be9a3e35f89b66d548e3b2a6a9e96de9a66c63840dcdc5eb766
fetched_at: '2026-06-29T00:08:38.228169+00:00'
page_id: '285641990'
product: rm
source: tdn-rm
title: FINANCEIRO01-335 Alteração Global Cli/For em lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285641990
version: 101
---

# ALTERAÇÃO DE CLIENTE/FORNECEDOR EM LANÇAMENTO COM DADOS BANCÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Alteração Global de lançamento financeiro. |
| **Situação/Requisito:** | Ocorre erro de Foreign Key quando informado no processo de alteração global um cliente/fornecedor sem dados bancários em lançamento com Id de Pagamento Eletrônico informado. |
| **Solução/Implementação:** | Se o registro informado no campo alterado não possui dados bancários conforme o Id de Pagamento Eletrônico do lançamento esse campo será limpo ou carregado default caso este esteja informado no cliente/fornecedor. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** |  |
| **Requisito:** | FINANCEIRO01-335. |

divs
