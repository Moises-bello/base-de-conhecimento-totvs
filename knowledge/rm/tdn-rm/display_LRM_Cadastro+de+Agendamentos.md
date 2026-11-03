---
content_hash: 58cad5d7edd03e03575fb29ece7fed427a934ede701e42e8fdb3cd56a9ce531a
fetched_at: '2026-06-29T00:11:32.890217+00:00'
page_id: '750397280'
product: rm
source: tdn-rm
title: Cadastro de Agendamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Agendamentos
version: 24
---

## O que é ?

O Cadastro de Agendamentos no TOTVS Automação de Testes é uma funcionalidade que permite programar a execução automática de tarefas, testes ou fluxos de trabalho em horários ou períodos específicos, sem necessidade de intervenção manual.

## Para que Serve?

Serve para automatizar a execução de tarefas, testes ou fluxos de trabalho em horários específicos, garantindo eficiência, consistência e redução de intervenções manuais. Ele é útil para programar atividades de forma pré-definida, integrar processos e otimizar o uso do sistema.

## Exemplo de Uso

aExemplos de Mutations na API TestFlow: Criação, Atualização e Exclusão de Agendamentos1. Query - Inclusão (Create Schedule)

Esta query adiciona um novo agendamento ao sistema. Os detalhes do agendamento, como nome, descrição, permissões, gatilhos (triggers) e atividades, são fornecidos no corpo da requisição.

xmlMidnight1Query - Inclusãotruetrue2. Query - Alteração (Update Schedule)

Atualiza um agendamento existente no sistema. Requer o ID do agendamento que será modificado, além dos novos valores.

xmlMidnight1Parâmetrostruetrue3. Query - Exclusão (Delete Schedule)

Remove um agendamento específico do sistema com base em seu ID.

xmlMidnight1Query - Alteraçãotruetrue4. Parâmetros

Objeto JSON que representa um agendamento (schedule) contendo diversas configurações e atributos. Ele abrange informações sobre o próprio agendamento, permissões de usuários, gatilhos, ambientes de execução, atividades, entre outros. A seguir, apresento uma descrição detalhada de cada campo.

xmlMidnight1Parâmetrostruetrue5. Exclusão de um Agendamento

Essa query remove um agendamento do sistema. O ID do agendamento a ser excluído deve ser fornecido.

xmlMidnight1Query - Exclusãotruetrue

## Validações e Campos Gerais

A seguir, descrevemos os campos utilizados em um objeto de configuração de agendamento:

Campos Gerais

* **displayName**: Tipo `string`, com tamanho máximo de 128 caracteres. Este campo é obrigatório e representa o nome de exibição da entidade.
* **version**: Tipo `string`, com tamanho máximo de 16 caracteres. Também obrigatório, refere-se à versão da entidade.
* **description**: Tipo `string`, com tamanho máximo de 512 caracteres. Este campo é obrigatório e descreve a entidade.
* **isEnabled**: Tipo `bool`. Não é obrigatório e indica se a entidade está ativa.
* **userGroupPermissions**: Tipo `list`. Este campo é obrigatório e define uma lista de permissões para os grupos de usuários associados.
* **userGroupId**: Tipo `int`. Obrigatório, indica o grupo existente ao qual o usuário que executa a chamada pertence. Deve conter pelo menos um grupo.
* **canModify**: Tipo `bool`. Não obrigatório, indica se o item pode ser modificado.
* **canDelete**: Tipo `bool`. Não obrigatório, indica se o item pode ser excluído.
* **canManagePermissions**: Tipo `bool`. Não obrigatório, indica se o item pode gerenciar permissões.
* **executionMode**: Tipo `string`. Obrigatório e define o modo de execução da entidade. Os valores possíveis são:
  + SEQUENTIAL\_AT\_EVERY\_ENVIRONMENT
  + SEQUENTIAL\_AT\_ONE\_ENVIRONMENT
* **notificationCondition**: Tipo `string`. Não obrigatório, e define a condição para envio de notificações. Os valores possíveis são:
  + NONE
  + ON\_SUCCESS
  + ALWAYS
  + ON\_ERROR
Notificações 

* **mailAddressNotificationTargets**: Tipo `list<string>`. Não obrigatório, define uma lista de e-mails para envio de notificações.
* **mailAddress**: Tipo `string`. Obrigatório, representa o endereço de e-mail no formato válido (xxx@xxx.xxx).
Triggers (Gatilhos)

* OnceTriggers:
  + onceTriggers: Tipo `list`. Não obrigatório, mas se presente, não pode ser nulo. Define uma lista de gatilhos únicos.
  + whenDate: Tipo `dateTime`. Não obrigatório, especifica a data em que o gatilho será ativado.
  + whenTime: Tipo `dateTime`. Não obrigatório, especifica a hora em que o gatilho será ativado.
* DailyTriggers:
  + dailyTriggers: Tipo `list`. Não obrigatório, mas se presente, não pode ser nulo. Define uma lista de gatilhos diários.
  + when: Tipo `dateTime`. Não obrigatório, especifica a data e hora em que o gatilho será ativado.
  + interval: Tipo `dateTime`. Não obrigatório, especifica o intervalo entre as ativações.
* WeeklyTriggers:
  + weeklyTriggers: Tipo `list`. Não obrigatório, mas se presente, não pode ser nulo. Define uma lista de gatilhos semanais.
  + when: Tipo `dateTime`. Não obrigatório, especifica a data e hora em que o gatilho será ativado.
  + daysOfWeek: Tipo `list<string>`. Não obrigatório, especifica os dias da semana em que o gatilho será ativado. Valores possíveis: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY.
Período de Atividade

* **activePeriod**: Tipo `list`. Obrigatório, define o período em que o agendamento estará ativo.
  + **startAt**: Tipo `dateTime`. Obrigatório, especifica a data e hora de início do período ativo.
  + **endAt**: Tipo `dateTime`. Obrigatório, especifica a data e hora de término do período ativo
Execução de Atividades

* **executionEnvironments**: Tipo `list`. Obrigatório, define a lista de ambientes onde as atividades serão executadas.
  + **serverName**: Tipo `string`. Obrigatório, representa o nome do servidor onde as atividades serão executadas.
  + **environmentId**: Tipo `string`. Obrigatório, deve existir na base de dados, e o usuário logado precisa ter permissão para acessar o registro.
* **activities**: Tipo `list<activity>`. Obrigatório, especifica as atividades que serão executadas.
  + **sortKey**: Tipo `int`. Obrigatório, a chave de ordenação inicial. Deve começar em 0 e ser crescente.
  + **activityId**: Tipo `int`. Obrigatório, deve existir na base de dados, e o usuário logado precisa ter permissão para acessar o registro.
