---
content_hash: 5d3a051a1bf28b72b9c4182dc537c7085ea972fbf987ad63ad9d3daaad6c8b10
fetched_at: '2026-06-29T00:08:21.574571+00:00'
page_id: '269060102'
product: rm
source: tdn-rm
title: MEDU_777_DT_Disciplinas_Matriz_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU_777_DT_Disciplinas_Matriz_Curricular
version: 101
---

# DISCIPLINAS DA MATRIZ CURRICULAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Disciplinas da Matriz Curricular* |
| **Situação/Requisito:** | *Ao tentar acessar o cadastro de Disciplina da matriz curricular do aluno o sistema emite o erro: MaxLength applies to string data type only. You cannot set Column 'IDUNIDADEPONTO' property MaxLength to be non-negative number. O mesmo incidente ocorre no cadastro de Disciplinas Optativas e Eletivas da matriz curricular.* |
| **Solução/Implementação:** | *Ajuste no dataset EduTurma e EduDiscGrade para que a coluna IDUNIDADEPONTO seja inteiro e não string.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs

96785
