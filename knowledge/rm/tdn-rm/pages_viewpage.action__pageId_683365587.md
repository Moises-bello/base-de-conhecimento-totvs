---
content_hash: 7d23b21808f25153640ee8d07b977de60382fc7a341703d2f8ae2f64b631fe9d
fetched_at: '2026-06-29T00:11:18.149987+00:00'
page_id: '683365587'
product: rm
source: tdn-rm
title: 9- Frequência por turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683365587
version: 57
---

Nesta tela o professor irá registrar a presença e ausência para um aluno ou mais alunos, e ela será registrada para todas as turmas e disciplinas daquele professor no dia informado.

false

**Disponível apenas para o Contexto Ensino Básico**

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Digitação de frequência por turma diária.**

Aulas dadas

A opção de "Aulas dadas", trata-se da quantidade de aulas lecionadas até o presente dia.

Este campo se torna obrigatório quando no cadastro da etapa a opção "**Obrigatório digitação de nº de aulas dadas**" esteja **marcado**.

Ao lado do campo "Aulas dadas" na tela de frequência diária, são exibidos dois botões que possuem a finalidade de sugerir e facilitar o preenchimento deste campo.

São eles:

* **Etapa:** o cálculo de aulas dadas por etapa é feito considerando as aulas compreendidas entre a data inicio e fim da etapa
* **Período:** o calculo de aulas dadas por período é feito considerando o primeiro dia de aula da etapa até a data final selecionado pelo professor, ou então o total de aulas já liberadas para visualização (aulas que já ocorreram). O que for maior

Não exibir a informação da quantidade de planos de aula para Etapa

O sistema não exibe a quantidade de aulas cadastradas na etapa quando a turma/disciplina possui mais de uma subturma e a quantidade de aulas cadastras para cada subturma são diferentes.

Exemplo: SUBTURMA 1 = 6 aulas cadastradas e SUBTURMA 2 = 5 aulas cadastradas, desta forma o sistema não exibe a quantidade de aulas da etapa

Lista de alunos disponíveis

O sistema irá listar os alunos disponíveis na turma/disciplina, considerando a seguinte regra:

Quando a opção "**Disponível para digitação de notas/faltas e Agenda Infantil**" esteja **marcada**no cadastro da situação de matrícula vinculada a disciplina do aluno.

Lista de planos de aulas disponíveis

O portal irá listar os planos de alunas disponíveis na turma/disciplina, considerando a seguinte regra:

falsePeríodo do professor na turma/disciplina

Se o professor da turma/disciplina tiver um período informado (Data de Início e Término) definido, o portal irá exibir a relação de planos de aula até a data limite em que o professor estiver contido no período da turma/disciplina. Caso o período não esteja preenchido, ele não será considerado.

Parâmetro "Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina"

Caso o parâmetro "**Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina**" esteja **marcado**, a **regra acima será desconsiderada**. Parâmetro disponível em: **Configurações | Parâmetros | RM Portal| RM Portal | Portal Geral 1/18**

Parâmetro "Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina"

Caso o parâmetro "**Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina**" esteja **marcado**, a **regra acima será desconsiderada**. Parâmetro disponível em: **Configurações | Parâmetros | RM Portal| RM Portal | Portal Geral 1/18**

Visualizar horários mesmo não estando cadastrado no horário

A listagem de **horários**do professor, está diretamente associada ao Parâmetro: **Configurações | Parâmetros | RM Portal - Gerais | Portal - Geral 1/15 | Visualizar/Alterar plano de aula, frequência e quadro de horários sem que o professor esteja cadastrado no horário da turma.**

* Quando o parâmetro estiver **marcado**, o Professor irá visualizar todos os horários das Turmas em que ele está cadastrado, independente se também está alocado nos horários.
* Quando o parâmetro estiver **desmarcado**, o Professor irá visualizar apenas os horários em que ele está alocado.

Coluna de Status

A coluna de Status, corresponde a **situação de matrícula no período letivo** que o aluno está matriculado.

Divergência de frequência entre os horários das turmas/disciplina

Para o aluno que possuir divergência de frequência entre os horários das turmas/disciplina, o sistema irá destacar o RA e Nome do aluno com a cor vermelha, informando assim que ele possui presença/ausência em algumas aulas do dia, porém não em todas que o professor leciona.

Digitação de frequência

Ao selecionar o botão de "Pesquisar", o portal irá listar a relação de alunos matriculados nas turmas/disciplinas.

Presença e Ausência

Para marcar a Ausência para o(s) aluno(s), o professor deverá marcar com ícone onde para o lado direito o aluno está "**Ausente**" no horário relativo a sua coluna, já quando marcado com o ícone onde para o lado esquerdo o aluno "**Presente**" no horário especificado.

Digitação de faltas

A digitação de faltas **ficará disponível** caso atenda as seguintes regras:

