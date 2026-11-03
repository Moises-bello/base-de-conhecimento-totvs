---
content_hash: e8fc89da887194a7dce5bf23b4f57e111595fc2088c5613fbcbfd5c5d5460150
fetched_at: '2026-06-29T00:12:10.841577+00:00'
page_id: '953003755'
product: rm
source: tdn-rm
title: Grupo ZC - Informações do Registro de Aquisição de Cana
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003755
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo ZC - Informações do Registro de Aquisição de Cana** | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Mais Informações** |
| 409 | ZC01 | cana | Grupo Cana | G | A01 |  | 0-1 |  | Informações de registro aquisições de cana v2.0 | NÃO SERÁ GERADO |
| 410 | ZC02 | safra | Identificação da safra | E | ZC01 | C | 1-1 | 4-9 | Informar a safra, no formato: "AAAA" ou "AAAA/AAAA". v2.0 | NÃO SERÁ GERADO |
| 411 | ZC03 | ref | Mês e ano de referência | E | ZC01 | C | 1-1 | 7 | Informar o mês e ano de referência, no formato: "MM/AAAA". v2.0 | NÃO SERÁ GERADO |
| 412 | ZC04 | forDia | Grupo Fornecimento diário de cana | G | ZC01 |  | 1-31 |  | Informar os fornecimentos diários de cana v2.0 | NÃO SERÁ GERADO |
| 427 | ZC05 | dia | Dia | A | ZC04 | N | 1-1 | 1-2 | v2.0 | NÃO SERÁ GERADO |
| 414 | ZC06 | dia | Quantidade | E | ZC04 | N | 1-1 | 11v10 | Quantidade em KG v2.0 | NÃO SERÁ GERADO |
| 415 | ZC07 | qTotMes | Quantidade Total do Mês | E | ZC01 | N | 1-1 | 11v10 | v2.0 | NÃO SERÁ GERADO |
| 416 | ZC08 | qTotAnt | Quantidade Total Anterior | E | ZC01 | N | 1-1 | 11v10 | v2.0 | NÃO SERÁ GERADO |
| 417 | ZC09 | qTotGer | Quantidade Total Geral | E | ZC01 | N | 1-1 | 11v10 | v2.0 | NÃO SERÁ GERADO |
| 418 | ZC10 | deduc | Grupo Deduções – Taxas e Contribuições | G | ZC01 |  | 0-10 |  | Informar as Deduções – Taxas e Contribuições v2.0 | NÃO SERÁ GERADO |
| 419 | ZC11 | xDed | Descrição da Dedução | E | ZC10 | C | 1-1 | 1-60 | Informar a Descrição da Dedução v2.0 | NÃO SERÁ GERADO |
| 420 | ZC12 | xDed | Valor da Dedução | E | ZC10 | N | 1-1 | 13v2 | v2.0 | NÃO SERÁ GERADO |
| 421 | ZC13 | vFor | Valor dos Fornecimentos | E | ZC01 | N | 1-1 | 13v2 | Valor dos Fornecimentos v2.0 | NÃO SERÁ GERADO |
| 422 | ZC14 | vFor | Valor Total da Dedução | E | ZC01 | N | 1-1 | 13v2 | Valor das deduções v2.0 | NÃO SERÁ GERADO |
| 423 | ZC15 | vFor | Valor Líquido dos Fornecimentos | E | ZC01 | N | 1-1 | 13v2 | Valor Líquido dos Fornecimentos v2.0 | NÃO SERÁ GERADO |
