---
content_hash: bd36cb5d1850199e9bc4560385a0fc8ccc9bf329f1814141c8b79a38222ee8e2
fetched_at: '2026-06-29T00:08:25.541951+00:00'
page_id: '270917810'
product: rm
source: tdn-rm
title: 349635 MEDU-1933 DT Visão de Lotes Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270917810
version: 113
---

# Visão de Lotes Contábeis

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Atualização da Capa de Lotes Contábeis |
| **Situação/Requisito:** | Interpretação da demanda: Após atualização do patch 12.1.13.136 ao acessar a visão de lotes é apresentado a seguinte mensagem de erro:  All queries combined using a UNION, INTERSECT OR EXCEPT operator must have na equal number of expressions in their target lists. |
| **Solução/Implementação:** | Ajuste no DataServer de lote para que quando o parâmetro "Visualizar lotes sem lançamentos de outros sistemas" estiver marcado as consultas onde existem o comando UNION recebam também a coluna RECCREATEDON. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 349635 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
