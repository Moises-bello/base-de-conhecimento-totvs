---
content_hash: 060b1e159f622659c72011d4d3aeda839adb11bfde56ac1777fe5bd5c1c7ccb0
fetched_at: '2026-06-29T00:12:10.237234+00:00'
page_id: '953000530'
product: rm
source: tdn-rm
title: Grupo H – Detalhamento de produtos e serviços da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000530
version: 6
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupo H – Detalhamento de produtos e serviços da NF-e** | | | | |
| **Campo** | **Ele** | **Pai** | **Ocorrência** | **Campo de Origem** |
| **det** | **G** | **A01** | **1-990** |  |
| nitem | A | H01 | 1-1 | TITMMOV.NUMEROSEQUENCIAL |
| vItem | E | H01 | 0-1 | A tag **`vItem`** representa o **valor total de cada item** da NF-e. Até **31/12/2026**, seu cálculo deve considerar:   * **Valor do produto (`vProd`)** * **(-)** Descontos (`vDesc`) * **(+)** Frete, seguro e outras despesas * **(+)** Impostos aplicáveis (ex.: ICMS ST, II, IPI etc.)   🚫 **Importante:** tributos **IBS, CBS e IS não compõem** o `vItem` até essa data.  Observação: Qualquer dúvida conferir a NT 2025 002\_1.30. |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupo VC. Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e** | | | | |
| **Campo** | **Ele** | **Pai** | **Ocorrência** | **Campo de Origem** |
| DFeReferenciado | **G** | **H01** | **1-990** |  |
| chaveAcesso | E | VC01 | 1-1 |  |
| nItem | E | VC01 | 0-1 |  |
