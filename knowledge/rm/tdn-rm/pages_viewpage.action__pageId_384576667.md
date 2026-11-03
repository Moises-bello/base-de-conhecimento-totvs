---
content_hash: 5836d2542e8d61d9d3b2aace4b8b4370b9005415e9cc38ccf048a3142fd61564
fetched_at: '2026-06-29T00:09:07.535369+00:00'
page_id: '384576667'
product: rm
source: tdn-rm
title: 2070153 EDUCACIONAL01-3795 DT Validações de permissões de acesso ao quadro
  de montagem de horários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384576667
version: 86
---

# VALIDAÇÕES NAS PERMISSÕES DE ACESSO AO QUADRO DE MONTAGEM DE HORÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Quadro de montagem de horários* |
| **Situação/Requisito:** | Ao acessar a tela de montagem de quadro de horário com um usuário que não possui todas as permissões do sistema é apresentada a mensagem de erro “Object reference not set to an instance of an object”. |
| **Solução/Implementação:** | Inclusão de validações das permissões de acesso a tela de montagem de quadro de horários. Ao acessar a tela, essas validações não eram realizadas.  Permissões necessárias:   * + *Visualização de informações de professores;*      - *[01.01.04] - Professores*   + *Visualização de informações de turmas/disciplinas;*      - *[01.03.05] - Turmas/Disciplinas*   + *Visualização de informações da subturma;*      - *[01.03.05.08] - Subturmas*   + *Inclusão/Alteração/Exclusão de professores da turma;*      - *[01.03.05.04.01] - Incluir p*rofessor da turma/disciplina**     - *[01.03.05.04.02] - Excluir p*rofessor da turma/disciplina**     - *[01.03.05.04.03] - Editar professor da turma/disciplina*   + *Inclusão/Alteração/Exclusão de horários da turma;*      - *[01.03.05.06.01] *- Incluir horário da turma/disciplina**     - *[01.03.05.06.02] *- Excluir horário da turma/disciplina**     - *[01.03.05.06.03] - Editar horário da turma/disciplina*   + *Inclusão/Alteração/Exclusão de professores do horário da turma;*      - *[01.03.05.06.04.01] *- Incluir professor do horário**     - *[01.03.05.06.04.02] *- Incluir professor do horário**     - *[01.03.05.06.04.03] - Incluir professor do horário*   + *Inclusão/Alteração/Exclusão de horários da subturma;*      - *[01.03.05.08.04.01] *- Incluir horário da subturma**     - *[01.03.05.08.04.02] *- Excluir horário da subturma**     - *[01.03.05.08.04.03] - Editar horário da subturma* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
