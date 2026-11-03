---
content_hash: 0ce254d9bec99777ac32329bd55d818320d30abbe233c2f5a76ac089cc6e69e3
fetched_at: '2026-06-28T21:35:31.673277+00:00'
page_id: '960992997'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Regras do formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960992997
version: 11
---

# Falando de regras do formulário...

---

Regras do formulário são eventos que podem ocorrer no formulário criado, em determinada atividade e em um campo específico. Estes eventos ocorrem apenas em atividades normais ou atividade de início de um processo.

Como ações, é possível escolher entre desabilitar um campo, validar valor, definir um valor e desaparecer com o campo na tela. Este procedimento gera um evento de formulário com as configurações definidas.

exemplo

Quando um colaborador seleciona o setor TI como solicitante, uma regra de formulário pode automaticamente exibir um campo adicional para informar o modelo do equipamento desejado. Se outro setor for selecionado, esse campo permanece oculto. Evitando confusões e tornando o preenchimento mais rápido.

## Ordem de execução das regras no novo editor de formulários

---

A execução das regras segue uma hierarquia definida para garantir que comportamentos gerais sejam aplicados antes dos mais específicos. Seguindo a ordem abaixo:

**Regras gerais (válidas para todas as atividades)**

Executadas primeiro:

1. Em todas as atividades
2. Agrupadores gerais

   * Painel
   * Abas
   * Tabela
3. Campo específico geral

**Regras específicas da atividade atual**

Após concluir as regras gerais, a plataforma executa as regras referentes à atividade em que o formulário está sendo utilizado, também seguindo a mesma prioridade:

1. Atividade específica
2. Agrupadores da atividade

   * Painel
   * Abas
   * Tabela
3. Campo específico da atividade

Essa estrutura garante que primeiro sejam aplicadas regras mais amplas, que impactam o formulário inteiro, e depois as regras direcionadas ao contexto da atividade atual, sempre da mais geral para a mais específica.

## Adicionar regra

---

Siga os passos abaixo após configurar o processo e o formulário no qual será adicionado a regra.

Dica!

