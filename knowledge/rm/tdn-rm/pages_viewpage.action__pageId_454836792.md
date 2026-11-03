---
content_hash: dafce086759fb97fbf6e5945cd4d06e7848e78765e66fbfcb2a4bd0f9ae147b2
fetched_at: '2026-06-29T00:10:13.084975+00:00'
page_id: '454836792'
product: rm
source: tdn-rm
title: EDUCACIONAL01-7342 DT Cadastro de turma/disciplina sem matriz aplicada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454836792
version: 1
---

# CADASTRO DE TURMA/DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Educacional |
| **Módulo:** | Educacional |
| **Função:** | Cadastro de Turma/Disciplina |
| **Situação/Requisito:** | Ao inserir turma/disciplina com código de turma igual azero e sem preencher a matriz aplicada, o sistema apresentava incorretamente mensagem de “Violação de chave estrangeira”. |
| **Solução/Implementação:** | Otimização no menu Currículo e Oferta | Turmas/disciplina, ao inserir uma turma/disciplina sem matriz aplicada e com código de turma igual a zero (valor default), o sistema emitirá mensagem de alerta para informar um código de turma. Por exemplo, turma mista.  Quando a turma/disciplina não tiver matriz aplicada preenchida, deve ser preenchido um código de turma durante o cadastro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
