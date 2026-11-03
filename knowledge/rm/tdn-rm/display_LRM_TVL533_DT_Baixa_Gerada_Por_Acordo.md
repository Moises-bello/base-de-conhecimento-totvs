---
content_hash: 2eda41d5bc370bb2a279088781e6050ceea215d1e2e5703c666e4be5e312dfc5
fetched_at: '2026-06-29T00:08:15.083123+00:00'
page_id: '244728573'
product: rm
source: tdn-rm
title: TVL533_DT_Baixa_Gerada_Por_Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVL533_DT_Baixa_Gerada_Por_Acordo
version: 114
---

# Geração de Acordo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Geração de Acordo |
| **Situação/Requisito:** | Ao efetuar um acordo para um lançamento na segunda moeda e conta caixa em moeda local, o sistema não está convertendo corretamente o item de baixa do lançamento de acordo, gerando contabilização inconsistente. |
| **Solução/Implementação:** | Ajuste no serviço de baixa por Acordo para que nos cenários em que o lançamento esta em moeda estrangeira e a conta caixa em moeda local o item de baixa seja convertido para cotação. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000084 |

divs
