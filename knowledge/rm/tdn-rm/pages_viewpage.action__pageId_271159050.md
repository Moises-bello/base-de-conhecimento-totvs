---
content_hash: c5dcc0dcaec2697515dcd3a38b3d07da33f3396050e97340edd29911703be827
fetched_at: '2026-06-29T00:08:25.843648+00:00'
page_id: '271159050'
product: rm
source: tdn-rm
title: RMEDU00001_Reservas de Recurso e Instalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271159050
version: 5
---

|  |  |
| --- | --- |
| **Produto:** | Totvs Educacional |
| **Versões:** | 12.1.14 |
| **Processo:** | Reservas de Recurso e Instalação |

**Reserva de Recurso**

Implementado no sistema a possibilidade de o professor fazer reserva de um recurso para ser usado em aula (dia + hora inicio + hora fim). Essa reserva pode ser feita pelo Portal, com uma data mínima de antecedência. O professor deve identificar os equipamentos pelo tipo e não pelo recurso físico em si.

**Reserva de Instalações**

Implementando no sistema a possibilidade de o professor fazer uma reserva de sala para data/horário  específico, não necessariamente vinculado ao horário de aula. Também pode ser feito pelo Portal, com mínimo de antecedência.

**Requisitos:**

* **Professor possuir acesso aos menus: reserva de recursos e reservas de instalações;**
* **Usuário do sistema possuir acesso ao menu: reserva de recurso e instalação;**
* **Os devidos cadastros de instalações e reservas estarem inseridos no sistema;**
* **Sistema estar estar devidamente parametrizado, de acordo com a regra de negócio da instituição.**

**RESERVA DE RECURSOS**

Para que seja possível realizar a **Reserva de Recursos** no sistema, primeiramente devem ser cadastrados os tipos de recursos e os recursos a serem disponibilizados na instituição.

| Acesse: CURRÍCULO E OFERTA / AUXILIARES / TIPOS DE RECURSOS |
| --- |

Ao criar um tipo de recurso, deve-se marcar o mesmo para permitir ou não reserva.

| Acesse: CURRÍCULO **E OFERTA/ AUXILIARES / RECURSOS** |
| --- |

Cadastre um recurso, vincule-o ao Tipo de Recurso cadastrado.

Ao entrar no cadastro de recurso em '**CURRÍCULO** **E OFERTA/ AUXILIARES / TIPOS DE RECURSOS e/ou RECURSOS'**, uma tela pode ser aberta automaticamente em caso de existência de algum recurso que não tenha sido vinculado à filial. Esta janela é um assistente para vinculação de recursos à Filial. Na criação do recurso deve-se informar a qual tipo de recurso este será associado. Para este também se deve informar se permite ou não reserva.

| Acesse ATIVIDADES ACADÊMICAS / RESERVA DE RECURSO E INSTALAÇÃO |
| --- |

No cadastro da Atividade agendada deve-se marcar para qual tipo de pessoa esta reserva estará associada (Aluno e/ou Professor) e qual é o tipo a qual esta permite reserva (Recurso e/ou Instalação), caso seja marcado algum tipo de reserva, somente será possível rodar o processo e fazer a reserva deste tipo escolhido.

Após configurações, o processo para Reserva de Recursos pode ser efetuado.

Selecione uma pessoa cadastrada e avance.

No processo de reserva, pode-se ou não fazer uma seleção por plano de aula, buscando assim o professor, turma e o dia da aula.

Em caso de não utilização do plano de aula para a reserva, será necessário Selecionar o período que compreende a reserva de recursos, o horário, os dias da semana em questão em que a reserva de recurso poderá ser efetuada e em caso de feriados, considerar ou não de acordo com calendário. Configure e avance o processo.

Selecione o tipo e o Recurso a serem reservados e avance.

Para que o recurso seja apresentado no processo de reserva para escolha é necessário que em: **CONFIGURAÇÕES / PARÂMETROS / SECRETARIA / GERAL**, o parâmetro **"Seleção de recurso durante a reserva"** esteja marcado.

Na atividade agendada é possível inserir os usuários que terão a reserva de recurso e/ou instalações associadas à agenda global situada em **SERVIÇOS GLOBAIS / GESTÃO / AGENDA.**

Para que a reserva de recurso seja exportada para a agenda é necessário que o parâmetro na criação da reserva de recurso **'Permite exportação para agenda global'** esteja marcado.

Selecione um usuário, caso tenha interesse e avance.

Após as configurações, o processo pode ser executado e o recurso será reservado à pessoa escolhida no início do processo.

Ao acessar a agenda através dos serviços globais, é possível verificar o agendamento da reserva de recursos.

| Acesse: ATIVIDADES ACADÊMICAS/ RESERVA DE RECURSO E INSTALAÇÃO / Anexo / RESERVA DE RECURSO pode-se verificar que o recurso foi agendado. |
| --- |

O Totvs Educacional em Reserva de Recursos e Instalação possui integração com o Totvs Gestão Patrimonial. Ao cadastrar um recurso no sistema pode-se atribuir um nome ao recurso ou utilizar do nome cadastrado em um determinado 'BEM' cadastrado no Totvs Gestão Patrimonial.

* Abra o Totvs Gestão Patrimonial em CADASTROS / BENS. Cadastre um novo bem através do botão . O bem em questão deve estar vinculado à filial para o qual o Recurso criado no Totvs Educacional também foi associado.
* Entre no recurso criado e marque o parâmetro 'Cadastrar bem existente' e procure pelo 'bem' inserido ao Totvs Gestão Patrimonial e salve.

