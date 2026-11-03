---
content_hash: 171f648923672f72bdc2b5b40a880395e7ce67a912b9cda16c0bbdeec70bf10f
fetched_at: '2026-06-29T00:06:27.922682+00:00'
page_id: '233738892'
product: rm
source: tdn-rm
title: TUIAKP_DT_Exclusao_Disciplina_Matriz_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIAKP_DT_Exclusao_Disciplina_Matriz_Curricular
version: 122
---

# EXCLUSÃO DE DISCIPLINA DA MATRIZ CURRICULAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Exclusão da Disciplina na Matriz Curricular* |
| **Situação/Requisito:** | *Ao tentar excluir disciplina de uma matriz curricular que foi originada pelo processo de cópia de matriz curricular, o sistema emite o seguinte erro: "Não é possível excluir a disciplina. Ela já está associada à uma turma." A consistência é indevida, pois a nova matriz não possui turma associada. O mesmo acontece quando se tenta excluir um disciplina X de uma matriz Y que não possui nenhum vínculo de turma na matriz Y, entretanto a mesma disciplina X possui vínculo com uma turma Z em uma outra matriz.* |
| **Solução/Implementação:** | *Ajuste na consulta que valida se uma disciplina possui turma associada inserindo em seu filtro o campo CODGRADE, para que seja verificado apenas na grade onde está sendo feito a tentativa de exclusão.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUK526, TUIP61* |
| **Requisito (ISSUE):** | *N/A* |

divs
