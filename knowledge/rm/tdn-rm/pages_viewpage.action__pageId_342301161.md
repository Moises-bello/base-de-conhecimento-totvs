---
content_hash: 808029eef25e32fbdfd9313c165da657c27bc988b04eb83708844a5501ec325e
fetched_at: '2026-06-29T00:08:52.703681+00:00'
page_id: '342301161'
product: rm
source: tdn-rm
title: 2202097 DEDUINTEGRACOES-1762 DT Geração de movimentos não gera todos os movimentos
  do filtro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342301161
version: 90
---

# GERAÇÃO DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de movimentos em regime de caixa |
| **Situação/Requisito:** | Ao gerar movimento em regime de caixa para vários boletos, caso o processamento encontre um boleto cancelados, o processo é abortado, não gerando movimento para os boletos subsequentes. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de movimentos, em regime de caixa, de forma que o sistema não aborte a execução do processo quando existirem boletos a serem processados e o sistema se deparar com um boleto cancelado.. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | [#2675703](https://totvssuporte.zendesk.com/agent/tickets/2675703 "Open ticket in Zendesk Support") |
| **Requisito:** | N/A. |

divs
