---
content_hash: dbf3efd68c0937b9e5a5862975d9174cab923f50621bcdda91ed286d6156dba2
fetched_at: '2026-06-29T00:06:22.317185+00:00'
page_id: '223914216'
product: rm
source: tdn-rm
title: TTYMBH_DT_Contabilização_Contrato_Lancamentos_Cancelados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223914216
version: 120
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | Ao gerar a contabilização para um contrato que possuas parcelas cujos os lançamentos financeiros estão baixados, porém haviam sido cancelados anteriormente, os valores da contabilização para serviço e bolsa estão fincando incorretos. Como o status final da parcela é baixado, o valor original não precisaria ser calculado. |
| **Solução/Implementação:** | *Foi realizada otimização do processo de simulação de parcelas de um contrato, de forma que lançamentos cancelados não sejam processados em caso de existir um lançamento baixado para a parcela.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
