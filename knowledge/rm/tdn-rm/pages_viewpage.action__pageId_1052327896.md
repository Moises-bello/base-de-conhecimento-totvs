---
content_hash: 34cdbb744341a12532df745aac00e53b4a1e6a44d1f174ad84f679455a95d2ec
fetched_at: '2026-06-29T00:05:51.611167+00:00'
page_id: '1052327896'
product: rm
source: tdn-rm
title: Agendamento Dinâmico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052327896
version: 33
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Dados do Paciente**

   1. **Últimos Atendimentos**
   2. **Documentos**
3. **Utilização**
   1. **Inserir Exame**
   2. **Inserir Consulta**
   3. **Agendamentos Futuros**
   4. **Agendamentos Perdidos**
   5. **Agendamentos Selecionados**
4. **Configurações / Parâmetros**

Visão geralVisão Geral

## **01. VISÃO GERAL**

O Agendamento Dinâmico foi desenvolvida para tornar o processo de agendamento mais rápido, intuitivo e direcionado, principalmente para cenários onde é necessário pesquisar a disponibilidade de exames e consultas de forma ágil.  
Diferente da agenda tradicional, essa rotina permite que o usuário pesquise diretamente por exames específicos, considerando automaticamente regras contratuais e disponibilidade real, sem depender de configurações mais complexas de períodos por especialidade.  
A rotina está disponível em:      
**Atendimento > Agenda de Atendimentos > Agendamento Dinâmico**  
Seu principal objetivo é simplificar a jornada de agendamento, concentrando em uma única tela todas as etapas necessárias para localizar datas, horários e unidades disponíveis.

Ao acessar o Agendamento Dinâmico, o primeiro passo é informar o convênio e o plano, pois são essas informações que determinam quais exames estarão disponíveis para agendamento, de acordo com as regras contratuais já existentes no sistema.

Após esse preenchimento, o usuário pode iniciar a busca pelos exames ou consultas. Nesse momento, os **dados do paciente ainda não são obrigatórios**, permitindo que a consulta de disponibilidade seja feita de forma mais rápida. Esses dados só serão exigidos no momento da confirmação do agendamento.

Dados do paciente

## **02. Dados do Paciente**

A seção de Dados do Paciente tem como objetivo complementar o agendamento com as informações cadastrais necessárias para sua efetivação, além de disponibilizar recursos que auxiliam no atendimento.

Embora o preenchimento desses dados **não seja obrigatório no início do processo** (selecionar horários), ele se torna **obrigatório no momento da confirmação do agendamento**. Isso permite que a busca por disponibilidade de exames e consultas seja feita de forma mais ágil, deixando o preenchimento completo apenas para a etapa final.

Ao informar o paciente o sistema realiza a busca e carrega automaticamente seus dados cadastrais, como data de nascimento, telefone, e-mail, informações do convênio, entre outros. Esses dados garantem mais segurança e assertividade no momento de concluir o agendamento.

Após o preenchimento, a tela passa a disponibilizar duas abas complementares, que enriquecem o atendimento com informações adicionais do paciente.

Abas do pacienteÚltimos Atendimentos

A aba **Últimos Atendimentos** apresenta o histórico recente do paciente na instituição. Nela, é possível visualizar informações como datas de entrada e saída, agendamentos realizados, unidade de atendimento, convênio e status. Essa visão permite que o atendente tenha mais contexto sobre o histórico do paciente, auxiliando na tomada de decisão, principalmente em situações de reagendamento ou continuidade de atendimento.

Documentos

Já a aba **Documentos** permite consultar e gerenciar todos os arquivos vinculados ao paciente, centralizando informações importantes que podem ser necessárias durante o atendimento ou no momento do agendamento.

O sistema disponibiliza o campo **Data de Inclusão**, que permite realizar filtros com base na data em que os documentos foram inseridos. Esse recurso facilita a visualização e a localização dos registros, tornando mais simples identificar documentos recentes ou específicos do paciente.

