---
content_hash: b51cb729f03581d59ee88a785fb1ca5efe0514d51304364a75313bc3fb497618
fetched_at: '2026-06-29T00:08:19.436250+00:00'
page_id: '267786444'
product: rm
source: tdn-rm
title: TVUVO8_DT_Diario_De_Classe
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUVO8_DT_Diario_De_Classe
version: 114
---

# DIÁRIO DE CLASSE - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Diário de classe* |
| **Situação/Requisito:** | *Ao realizar a pesquisa em um etapa no diário de classe no portal, uma mensagem de erro de objeto não referenciado é apresentada.* |
| **Solução/Implementação:** | *Foi identificado que tentar realizar uma pesquisa em uma turma/disciplina que não possui alunos matriculados, o sistema realiza uma validação considerando uma informação que apenas preenchida quando a turma/disciplina possui algum aluno matriculado. Foi realizado um tratamento para que o sistema execute as pesquisa independente se a turma/disciplina possui ou não alunos.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
