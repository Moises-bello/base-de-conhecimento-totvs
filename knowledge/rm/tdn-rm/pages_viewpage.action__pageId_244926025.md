---
content_hash: 83293a3242c82873aea77e37b53244d67cabaa6c6d37724dfd92ec10b50adf01
fetched_at: '2026-06-29T00:08:15.862594+00:00'
page_id: '244926025'
product: rm
source: tdn-rm
title: TVOCLF_DT_Contabilização_Com_Operação_Inválida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244926025
version: 110
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *O comportamento atual permitia ao sistema não tentar a contabilização de um evento que não tivesse tido as partidas contábeis carregadas durante o processamento do evento contábil, sem acusar erro no processamento, permitindo que somente contabilizações de apropriação de contrato fossem geradas, caso o evento tenha fórmulas desenvolvidas para esse fim. Assim, ao ser gerada contabilização de uma parcela mensal, caso o sistema não conseguisse carregar as partidas do evento contábil, não era gerada a contabilização no sistema Contábil, porém a parcela mensal passava a ser considerada como como contabilizada.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de contabilização por competência, de forma a não permitir que uma apropriação mensal seja concluída com sucesso, caso o sistema não consiga carregar as partidas contábeis do evento utilizado.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.13* |
| **Versão Corrigida:** | *12.1.13* |
| **Versão Expedida:** | *12.1.13* |

divs