Ao acessar essa aba, o usuário visualiza uma listagem com os documentos já cadastrados, organizados de forma clara. Nessa listagem, é possível identificar o tipo do documento, sua descrição, o nome do arquivo e o formato, além de contar com ações que permitem visualizar ou baixar o arquivo sempre que necessário. Isso facilita o acesso rápido a itens como pedidos médicos, guias de autorização e laudos, sem a necessidade de navegar para outras rotinas do sistema.

Além da consulta, a tela também possibilita a inclusão de novos documentos. O usuário pode anexar arquivos arrastando diretamente para a área indicada ou selecionando do computador. Antes de adicionar, é possível definir o tipo do documento, garantindo a correta organização das informações. Após isso, basta confirmar a inclusão para que o arquivo fique disponível no cadastro do paciente.

Essa seção é especialmente importante para manter todas as informações organizadas em um único local, proporcionando mais agilidade, segurança e contexto durante o processo de agendamento, além de garantir que todos os dados obrigatórios estejam devidamente preenchidos antes da confirmação.

Utilização

## **03. UTILIZAÇÃO**

agendaInserir Exame

**Inserir Agendamentos**

Nesta opção é possível escolher horários para **novos** **agendamentos** ao escolher o exame, data e horário desejado.

Caso queira filtrar a lista de exames a ser apresentada, é possível selecionar um **grupo de exames (funcionalidade opcional)**, e então escolher o(s) exame(s) desejado(s).   
*Os grupos de exames são cadastrados no menu Cadastro> Unidade de diagnostico > Grupo de exames*

Assim que o **exame** desejado é **selecionado**, o **botão azul será habilitado** para pesquisar os dias disponiveis no mês / ano presente no calendário. As setas do calendário também fazem busca, porém para o próximo mês, de acordo com a seta escolhida.

Ao realizar a busca, as **datas disponíveis** são carregadas para o calendário para o agendamento.

Podendo ser representados por três cores:

* Datas verdes: dias com horários disponíveis
* Datas amarelas: dias sem horários disponíveis
* Data cinza: dia selecionado
* Data sem cor: dia indispónivel

**Unidade / Agenda**

Este filtro irá ser preenchido após a busca do exame, nele conterá todas as unidades que possuem datas disponíveis no calendário.

É possível remover unidades do filtro para visualizar no calendário apenas os dias disponíveis na unidade restante.

**Atenção:** é possível adicionar até **três exames simultaneamente caso tente adicionar mais a seguinte mensagem aparecerá**

Caso mais de um exame seja selecionado, o campo **“Disponibilidade por”** será habilitado, onde o usuário pode definir como deseja buscar os horários:

* Por **dia**, retornará os dias que possuem os exames selecionados.
* Ou por **horários sequenciais**, facilitando quando há necessidade de organizar múltiplos exames em sequência no mesmo dia.

Ao selecionar uma data no calendário, a tela passa a apresentar os **horários disponíveis**, já considerando todos os filtros aplicados, como exame, unidade e tipo de disponibilidade. Além disso, também são exibidos horários que já estão **ocupados**, o que ajuda na tomada de decisão, principalmente em cenários onde é necessário encaixar mais de um exame no mesmo dia.

Nesse momento, o usuário pode utilizar os **filtros de horário** para refinar ainda mais a busca. É possível:

* Selecionar as **unidades** desejadas
* Filtrar por **agenda específica** (quando houver mais de uma vinculada)
* Definir o **turno**, como manhã ou tarde
* E também visualizar por **status**, escolhendo entre horários disponíveis, agendados ou ambos

Esses filtros ajudam a encontrar o horário ideal de forma mais rápida, sem a necessidade de refazer toda a busca.

**Agendar:**

Ao clicar no botão , o horário desejado será adicionado entre os **Agendamentos selecionados**. O horário selecionado será marcado como selecionado.

Horários com horário de início coincidente com **agendamentos selecionados** serão desabilitados para inclusão de novos registros.

**Encaixe:**

É possível realizar encaixes, caso a agenda permita, ao clicar no ícone  presente em horários agendados, que servirão de modelo para o novo agendamento.

O modal de encaixe apresentará as informações do modelo e terá um campo em que o usuário informará o horário do encaixe.

No carrinho, o agendamento será apresentado com a tag encaixe.

Inserir Consulta

## **01. Agendamento Consulta**

