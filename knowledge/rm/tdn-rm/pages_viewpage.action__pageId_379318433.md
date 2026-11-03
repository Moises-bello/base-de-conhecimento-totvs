---
content_hash: f48ee82338bec27af40d75da4ca901b1af3d11ebd94a1f82b4336967e7125694
fetched_at: '2026-06-29T00:09:02.521685+00:00'
page_id: '379318433'
product: rm
source: tdn-rm
title: 2116506 EDUCACIONAL01-4474 DT Cadastro de Professores na Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379318433
version: 85
---

# CADASTRO DE PROFESSORES NA TURMA/DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Cadastro de Professores na Turma/Disciplina* |
| **Situação/Requisito:** | *Ao tentar cadastrar o professor duas vezes na turma/disciplina o sistema estava bloqueando e emitindo a seguinte mensagem:  "Professor já possui cadastro na Turma/Disciplina no período informado.".* |
| **Solução/Implementação:** | *Foi retirado o bloqueio do cadastro do mesmo professor duas vezes na mesma turma/disciplina se ele possuir a permissão "Permitir superalocação professores".  Se a permissão estiver habilitada, uma mensagem de aviso é exibida e o registro é salvo. Se não possuir, o sistema bloqueia o cadastro.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
