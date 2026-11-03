---
content_hash: 211790d47aa20f95e65ffe22767138f37b37a38829c85798f461f528545aaec4
fetched_at: '2026-06-29T00:06:17.866130+00:00'
page_id: '213986053'
product: rm
source: tdn-rm
title: TTRJNH_DT_Exclusao_Disciplinas_Matriz_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRJNH_DT_Exclusao_Disciplinas_Matriz_Curricular
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
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *N/A* |
| **Versão Expedida:** | *N/A* |

divs
