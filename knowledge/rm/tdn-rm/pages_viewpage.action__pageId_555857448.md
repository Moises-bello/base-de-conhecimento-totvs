---
content_hash: 50613594bb74242d9279112370a98974ed139afcebb036317aec005e3aee3e0e
fetched_at: '2026-06-29T00:10:46.730019+00:00'
page_id: '555857448'
product: rm
source: tdn-rm
title: 3- Frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555857448
version: 169
---

Nesta tela, o professor irá registrar a presença ou ausência para todos os alunos de uma determinada turma/disciplina, em uma etapa e período de data previamente informado.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Frequência diária.**

Filtros

Os filtros podem ser preenchidos:

* Etapa;
* Subturma;
* Data: Esse filtro é correspondente ao intervalo de datas correspondente as aulas da turma/disciplina.

Filtros padrão ao abrir a tela

O portal irá carregar os filtros padrão ao abrir a tela de acordo com a seguinte regra:

* **Data:** Caso a turma/disciplina selecionada tenha uma data especificada na coluna "Data da aula" do diário de classe, ao abrir a tela de frequência diária de data do grupo de filtros, será automaticamente preenchida com esta data. Caso contrário, este campo virá carregado com a data corrente preenchida.
* **Etapa:** Caso tenha alguma etapa disponível onde a data especificada no filtro da data mencionada acima esteja dentro do período de digitação desta etapa.
Filtros obrigatórios

É obrigatório preencher os filtros etapa e de data, sendo que a data informada deve estar dentro do período cadastrado para digitação da etapa.

Período da etapa

As etapas que possuírem o **período de início e término preenchido**no seu cadastro, o portal irá limitar apenas a seleção dentro deste período no filtro de data. Caso a etapa possua **período de início e término** **não preenchido**, o portal não irá limitar nenhum período.

O sistema irá contabilizar somente se

Aulas dadas

A opção de "Aulas dadas", trata-se da quantidade de aulas lecionadas até o presente dia.

Este campo se torna obrigatório quando no cadastro da etapa a opção "**Obrigatório digitação de nº de aulas dadas**" esteja **marcado**.

Ao lado do campo "Aulas dadas" na tela de frequência diária, são exibidos dois botões que possuem a finalidade de sugerir e facilitar o preenchimento deste campo.

São eles:

* **Etapa:** o cálculo de aulas dadas por etapa é feito considerando as aulas compreendidas entre a data inicio e fim da etapa
* **Período:** o calculo de aulas dadas por período é feito considerando o primeiro dia de aula da etapa até a data final selecionado pelo professor, ou então o total de aulas já liberadas para visualização (aulas que já ocorreram). O que for maior

Observação

Quando a turma/disciplina possuir subturma e a mesma for selecionada no filtro, a subturma é considerada no calculo das aulas dadas, ou seja, a sugestão de aulas vai ser o total de aulas da subturma

Não exibir a informação da quantidade de planos de aula para Etapa

O sistema não exibe a quantidade de aulas cadastradas na etapa quando a turma/disciplina possui mais de uma subturma e a quantidade de aulas cadastras para cada subturma são diferentes.

Exemplo: SUBTURMA 1 = 6 aulas cadastradas e SUBTURMA 2 = 5 aulas cadastradas, desta forma o sistema não exibe a quantidade de aulas da etapa

Número de aulas por etapa

Quando uma turma/disciplina possuir subturmas, o sistema informa os horários de acordo com as subturmas, mesmo quando ela não estiver sido selecionada no filtro. Quando não possuir subturmas, o sistema informa os horários de aula da própria turma/disciplina.

Lista de alunos disponíveis

O sistema irá listar os alunos disponíveis na turma/disciplina, considerando a seguinte regra:

Quando a opção "**Disponível para digitação de notas/faltas e Agenda Infantil**" esteja **marcada** no cadastro da situação de matrícula vinculada a disciplina do aluno.

Lista de planos de aulas disponíveis

O portal irá listar os planos de alunas disponíveis na turma/disciplina, considerando a seguinte regra:

falsePeríodo do professor na turma/disciplina

Se o professor da turma/disciplina tiver um período informado (Data de Início e Término) definido, o portal irá exibir a relação de planos de aula até a data limite em que o professor estiver contido no período da turma/disciplina. Caso o período não esteja preenchido, ele não será considerado.

Parâmetro "Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina"

