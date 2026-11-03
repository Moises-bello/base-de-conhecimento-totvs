---
content_hash: db2523965c8807e844f5268034c4fc49d83f49bb2978d1894280353b2b9eab8d
fetched_at: '2026-06-29T00:08:41.252007+00:00'
page_id: '286521241'
product: rm
source: tdn-rm
title: 1194257 FINANCEIRO01-2001 DT CnabAceite com valor nulo.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286521241
version: 103
---

# Campo CnabAceite com valor null

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de Boleto |
| **Situação/Requisito:** | Ao salvar um boleto o sistema está informando valor nulo no campo CNABACEITE sendo que o valor deve ser entre 0 e 1. |
| **Solução/Implementação:** | Agora caso o campo seja enviado como nulo, será salvo valor 0. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1149857, 1224246, 1248560, 1256344, 1261525, 1268935 |
| **Requisito:** | FIN000268 |

divs
