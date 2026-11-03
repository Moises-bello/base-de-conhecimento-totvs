---
content_hash: 1141b3487eb11f8fafdff75e9c37f8cd8f4d8bcf807ff543ed5bd3ba9063698d
fetched_at: '2026-06-29T00:08:34.214018+00:00'
page_id: '274651679'
product: rm
source: tdn-rm
title: 527245 FINANCEIRO01-313 - Estorno de Orçamento no lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274651679
version: 96
---

# ESTORNO DE ORÇAMENTO FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Controle Orçamentário. |
| **Situação/Requisito:** | Após realizar uma movimentação de orçamento via lançamento onde houve bloqueio por exceder o valor disponível é realizada uma realocação orçamentária liberando o registro. Ao realizar uma alteração no lançamento desbloqueado (em campos que não afetam o orçamento) está sendo feito um estorno do valor movimentado e novo bloqueio. |
| **Solução/Implementação:** | Estorno de orçamento na alteração de lançamento será feito somente se algum dos campos que afetam orçamento for alterado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 527245. |
| **Requisito:** | FINANCEIRO01-313. |

divs