* A data **não estiver com a frequência liberada**;
* A etapa esteja com a opção **"Período de Digitação"** **preenchida e válida** em relação a data atual. Caso não esteja preenchido, o sistema irá desconsiderar esta regra;

Bloqueio de registro de frequencia apenas em horario de aula

**Este parâmetro se aplica apenas para os portais**

Ao configurar o parâmetro "**Permitir realizar/alterar frequência diária somente durante o horário de aula**", a edição de frequência será permitida apenas se for feito dentro do **horário final** da aula acrescentado dos minutos de tolerância parametrizado.

Bloquear alteração de notas e faltas

**Esta regra se a aplica a cada aluno da lista disponível**

O sistema irá **bloquear** as alterações das faltas caso a opção "**Bloquear alterações de notas e faltas**" esteja **marcada** no cadastro da **situação de matrícula na disciplina** de cada aluno.

Perfil de coordenador para habilitar/desabilitar a edição da frequência

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando a frequência de **outro professor** (que não ele mesmo), o portal permitirá que o coordenador **habilite/desabilite a edição da frequência.** Essa ação será permitida com base na permissão de: "**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Frequência diária | Permite o coordenador do curso alterar as informações". **Saiba mais em****

Presença e Ausência para todos os horários do dia

Ao selecionar a opção "Todas do dia", o sistema irá marcar como presença/ausência para todos os horários disponíveis no dia.

Liberar frequência após salvar

Para realizar a liberação da frequência diária para a visualização dos alunos, deve-se marcar a opção de liberação conforme abaixo:

**ATENÇÃO: Ao salvar a frequência por turma utilizando a opção "Liberar frequência após salvar" marcada:**

* **Não será possível realizar alterações nas frequências diárias dos alunos, nem remover a liberação destas frequências. (A Instituição de Ensino poderá cancelar a liberação através do processo: [Liberar/Cancelar frequência diária](https://tdn.totvs.com/x/1sMpJw) disponível no RM.exe).**
* **Consequentemente, todas as frequências liberadas ficam "disponíveis para os alunos" e serão exibidas na tela de frequência diária para o professor apenas para a visualização;**

Esta opção aparece somente se o parâmetro "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" estiver **desmarcado**. Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Alterar frequência pelo portal e app mesmo após liberar o dia

Para permitir que o professor consiga alterar registros da frequência diária, mesmo após a liberação de frequência já tenha sido realizada, é necessário habilitar o parâmetro "Alterar frequência pelo portal e app mesmo após liberar o dia**"**. O parâmetro está disponível em: **Serviços Globais | Sistema: Educacional | (selecionar o perfil) | Anexo | Parâmetros Educacionais | Notas e Faltas".**

Turma gerencial e gerenciada

Ao marcar o parâmetro "**Parâmetros | RM Portal | Secretaria |****Utilizar Turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula e upload de materiais no portal**".

As faltas e presenças na tela de “Frequência por Turma” serão realizadas através da turma/disciplina gerencial, porém internamente o sistema realiza as faltas e presenças nas turmas gerenciadas correspondente.

O objetivo da Turma/Disciplina Gerencial é possibilitar os professores ao acessar as informações agrupadas das **turmas/disciplinas gerencias** (relacionadas) a uma única **turma/disciplina gerencial, assim ele consegue lançar notas e faltas de uma única vez, ao invés de ter que selecionar as turmas/disciplinas separadamente.** Para isso, as turmas/disciplinas gerenciadas devem ter a mesma etapa de nota, falta, avaliação, professor, horário, plano de aula, mas não necessariamente o mesmo turno.

Justificativa de ausência

Ao definir ausência para um aluno, é exibido ao lado do botão uma nova opção para definir uma justificativa para a ausência. **Para saber mais acesse** 

A justificativa com a cor **a****marela** indica uma falta não abonada, conforme descrito na legenda.

A justificativa com a cor **verde** indica uma falta abonada, conforme descrito na legenda.

Perfil de professor para justificar a ausência

Para poder incluir, alterar e excluir uma justificativa, o perfil do usuário do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Frequência diária | Permitir ao professor justificar faltas**

Perfil de coordenador para justificar a ausência

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando a frequência de **outro professor** (que não ele mesmo), o portal permitirá que o coordenador inclua, altere e exclua justificativas. Essa ação será permitida com base na permissão de: "**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Frequência diária | Permite o coordenador justificar faltas". **Saiba mais em****

Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina

A contabilização de abono ou não das faltas, poderá ser altera pelo **coordenador** se o parâmetro "**Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina**" estiver **marcado**. Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Status da frequência

Na tabela contendo a frequência dos alunos algumas colunas são marcadas preenchendo o fundo da célula para indicar algumas informações referente a frequência. Acima da tabela é exibido uma legenda indicando o significado da cor preenchida na célula.
