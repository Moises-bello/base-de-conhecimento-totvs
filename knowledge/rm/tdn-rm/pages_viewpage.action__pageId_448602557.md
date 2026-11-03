---
content_hash: 33d96043e5160a891ad00c6c10d8462ad53671d6c3a081cccb9c8d2f9888362d
fetched_at: '2026-06-29T00:09:55.654104+00:00'
page_id: '448602557'
product: rm
source: tdn-rm
title: 4719337 EDUCACIONAL01-7797 DT Exclusão de Disciplinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448602557
version: 78
---

# MATRÍCULA EM DISCIPLINAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula em disciplinas* |
| **Situação/Requisito:** | *Ao excluir uma determinada matrícula em disciplinas o sistema estava retornando um erro de objeto nulo.* |
| **Solução/Implementação:** | ***Foi identificado que a situação ocorre pois ao carregar as disciplinas do aluno, estavam sendo carregadas disciplinas de outros cursos e níveis de ensino, ocasionando a falha ao tentar buscar o status da disciplina que é de outro nível de ensino. Foi feito o ajuste.*** |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
