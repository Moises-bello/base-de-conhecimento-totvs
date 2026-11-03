---
content_hash: a389c4665dc6033ab8f6c0e1d1584a9927cd44a39a5d45b117b55ba04a1dab04
fetched_at: '2026-06-29T00:06:09.451639+00:00'
page_id: '203754772'
product: rm
source: tdn-rm
title: TTFNNQ_DT_Mudar_Turma
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFNNQ_DT_Mudar_Turma
version: 1
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
| **Versões/Release:** | *12.1.8* |
