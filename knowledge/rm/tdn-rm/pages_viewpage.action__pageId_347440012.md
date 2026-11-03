---
content_hash: aa13afa6a2b6a38d931faca493e46c0f33447cc97b09b4ecb2c0b49c70b26121
fetched_at: '2026-06-29T00:08:54.875446+00:00'
page_id: '347440012'
product: rm
source: tdn-rm
title: 2464257 DEDUINTEGRACOES-2120 DT Geração de lançamentos com aproveitamento de
  crédito em conta corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=347440012
version: 88
---

# GERAÇÃO DE LANÇAMENTO COM APROVEITAMENTO DE CRÉDITO EM CONTA CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Não esta sendo possível gerar lançamento com aproveitamento de valores quando temos mais créditos que o valor líquido do lançamento. |
| **Solução/Implementação:** | Consideração somente do valor líquido do lançamento sem considerar o valor já aplicado tendo em vista que o valor líquido do lançamento, há algum tempo atrás, passou a ser cálculado em memória. E, como o cálculo está sendo feito em memória, os valores aplicados em conta corrente já são considerados para o valor líquido do lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
