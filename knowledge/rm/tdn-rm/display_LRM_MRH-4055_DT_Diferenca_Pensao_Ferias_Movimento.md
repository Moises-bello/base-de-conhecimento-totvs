---
content_hash: cd19373158f2b99808c8c0c38a60094548c3fafbcc8aa604b8d35b635a02994c
fetched_at: '2026-06-29T00:08:25.501033+00:00'
page_id: '270916391'
product: rm
source: tdn-rm
title: MRH-4055_DT_Diferenca_Pensao_Ferias_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-4055_DT_Diferenca_Pensao_Ferias_Movimento
version: 111
---

# DIFERENÇA DE PENSÃO DE FÉRIAS GRAVANDO MOVIMENTO INCORRETO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de Férias* |
| **Situação/Requisito:** | *Quando é calculada diferença de pensão de férias com mais de um dependente, onde existe um pensionista atual que no mês original não era dependente de pensão, no movimento de pensão deste dependente está sendo informado -1.* |
| **Solução/Implementação:** | *Ajuste no cálculo da diferença de pensão de férias, para não informar nenhum valor no movimento de pensão, quando o pensionista não era dependente de pensão no mês original.* |
| **Chamados relacionados:** | MRH-4055 |
| **Requisito (ISSUE):** | MRH-4055 |

divs