Nesta opção é possível escolher horários para **novos** **agendamentos de consulta** por especialidade **ou** por prestador, unidade atendimento, data e hora.  
O prestador corresponde ao proprietário da agenda ou seja, para as agendas do tipo médico.

## **02. Busca dos dias com agendamento no mês calendário**

Quando a **especialidade** ou o **prestador** for **selecionado**, o **botão de pesquisa (Azul)** será habilitado. Ao realizar a pesquisa, as **datas disponíveis** são apresentadas no calendário e as **unidade de atendimento** será exibida logo abaixo;

A seleção da **unidade de atendimento**, altera os dias do calendário, mostrando apenas os dias que correspondem a(s) unidade(s) de atendimento selecionada(s);

No **calendário**, as setas também fazem busca para o mês anterior ou próximo mês. Ao apresentar os dias da agenda no **calendário**, a disponibilidade da agenda será representada por cores, onde:

* Verde: dia com horários disponível;
* Amarela: dia sem horários disponível;
* Cinza: dia selecionado;
* Sem cor (Branco): dia indisponível.

## **03. Listagem dos horários de consulta**

Ao selecionar o dia no calendário, a tela passa a apresentar os **horários de agendamento (disponíveis e comprometidos)**, já considerando os filtros aplicados (dia, especialidade e unidade atendimento).

Logo acima da listagem de horários possui a opção **filtros de horário** para refinar os agendamento exibidos na listagem:

* Seleção múltipla por unidade de atendimento;
* Seleção múltipla por agenda;
* Seleção múltipla por turno;
* Seleção múltipla por status;

* O botão de consulta de preço (ícone ), só estará habilitado se o convênio informado for do tipo particular;
* O botão de adicionar consulta (ícone ), só estará habilitado se o agendamento estiver com status disponível;
* O botão de encaixe de consulta (ícone ), só estará habilitado se a agenda possuir quantidade máxima de encaixe maior que zero e o status do agendamento for: Agendado, Confirmado, Sala de espera, Atendimento interrompido, Atendido, Falta sem justificativa, Feriado, Cancelado, Em andamento, Bloqueado por agenda cirurgia, Reagendado, Reservado;

## **04. Adicionar agendamento de consulta no carrinho**

Regras de validação ao adicionar uma consulta no carrinho:

* É obrigatório informado um convênio ativo;
* É obrigatório informado um plano ativo de acordo com configuração do contrato;
* É obrigatório informado uma atividade;
* É obrigatório informar uma especialidade;
* Se for um agendamento de encaixe:
  + Será validado se já não possui agendamento no mesmo data e hora do encaixe;
  + Será validado o quantidade limite de encaixe disponível;
* Se for uma agenda do tipo médica:
  + Será validado se o médico pertence ao convênio;
* Será validado se o convenio é valido;

## **05. Confirmar agendamento de consulta**

Regras de validação ao confirmar o agendamento de consulta:

* Será executada todas as regras de validação do carrinho;
* É obrigatório informar um paciente;
* É obrigatório informar o nome do paciente;
* É obrigatório informar o CPF do paciente;
* É obrigatório informar a data nascimento paciente de acordo com configuração;
* É obrigatório informar o telefone do paciente;
* Valida se o horário já foi reservado por outro usuário;
Agendamentos Futuros 

#### **Agendamentos Futuros**

Esta tela exibe os exames programados que ainda serão realizados.

* **Visualização Detalhada:** Ao clicar no ícone de seta de uma linha específica, o sistema expande o registro, permitindo que o usuário visualize detalhes complementares do agendamento, como preparos específicos para o exame, observações médicas ou dados da unidade de atendimento, sem precisar sair da tela principal.
* **Lista de Exames:** Apresenta colunas com a Data, Hora e o Nome do Exame (ex: Angiotomografia, TC de Coluna, Cintilografia e USG).
* **Ações Rápidas:** Ao clicar no ícone de opções (três pontos), abre-se um menu suspenso com as funções de Reagendar ou Cancelar.
* **Calendário Auxiliar:** À direita, um calendário do mês vigente, auxilia na visualização temporal dos compromissos.

**Reagendar:**

