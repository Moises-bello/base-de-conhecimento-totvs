---
content_hash: 47c70f0f213c4d3e222880bba13d8e8c07d493081c1f1f92644cdf0f46578786
fetched_at: '2026-06-29T00:09:00.985351+00:00'
page_id: '370617240'
product: rm
source: tdn-rm
title: 3109104 EDUCACIONAL01-5370 DT Matricular em disciplina alterando situação de
  matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370617240
version: 1
---

# MATRICULAR NAS DISCIPLINAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Matricular nas disciplinas |
| **Situação/Requisito:** | Ao realizar matricula em um turma/disciplina que já esteja matriculada, o sistema apresentava incorretamente erro de chave duplicada, ao invés de atualizar o status da turma/disciplina.  Somente ocorria se o status anterior da turma/disciplina matriculada estava desmarcado “É uma disciplina em curso”. |
| **Solução/Implementação:** | Alteração na matrícula em turma/disciplina:  - Se a turma/disciplina já estiver matriculada, o sistema irá apenas atualizar o status da disciplina.  - Se a turma/disciplina não estiver matriculada, será inserida. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
