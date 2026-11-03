---
content_hash: 1a147e82d371f63bb8bfa74322c9897b19559e3233874544c70980433fad8abf
fetched_at: '2026-06-29T00:12:02.595850+00:00'
page_id: '901960939'
product: rm
source: tdn-rm
title: Dados do PIS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901960939
version: 5
---

# PIS - Dados do PIS

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **PIS** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **0-1** | **Grupo de Escolha** | **Dados do PIS** |
| CST | PIS | 1-1 | Elemento | TTRBMOV.SITTRIBUTARIA (PIS)  Item do movimento, pasta Tributos   É considerado somente as situações tributarias abaixo:  01 – Tributável com alíquota básica 02 – Tributável com alíquota diferenciada 06 – Tributável com alíquota zero 07 – Operação isenta de contribuição 08 – Operação sem incidência da contribuição 09 – Operação com suspensão da contribuição 49 – Outras operações de saída |
| vBC | PIS | 1-1 | Elemento | TTRBMOV.BASEDECALCULO (PIS)  Item do movimento, pasta Tributos |
| pPIS | PIS | 1-1 | Elemento | TTRBMOV.ALIQUOTA (PIS)  Item do movimento, pasta Tributos |
| vPIS | PIS | 1-1 | Elemento | TTRBMOV.VALOR (PIS)  Item do movimento, pasta Tributos |

Exemploxml

01
100.00
3.00
10.00
]]>
