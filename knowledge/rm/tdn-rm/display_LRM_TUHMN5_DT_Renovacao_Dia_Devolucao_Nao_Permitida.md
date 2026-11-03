---
content_hash: 98c4c4cce79f16e2473c4054668fef56d01de83d9a48b8f640b1cdc96dc03139
fetched_at: '2026-06-29T00:06:28.058595+00:00'
page_id: '233744941'
product: rm
source: tdn-rm
title: TUHMN5_DT_Renovacao_Dia_Devolucao_Nao_Permitida
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHMN5_DT_Renovacao_Dia_Devolucao_Nao_Permitida
version: 118
---

# MOVIMENTAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentações - Renovação* |
| **Situação/Requisito:** | *Foi identificado que mesmo com o parâmetro marcado para permitir renovações somente na data de devolução o sistema não estava permitindo a renovação.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado por uma inconsistência na comparação da data atual com a data prevista de devolução de empréstimo, que na data prevista considera data e hora e a data atual somente a data, sem considerar a hora, o que gerava a diferença das datas. Foi feito o ajuste para que ambas as datas utilizem somente o valor de data na comparação, evitando assim a diferença.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUKLZ2* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.11* |
| **Versão Corrigida:** | *11.82.43*  *12.1.11* |
| **Versão Expedida:** | *11.82.43*  *12.1.11* |

divs
