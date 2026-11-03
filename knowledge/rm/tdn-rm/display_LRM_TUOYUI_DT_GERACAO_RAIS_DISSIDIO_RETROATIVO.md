---
content_hash: 20158fb21533e389330c295bd9b95d6af83de987a7da3d101ebe375781448ec7
fetched_at: '2026-06-29T00:08:03.967939+00:00'
page_id: '235331220'
product: rm
source: tdn-rm
title: TUOYUI_DT_GERACAO_RAIS_DISSIDIO_RETROATIVO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOYUI_DT_GERACAO_RAIS_DISSIDIO_RETROATIVO
version: 116
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | *Rotina RAIS está deduzindo valor de dissídio retroativo do mês errado.* |
| **Solução/Implementação:** | Ajuste em rotina RAIS para buscar valor de dissídio retroativo do mês corretamente para dedução e rateio para seus respectivos meses. A rotina passou a considerar o campo MESREF da tabela PFVERBADIS ao invés da data de pagamento do evento no envelope, dessa forma a rotina considera o mês de competência corretamente para dedução. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUOYUI |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
