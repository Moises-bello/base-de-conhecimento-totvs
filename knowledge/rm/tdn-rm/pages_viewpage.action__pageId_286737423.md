---
content_hash: 31ce87bf3ab75854b46caae76923690d3722276d9aaa4229cab8ff5c6294d9f7
fetched_at: '2026-06-29T00:08:41.620242+00:00'
page_id: '286737423'
product: rm
source: tdn-rm
title: 1268413 EDUCACIONAL01-2244 Exclusão de Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286737423
version: 103
---

# Exclusão de Aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Exclusão de Aluno* |
| **Situação/Requisito:** | *Ao tentar excluir um aluno gerado pelo processo de matricula do Processo Seletivo terceirizado o sistema apresentava um erro de chave estrangeira.* |
| **Solução/Implementação:** | *Foi realizado um ajuste na rotina de cancelamento de matricula do processo seletivo terceirizado para quando excluir o curso/habilitação de um aluno gerado através do*  *processo matricula do processo seletivo desvinculando o aluno do candidato do processo seletivo.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs

Foi implementado uma rotina para simular o cancelamento de matricula do processo seletivo terceirizado, para quando excluir o curso/habilitação de um aluno gerado através do processo matricular do Processo Seletivo desvinculando o aluno(SALUNO) do candidato do processo seletivo(SCANDIDATOPROCSEL)
