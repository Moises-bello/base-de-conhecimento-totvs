---
content_hash: 1c2eefd082addc97ee8ec8e60b3afbafdde4ed75e2b89776c0d458d7a815045d
fetched_at: '2026-06-29T00:06:08.462707+00:00'
page_id: '201747064'
product: rm
source: tdn-rm
title: TTEDJV_DT_Mudar_Turma
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEDJV_DT_Mudar_Turma
version: 2
---

# MUDAR TURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ****Educacional**** |
| **Módulo:** | ****TOTVS Gestão Educacional**** |
| **Função:** | *Mudar Turma* |
| **Situação/Requisito:** | *Ao tentar realizar o processo de mudança de turma do aluno aparece o erro: "Ocorreu um erro na inclusão da matrícula: SqlDateTime overflow. Must be between 1/1/1753 12:00:00 AM and 12/31/9999 11:59:59 PM".* |
| **Solução/Implementação:** | **Alteração na rotina de mudança de turma para permitir gravar o campo o campo de data de matrícula com valor nulo, pois esse campo não é obrigatório no CLASSIS.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **Versões/Release:** | *11.82.40/11.82.41* |
