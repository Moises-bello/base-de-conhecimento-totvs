---
content_hash: e58f185c61c42b60db9a84f6223b1c619abbd8513905e891c6eb4a5d39770e96
fetched_at: '2026-06-29T00:09:00.957106+00:00'
page_id: '370613257'
product: rm
source: tdn-rm
title: 3060971 DEDUINTEGRACOES-2565 DT Erro ao gerar lançamento com faixas de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370613257
version: 88
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Erro ao gerar lançamento estava ocorrendo erro para contratos com cancelamento parcial e cancelamento total ao mesmo tempo. Para essa situação específica, o sistema não estava passando o parâmetro de data de matrícula para a consulta SQL, causando o erro reportado. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, para cenários que utilizam cálculo por crédito, através do uso de faixas de crédito, para quando existem cancelamento total de cancelamento parcial juntos em um mesmo contrato. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
