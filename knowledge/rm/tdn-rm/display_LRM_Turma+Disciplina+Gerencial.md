---
content_hash: 2b7378662d7928c63ea999fef9de7406694fbb1ce92a27087249341b6bfc6ceb
fetched_at: '2026-06-29T00:08:38.297851+00:00'
page_id: '285647133'
product: rm
source: tdn-rm
title: Turma Disciplina Gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/Turma+Disciplina+Gerencial
version: 114
---

## Visão Geral

O objetivo da “Turma\disciplina Gerencial” é reduzir o custo com professores alocados em turma\disciplinas com poucos alunos matriculados, possibilitando ao cliente agrupar turmas\disciplinas “relacionadas” a uma única turma\disciplina gerencial. Para isso, as turma\disciplinas devem ter a mesma etapa de nota, falta, avaliação, horário, plano de aula e etc, mas não necessariamente o mesmo turno.

***Acesse: Currículo e Oferta / Oferta / Turmas\Disciplinas***

Edite o registro no cadastro de turma/disciplina e marque o parâmetro na tela, chamado “Turma Disciplina - Gerencial” e salve a alteração.

**Lembrando:** Para que uma turma/disciplina possa se tornar “gerencial”, ela não deve possuir nenhum aluno vinculado (independente da situação de matrícula) e não pode estar sendo gerenciada por outra turma/disciplina. O campo ficará desabilitado quando a turma/disciplina possuir aluno vinculado (independente da situação de matrícula), estiver sendo gerenciada por outra turma/disciplina ou quando ela já for gerencial e possuir gerenciadas.

Ao marcar uma turma/disciplina como gerencial e salvar o registro, será habilitado um anexo chamado “Turma/Disciplina Gerenciada”, conforme mostra a figura abaixo:

Este anexo irá armazenar todas as turma/disciplinas que estão sendo “gerenciadas” pela turma/disciplina gerencial

**Como associar turma/disciplina a uma turma/disciplina gerencial:**

* **1. Pelo anexo “Turma/Disciplina Gerenciada”:**

Clique em novo, informe os dados: Filial, Nível de ensino, Período letivo, Turma e Turma/disciplina, conforme figuras abaixo:

* **Pelo processo “Associar turma/disciplina como gerenciadas”:**

**Acesse: Atividades Acadêmicas / Assistentes / Associar turma/disciplina como gerenciadas**

Ao acessar o processo, informe o período letivo e a turma/disciplina gerencial:

No segundo passo do processo, temos 3 possibilidades para selecionar turma/disciplina a ser gerenciada:

* **Turma/Disciplina:**

Informe a turma/disciplina desejada e depois clique no botão “Adicionar”, o sistema irá incluir essa turma/disciplina na lista a ser associada. Conforme figura abaixo:

**Lembrete**: Caso queira adicionar mais turma/disciplina, basta clicar no botão “< Voltar” e repetir o processo.

* **Matriz Aplicada:**

Informe a matriz aplicada desejada e depois clique no botão “Adicionar”, o sistema irá incluir todas as turma/disciplinas na lista a ser associada. Conforme figura abaixo:

Neste momento, podem existir várias turma/disciplinas da matriz aplicada selecionada e não necessariamente serão todas associadas à turma/disciplina gerencial. Para excluir alguma turma/disciplina da lista, basta marcar o registro “[X]” e clicar no botão “Remover”. Conforme mostra a figura abaixo:

**Lembrete:** Essa funcionalidade de remover registros da lista que será associada como gerenciada, pode ser usado nos 3 tipos de filtros (Turma/disciplina, Matriz aplicada ou Consulta SQL).

1. **Consulta SQL:**

Informe a consulta SQL, caso a mesma tenha parâmetros, informe-os na tabela abaixo da consulta. Depois clique no botão “Executar”, caso sua consulta tenha retornado algum registro, o resultado será exibido na tabela ao lado, chamada “Resultado da consulta SQL”. Depois basta clicar no botão “Adicionar”, o sistema irá incluir todas as turma/disciplinas baseado no resultado da consulta SQL executada. Conforme figura abaixo:

**Depois de selecionar as turma/disciplinas que serão associadas à turma/disciplina gerencial, basta clicar no botão “Avançar” e executar o processo.**

