---
content_hash: cf266ab7bd951a17108df24e5f5e95f83c5e5bb11593761673769973d8592b59
fetched_at: '2026-06-29T00:09:31.755185+00:00'
page_id: '425458710'
product: rm
source: tdn-rm
title: Enturmação em turma mista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458710
version: 15
---

O conceito de Turma Mista consiste numa turma disciplina que não pertence a uma matriz aplicada. Nesta turma podem ser matriculados alunos de diferentes matrizes. Um aluno só pode ser matriculado em uma turma mista caso já esteja matriculado em uma turma/disciplina da mesma disciplina, denominada turma "origem". Assim como na turma "origem", a turma mista possui controle de notas, faltas, plano de aula e frequência.  
O grande intuito de uma turma mista é ser um agrupador de alunos de vários cursos ou matrizes curriculares, para facilitar o gerenciamento da instituição em relação a locação de sala, professores, etc.  
A tela de enturmação em turmas mistas é o principal processo por onde os alunos serão vinculados a uma turma mista. Estes alunos devem estar regularmente matriculados em uma turma origem para serem matriculados em uma turma mista da mesma disciplina.   
Observações às regras da turma mista:

* **A principal regra** é que um aluno só conseguirá ser enturmado em uma turma mista se ele já estiver matriculado em uma turma convencional, da mesma disciplina da turma mista.
* A digitação de notas, poderá ser feita através da turma mista. Neste caso as notas/faltas digitadas serão replicadas para a turma de origem do aluno, pois o controle acadêmico do aluno será baseado na turma original dele.
* No caso da digitação de notas, se esta for feita na turma de origem direto, a nota não será replicada para a turma mista.
* A mudança de situação de matrícula, quando feita na **TURMA DE ORIGEM** do aluno, será replicada para o registro dele na turma mista. Entretanto o contrário não se aplicará.
* **DESENTURMAR** um aluno de uma turma mista significa **EXCLUIR** o registro na turma mista, mas **APENAS** nela. O aluno continua matriculado na turma de origem.

**Choques de Horários**

Devemos lembrar que a Turma Mista se torna forte caso o aluno possua matrícula. Sendo assim, a disciplina normal passa a ser uma receptora de dados da Turma Mista. Desta forma, choques de horário serão validados pela Turma Mista e não pelas Normais.

Durante a Enturmação em Turma Mista, caso o sistema identifique inconsistências entre turmas mistas e/ou disciplinas, será exibida na tela uma mensagem informando as disciplinas referentes aos choques de horários.

Sendo as validações seguintes:

* Turma Mista com Turma Mista - Caso o aluno esteja matriculado na Turma Mista "A" que possui o horário "X" e tente realizar a enturmação da Turma Mista "B" com o mesmo horário, o choque de horário será entre as Turmas Mistas.
* Turma Mista com Disciplina normal - Caso o aluno esteja matriculado na Disciplina "A" (de uma turma normal) e tente realizar a enturmação da Turma Mista "B" com o mesmo horário da disciplina normal, o choque de horário será entre a Turma Mista "B" e Disciplina "A".

Validações onde o choque não ocorrem:

* Turma Mista com a própria disciplina - Caso o aluno esteja matriculado na Disciplina "A" com horário "X" e realize a enturmação na Turma Mista da mesma disciplina com o mesmo horário, o mesmo será enturmado.
* Turma Mista com Disciplina que possui Turma Mista em outro Horário - Caso o aluno esteja matriculado na Disciplina "A" no horário "X" e Turma Mista "A" no horário "Y", ao tentar realizar a enturmação da Turma Mista "B" no horário "X" será realizada a enturmação.

**Importante: Validações de Inconsistência**

* Caso o aluno possua duas matrículas na mesma disciplina e no mesmo período letivo, porém em turmas diferentes com a mesma situação de matrícula que tenha como os itens "conta como aluno matriculado" e "disciplina" marcados, ao selecionar os alunos na enturmação em turma mista o sistema irá bloquear a seleção informando ao usuário que existe uma inconsistência deste tipo e a mesma deverá ser ajustada para prosseguir na seleção;
* Caso o aluno possua uma matrícula em alguma disciplina que contenha data de matrícula vazia, o sistema também irá bloquear a seleção e irá informar a inconsistência ao usuário, sendo o mesmo deverá ajustá-la para prosseguir na seleção.