* [Clique aqui](https://tdn.totvs.com/x/DUxGMw) e saiba mais sobre como configurar processos.
* [Clique aqui](https://tdn.totvs.com/x/jH6MNg) para saber como criar e editar um formulário de processo.

**01.** Clique em **Regras do formulário** .

**02.** Na modal apresentada, clique em **Adicionar regra**.

**03.** Em **Quando a solicitação chegar na atividade** selecione em qual atividade a regra definida para o campo será executada.

**04.** Em **o campo** selecione o campo para o qual a regra será definida.

**05.** Em **do formulário será** selecione a ação da regra que será definida, sendo possível definir entre:

* **Ocultado**: determina que o campo será ocultado quando a solicitação estiver na atividade que foi selecionada na regra.
* **Exibido**: determina que o campo será exibido somente quando a solicitação estiver na atividade que foi selecionada na regra.
* **Desabilitado**: determina que o campo será exibido desabilitado para preenchimento quando a solicitação estiver na atividade que foi selecionada na regra.
* **Habilitado**: determina que o campo será exibido habilitado para preenchimento quando a solicitação estiver na atividade que foi selecionada na regra.
* **Obrigatório**: determina que o campo será obrigatório para preenchimento quando a solicitação estiver na atividade que foi selecionada na regra.
* **Opcional**: a regra Opcional sobrescreve a regra Obrigatório em atividades específicas. Quando um campo está configurado como Obrigatório em todas as atividades, ao aplicar a regra Opcional em uma atividade específica, o campo deixa de ser obrigatório **apenas nessa atividade**.

#000000#f2f2f2

Quando um campo do tipo **Painel** estiver com a propriedade **“Permite abrir e fechar?”** ativada, ele disponibilizará nas regras as ações **Expandido** e **Retraído**.

Assim, ao criar ou configurar uma regra e selecionar o campo Painel, será possível definir se ele será exibido **expandido ou retraído** quando a solicitação chegar à atividade definida no passo **“Quando a solicitação chegar na atividade”**.

#5A5A5A#f2f2f2

* **Definido valor**: determina que será atribuído um valor específico para o campo quando a solicitação estiver na atividade selecionada na regra. Ao utilizar esta opção é apresentado outros campos para finalizar a configuração. No campo "**com**" defina um valor entre:

O que isso significa?

**Personalização**

* **Valor fixo**: nesta opção é necessário preencher o valor que será aplicado no campo "**igual a**".

Exemplo

Vemos na imagem que a regra será aplicada quando chegar na atividade **Complementar dados**, o campo **Departamento** será preenchido automaticamente com o **valor fixo** definido como **Diretoria**.

**Usuário atual**

* **Código do usuário**: ao selecionar esta opção o campo do formulário será preenchido com o código do usuário.
* **Nome**: ao selecionar esta opção o campo do formulário será preenchido com o nome do usuário.
* **Nome completo**: ao selecionar esta opção o campo do formulário será preenchido com o nome completo do usuário.
* **E-mail**: ao selecionar esta opção o campo do formulário será preenchido com o e-mail do usuário.

**Solicitação**

* **Data de abertura**: ao selecionar esta opção o campo do formulário será preenchido com a data de abertura da solicitação.
* **Data atual**: ao selecionar esta opção o campo do formulário será preenchido com a data de atual do dia.
* **Código da atividade**: ao selecionar esta opção o campo do formulário será preenchido com o código da atividade.
* **Código da solicitação**: ao selecionar esta opção o campo do formulário será preenchido com o código da solicitação.
* **Usuário solicitante**: ao selecionar esta opção o campo do formulário será preenchido com o usuário solicitante.
* **E-mail do solicitante**: ao selecionar esta opção o campo do formulário será preenchido com o e-mail do usuário solicitante.
#5A5A5A#f2f2f2

* **Validado valor**: determina que será executada uma validação de valor no campo quando a solicitação estiver na atividade selecionada na regra. Nesse caso, é necessário satisfazer as condições do tipo Ou e E.

Neste caso, o campo **satisfazendo** será apresentado, para configurar a condição do tipo (E) ou (OU).

Exemplo

No processo de pagamento de férias, a regra garante que a **Data de Pagamento** das férias não seja registrada após a **Data de Início das férias (data do vencimento)**, evitando inconsistências no cronograma de pagamento ao colaborador.

Outras opções de validação de valor selecionando um operador:

* **Maior que**: determina que o campo do formulário terá o valor validado atendendo a uma condição maior que o valor selecionado.
* **Maior ou igual que**: determina que o campo do formulário terá o valor validado atendendo a uma condição maior que ou igual ao valor selecionado.
* **Menor que**: determina que o campo do formulário terá o valor validado atendendo a uma condição menor que o valor selecionado.
* **Menor ou igual que**: determina que o campo do formulário terá o valor validado atendendo a uma condição menor ou igual ao valor selecionado.
* **Igual a**: determina que o campo do formulário terá o valor validado atendendo a uma condição igual ao valor selecionado.
* **Diferente de**: determina que o campo do formulário terá o valor validado atendendo a uma condição diferente ao valor selecionado.

Outras opções de validação de valor selecionando um valor:

* **Campo do formulário**;
* **Valor específico**;
* **Número da solicitação**;
* **Matrícula do usuário logado**;
* **Data atual**;
* **Vazio**.

* **Validado formato**: determina que será executada uma validação de formato no campo quando a solicitação estiver na atividade selecionada na regra. Nesse caso, é necessário satisfazer as condições do tipo Ou e E.
* **Executado eventos**: determina que será executado um evento no campo quando a solicitação estiver na atividade selecionada na regra.

**06.** Após preencher todos os campos com as regras e eventos de processo que forem necessários, clique em **Salvar**.

#f2f2f2#f2f2f2Adicionando eventos

Ao definir que a regra irá executar eventos de processo, é necessário definir os eventos que ocorrerão no campo definido quando a solicitação estiver na atividade selecionada.

**01.** Clique em **Adicionar evento** ;

**02.** Defina o valor selecionando um operador entre:

* Maior que;
* Maior ou igual a;
* Menor que;
* Menor ou igual a;
* Igual a;
* Diferente de.

**03.** Defina o valor selecionado um valor para o campo entre:

* Campo do formulário;
* Valor específico;
* Número da solicitação;
* Matrícula do usuário logado;
* Data atual;
* Vazio.

**03.** Defina a ação que ocorrerá no campo, sendo possível definir entre:

* Ocultado
* Exibido
* Desabilitado
* Habilitado
* Preenchido
* Filtrado

Ou seja a configuração do evento ocorre desta forma:

* **Campo monitorado**: Irá ao evento?
* **Evento**: Ao mudar o valor do campo Irá ao evento
* **Ação**: Habilitar o campo Múltipla escolha

exemplo

A empresa irá realizar um evento interno e, para organizar a participação dos colaboradores, foi disponibilizado um formulário. Nesse formulário, há um campo chamado **Irá ao evento?**, no formato de seleção única, com as opções **Sim** e **Não**. Caso o colaborador selecione a opção **Sim**, um segundo campo, do tipo múltipla escolha, será automaticamente exibido para que ele possa fornecer informações adicionais sobre sua participação.

Por exemplo, o campo exibido contém opções como:

* Necessita de transporte
* Participará do *coffee break*
* Precisa de acessibilidade

Se a opção **Não** for selecionada, o campo múltipla escolha permanecerá oculto, já que as informações complementares não são necessárias neste caso.

Dica!

* É possível adicionar múltiplos eventos ao formulário, conforme a necessidade do processo.
* É possível excluir os eventos adicionados a partir do ícone  ao lado direto do evento adicionado.

## Como funcionam as condições?

---

Ao adicionar regras dos tipos Validar valor e Validar formato, é preciso definir condições para que essas validações sejam aplicadas, escolhendo entre as opções 'E' ou 'OU'. A seguir, explicaremos como cada uma dessas condições funciona.

### Condição do tipo E

Esse tipo de condição funciona de forma integral, ou seja, ao adicionar uma regra com a condição do tipo E todas as condições definidas precisam ser verdadeiras para que a ação aconteça.

exemplo

Uma empresa automatizou o fluxo de aprovação de férias e configurou uma regra para que o RH seja notificado somente quando todas as etapas forem concluídas.

Sendo a regra: Notificar o RH quando todas as condições abaixo forem atendidas.

Sendo as condições:

* A solicitação esteja com o status de Aguardando agendamento no RH
* Líder direto tenha aprovado a solicitação
* Gestor da área tenha aprovado a solicitação

Neste caso, a notificação ao RH só será enviada se todas essas condições forem verdadeiras ao mesmo tempo.

### Condição do tipo OU

Este tipo de condição funciona de forma isolada, ou seja, ao adicionar uma regra com a condição do tipo OU apenas uma das condições definidas precisam ser verdadeiras para que a ação aconteça.

exemplo

Uma empresa automatizou o fluxo de aprovação de férias e configurou uma regra para que o RH seja notificado assim que uma das etapas forem concluídas.

Sendo a regra: Notificar o RH assim que houver alguma movimentação na solicitação.

Sendo as condições:

* A aprovação do líder foi concluída com sucesso
* A aprovação do gestor da área foi concluída com sucesso
* A solicitação esteja com o status de Aguardando agendamento no RH

Neste caso, a notificação ao RH será enviada assim que uma das condições acima forem atendidas.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
