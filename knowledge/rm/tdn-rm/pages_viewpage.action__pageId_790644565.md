---
content_hash: 70954da465d92a18b36a16f05735f7ddbf41f1b6b43a7aa01fe4c941f3a0548e
fetched_at: '2026-06-29T00:11:39.863509+00:00'
page_id: '790644565'
product: rm
source: tdn-rm
title: Secretaria - Parâmetros Gerais 2/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790644565
version: 2
---

### Utilizar turma/disciplina e subturma com horário independentes

#### Parâmetro Desmarcado

* Caso o parâmetro esteja marcado e o aluno **NÃO** esteja matriculado em nenhuma subturma, deve trazer os horários vinculados a turma/disciplina.
* Caso o aluno esteja matriculado em uma subturma, segue as regras:
  + Se a subturma possuir horário vinculado, traz os horários vinculados a subturma e a turma/disciplina.
  + Se a subturma **NÃO**possuir horário vinculado, traz os horários vinculados a turma/disciplina.

#### Parâmetro Marcado

* Caso o parâmetro esteja marcado e o aluno **NÃO** possua subturma deve mostrar apenas os horários das disciplinas em que o aluno foi matriculado.
* Caso o parâmetro esteja marcado os horários apresentados devem ser todos os relacionados a turma/disciplina no qual o aluno esta matriculado e todos os horários das subturmas que o aluno esta matriculado.

Quando o parâmetro utilizar turma/disciplina e subturma com horários independentes for marcado, não é possível desmarcar a opção.
