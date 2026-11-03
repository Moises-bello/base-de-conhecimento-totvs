---
content_hash: e686168b837cb188be5339527032674454b6d64b19c1836eedae48754ab7949f
fetched_at: '2026-06-29T00:09:04.190947+00:00'
page_id: '382558797'
product: rm
source: tdn-rm
title: DSAUGHFATF-855 - Duplicidade de Vigências em Emissão de Fatura para Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382558797
version: 1
---

# Duplicidade de Vigências em Emissão de Fatura para Convênio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Função:** | Emissão de Fatura para Convênios |
| **Situação/Requisito:** | O sistema não estava levando em consideração a DATA\_VIGENCIA  ao trazer a lista de convênios  da tela "Emissão de Fatura para Convênios",  isso fazia com que a lista trouxesse convênios duplicados. |
| **Solução/Implementação:** | Foi alterada a consulta para considerar a vigência na lista de convênios. |
| **Tickets relacionados:** | <https://totvssuporte.zendesk.com/agent/tickets/3022502> |
