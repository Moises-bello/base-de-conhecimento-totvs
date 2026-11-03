---
content_hash: 0d39b359dabe3826ac3ca8824f963ac137f14218afe2ef2c594a80c1ac783987
fetched_at: '2026-06-29T00:08:21.964021+00:00'
page_id: '269070299'
product: rm
source: tdn-rm
title: 120946_DT_Recibo_Multa_Gerado_Sem_Multa
type: documentation
url: https://tdn.totvs.com/display/LRM/120946_DT_Recibo_Multa_Gerado_Sem_Multa
version: 110
---

# MOVIMENTAÇÕES - EMISSÃO DE RECIBO DE MULTA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Movimentações - emissão de recibo de multa* |
| **Situação/Requisito:** | *Quando o parâmetro para emitir recibo de multa na operação de devolução está selecionado, o relatório de multa é gerado todas as vezes que uma devolução é feita, mesmo para devoluções dentro do prazo e que não tenham multa.* |
| **Solução/Implementação:** | *Foi identificado que a única validação que o sistema faz para emitir o relatório de multa é se o parâmetro está marcado, sendo assim, foi inserido uma validação pelo total da multa, ou seja, para que o relatório seja gerado é necessário que o parâmetro esteja marcado e o empréstimos não tenha multa.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
