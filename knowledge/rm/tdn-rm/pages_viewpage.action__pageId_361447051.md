---
content_hash: e25e97021d6e9f49cb48c6f63aa5671c7767d5a248e04d6a18bbc9a7052d8ea7
fetched_at: '2026-06-29T00:08:58.871530+00:00'
page_id: '361447051'
product: rm
source: tdn-rm
title: 2234355 EDUCACIONAL01-4098 Validar capacidade da sala com o máximo de alunos
  da sub-turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361447051
version: 1
---

# HORÁRIO DA SUB-TURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Cadastro do horário da subturma |
| **Situação/Requisito:** | Ao alocar uma sala no horário da subturma da turma/disciplina, o sistema verifica a capacidade e quantidade de alunos matriculados da turma/disciplina e não da subturma. |
| **Solução/Implementação:** | No cadastro de Horário da Subturma, ao preencher uma sala, o sistema valida se a capacidade da sala comportará a capacidade máxima de alunos da turma/disciplina. Caso esteja marcado o parâmetro geral da Secretaria “Utilizar turma/disciplina e subturma com horários independentes”, o sistema irá verificar a capacidade máxima de alunos na Subturma.  No Processo “Geração de horário” foi incluído validação da capacidade da sala com a capacidade máxima de aluno, observando a sub-turma, caso esteja utilizando horário independente. Será observado o parâmetro do perfil do usuário “Permitir alocar salas com turmas/disciplinas acima da capacidade”. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
