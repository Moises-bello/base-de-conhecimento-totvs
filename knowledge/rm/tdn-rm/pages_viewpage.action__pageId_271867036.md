---
content_hash: 74b72edf1165000d8a0caca46dc0bf4f1b68c78145354b6ca2cdac5aeff5d00e
fetched_at: '2026-06-29T00:08:28.910168+00:00'
page_id: '271867036'
product: rm
source: tdn-rm
title: 548633 MEDU-2808 DT Horário Turma/disciplina data final inválida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271867036
version: 111
---

# HORÁRIO DA TURMA/DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Horário da turma/disciplina* |
| **Situação/Requisito:** | No anexo Horário da turma/disciplina, o sistema altera automaticamente a data final do horário quando existe uma inconsistência com a data final da turma/disciplina. Porém Usuários com permissão de somente Consulta não deverá ser realizado esta alteração. |
| **Solução/Implementação:** | Alteração no comportamento do sistema para não alterar automaticamente a data final e nem a data inicial do Horário da Turma/Disciplina quando as mesmas estão inconsistentes.  O sistema continuará emitindo mensagem de alerta e caberá ao usuário alterar esta data para um valor válido, caso este usuário tenha permissão de acesso para alteração/inclusão.  As validações destas datas serão apresentadas sempre que um registro for Salvo OU quando clicamos/sairmos dos campos de data. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