Caso o parâmetro "**Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina**" esteja **marcado**, a **regra acima será desconsiderada**. Parâmetro disponível em: **Configurações | Parâmetros | RM Portal| RM Portal | Portal Geral 1/18**

falsePeríodo informado da etapa

A etapa esteja com a opção **"Data de início" e "Data de término"** **preenchida e válida** em relação a data atual. Caso não esteja preenchido, o sistema irá desconsiderar esta regra;

Limitar o número máximo de registro

O RM disponibiliza um recurso para limitar a quantidade de registros a serem retornados em uma requisição ao servidor por cada DataServer do ERP (nesta tela, o DataServer é o EduFrequenciaDiariaData) com o intuito de evitar tráfego desnecessário ou sobrecarga dos servidores que possam afetar a performance para os demais usuários.

Em caso onde possa ser especificado algum filtro pelo usuário na tela de frequência diária, que retornem uma quantidade de registros maior do que o limite pré-estabelecido para este DataServer, o sistema irá retornar uma mensagem de erro, descrevendo a situação e não será mostrado nenhum dado para o usuário.

Visualizar horários vinculados a turma/disciplina e a subturma

A lista de **horários** das turmas/disciplina que possui subturmas e que estiverem selecionados o filtro de subturma, de acordo com a seguinte regra:

* **Se filtrar por subturma**, o portal deverá listar **apenas os horários que estiverem vinculados a subtutrma** selecionada, sendo os horários dependentes da turma ou independentes;
* **Se não filtrar por subturma**, o portal deverá listar **apenas os horários vinculados na turma/disciplina**. De modo caso exista um horário na subturma independente, não será listado
Visualizar horários mesmo não estando cadastrado no horário

A listagem de **horários**do professor, está diretamente associada ao Parâmetro: **Configurações | Parâmetros | RM Portal - Gerais | Portal - Geral 1/15 | Visualizar/Alterar plano de aula, frequência e quadro de horários sem que o professor esteja cadastrado no horário da turma.**

* Quando o parâmetro estiver **marcado**, o Professor irá visualizar todos os horários das Turmas em que ele está cadastrado, independente se também está alocado nos horários.
* Quando o parâmetro estiver **desmarcado**, o Professor irá visualizar apenas os horários em que ele está alocado.

Coluna de Status

A coluna de Status, corresponde a **situação de matrícula na disciplina** que os alunos estão matriculados.

Digitação de frequência

Ao selecionar o botão de "Pesquisar", o portal irá listar a relação de alunos matriculados nas turmas/disciplinas juntamente com a relação de aulas existentes para esta Turma/Disciplina dentro do período especificado.

Presença e Ausência

Para marcar a Ausência para o(s) aluno(s), o professor deverá marcar com ícone onde para o lado direito o aluno está "**Ausente**" no horário relativo a sua coluna, já quando marcado com o ícone onde para o lado esquerdo o aluno "**Presente**" no horário especificado.

Digitação de faltas

A digitação de faltas **ficará disponível** caso atenda as seguintes regras:

* A data **não estiver com a frequência liberada**;
* A etapa esteja com a opção **"Período de Digitação"** **preenchida e válida** em relação a data atual. Caso não esteja preenchido, o sistema irá desconsiderar esta regra;

Bloqueio de registro de frequencia apenas em horario de aula

**Este parâmetro se aplica apenas para os portais**

Ao configurar o parâmetro "**Permitir realizar/alterar frequência diária somente durante o horário de aula**", a edição de frequência será permitida apenas se for feito dentro do **horário final** da aula acrescentado dos minutos de tolerância parametrizado.

| Dentro do intervalo com tolerância de 15 minutos |
| --- |

| Fora do intervalo com tolerância de 15 minutos |
| --- |

Bloquear alteração de notas e faltas

**Esta regra se a aplica a cada aluno da lista disponível**

O sistema irá **bloquear** as alterações das faltas caso a opção "**Bloquear alterações de notas e faltas**" esteja **marcada** no cadastro da **situação de matrícula na disciplina** de cada aluno.

Perfil de coordenador para habilitar/desabilitar a edição da frequência

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando a frequência de **outro professor** (que não ele mesmo), o portal permitirá que o coordenador **habilite/desabilite a edição da frequência.** Essa ação será permitida com base na permissão de: "**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Frequência diária | Permite o coordenador do curso alterar as informações". **Saiba mais em****

Sincronizar o número da faltas do aluno na etapa

O sistema possui o recurso de sincronizar o número de faltas do aluno na etapa com base na quantidade de faltas diária lançadas, caso atenda as seguintes regras:

