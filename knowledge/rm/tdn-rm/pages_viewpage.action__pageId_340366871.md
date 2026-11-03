---
content_hash: 9d45d9b89ab13fb0a4096e2c8895a09fcfcb9a3383c48eb292bc622db7265ac6
fetched_at: '2026-06-29T00:08:52.496038+00:00'
page_id: '340366871'
product: rm
source: tdn-rm
title: 2162172 FINANCEIRO01-5139 DT Controle orçamentário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=340366871
version: 1
---

# Orçamento - Controle de orçamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira |
| **Função:** | Orçamento - Controle de orçamento |
| **Situação/Requisito:** | Com controle orçamentário parametrizado corretamente no Totvs Gestão Financeira, os lançamentos financeiros a pagar não afetam o controle orçamentário quando oriundos do Totvs Gestão Estoque, Compras e Faturamento. |
| **Solução/Implementação:** | Primeira situação: Quando no Totvs Gestão Estoque, Compras e Faturamento estiver habilitado controle orçamentário, e o Totvs Gestão Financeira estiver com a parametrização de "Integração ao Controle Orçamentário" desabilitado, o sistema deve afetar o orçamento somente Totvs Gestão Estoque, Compras e Faturamento pela criação de movimento.  Segunda situação: Quando no Totvs Gestão Estoque, Compras e Faturamento estiver habilitado controle orçamentário, e o Totvs Gestão Financeira estiver com a parametrização de "Integração ao Controle Orçamentário" também habilitada, o sistema deve afetar o orçamento somente Totvs Gestão Estoque, Compras e Faturamento pela criação de movimento.  Terceira situação: Quando no Totvs Gestão Estoque, Compras e Faturamento estiver desabilitado controle orçamentário, e o Totvs Gestão Financeira estiver com a parametrização de "Integração ao Controle Orçamentário" habilitada, o sistema deve afetar o orçamento somente Totvs Gestão Financeira pela criação e/ou baixa do lançamento. |
| **Conversores e Parâmetros:** | Integração ao Controle Orçamentário |
| **Tickets relacionados:** | 2162172 |
| **Requisito:** | FIN000195 |
| **Documento de Referência:** | N/A. |