A ação de reagendar permite que o usuário reagende o item desejado. Ao clicar na opção o agendamento ficará em negrito e o calendário será carregado para que o usuário escolha o novo horário desejado.

O horário novo será inserido no carrinho com a tag Reagendamento e o horário anterior indicado.

Ao confirmar o agendamento deste novo horário, as informações complementares do agendamento anterior será movida para o novo agendamento e o anterior será excluido.

**Cancelar:**

Ao clicar em cancelar, o agendamento futuro selecionado será excluído após confirmação.

Agendamentos Perdidos 

#### **Agendamentos Perdidos**

Esta tela lista os agendamentos de exames que não foram realizados (sem registro de atendimento) nas datas previstas.

* **Visualização Detalhada:** Ao clicar no ícone de seta de uma linha específica, o sistema expande o registro, permitindo que o usuário visualize detalhes complementares do agendamento, como preparos específicos para o exame, observações médicas ou dados da unidade de atendimento, sem precisar sair da tela principal.
* **Histórico de Faltas:** Exibe registros passados (ex: Teste Ergométrico e USG Abdome) com suas respectivas datas e horários originais.
* **Navegação:** Possui barras de rolagem vertical e horizontal para gerenciar listas extensas de ausências.
* **Ações Rápidas:** Ao clicar no ícone de opções (três pontos), abre-se um menu suspenso com a função de Reagendar.

Agendamentos cancelados / excluidos não aparecem nesta listagem.

**Reagendar:**

A ação de reagendar permite que o usuário reagende o item desejado. Ao clicar na opção o agendamento ficará em negrito e o calendário será carregado para que o usuário escolha o novo horário desejado.

O horário novo será inserido no carrinho com a tag Reagendamento e o horário anterior indicado.

Ao confirmar o agendamento deste novo horário, as informações complementares do agendamento anterior será movida para o novo agendamento e o anterior será excluido.

Agendamentos Selecionados

Ao lado direito da tela de Agendamentos, temos o carrinho de agendamentos. Ele está inicialmente vazio e quando um horário desejado é selecionado, seja para agendamento, reagendamento ou encaixe, ele é adicionado a um **carrinho de agendamentos.**

Nesse espaço, o usuário pode revisar os itens incluídos antes de finalizar.

Dentro do carrinho, é possível complementar o agendamento com algumas informações adicionais, como:

* Observações sobre o exame
* Médico solicitante
* Situação do agendamento

Também é possível visualizar os **detalhes do exame**, incluindo orientações de preparo e informações contratuais.

Configurações / Parâmetros

## **04. Configurações / Parâmetros**

O Agendamento Dinâmico não cria novas regras de negócio, mas utiliza as configurações já existentes no sistema de forma mais organizada e visível para o usuário.

Para que um exame esteja disponível na busca, é necessário que exista uma relação correta entre suas configurações. Isso significa que o exame precisa estar vinculado a uma especialidade, que essa especialidade esteja presente nos períodos da agenda, e que o exame também esteja associado à agenda utilizada. Caso algum desses vínculos não esteja configurado, o exame não será apresentado na tela de busca.

Além disso, todas as **regras contratuais** continuam sendo respeitadas. Ou seja, exames bloqueados para determinado convênio ou plano não serão exibidos, garantindo que apenas opções válidas sejam apresentadas ao usuário.

Outro ponto importante é a existência de uma **validação de intervalo entre exames**, que impede o agendamento de determinados procedimentos dentro de um período mínimo já definido no sistema. Essa regra já está implementada e não é configurável.

A rotina também conta com filtros que auxiliam na navegação, como a seleção por grupo de exames, unidades e períodos do dia, tornando a busca mais rápida e eficiente.

Por fim, vale destacar que o Agendamento Dinâmico cada funciona como um facilitador do processo de agendamento. A visualização completa da agenda e demais operações continuam disponíveis na agenda tradicional do sistema.

### Períodos Especiais

Os **períodos especiais** são utilizados quando há necessidade de modificar os horários definidos em um período padrão de uma agenda.

#### Comportamento

O efeito de um período especial depende do seu tipo:

* **Substituição**: o período especial substitui completamente os horários do período padrão.
* **Complemento**: o período especial adiciona novos horários aos já existentes no período padrão.

