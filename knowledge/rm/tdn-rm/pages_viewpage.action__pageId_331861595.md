---
content_hash: 137c976eb3f247ca1ae954eacb702a60bdc1a1d3d258c59ff0eb21fa366a21de
fetched_at: '2026-06-29T00:08:50.074303+00:00'
page_id: '331861595'
product: rm
source: tdn-rm
title: 2075421 DEDUINTEGRACOES-1534 DT Inclusão de parcela extra com competência vazia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331861595
version: 1
---

# INCLUSÃO DE PARCELA EXTRA COM COMPETÊNCIA VAZIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Geração de parcelas extras |
| **Situação/Requisito:** | Ao utilizar o assistente de geração de parcelas extras de contratos e com a competência vazia não estava sendo possível finalizar a geração. |
| **Solução/Implementação:** | Foi realizado um ajuste para que quando a competência estiver vazia seja gravado o valor nulo no lugar do valor de data mínimo, que era a causa da mensagem de erro apresentada no processo. |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Documento de Referência:** | *N/A* |