Caso o processo tenha executado com sucesso, o mesmo irá informar a quantidade de turma/disciplina selecionada e as que foram associadas. Isso porque para realizar a associação, o sistema irá realizar várias validações necessárias, e caso uma delas não seja atendida, nenhuma turma/disciplina será associada.

**Lembrete: Será possível associar turma/disciplina a uma gerencial, somente quando:**

1. Que não esteja sendo gerenciada por outra turma/disciplina e não seja gerencial;
2. Tenha as mesmas etapas de nota e falta da turma/disciplina gerencial;
3. Tenha as mesmas avaliações da turma/disciplina gerencial;
4. Tenha os mesmos horários da turma/disciplina gerencial, sendo turnos iguais ou diferentes;
5. Tenha o mesmo plano de aula da turma/disciplina gerencial (número da aula, data, código do horário, conteúdo previsto e conteúdo realizado);
6. A soma dos alunos matriculados seja igual ou inferior ao total de vagas da turma/disciplina gerencial;
7. Tenha a mesma data inicial e final da turma/disciplina gerencial;
8. Tenha o mesmo tipo de nota (numérico ou conceitual) da turma/disciplina gerencial;
9. Tenha a mesma url da aula on-line.

**Acesse: Currículo e Oferta / Oferta / Turmas\Disciplinas**

Após associar as turma/disciplinas a uma gerencial, as mesmas podem ser visualizadas no anexo “Turma/Disciplina Gerenciada” da turma/disciplina gerencial. Conforme figura abaixo:

Depois que as turma/disciplinas são associadas a uma gerencial, o controle de vaga será pela turma/disciplina gerencial.

**Exemplo:**

Na turma/disciplina **gerencial** abaixo, temos 1 aluno matriculado e o número máximo de alunos é 1.

**Lembrando:**O campo “Alunos matriculados” de uma turma/disciplina gerencial é a soma das matriculas das suas turma/disciplinas gerenciadas, neste exemplo, a soma de matriculas das turma/disciplinas:

Neste exemplo, a turma/disciplina de código 937 (DIR00001 – 146-1) possui 1 aluno matriculado e a de código 975 (TPD00005 – A049-1) não possui nenhum aluno matriculado ainda.

Ao realizar a matricula de um aluno, na turma/disciplina gerenciada (TPD00005/A049-1), o sistema não irá permitir, visto que a turma/disciplina gerencial (TURGERENCIAL/A173-1) possui 1 vaga e já tem 1 aluno matriculado. Conforme figuras abaixo:

Ou seja, o controle de vagas foi realizado pela turma/disciplina gerencial.

**Novo parâmetro de sistema:**

Foi criado um novo parâmetro no sistema para facilitar os processos de digitação, tais como: Nota, falta, avaliação, frequência, plano de aula, etc.

Ao marcar este parâmetro *“Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária e plano de aula”,* o sistema terá os seguintes comportamentos:

As telas de digitação (“Digitação de nota e falta” e “Digitação de frequência diária”) serão realizadas pela turma/disciplina gerencial. O sistema não irá permitir selecionar as turma/disciplinas gerenciadas, somente a turma/disciplinas gerencial.

A alteração e a inclusão de professor deve ser realiza na turma/disciplina gerencial e essas informações serão replicadas para as respectivas turmas/disciplinas gerenciadas. O sistema não irá permitir alteração e inclusão de professor na turma/disciplina gerenciada.

Importante:

* As informações do professor relacionadas a integração do Educacional com o módulo de Ponto não serão replicadas da gerencial para as gerenciadas:
  + Faltas, substituto e reposição
* As informações do professor relacionadas a integração do Educacional com o módulo de Folha não serão replicadas da gerencial para as gerenciadas:
  + Compõe Salário e Aulas por Semana

**Perguntas frequentes:**

*1) Como a turma gerencial é exibida no relatório do Censo?*

R. No relatório do censo é exibido a turma gerenciada.

*2) Como funciona com o complemento da disciplina?*

R. O complemento da disciplina é vinculado à turma disciplina gerenciada.

*3) Como o aluno e o professor irão visualizar a turma no portal?*

R. O aluno não visualiza a turma disciplina gerencial em nenhum momento. Já os professores conseguem visualizar para a digitação de notas/faltas, quadro de horários, etc.

*divs*
