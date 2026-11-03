---
content_hash: 9fe2ea3db153f6e95da9dedc3595f49ef4eba12cd017ad53098f1967ba52d0c4
fetched_at: '2026-06-29T00:08:11.546784+00:00'
page_id: '243012527'
product: rm
source: tdn-rm
title: TVCPVP_DT_Periodo_Bloqueado_Campo_Hora_Desbloqueado
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCPVP_DT_Periodo_Bloqueado_Campo_Hora_Desbloqueado
version: 114
---

# ENVELOPE DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope de Pagamento* |
| **Situação/Requisito:** | Ao bloquear o período 1 e 3 do envelope de pagamento e acessar um evento do tipo hora no período 3, o campo hora fica habilitado deixando alterar a hora, porem o envelope não recalculado devido ao período ser bloqueado, mas a informação da hora é permitida ser alterada, ao acessar o período 1 o evento do tipo hora possui o campo hora bloqueado, e ao selecionar o período todos e acessar o evento do período 1 e 3 o campo hora está bloqueado, e ao acessar no mesmo momento o período 3 o campo hora está bloqueado. |
| **Solução/Implementação:** | Ajustado regra se deve ou não permitir a edição do campo Hora no envelope  de pagamento quando o período está bloqueado. |
| **Chamados relacionados:** | *TVCPVP* |

divs
