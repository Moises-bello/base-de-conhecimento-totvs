---
content_hash: 06fd75dcc06f190e8c6b58e11662b75411fc7ee27b7ddc845e4e5c8617a65ab7
fetched_at: '2026-06-29T00:08:36.036861+00:00'
page_id: '284332114'
product: rm
source: tdn-rm
title: CONTROLADORIA01-239 DT Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284332114
version: 96
---

# Plano de Contas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | Plano de Contas. |
| **Situação/Requisito:** | Ao executar o relatório Plano de Contas a seguinte mensagem é apresentada: " Object reference not set to an instance of an object. " Essa mensagem está relacionada a consulta feita no Oracle com o comando IN (...). |
| **Solução/Implementação:** | Ajuste no filtro da query que gera o relatório Plano de Contas para quebrar a instrução "IN" em partes menores para que o RDB possa executar a consulta. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
