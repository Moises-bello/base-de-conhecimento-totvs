---
content_hash: 6fb3d3f9d20c559765a13594105cad13264cc9f1b0328072d4c61f6781082a1b
fetched_at: '2026-06-29T00:10:57.179422+00:00'
page_id: '594422888'
product: rm
source: tdn-rm
title: 10. Itinerário Formativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=594422888
version: 46
---

**Este Menu está disponível apenas para o contexto ENSINO BÁSICO.**

## Matrícula no itinerário formativo

Os usuários do Novo Portal do Aluno (aluno, pais e responsáveis) que utilizam o processo de Confirmação de Matrícula Web poderão alterar(Incluir e excluir opcionalmente conforme configuração) os  disponíveis para o aluno.

Visão no Portal do Aluno onde é possível selecionar um itinerário para adicionar, ou desmarcar para excluir.

**A partir da 12.1.2205 é possível escolher quais disciplinas de itinerário o aluno quer cursar**, em versões anteriores a release 12.1.2205 as disciplinas de itinerários formativos em nenhum momento serão exibidas. Em todas as versões turmas não são exibidas no portal.

No passo das  não serão exibidas as disciplinas de itinerário formativo.

A partir da versão release **12.1.2205** o layout da tela foi alterado para que possa ser exibido um feedback de quantidade de itinerário mínimos e máximo, bem como a quantidade que já foi selecionada.

Caso as disciplinas selecionadas estejam fora do padrão de mínimo e máximo que pode ser selecionado pelo aluno, o campo de itinerários selecionados fica em vermelho.

Se as disciplinas dentro do itinerário formativo estiver com a carga horária fora do padrão mínimo e máximo, o campo de carga horária selecionado fica em vermelho.

Foi criada uma Parametrização para possibilitar que este novo passo esteja visível ou não no portal:

* Acesse Configurações > RM Portal > RM Portal Matricula > Geral 5/5;

Mudança de regra

A partir das versões **12.1.27.363**, **12.1.28.295**, **12.1.29.259**, **12.1.31.165**, **12.1.32.106** e **12.1.33**e com **todos** os **scripts** dos respectivos patches **executados**, este parâmetro de **exibir o itinerário formativo durante a matrícula**, deixa de ser um parâmetro geral e passa a ser um parâmetro da .

E somente será possível adicionar ou excluir um itinerário de acordo com a parametrização definida na Situação de Matrícula: 