Campo "Aulas dadas" preenchido

O sistema irá contabilizar somente se o campo **"Aulas dadas"** esteja **preenchido**.

Subturma

O sistema irá contabilizar as faltas atendendo o critério da subturma. Caso a subturma seja selecionada, o sistema irá contabilizar as faltas apenas dos alunos da subturma selecionada, caso não seja selecionada nenhuma subturma ou não exista, será contabilizado as faltas para todos os alunos da turma/disciplina.

Período da etapa 

O sistema irá considerar as etapas de faltas que atenderem os critérios, se a etapa esteja:

* Se **"Data de início"** e**"Data de término"** **não** **preenchida** (em branco);
* Se **"Data de início"** e**"Data de término" esteja** **preenchida** e a **data da falta** (data em que o aluno recebeu a **ausência**) esteja dentro deste período.

Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina

O sistema irá contabilizar somente se o parâmetro "**Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina**" estiver **desmarcado**. Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Após o **coordenador realizar a liberação da frequência do dia**, o sistema irá realizar o **sincronismo automaticamente.**

Coluna de falta(s)

A coluna de falta(s) corresponde a quantidade de **ausências** que o aluno possui **dentro do período selecionado no filtro**, ou seja apenas dos planos de aula **que estão sendo exibidos na tela.** A quantidade irá contabilizar as faltas durante o lançamento da frequência diária.

Justificativa abonada ou não

A quantidade de **ausências** não leva em consideração se a justificativa da ausência é abonada ou não.

Liberar frequência após salvar

Para realizar a liberação da frequência diária para a visualização dos alunos, deve-se marcar a opção de liberação conforme abaixo:

Apenas as frequências listadas para o professor, considerando os filtros utilizados para a pesquisa é que serão liberadas para os alunos. As frequências que estiverem fora dos critérios de pesquisa, não serão liberadas.

**ATENÇÃO: Ao salvar a frequência por turma utilizando a opção "Liberar frequência após salvar" marcada:**

* **Não será possível realizar alterações nas frequências diárias dos alunos, nem remover a liberação destas frequências. (porém a Instituição de Ensino poderá cancelar a liberação através do processo: [Liberar/Cancelar frequência diária](https://tdn.totvs.com/x/1sMpJw) disponível no RM.exe).**
* **Consequentemente, todas as frequências liberadas ficam "disponíveis para os alunos" e serão exibidas na tela de frequência diária para o professor apenas para a visualização;**

Esta opção aparece somente se o parâmetro "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" estiver **desmarcado**. Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Alterar frequência pelo portal e app mesmo após liberar o dia

Para permitir que o professor consiga alterar registros da frequência diária, mesmo após a liberação de frequência já tenha sido realizada, é necessário habilitar o parâmetro "Alterar frequência pelo portal e app mesmo após liberar o dia**"**. O parâmetro está disponível em: **Serviços Globais | Sistema: Educacional | (selecionar o perfil) | Anexo | Parâmetros Educacionais | Notas e Faltas".**

Turma gerencial e gerenciada

Ao marcar o parâmetro "**Parâmetros | RM Portal | Secretaria |****Utilizar Turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula e upload de materiais no portal**".

O sistema terá o seguinte comportamento: As faltas e presenças na tela de “Frequência Diária” serão realizadas através da turma/disciplina gerencial, porém internamente o sistema replica as informações para as turmas gerenciadas correspondentes.

O objetivo da Turma/Disciplina Gerencial é possibilitar aos professores ao acessar as informações agrupadas das **turmas/disciplinas gerenciais** (relacionadas) a uma única **turma/disciplina gerencial, assim ele consegue lançar notas e faltas de uma única vez, ao invés de ter que selecionar as turmas/disciplinas separadamente.** Para isso, as turmas/disciplinas gerenciadas devem ter a mesma etapa de nota, falta, avaliação, professor, horário, plano de aula, mas não necessariamente o mesmo turno.

Turma mista

Ao realizar uma Frequência Diária em uma **Turma Mista**, os registros **não serão replicados** para a **Turma de Origem** e vice-versa.

Aula geminada

Após realizar o filtro pelas frequências diárias, será exibido uma tabela contendo o nome do aluno, as aulas cadastradas para o período informado no filtro e as respectivas frequência dos alunos.

Em dias de aula que tenham mais de um horário cadastrado, a alteração de frequência feita em um horário será propagada para todos os horários daquele dia para aquele aluno.

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
