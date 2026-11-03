---
content_hash: 1fde166f81d7964f141594c6d360985a421138ddde31d069dd6d32d4d300b56b
fetched_at: '2026-06-29T00:08:28.348153+00:00'
page_id: '271675618'
product: rm
source: tdn-rm
title: MEDU-2483 DT Valores de créditos matriculados em turma livre não pertencente
  à grade do aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271675618
version: 113
---

# VALORES DE CRÉDITOS MATRICULADOS EM TURMA LIVRE NÃO PERTENCENTE À GRADE DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de lançamentos / Simulação de valores de parcelas / Simulação de valores na matrícula online* |
| **Situação/Requisito:** | *Sistema não considera o parâmetro "Usar valor do crédito financeiro da matriz do aluno" na geração de lançamentos ou simulação de valores no contrato e simulação de valores na matrícula online. Os valores considerados eram sempre os valores cadastrados na turma disciplina matriculada.* |
| **Solução/Implementação:** | *O parâmetro 'Usar valor do credito financeiro da matriz do aluno' passou a ser verificado na obtenção de valores de créditos para disciplinas matriculadas de turmas livres que não estão na grade do aluno. Se o parâmetro estiver MARCADO, será buscado o valor da disciplina equivalente (caso o valor seja maior que zero). Se o parâmetro estiver DESMARCADO, o sistema continuará obtendo o valor de créditos da turma disciplina matriculada.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