#### Regras de Exibição

* Quando houver **sobreposição de horários** entre o período padrão e o período especial, o sistema exibirá **apenas um dos horários**, evitando duplicidade.

#### Observações

* A definição correta do tipo de período especial é essencial para garantir o comportamento esperado da agenda.
* Recomenda-se revisar possíveis conflitos de horários ao configurar períodos complementares.

### Cadastro de Exames por agenda

Os itens cadastrados na agenda estarão disponíveis para agendamento.

Caso um exame seja excluído da agenda, ele será automaticamente removido de todos os períodos nos quais estava previamente associado.

### Cadastro de Exames por período

Os **exames cadastrados na agenda** podem ser vinculados aos **períodos da agenda**, possibilitando a aplicação de filtros por período. Esse vínculo permite que o sistema relacione cada exame aos intervalos de data e horário definidos na agenda, garantindo maior controle e organização das informações.

Ao aplicar o filtro por período da agenda, o sistema verifica se existem exames associados aos períodos selecionados. Caso haja registro, serão exibidos **somente os exames que possuem vínculo com os períodos da agenda informados**, tornando a consulta mais precisa e objetiva. Essa funcionalidade facilita a visualização dos exames corretamente agendados em cada período, evitando a exibição de informações que não estejam relacionadas ao intervalo selecionado e contribuindo para mais agilidade e assertividade no processo de gestão e atendimento.

### Cadastro de Prazo de Autorização de Exames

A funcionalidade de **Cadastro de Prazo de Autorização** permite definir regras de prazo para liberação de exames com base em convênios, garantindo que o agendamento respeite períodos mínimos antes da realização do atendimento.

#### Localização

O cadastro deve ser disponibilizado no menu de **Cadastros | Uso Geral | Agendamento**.  
Além desse lugar, ele pode ser acessado pelo Cadastro de Convênios e Cadastro de Exames e Serviços.

#### Utilização no Processo de Agendamento

Durante o processo de agendamento, o sistema deve aplicar automaticamente as regras configuradas.

* Quando houver configuração
  + A data e hora atual devem ser utilizadas como referência
  + O sistema deve:
    1. Adicionar o número de dias configurado
    2. Liberar apenas datas de agendamento **a partir desse prazo**
    3. Caso seja definido "Dia útil", o sistema não considera sábado, domingo e feriado (utiliza o calendário definido na agenda de atendimentos ou na filial) para a contagem de dias.
* Quando não houver configuração
  + O agendamento deve ser permitido **sem restrição de prazo**

### Parâmetros por perfil

* **Parâmetro para incluir agendamentos**
  + Se estiver desabilidade não será permitido incluir horario ou encaixe de exame ou consulta no carrinho;
* **Parâmetro para incluir agendamentos**
  + Se estiver desabilidade não será permitido cancelar horario de exame;
* **Parâmetro para incluir encaixe**
  + Se estiver desabilidade não será permitido incluir encaixe de exame ou consulta no carrinho;
* **Parâmetro para ignorar regras de tempo de autorização de exames**

Esta funcionalidade visa controlar a visibilidade dos horários na agenda de exames, com base no perfil do usuário. O objetivo é permitir que determinados perfis visualizem a grade completa de dias, enquanto outros fiquem restritos a uma visualização baseadas nas datas seguintes ao tempo tempo de autorização gasto pelas operadoras.

Com a permissão desmarcada, o sistema sempre considera a data atual + o número de dias necessários para a autorização.   
Exemplo: se é necessário um dia para autorização, o sistema somente disponibilizará os horários do dia seguinte para agendamento.  
Com a permissão concedida, o sistema existe a data atual para agendamento caso a agenda possua atendimento.

* #### Parâmetro para ignorar a validação de duplicação de exame num prazo de 30 dias

  Por padrão, o sistema realiza uma validação para impedir a criação de agendamentos futuros duplicados para o mesmo cliente.

  Foi adicionada uma permissão por perfil de usuário que permitirá desconsiderar essa validação, possibilitando a realização de múltiplos agendamentos futuros, para o mesmo exame, mesmo quando já existir um registro previamente agendado.
