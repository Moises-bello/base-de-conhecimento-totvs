---
content_hash: a2b6a64c463101027f43dd0aa27c231961663d2082a96f699a51a7f9a9b5e92e
fetched_at: '2026-06-29T00:12:02.612677+00:00'
page_id: '901961116'
product: rm
source: tdn-rm
title: Grupo de informações de retenção de tributos federais (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901961116
version: 6
---

# retTrib - Grupo de informações de retenção de tributos federais

Layout

Ao gerar um dos impostos pertencentes a esse grupo, os demais serão classificados como obrigatórios e, caso não sejam informados no movimento, o sistema irá gerar de forma automática as tags dos tributos ausentes com valores zerados.

Campos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **retTrib** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **0-1** | **Grupo de Escolha** | **Grupo de informações de retenção de tributos federais** |
| vRetPIS | retTrib | 1-1 | Elemento | TTRBMOV.VALOR (PISRF)  Item do movimento, pasta Tributos |
| vRetCofins | retTrib | 1-1 | Elemento | TTRBMOV.VALOR (COFINSRF)  Item do movimento, pasta Tributos |
| vRetCSLL | retTrib | 1-1 | Elemento | TTRBMOV.VALOR (CSLLRF)  Item do movimento, pasta Tributos |
| vBCIRRF | retTrib | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (IRRF)  Item do movimento, pasta Tributos |
| vIRRF | retTrib | 1-1 | Elemento | TTRBMOV.VALOR (IRRF)  Item do movimento, pasta Tributos |

Exemploxml
0
0
0
0
0
]]>
