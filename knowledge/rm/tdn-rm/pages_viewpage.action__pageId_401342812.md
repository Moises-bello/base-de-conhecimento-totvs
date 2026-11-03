---
content_hash: fcfead3d50d5c379dfa26189b17a4f6a508f2a8cc17d887caf1d0605e7a1e3a2
fetched_at: '2026-06-29T00:09:10.589971+00:00'
page_id: '401342812'
product: rm
source: tdn-rm
title: 3733411 DEDUINTEGRACOES-3284 DT Cópia de feriados e eventos acadêmicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=401342812
version: 82
---

# CÓPIA DE FERIADOS E EVENTOS ACADÊMICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Cópia de feriados |
| **Situação/Requisito:** | Sistema não está copiando corretamente os eventos acadêmicos na cópia de eventos entre calendários. Calendário não estava sendo levado em consideração. |
| **Solução/Implementação:** | Consideração do código do calendário na cópia de eventos acadêmicos. O código do calendário não estava sendo considerado e, como existiam dois eventos com o mesmo Id e calendários diferentes, o sistema estava considerando o evento do calendário errado. Ajuste na substituição de dados de um evento acadêmico. O nome do evento não estava sendo atualizado no evento de destino caso o mesmo já existisse. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
