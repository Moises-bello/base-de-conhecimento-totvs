---
content_hash: 0aea3897df1822b853757a25c08ea69879a81ca26bdd008321fed777a0d2faca
fetched_at: '2026-06-29T00:08:19.478534+00:00'
page_id: '267788163'
product: rm
source: tdn-rm
title: TVXITP_DT_Visao_Emprestimos_Duplicado_Mais_DeUM_RA
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXITP_DT_Visao_Emprestimos_Duplicado_Mais_DeUM_RA
version: 112
---

# VISÃO DE EMPRÉSTIMOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Visão de empréstimos* |
| **Situação/Requisito:** | *Quando o usuário da biblioteca possui mais de um registro acadêmico (RA) no educacional, a visão de empréstimos repete o empréstimo pela quantidade de registros acadêmicos que o usuário tiver, porém não está repetido na base dados, somente na visão.* |
| **Solução/Implementação:** | *Foi identificado uma inconsistência na consulta que repetia os empréstimos no caso de mais de um RA, foi feito o ajuste na consulta sql que retorna a visão de empréstimos para que não repita os empréstimos porém concatene os RA's em um único registro da visão.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
