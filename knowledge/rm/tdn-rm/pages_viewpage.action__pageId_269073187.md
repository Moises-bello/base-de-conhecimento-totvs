---
content_hash: c120c1fb9299585779fcf43f5d271ff6663037c5971f2e263aa03a35b738f4ba
fetched_at: '2026-06-29T00:08:22.116683+00:00'
page_id: '269073187'
product: rm
source: tdn-rm
title: 166383_Simulação_Parcela_Matricula_Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269073187
version: 107
---

# Matricula Online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Simulação de Parcela na Matricula Online |
| **Situação/Requisito:** | Quando o número de créditos financeiro é alterado diretamente na disciplina matriculada no período letivo não está refletindo na simulação de parcelas disponibilizada no portal do aluno no momento da matricula online.  Já na simulação de parcelas do sistema (MDI) está correto. |
| **Solução/Implementação:** | Melhoria na simulação de parcelas disponível na matricula online para que o número de créditos financeiros a ser considerado seja o número de créditos informado na disciplina matriculada (SMATRICULA.NUMCREDITOSCOB), se esta informação não estiver preenchida o sistema considera o número de créditos financeiro definido na disciplina da grade. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-990 |
| **Requisito (ISSUE):** |  |

divs
