---
content_hash: 55d208a870ba1c6bc124167cf7664c27ea6eceabd45c221edb7b1378df177039
fetched_at: '2026-06-29T00:09:34.114484+00:00'
page_id: '425459144'
product: rm
source: tdn-rm
title: Turmas
type: documentation
url: https://tdn.totvs.com/display/LRM/Turmas
version: 23
---

Esta funcionalidade permite que seja cadastrada as turmas em que os alunos serão matriculados.

Para realizar o cadastro é necessário algumas parametrizações:

* O cadastro da turma só pode ser vinculado a uma matriz aplicada que tenha sua parametrização por curso cadastrada.  
  Caso a turma não seja vinculada a nenhuma matriz aplicada, será criada uma Turma Livre. Nessa turma pode ser inclusa qualquer disciplina.
* A turma só pode ser vinculada a matrizes curriculares que possuem o campo controle de vagas preenchido.
* O número máximo de alunos da turma é obrigatório quando na matriz curricular vinculada a turma determinar que o controle de vagas é realizado "Por Turma".
* O código da turma, pode ser configurado através de máscara.
* RM Labore (Integração do Classis) - Nº. de alunos: Informar a quantidade de alunos matriculados para que possa fazer o cálculo de adicional por aluno no RM Labore.
* Data - Informe a data que é realizada o cálculo de adicional por aluno para os professores.

São quatros as modalidades de ensino disponíveis: Regular, Especial, JÁ (Educ. de Jovens e Adultos) e Profissional.

No cadastro da turma pode informar o link para [aula online](https://tdn.totvs.com/display/LRM/Aula+Online?moved=true) pelo campo "Aula Online". O link ficará disponível nos portais Educacionais para o aluno e para o professor. O professor poderá atualizar ou informar um novo link da aula online pelo portal do Professor.

O campo de **alunos matriculados** irá conter a quantidade de alunos matriculados na turma. Somente irá contar o aluno que possui **Turma**preenchida na matrícula do período letivo.

Balanceamento de turma

É possível habilitar a turma para que seja processado o balanceamento durante a matrícula de ingressantes, para maiores informações [clique aqui](https://tdn.totvs.com/display/LRM/Balanceamento+de+Turma).

Informações Complementares

---

[Turma/Disciplina](http://tdn.totvs.com/x/C-9bGQ)

Como Fazer

---

[Associar disciplinas da matriz aplicada à turma](http://tdn.totvs.com/x/d-xbGQ)

[Gerar Plano Aula Sequencial](http://tdn.totvs.com/x/cvtbGQ)
