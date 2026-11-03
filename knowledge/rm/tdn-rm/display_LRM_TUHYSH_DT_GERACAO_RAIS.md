---
content_hash: 1af462687080d226c06f4dddff69645535cbea22535df46d76eb9ab66c692142
fetched_at: '2026-06-29T00:06:27.191700+00:00'
page_id: '231899506'
product: rm
source: tdn-rm
title: TUHYSH_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHYSH_DT_GERACAO_RAIS
version: 121
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Erro no validador da RAIS alegando tipo de demissão inconsistente |
| **Solução/Implementação:** | Ajuste em rotina RAIS para considerar soma de data de inicio do aviso com número de dias de aviso deduzido de dia (pois a soma já contempla a data de início) evitando assim casos de projeção de aviso prévio que finalizam em 31/12/AnoBase (data limite do ano base) |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUHYSH TUIYIA |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.10* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
