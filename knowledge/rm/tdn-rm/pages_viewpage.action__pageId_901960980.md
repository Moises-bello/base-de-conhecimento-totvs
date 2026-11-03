---
content_hash: b9c43423acca8d2883d724f2208058441ae93f6e9ce14469c09f4c129fc00ec1
fetched_at: '2026-06-29T00:12:02.600885+00:00'
page_id: '901960980'
product: rm
source: tdn-rm
title: Dados do COFINS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960980
version: 5
---

# COFINS - Dados do COFINS

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **COFINS** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **0-1** | **Grupo de Escolha** | **Dados do COFINS** |
| CST | COFINS | 1-1 | Elemento | TTRBMOV.SITTRIBUTARIA (COFINS)  Item do movimento, pasta Tributos   É considerado somente as situações tributarias abaixo:  01 – Tributável com alíquota básica 02 – Tributável com alíquota diferenciada 06 – Tributável com alíquota zero 07 – Operação isenta de contribuição 08 – Operação sem incidência da contribuição 09 – Operação com suspensão da contribuição 49 – Outras operações de saída |
| vBC | COFINS | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (COFINS)  Item do movimento, pasta Tributos |
| pCOFINS | COFINS | 1-1 | Elemento | TTRBMOV.ALIQUOTA (COFINS)  Item do movimento, pasta Tributos |
| vCOFINS | COFINS | 1-1 | Elemento | TTRBMOV.VALOR (COFINS)  Item do movimento, pasta Tributos |

Exemploxml

01
100.00
7.60
10.00
]]>
