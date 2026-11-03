---
content_hash: 47cb4dc71b4a6ae46e4329a237bdeca43c62838901e0ae58b8ea73c150342bab
fetched_at: '2026-06-29T00:06:22.381884+00:00'
page_id: '223916074'
product: rm
source: tdn-rm
title: TTYWA2_DT_Contabilização_Contrato_Lancamentos_Cancelados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223916074
version: 124
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
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
