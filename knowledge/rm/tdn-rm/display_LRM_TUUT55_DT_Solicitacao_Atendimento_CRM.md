---
content_hash: 817646895727d91a6475a8ca95c70ee51e93e4116e7137dc1bbfec11c3c15995
fetched_at: '2026-06-29T00:08:07.285551+00:00'
page_id: '237378389'
product: rm
source: tdn-rm
title: TUUT55_DT_Solicitacao_Atendimento_CRM
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUT55_DT_Solicitacao_Atendimento_CRM
version: 117
---

# SOLICITAÇÃO DE ATENDIMENTO CRM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Solicitação de Atendimento CRM* |
| **Situação/Requisito:** | *Caso a data de solicitação nos parâmetros do educacional estiver definida com a data atual, o sistema não deixa realizar a solicitação. Uma vez que a data de solicitação for definida a partir do dia de hoje por exemplo, 06/05 o sistema deveria deixar a solicitação ser finalizada. Mas o sistema entende que somente a partir do próximo dia que a solicitação pode ser realizada.* |
| **Solução/Implementação:** | *Ajuste no filtro da consulta sql que habilita o botão avançar no processo de solicitação de atendimento (crm), foi necessário formatar a data de hoje em dd/mm/aaaa apenas sem o horário.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
