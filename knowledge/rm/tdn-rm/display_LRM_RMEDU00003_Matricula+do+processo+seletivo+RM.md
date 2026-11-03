---
content_hash: c1c4ac15cef9f7dee141bbd7bf66b0a18e08af28b845fdf273526e5107c8c5ae
fetched_at: '2026-06-29T00:08:24.142097+00:00'
page_id: '270105230'
product: rm
source: tdn-rm
title: RMEDU00003_Matricula do processo seletivo RM
type: documentation
url: https://tdn.totvs.com/display/LRM/RMEDU00003_Matricula+do+processo+seletivo+RM
version: 9
---

Matricula do processo seletivo RM

|  |  |
| --- | --- |
| **Produto:** | Gestão Educacional |
| **Versão:** | 12.1.14 |
| **Processo:** | Matricula do processo seletivo RM |
| **Data da publicação:** |  |

Clique aqui para expandir o índice

A rotina de matricula do processo seletivo RM, é um processo, que permite as instituições, utilizar dados dos candidatos do processo seletivo, que a instituição realizou através do módulo: processo seletivo, da linha RM, no módulo: gestão educacional, integrando assim os dois sistemas.

Requisitos:

Os candidatos aptos a serem matriculados no sistema são aqueles que estão na lista dos candidatos da última chamada ocorrida pelo processo seletivo em questão, ou seja, o status do candidato deve estar “Em chamada” (id interno do sistema=5).

Para matricular candidatos que foram aprovados em um processo seletivo do módulo Processo Seletivo RM é necessário que determinado processo seletivo tenha uma área de interesse ofertada vinculada a uma matriz aplicada do curso/habilitação do TOTVS Educacional.

Toda a estrutura para matricula deve ser criada, Parametrização por curso, turmas, turmas disciplinas, planos de pagamento e etc...

## 1.Cadastros

### 1.1 Cadastro da matriz

Módulo processo seletivo | cadastros | processo seletivo | anexo | área de interesse ofertada | guia: identificação | área de interesse

Importante:

Para que seja possível preencher as informações do curso, habilitação, grade e turno, o campo: área de interesse cliente, não pode estar preenchido. Esse campo deve ser preenchido, quando a instituição fornece o serviço de realizar o processo seletivo para outra instituição, indicando nesse campo, qual foi essa instituição.

Módulo processo seletivo | cadastros | processo seletivo | anexo | candidatos inscritos

Para que o candidato seja visualizado no processo, o mesmo deve estar com o status 5: em chamada.

### 1.2 Cadastro da parametrização por curso

Módulo gestão educacional | currículo e oferta | oferta | parametrização por curso

Para o período letivo desejado, deve existir uma parametrização por curso cadastrada e parametrizada, para a matriz aplicada informada no processo seletivo onde o candidato está inscrito.

### 1.3 Cadastro da turma

Módulo gestão educacional | currículo e oferta | oferta | turmas

A turma onde o aluno será matriculado, também deve estar cadastrada e parametrizada.

Módulo gestão educacional | currículo e oferta | oferta | turmas/disciplinas

As turmas/disciplinas da turma, também devem estar cadastradas e parametrizadas.

## 2. Matriculando o candidato

Matricula e avaliação | matricula | processo seletivo RM | matricular

Escolha o processo seletivo e área ofertada, de onde o sistema irá buscar os candidatos aptos a serem matriculados

Selecione o candidato

O sistema permite parametrizar, qual período letivo e turma, o candidato será matriculado como aluno, qual a situação de matricula, no curso, período letivo e nas disciplinas, qual será o tipo de matricula do aluno, qual campus o aluno está matriculado e a data de ingresso no curso.

Deve-se atentar, para os casos, onde o candidato que está sendo matriculado, já é ou foi aluno da instituição, em outro curso por exemplo. O sistema trabalha da seguinte forma:

* Não matricula o candidato, se o mesmo tiver 2 ou mais RA's;
* Gera um novo RA para o candidato;
* Matricula o candidato utilizando RA existente. Nesse caso, de 3 formas diferentes:

                                                                                                                                                      - Utiliza o primeiro RA encontrado;

                                                                                                                                                      - Priorizar RA do mesmo nível de ensino;

                                                                                                                                                      - Matricular somente se encontrar RA no mesmo nível de ensino.

Como parâmetros financeiros, temos as seguintes possibilidades: cadastrar contrato, plano de pagamento e cadastrar o próprio aluno como responsável financeiro, ou o responsável financeiro do processo seletivo.

O usuário que realiza a matricula, pode selecionar algumas flags, que influenciam diretamente na matricula ou não do candidato:

* Matricular em turmas com excessos de alunos;
* Matricular alunos sem documentos obrigatórios entregues;
* Matricular alunos com ocorrencias que bloqueiam a matricula;
* Matricular alunos após a data de limite de matricula no período letivo;
* Matricular alunos com choque e horários;
* Matricular alunos inadimplentes;
* Matricular alunos em disciplinas que o pré/correquisito não foi cumprido;
* Matricular alunos com créditos abaixo/acima do nº minimo/máximo de créditos do período letivo;
* Alterar situação de matricula ou matricular aluno com empréstimos em atraso;
* Alterar situação de matricula ou matricular alunos com débitos na biblioteca.

Lembrando que, o perfil associado ao usuário que está realizando o processo, deve ter todas essas permissões habilitadas.

**Contexto Superior:**

Quando o contexto do sistema é de Ensino Superior é permitido o vínculo dos acertos em provas do vestibular (Provas do Processo seletivo) às Provas de vestibular do sistema (TOTVS Educacional). Desta forma é possível, por exemplo, vincular notas de provas diferentes do candidato a uma única nota de uma prova de vestibular do sistema.

Ao final do processo, é apresentada a tela de log
