---
content_hash: 94b63add75612813792e90feda2befeff1eaa3d0bd2359bb15602c326ddcccc3
fetched_at: '2026-06-29T00:09:30.907353+00:00'
page_id: '425458558'
product: rm
source: tdn-rm
title: Numeração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458558
version: 15
---

## Processo

Este processo tem finalidade para numerar os alunos matriculados nas turmas/disciplinas de um determinado período letivo. O processo poderá ser realizado manual ou automático.

O processo **manual** poderá ser realizado através do menu **Matrícula e Avaliação | Numeração.** Neste os alunos podem ser numerados de duas formas, conforme abaixo:

* **Numerar Turma**, sendo este necessário informar o tipo de numeração, que poderá ser:
  + Por Nome;
  + Por n° de matricula;
  + Por sexo e por nome (Homens primeiro);
  + Por sexo e por nome (Mulheres primeiro).
* **Atribuir último número do diário a novo aluno**, sendo este o novo aluno não numerado receberá o último número do diário.

A rotina de numeração do ensino básico foi alterada para verificar se o status de matrícula do período letivo possui o parâmetro “Aluno com esta situação de matrícula é exibido no diário” marcado ou se o  parâmetro “Aluno ativo” está marcado e alguma disciplina possui o status “Aluno com esta situação de matrícula é exibido no diário” marcado.

Importante

A partir das versões 12.1.25.280, 12.1.26.226, 12.1.27.184, 12.1.28.116 e 12.1.29 (release) a numeração irá considerar o **nome social** do aluno, caso o mesmo esteja preenchido. Ou seja, se o nome social estiver preenchido o mesmo será o nome do aluno ao numerá-lo pelo nome, caso contrário será considerado o nome civil. Todos os parâmetros relativos a numeração para considerar nome social, foram removidos.

O mesmo vale para a numeração automática.

## Numeração Automática

O processo **automático** será realizado sempre que um novo aluno for matriculado em uma turma/disciplina, sendo este por mudança de turma, enturmação e qualquer processo que faça matrícula de aluno. Os alunos recém matriculados serão numerados conforme a parametrização da matrícula, localizado no menu Configurações | Parâmetros | Matrícula. Porém, para que isso ocorra na parametrização por curso a data limite de numeração automática não poderá ser menor que a data atual, caso seja menor não será feita a numeração automática, caso seja maior a numeração ocorrerá automaticamente, sendo que estas regras são válidas para o **ensino básico**. As regras que são válidas para o **ensino superior** são: caso a data limite seja menor que a data atual, será atribuído o último número do diário para o aluno, caso a data seja maior o processo automático irá ocorrer da forma que foi parametrizada. As opções disponíveis para a numeração automática são as mesmas do processo manual **Numerar Turma.**

## Numeração de Turma Gerencial

O processo provê de uma opção, chamada **Efetuar a numeração pela turma/disciplina gerencial quando a mesma for encontrada**, que tem por objetivo, numerar todos alunos que estão matriculados em turmas/disciplinas gerenciadas. Ou seja, todos os alunos das gerenciadas serão numerados de forma agrupada sendo uma única numeração para a gerencial. Este mesmo parâmetro poderá ser utilizado na numeração automática (**Gerar a numeração pela turma Gerencial**).   
**Exemplo:**   
Uma turma/disciplina Gerencial G1, possui duas turmas/disciplinas gerenciadas GD1 e GD2, sendo:

* GD1, possui dois alunos matriculados:
  + Raul Benjamin Ribeiro
  + Calebe Diego Vitor Pereira
* GD2, possui também dois alunos matriculados:
  + Pedro Anthony Almeida
  + Danilo Henrique Tomás Cardoso

Ao efetuar a numeração pela gerencial G1, a seguinte numeração será atribuída aos alunos:

* 1 - Calebe Diego Vitor Pereira
* 2 - Danilo Henrique Tomás Cardoso
* 3 - Pedro Anthony Almeida
* 4 - Raul Benjamin Ribeiro

## Numeração na Enturmação e Enturmação Turma Mista

Nos dois processos é possível efetuar a Numeração, toda vez que enturmar ou desenturmar o(s) aluno(s), clicando no botão **Numeração automática**. Entretanto, para isso é necessário parametrizar a numeração automática.

## Numeração de Turma Mista

No **ensino superior**, para efetuar a numeração da turma mista, basta selecionar no processo a turma mista, bem como a turma/disciplina, visualizar a numeração anterior, selecionar o modo de numeração e executar o processo, como já é feito para uma turma/disciplina comum/normal.

