---
content_hash: be2ab35730e5705a8f97037444667a3f0734de2becd8268af7564f2de9c71d65
fetched_at: '2026-06-29T00:09:33.898144+00:00'
page_id: '425459076'
product: rm
source: tdn-rm
title: Enturmação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459076
version: 19
---

A enturmação tem como objetivo realizar a distribuição dos alunos, que estão matriculados em algum período, em turmas ofertadas pela instituição de ensino.

Na tela de enturmação é possível executar os seguintes processos: enturmação, desenturmação (que é o processo inverso à enturmação), numeração dos alunos nas turmas e mudança de turma.

# **Ensino Superior**

## Filtro da Tela

* Período Letivo: campo obrigatório que é utilizado para filtrar os alunos e turmas exibidos no processo.
* Matriz Aplicada: campo não obrigatório para o processo. Ele é utilizado para filtrar as turmas exibidas para execução da enturmação.
* Situação de Matrícula após a enturmação: campo obrigatório para execução do processo de enturmação. O valor selecionado no campo será atribuído a matrícula do aluno nas disciplinas após execução do processo.
* Campus/Polo: campo não obrigatório utilizado para filtrar as turmas do campus/polo selecionado.
* Período: campo não obrigatório utilizado para filtrar os períodos as turmas que serão exibidas na tela.
* Disciplina: campo não obrigatório utilizado para filtrar as disciplinas das turmas que serão exibidas na tela.
* Não remanejar alunos com Notas/faltas
* Lista disciplinas equivalentes: quando marcado serão exibidos as disciplinas equivalentes de todas as disciplinas listadas na tela.

## Alunos sem turma

Serão exibidos os alunos, em ordem alfabética, que possuem matrícula no período letivo mas não possuem turma associada. É possível restringir ainda mais os registros exibidos ao utilizar o filtro de alunos existente no cabeçalho dessa lista:

As informações sobre Matriz Aplicada existente no filtro da tela não se aplicam aos alunos, elas são utilizadas para filtrar as turmas que serão exibidas para enturmação.

## Turmas

Serão exibidas as turmas, e suas disciplinas, ofertadas no período letivo e matriz aplicada selecionada no filtro e os alunos que fazem parte da turma. A lista de turmas também pode ser filtrada pelos campos Campus/Polo, Período, Disciplina e Listar disciplinas equivalentes.

Os alunos serão listados e ordenados de acordo com o número no diário.

## Processo de Enturmação

* A situação de matrícula após enturmação será utilizada para definir o status de matrícula no período letivo após a execução do processo.
* Caso o aluno já tenha matrícula na disciplina, o sistema não irá matriculá-lo novamente.

É possível, através do parâmetro ***"Bloquear enturmação para inadimplentes"***, na Parametrização do Educacional em *Matrícula | Movimento 1/3*, bloquear a enturmação de alunos quem tenham pendências financeiras

## Processo de Desenturmação

* O campo situação de matrícula após a enturmação não é utilizado nesse processo.
* Ao final do processo serão exclui as matrículas na turma/disciplina.

# **Ensino Básico**

## Filtro da Tela

* Período Letivo e Matriz Aplicada: são campos de preenchimento obrigatório que são utilizados para filtrar os alunos e turmas disponíveis para o processo de enturmação.
* Situação de Matrícula no Período Letivo após Enturmação: campo obrigatório para execução do processo de enturmação. O valor selecionado no campo será atribuído a matrícula do aluno no período letivo após execução do processo
* Situação de Matrícula no Período Letivo após Desenturmação: campo obrigatório para execução do processo de desenturmação. O valor selecionado no campo será atribuído a matrícula do aluno no período letivo após execução do processo.
* Situação de Matrícula Mudança de Turma - Disciplina Origem: campo obrigatório para execução do processo de mudança de turma (ver abaixo). O valor definido no campo será atribuído a matrícula na disciplina da turma de origem do aluno ao término do processo.
* Situação de Matrícula Mudança de Turma - Disciplina Destino: campo obrigatório para execução do processo de mudança de turma (ver abaixo). O valor definido no campo será atribuído a matrícula na disciplina da turma de destino do aluno ao término do processo.

## Alunos sem turmas

Serão exibidos os alunos que possuem matrícula no período letivo e matriz aplicada selecionada no filtro mas não possuem turma associada. É possível restringir ainda mais os registros exibidos ao utilizar o filtro de alunos existente no cabeçalho dessa lista:

## Turmas

Serão exibidas as turmas ofertadas no período letivo e matriz aplicada selecionada no filtro e os alunos que fazem parte da turma.

## Processo de Mudança de Turma

Para mudar a turma de um ou mais alunos, basta selecionar (clicar, se for um ou Ctrl+clicar se for vários) os alunos e arrastar para a turma correspondente:

As situações de matrículas definidas nos campos Situação de Matrícula Mudança de Turma - Disciplina Origem e Situação de Matrícula Mudança de Turma - Disciplina Destino, serão aplicadas nas disciplinas onde o aluno já possui turma, e as mesmas serão alteradas no processo.

## Disciplinas do Itinerário Formativo

O menu de Enturmação não está apto para a rotina do Novo Ensino Médio - Itinerário Formativo.

# **Validações Comuns**

## Choque de Horário

A **regra** de validação de  irá ocorrer da mesma forma que acontece em qualquer matrícula. Entretanto é no processo de enturmação, se o usuário tiver a permissão especial nos  de **matricular alunos com choque de horário** não será exibida nenhuma mensagem para o usuário e a enturmação será efetuada. Entretanto, se o usuário não tiver esta permissão marcada, ao enturmar o sistema irá exibir uma mensagem informando o choque de horários e a enturmação para estes alunos será bloqueada, os demais alunos que não tiverem choque a enturmação será processada normalmente.

Mensagem de erro de choque de horário, quando o usuário não tem permissão para matricular com choque de horário.
