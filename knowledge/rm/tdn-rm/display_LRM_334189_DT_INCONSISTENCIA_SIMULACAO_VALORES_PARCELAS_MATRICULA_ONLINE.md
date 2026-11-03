---
content_hash: 91f1e6914a9ffe331bb281e9b9c3a9ac4953fa6dd05ad54c783e153b8828a86c
fetched_at: '2026-06-29T00:08:25.065304+00:00'
page_id: '270911762'
product: rm
source: tdn-rm
title: 334189_DT_INCONSISTENCIA_SIMULACAO_VALORES_PARCELAS_MATRICULA_ONLINE
type: documentation
url: https://tdn.totvs.com/display/LRM/334189_DT_INCONSISTENCIA_SIMULACAO_VALORES_PARCELAS_MATRICULA_ONLINE
version: 109
---

# Simulação de valores de parcelas na matrícula online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Matrícula Online |
| **Situação/Requisito:** | As disciplinas que não são da grade do aluno, não estavam respeitando o parâmetro "conta credito financeiro(cobrança por credito)" no status da disciplina na simulação de parcela do portal. |
| **Solução/Implementação:** | Ajuste na query que retorna se a disciplina conta como créditos de cobrança a fim de que esse valor não seja nulo quando a disciplina for equivalente. Foi excluído o JOIN com o campo IDHABILITACAOFILIAL pois esse campo é diferente entre a matrícula do aluno e a disciplina equivalente.  Feito também um tratamento para que os valores de disciplinas equivalentes obedecessem o parâmetro "conta credito financeiro(cobrança por credito)" do status da disciplina. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | MEDU-1871 |
| **Requisito (informe o requisito relacionado):** |  |

divs