A partir da versão 12.1.2306.104 foi incluído o [agrupamento de itinerário formativos](https://tdn.totvs.com/pages/viewpage.action?pageId=756478182) no portal do aluno.

Para visualizar o Agrupamento de itinerário na confirmação de matricula, é necessário que na parametrização por curso a opção, “ Utiliza agrupamento de itinerários formativos”, esteja marcada.

O grupo de Itinerário somente é exibido, quando houver itinerários vinculados a ele que esteja com a data de disponibilidade válida ou com as datas sem preenchimento.

Durante a confirmação de matrícula o sistema valida a quantidade de mínimo e máximo de itinerário por agrupamento definida no [cadastro de agrupamento](https://tdn.totvs.com/pages/viewpage.action?pageId=756478182).

Além de verificar quais itinerários são obrigatórios dentro de cada grupo de acordo com flag "Obrigatório" marcada dentro do cadastro de disponibilidade do itinerário formativo.

Caminho: Currículo Oferta| Oferta| Parametrização por curso| Disponibilidade do Itinerário formativo.

## Enturmação no Itinerário

Na , no anexo Disponibilidade do Itinerário Formativo, é possível informar a turma do Itinerário Formativo para enturmação.

Somente serão exibidas turmas que possua no mínimo uma disciplina do Itinerário Formativo selecionado.

Visualização e Escolha de Disciplinas

Disponível apenas a partir da release 12.1.2205.

É possível visualizar e escolher as disciplinas de itinerário formativo. Para isso basta clicar no itinerário para expandir e visualizar as disciplinas. A partir daí o aluno poderá escolher quais as disciplinas deseja cursar dentro de cada itinerário de seu interesse. Porém para isso ocorrer é necessário ir na  criar o registro referente ao itinerário e marcar o parâmetro para exibir as disciplinas do itinerário formativo.

Serão exibidas todas as disciplinas que foram cadastradas no itinerário formativo independente de existir ou não a oferta de turma. Entretanto, para que o aluno seja de fato matriculado na disciplina selecionada, é necessário que seja parametrizado a turma na  no anexo da .

O número de vagas apresentado para cada disciplina é o número máximo de alunos definido na  da turma parametrizada na , caso não tenha sido preenchido este campo na  a coluna **Núm. de vagas** virá com o valor zerado.

Por meio o ícone  na coluna de  será possível o aluno visualizar quais são as áreas do conhecimento daquela disciplina. Ao clicar neste ícone um popup será aberto informando quais são estas áreas.

## Validações

### Disponibilidade sem turma

Para que a enturmação seja realizada a turma deverá estar preenchida na , caso não exista turma parametrizada, uma mensagem de erro, conforme abaixo, para o aluno será mostrada ao tentar avançar na matrícula.

### Disciplina sem vagas

Caso a disciplina do itinerário selecionada tenha número de vagas igual a 0, indica que número de alunos já matriculados na turma disciplina é igual ao **Nº máximo de alunos** informado no cadastro da  ou o **Nº máximo de alunos**na  está vazio ou zerado. Com isso, se não possuir vagas a mensagem abaixo será exibida.

É necessário informar o **número máximo de alunos** na  que oferta o Itinerário Formativo, mesmo se na turma principal do aluno, na matrícula no período letivo, existirem as disciplina de Itinerário Formativo oferecidas.

O controle de vagas virá sempre do cadastro da , quando o assunto for Itinerário Formativo, mesmo que o controle de vagas na  seja por **turma**.

A partir da versão 12.1.2306.133, na [disponibilidade de itinerário formativo](https://tdn.totvs.com/pages/viewpage.action?pageId=561843285), ao marcar a opção, "Exibir disciplinas do itinerário formativo durante a matrícula no portal do aluno",ocampo Turma do Itinerário Formativo torna-se obrigatório.

Para verificar a disponibilidade das disciplinas de Itinerário Formativo no portal, o sistema irá validar se a [turma disciplina](https://tdn.totvs.com/display/LRM/Turma+Disciplina)  referente a turma parametrizada em questão, está com a data inicial e final da matricula válida, ou em branco. E se a [turma disciplina](https://tdn.totvs.com/display/LRM/Turma+Disciplina) está ativa. Após essas validações as disciplinas são exibidas no portal.

A partir da versões 12.1.2306.159 , o Sistema permite mediante parametrização, realizar a escolha de turmas/disciplinas no momento de escolher as disciplinas dos itinerários formativos ,durante a confirmação de matrícula.

Para visualizar as Turmas o parâmetro "Utiliza escolha de turmas/disciplinas", disponível na [parametrização por curso](https://tdn.totvs.com/pages/viewpage.action?pageId=425458887) precisa está marcado.

As turmas disciplinas disponíveis para exibição são as que estão ativas, com data de inicio e fim de matricula valida.

A Visualização do quadro de horário é mediante a marcação do parâmetro "Utiliza escolha de turmas/disciplinas".

A exibição de características da turma, como Professor , controle de vaga é até mesmo choque de horário, ocorre se os parâmetros abaixo estiverem marcados.

Assim, acesse: Configurações | Parâmetros | 15.04 - RM Portal | 15.04.02 - RM portal Matricula | Portal - Matricula/ Geral 5/6

Apartir da versão 12.1.2306.175,12.1.2310.110 e 12.1.2402 foi incluído o parâmetro, Bloqueia alteração de situação matrícula em itinerário formativo na matrícula online.

 

Ao marcar este parâmetro, o status com essa parametrização configurada, não realiza a troca de situação de matrícula pela confirmação da rematrícula web ou matrícula de itinerário pelo menu exclusivo.

[Sistema Indústria](https://tdn.totvs.com/pages/releaseview.action?pageId=527384229)
