---
content_hash: 49f89efafb9a43b81e64485f019888da83003d4d941155e6efc3d9d422efcec6
fetched_at: '2026-06-29T00:06:17.766896+00:00'
page_id: '213985170'
product: rm
source: tdn-rm
title: TTQZC1_DT_Exclusao_Disciplinas_Matriz_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQZC1_DT_Exclusao_Disciplinas_Matriz_Curricular
version: 1
---

# EXCLUSÃO DE DISCIPLINAS DA MATRIZ CURRICULAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Exclusão de disciplinas da matriz curricular* |
| **Situação/Requisito:** | *Após adicionar uma disciplina na Matriz Curricular e em seguida clicar em "Excluir" ocorre o erro: Cadeia de entrada não estava em um formato incorreto.* |
| **Solução/Implementação:** | *Ajuste no método que verifica se a disciplina está associada a alguma turma da matriz, a mesma estava utilizando um filtro que convertia um campo que era string para inteiro.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8 e 12.1.9* |
| **Versão Corrigida:** | *N/A* |
| **Versão Expedida:** | *N/A* |

divs
