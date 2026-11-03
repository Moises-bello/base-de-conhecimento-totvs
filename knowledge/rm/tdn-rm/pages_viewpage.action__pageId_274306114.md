---
content_hash: a36dcc6f78971c76f6c1867187a3520fe86bebd1d37041aca4bae3d1cfcf6b89
fetched_at: '2026-06-29T00:08:33.182122+00:00'
page_id: '274306114'
product: rm
source: tdn-rm
title: 746816 EDUCACIONAL01-639 DT Fórmula de Faltas na Digitação de Notas de Etapas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274306114
version: 104
---

# FÓRMULA DE FALTAS NA DIGITAÇÃO DE NOTAS DE ETAPAS

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | **Educacional** |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Digitação de notas de etapas |
| **Situação/Requisito:** | Ao digitar a nota para uma etapa de falta, em casos específicos dependendo da fórmula do cliente, ocorre um erro de inserção do log (SLOGNOTAS) |
| **Solução/Implementação:** | Foi feito um tratamento para que seja possível inserir registro de log quando temos uma violação de chave primária na inserção da SLOGNOTA calculando  uma nova data de inserção no caso de existência de registro com a data a ser considerada na inserção. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
