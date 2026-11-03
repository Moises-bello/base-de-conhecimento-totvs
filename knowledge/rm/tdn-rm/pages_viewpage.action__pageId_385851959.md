---
content_hash: ec95e762e3e191936dc8b865d146a826ce39e7fbf2e5cd75afe63f08a7fef599
fetched_at: '2026-06-29T00:09:07.851917+00:00'
page_id: '385851959'
product: rm
source: tdn-rm
title: 2900332 CONTROLADORIA01-1797 DT Relatório Razão Sub Contas (RAS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385851959
version: 85
---

# Relatório Razão Sub Contas (RAS)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Razão Sub Contas (RAS) |
| **Situação/Requisito:** | Cliente informa que ao gerar o RAS (razão subcontas) sistema está trazendo um valor de 39,01, na coluna saldo inicial, entretanto o valor não foi informado, e deveria está zerado. |
| **Solução/Implementação:** | Ajuste na consulta que retorna os lançamentos dos itens das subcontas para que o saldo inicial seja formado corretamente com as informações anteriores ao período informado, ou seja o saldo inicial do item da subconta é composto pelo saldo final do período anterior. Exemplo:  Período: 01-01-2017 a 31-12-2017 =>O saldo inicial será formado pelo saldo final apurado até 31-12-2016. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | 2900332 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
