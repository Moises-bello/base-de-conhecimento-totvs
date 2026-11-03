---
content_hash: a520a54f18f0a43f0a80a382e9502ac250c4f14941c7c2791f65389f825aead2
fetched_at: '2026-06-29T00:09:02.545669+00:00'
page_id: '379319714'
product: rm
source: tdn-rm
title: 04.1.02 - Aulas
type: documentation
url: https://tdn.totvs.com/display/LRM/04.1.02+-+Aulas
version: 5
---

Essa funcionalidade permite aos alunos e responsáveis consultar o conteúdo previsto, realizado e a lição de casa cadastrados para suas aulas por turma/disciplina e por dia.

Dica

Clique nas imagens a seguir para ampliar.

**IMPORTANTE:**

* Caso o aluno possua o parametro de **horário independentes** (**MARCADO**) deve ficar atento a seguinte regra:
  + Caso o parâmetro esteja marcado e o aluno **NÃO** possua subturma deve mostrar apenas os horários das disciplinas em que o aluno foi matriculado.
  + Caso o parâmetro esteja marcado os horários apresentados devem ser todos os relacionados a turma/disciplina no qual o aluno esta matriculado e todos os horários das subturmas que o aluno esta matriculado.

* Caso o aluno possua o parametro de **horário independentes** (**DESMARCADO**) deve ficar atento a seguinte regra:
  + - Caso o parâmetro esteja marcado e o aluno **NÃO**esteja matriculado em nenhuma subturma, deve trazer os horários vinculados a turma/disciplina.
      * Caso o aluno esteja matriculado em uma subturma, segue as regras:
        + Se a subturma possuir horário vinculado, traz os horários vinculados a subturma e a turma/disciplina.
        + Se a subturma **NÃO**possuir horário vinculado, traz os horários vinculados a turma/disciplina.

**OBS:**

* O parâmetro de horário independentes fica localizado em:
  + Educacional → Educacional → Ambiente → Parâmetros → Educacional → Secretaria → Geral 2/7
