---
content_hash: 6347b6f259995fa73e20bf3e58f7c47e08a2de9074dccb176929aef643094924
fetched_at: '2026-06-29T00:08:25.560988+00:00'
page_id: '270918735'
product: rm
source: tdn-rm
title: MRH-4179_DT_Diferenca_Pensao_Ferias_RRA
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-4179_DT_Diferenca_Pensao_Ferias_RRA
version: 111
---

# DIFERENÇA DE PENSÃO DE FERIAS NÃO LANÇA VALOR DE RRA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de Férias* |
| **Situação/Requisito:** | *Quando o funcionário não teve o desconto de pensão no recibo de férias e é feito o cálculo da diferença de férias com um dependente configurado com data retroativa, é feito o cálculo e lançado o valor encontrado no evento de código de cálculo 197 - DIFERENÇA DE PENSÃO ALIMENTÍCIA FÉRIAS, porém não é lançado o evento de CC 210 - PENSÃO ALIMENTÍCIA JUDICIAL RRA FÉRIAS.* |
| **Solução/Implementação:** | *Ajuste no cálculo da diferença de pensão de férias para lançar o CC 210 mesmo quando o funcionário não teve o desconto de pensão no recibo de férias original.* |
| **Chamados relacionados:** | MRH-4179 |
| **Requisito (ISSUE):** | MRH-4179 |

divs
