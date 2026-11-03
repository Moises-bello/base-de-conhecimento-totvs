---
content_hash: 6b9f35b4ca5ab9bc04813751405d928e014a7972ec0b988b6545b572ad437f01
fetched_at: '2026-06-29T00:06:25.888762+00:00'
page_id: '224450046'
product: rm
source: tdn-rm
title: TUEWH1_DT_Enturmacao_Turma_Mista
type: documentation
url: https://tdn.totvs.com/display/LRM/TUEWH1_DT_Enturmacao_Turma_Mista
version: 121
---

# ENTURMAÇÃO EM TURMA MISTA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Enturmação em Turma Mista* |
| **Situação/Requisito:** | *Ao tentar enturmar aluno em turma mista apresenta erro. Falha ao ativar restrições. Uma ou mais linhas contêm valores que violam as restrições non-null, unique ou foreign-key. Este problema acontece porque existem alunos matriculado em uma mesma disciplina, porém em turmas diferentes. Este problema acontece, porque o sistema não barrou a desenturmação em turma normal de um aluno que estava enturmado em turma mista, com isso o sistema não excluiu a matrícula da disciplina deixando ela presa, sendo assim possível acontecer a inconsistência de matrícula em disciplinas iguais, porém em turmas diferentes.* |
| **Solução/Implementação:** | *Ajuste no processo de desenturmação do aluno, para que seja validado se o aluno está enturmado em turma mista, neste caso o sistema não deixaria a desenturmação prosseguir, ou se o aluno não está enturmado em turma mista, neste caso a desenturmação acontecerá normalmente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.9.104* |
| **Versão Expedida:** | *12.1.9.104* |

divs
