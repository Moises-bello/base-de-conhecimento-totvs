---
content_hash: 3ba8e4a267462d1600cfc471ec24218b13ae24e14bfc09d6f2ad87255d116f71
fetched_at: '2026-06-29T00:10:13.292944+00:00'
page_id: '455803442'
product: rm
source: tdn-rm
title: 5066975 EDUCACIONAL01-8229 DT Total de Faltas Após Mudança de Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=455803442
version: 1
---

# TOTAL DE FALTAS APÓS MUDANÇA DE TURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Fórmula |
| **Situação/Requisito:** | Quando o aluno tem turma de origem e é feito o processo "Mudar Turma", ao executar as fórmulas de apuração na turma de destino,  as faltas registradas na origem que já haviam sido enviadas para a turma de destino estão sendo somadas ao total de faltas devido à função "FALTASGLOBAL", que não considera a situação de matricula "Transferência de turma". |
| **Solução/Implementação:** | A rotina de mudança de turma foi alterada para marcar os registros da tabela SNOTAETAPA como copiados para outra turma.  A função de fórmula FALTASGLOBAL foi alterada para ignorar os registros da tabela SNOTAETAPA que foram copiados para outra turma. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
