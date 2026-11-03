---
content_hash: f589a6dcdf1f2c8b1a1fc48fcc4b0ee6d2fc2ab960be7d4cc10e27c6213ad506
fetched_at: '2026-07-02T19:24:22.537091+00:00'
page_id: '270903189'
product: protheus
source: tdn-tec
title: COMPILADOR 4GL - Consistência para elementos de record like não definidos no
  arquivo de schema.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270903189
version: 3
---

|  |  |
| --- | --- |
| Situação | COMPILADOR 4GL - Consistência para elementos de record like não definidos no arquivo de schema. |
| Ocorrência | Elementos de uma variável do tipo RECORD LIKE (4GL) definidos de acordo com arquivo de schema, não eram verificados na compilação. |
| Correção | Correção na consistência de elementos de acordo com o arquivo de schema onde caso o elemento não exista no arquivo, a compilação é interrompida. |
| Informações adicionais | * Referente à ocorrência: TTEC-1060 * Disponível a partir do build 7.00.131227a - 1.3.2 |
