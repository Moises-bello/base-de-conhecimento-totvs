---
content_hash: 35b35fd5646a7bd19aa98d2b010d42c636ed79680b65541cc40d89d3844ca8a7
fetched_at: '2026-06-29T00:12:02.579142+00:00'
page_id: '901960637'
product: rm
source: tdn-rm
title: ICMS Outros (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960637
version: 3
---

# ICMS90 - ICMS Outros

Este grupo será gerado sempre que o CFOP informado no item estiver configurado com o CST 90

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ICMS90** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **1-1** | **Grupo de Escolha** | **ICMS Outros** |
| CST | ICMS90 | 1-1 | Elemento | DREGRAICMS.SITTRIBUTARIA |
| **--- x — Sequência opcional do XML:** Será gerado sempre o que o **Valor do ICMS** do item for **maior que zero** | | | | |
| vBC | ICMS90 | 1-1 | Elemento da Sequencia | TTRBMOV.BASEDECALCULO (ICMS)  Item do movimento, pasta Tributos e Valores |
| pICMS | ICMS90 | 1-1 | Elemento da Sequencia | TTRBMOV.ALIQUOTA (ICMS)  Item do movimento, pasta Tributos e Valores |
| vICMS | ICMS90 | 1-1 | Elemento da Sequencia | TTRBMOV.VALOR (ICMS)  Item do movimento, pasta Tributos e Valores |

Exemploxml
90
301.98
12.00
36.24
]]>
