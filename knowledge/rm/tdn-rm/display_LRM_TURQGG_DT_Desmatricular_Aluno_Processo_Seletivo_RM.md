---
content_hash: d7f7d107ea35e143ac42f69b23df3f67294c3b5d47a73d82a45cbeef168a606f
fetched_at: '2026-06-29T00:08:04.741205+00:00'
page_id: '235580754'
product: rm
source: tdn-rm
title: TURQGG_DT_Desmatricular_Aluno_Processo_Seletivo_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/TURQGG_DT_Desmatricular_Aluno_Processo_Seletivo_RM
version: 117
---

# DESMATRICULAR ALUNO DO PROCESSO SELETIVO RM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Desmatricular aluno do processo seletivo RM* |
| **Situação/Requisito:** | *Ao desmatricular um aluno que possui solicitação no processo de desmatricular aluno do processo seletivo RM, o sistema travava o processo para todos os alunos e emitia mensagem de chave estrangeira.* |
| **Solução/Implementação:** | Melhoria no processo de desmatricular o aluno do processo seletivo RM, em caso de solicitações já cadastrada para o aluno que impeça desmatricular, o sistema vai continuar executando para os demais alunos do processo e avisará ao usuário no final do processo via log do problema. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TTPVK4 |
| **Requisito (ISSUE):** | *N/A* |

divs
