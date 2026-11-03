---
content_hash: c2733d59fdf7c0fef4b53de48314869d92c56f64f4cbd0a66ae040d92b68ccc8
fetched_at: '2026-06-29T00:08:26.452211+00:00'
page_id: '271180601'
product: rm
source: tdn-rm
title: 120367 MRH-2182 DT Planejamento de Despesas
type: documentation
url: https://tdn.totvs.com/display/LRM/120367+MRH-2182+DT+Planejamento+de+Despesas
version: 107
---

# PLANEJAMENTO DE DESPESAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Planejamento de Despesas |
| **Situação/Requisito:** | Quando se executa o planejamento de rateio de despesas, o valor apresentado no saldo disponível está negativo. |
| **Solução/Implementação:** | Tinha um problema na consulta que não considerava o CODCCUSTO como filtro, assim o calculo era feito sobre todo o valor. Assim foi colocado a condição para resolver o problema. Mas não deve ser colocado o valor total do Rateio de Despesa maior que o estipulado no Planejamento de Despesas se não a disponibilidade ficará negativa, que informa que foi colocado um valor superior ao planejado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-2182 |
| **Requisito (ISSUE):** |  |

divs