Por outro lado no **ensino básico**a partir da versão release 12.1.29 será possível numerar os alunos da turma mista por meio deste processo. Para isto, basta selecionar no processo o período letivo e a opção **Efetuar a numeração de turmas mistas**, com isso, as turmas que serão apresentadas serão somente turmas mista. Além disso, será possível selecionar uma disciplina específica para esta numeração. Ao selecionar a turma e/ou disciplina mista, basta visualizar a numeração anterior, selecionar o modo de numeração e executar o processo. Com isso, os alunos da turma mista serão numerados e seu número estará no cadastro da matrícula na turma/disciplina.

## Numeração de Turma de Itinerário Formativo

A partir dos parches 12.1.33.292, 12.1.34.192, 12.1.2205.130 e 12.1.2209 (release) será possível numerar alunos que matriculadas em turmas/disciplinas de itinerário formativo, o mesmo vale para a **numeração automática,** ou seja, a partir dos patches mencionados a numeração automática também irá funcionar para numerar as matrículas em itinerário formativo. A numeração sempre ocorrerá pela turma, ou seja, dada uma turma que contenha disciplinas da grade e de itinerário e consequentemente alunos matriculados nestas disciplinas, a numeração irá ocorrer pela turma em questão.

Exemplo de numeração

Turma A

* Matemática (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Português (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Eletrônica (disciplina de itinerário formativo)
  + Alberto Domingos

Ao numerar a turma A o resultado será:

* Matemática (disciplina da grade)
  + [ 2 ] Bernard Alves
  + [ 3 ] Calebe Diego
* Português (disciplina da grade)
  + [ 2 ] Bernard Alves
  + [ 3 ] Calebe Diego
* Eletrônica (disciplina de itinerário formativo)
  + [ 1 ] Alberto Domingos

Foi incluído um novo campo de filtro por itinerário formativo no processo de numeração.

Os itinerários a serem exibidos neste campos serão os que possuem vinculo com a matriz curricular e tenha parametrização por curso cadastrada. Caso informe um curso o campo de itinerário será filtrado para exibir apenas os que tem vinculo ao curso informado e assim por diante para a série, matriz curricular e turno. Se informar um itinerário, as turmas a serem exibidas, são turmas que possuem no mínimo uma turma/disciplina de itinerário formativo.

Outro detalhe muito importante é que ao informar um itinerário e clicar no botão de visualizar numeração atual, serão exibidos todas as turmas que contenha pelo menos uma turma/disciplina de itinerário formativo. As turmas serão exibidas com as disciplinas da grade e do itinerário selecionado, porque como foi dito a numeração é pela turma, então deverá ser exibidos as disciplinas de itinerário bem como as demais disciplinas da turma, segue exemplo.

Exemplo de numeração

Turma A

* Matemática (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Português (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Eletrônica (disciplina de **itinerário formativo** **1**)
  + Alberto Domingos

Ao selecionar o **itinerário formativo 1** e clicar no botão visualizar será exibido:

Turma A

* Matemática (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Português (disciplina da grade)
  + Bernard Alves
  + Calebe Diego
* Eletrônica (disciplina de **itinerário formativo** **1**)
  + Alberto Domingos

Se o aluno estiver matriculado em disciplinas da grade e do itinerário formativo em turmas diferentes, o comportamento do sistema muda. Dado que a numeração dos alunos toma a turma como referência central, cada turma terá sua própria numeração independente, preservando a integridade dos dados.

Exemplo de numeração

Turma A

* Matemática (disciplina da grade)
  + Alberto Domingos
  + Bernard Alves
  + Calebe Diego
* Português (disciplina da grade)
  + Alberto Domingos
  + Bernard Alves
  + Calebe Diego

Turma B

* Eletrônica (disciplina de itinerário formativo)
  + Calebe Diego
  + Douglas Mendes

Ao numerar o período letivo destas turmas, o resultado será:

Turma A

* Matemática (disciplina da grade)
  + [1]Alberto Domingos
  + [2]Bernard Alves
  + [3]Calebe Diego
* Português (disciplina da grade)
  + [1]Alberto Domingos
  + [2]Bernard Alves
  + [3]Calebe Diego

Turma B

* Eletrônica (disciplina de itinerário formativo)
  + [1]Calebe Diego
  + [2]Douglas Mendes
Importante

Caso o aluno possua turmas canceladas ou outras alterações da mesma natureza em seu vínculo, a numeração nessas turmas não será, obrigatoriamente, a mesma de sua matrícula ativa.