**Reserva de Recursos via Portal**

Entre Portal Corpore.net e selecione o menu Educacional como professor no menu **'RESERVA DE RECURSOS'**.

Clique sobre o botão 'Fazer reserva'. Assim será exibida uma janela para auxiliar na criação da reserva. Nesta janela selecione a atividade agendada criada no caminho: **ATIVIDADES ACADÊMICAS / RESERVA DE RECURSO E INSTALAÇÃO**, selecione o 'Tipo de Recurso' e o 'Recurso'.

Caso tenha interesse, identifique para qual turma/disciplina será associada a reserva atribuindo uma aula ou uma data inicial e final para a reserva. Após seleção e configuração, clique em salvar para que o recurso seja reservado.

**RESERVA DE INSTALAÇÕES**

Para proceder com a reserva de Instalação é necessário que os seguintes itens sejam criados.

* Campus
* Prédio
* Bloco
* Tipo de Sala
* Sala

| Acesse: CURRÍCULO E OFERTA / AUXILIARES / CAMPUS. |
| --- |

Insira um novo Campus e marque se este está ativo ou não.

| Acesse **CURRÍCULO E OFERTA/ AUXILIARES / TIPO DE SALA**. |
| --- |

Cadastre um novo tipo de sala, identifique se este permite ou não reserva e salve.

| Acesse CURRICULO E OFERTA/ AUXILIARES / PREDIOS/BLOCOS/SALAS. |
| --- |

Insira um novo Prédio, salve.

Em **Anexo / Bloco**, insira um novo bloco e salve.

Em **Anexo / Salas** faz-se um vínculo entre o PRÉDIO, o TIPO DE SALA e SALA. Deve-se identificar se esta sala permite ou não reserva.

O Totvs Educacional em Reserva de Recursos e Instalação possui integração com o Totvs Gestão Patrimonial. Ao cadastrar uma Sala no sistema em CURRÍCULO E OFERTA/ AUXILIARES / PRÉDIOS/BLOCOS/SALAS pode-se atribuir uma localidade cadastrada no Totvs Gestão Patrimonial.

Entre no Totvs Gestão Patrimonial em CADASTROS / LOCALIZAÇÕES e crie uma nova localização.

* Deve-se informar qual é o tipo da localidade (Interna ou Externa).
* Deve-se informar se a localidade está ativa ou não.
* Entre no Totvs Educacional no cadastro de Salas em CURRÍCULO E OFERTA/ AUXILIARES / PRÉDIOS/BLOCOS/SALAS e informe a localidade buscando o cadastro feito anteriormente no Totvs Gestão Patrimonial.

Após todas as inserções e configurações o processo para Reserva de Instalação pode ser executado.

Entre na atividade agendada criada no caminho: **ATIVIDADES ACADÊMICAS / RESERVA DE RECURSO E INSTALAÇÃO** do tipo 'Todos' ou 'Instalação' e rode o processo 'Reserva de Instalação'

Selecione uma pessoa cadastrada no sistema e avance.

Em caso de não utilização do plano de aula para a reserva, será necessário Selecionar o período que compreende a Reserva de Instalação, o horário, os dias da semana em questão em que a reserva de recurso poderá ser efetuada e em caso de feriados, considerar ou não de acordo com calendário. Configure e avance.

Selecione: Campus, Prédio, Bloco, Tipo de Sala, Sala e Avance.

Atualmente é possível já reservar um recurso na reserva de instalação. Para que isso seja possível é necessário amarrar no cadastro do Recurso um espaço físico. Acesse o cadastro da Recursos em **'Anexos / Associação de recurso a espaço físico'**e informe Prédio, Bloco e Sala. Caso o Recurso seja fixo no espaço físico, marque a opção **Exclusivo da sala**.

Na atividade agendada é possível inserir os usuários que terão a reserva de recurso e/ou instalações associadas à agenda situada em SERVIÇOS GLOBAIS/ GESTÃO / AGENDA.

Para que a reserva de Instalação seja exportada para a agenda é necessário que o parâmetro na criação da reserva de recurso **'Permite exportação para agenda global'** esteja marcado.

Selecione um usuário, caso tenha interesse e avance.

Após as configurações, o processo pode ser executado e o recurso será reservado à pessoa escolhida no início do processo.

A Instalação Reservada pode ser verificada em: **ATIVIDADES ACADÊMICAS / RESERVA DE RECURSO E INSTALAÇÃO / Anexo / RESERVA DE INSTALAÇÃO**.

**Reserva de Instalação via Portal**

Ao entrar no Portal Corpore.net, selecione o menu Educacional como professor no menu 'RESERVA DE INSTALAÇÕES.

Clique sobre o botão 'Fazer reserva'. Assim será exibida uma janela para auxiliar na criação da reserva.

* Selecione a atividade agendada criada no caminho: ATIVIDADES ACADÊMICAS / RESERVA DE RECURSO E INSTALAÇÃO
* Selecione o Campus, Prédio, Bloco, Tipo de Sala e Sala criados anteriormente.
* Caso tenha interesse, Identifique para qual turma/disciplina será associada a reserva atribuindo uma aula ou uma data inicial e final para a reserva.

Após seleção e configuração, clique em salvar para que o recurso seja reservado.
