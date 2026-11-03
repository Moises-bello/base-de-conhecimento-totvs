---
content_hash: 3ae9e90df56f8b4b21f03cc3dda520cf2c83f3d7f7fa0ae04d9d1033d37d48f2
fetched_at: '2026-06-29T00:09:07.923313+00:00'
page_id: '385858417'
product: rm
source: tdn-rm
title: 3344443 EDUCACIONAL01-5784 DT Copiar turmas entre períodos letivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385858417
version: 82
---

# COPIAR TURMAS ENTRE PERÍODOS LETIVOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Copiar turmas entre períodos letivos* |
| **Situação/Requisito:** | *Ao executar a cópia de turmas entre períodos letivos e que possuem turmas/disciplinas gerenciais vinculadas, e marcar a Flag: Copiar as Turma/disciplinas gerenciadas da turma/disciplinas gerenciais selecionadas o sistema emite a seguinte mensagem de erro: O objeto nulo deve ter um valor.* |
| **Solução/Implementação:** | *Realizado ajuste no processo de cópia de turmas entre períodos letivos, onde ele tentava buscar dados da matriz aplicada para definir o caption a ser exibido no log mesmo quando a turma não possuía matriz aplicada preenchida, o que ocasionava o erro reportado.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
