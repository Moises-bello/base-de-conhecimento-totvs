---
content_hash: 695a023461153fee5d09ce6083f484a6ee63d87938ecc368a0ee79d5eb8d2f3a
fetched_at: '2026-06-29T00:08:44.600833+00:00'
page_id: '309397389'
product: rm
source: tdn-rm
title: 1566373 DEDUINTEGRACOES-824 DT Erro ao gerar movimento para lançamentos baixados
  por acordo com boleto cancelado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309397389
version: 95
---

# GERAÇÃO DE MOVIMENTOS PARA BOLETOS CANCELADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Geração de movimentos |
| **Situação/Requisito:** | Erro ao gerar movimento para lançamentos baixados por acordo  com boleto cancelado |
| **Solução/Implementação:** | Ajuste para permitir geração de movimento para boletos cancelados por acordo. O erro ocorria porque o acordo para lançamentos únicos de um boleto seta o status do boleto para cancelado e, como fazíamos a validação de boletos cancelados sem verificar se o mesmo foi originado por um acordo, não conseguíamos emitir nota fiscal para lançamentos baixados por acordo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
