---
content_hash: f14ae132cc0801275b18c9063e301a792cfb8ec11143330fceb8e5a90807df37
fetched_at: '2026-06-29T00:09:33.267711+00:00'
page_id: '425458947'
product: rm
source: tdn-rm
title: Reserva de recurso
type: documentation
url: https://tdn.totvs.com/display/LRM/Reserva+de+recurso
version: 8
---

A reserva de recurso permite ao usuário reserve tipo de recursou ou recurso desejado para uma data/horário específico.  O processo é executado a partir de uma atividade cadastrada e agendada.

Para realizar a reserva de recurso são necessários os seguintes itens:

* **Tipo de recurso:** Tipos de recursos. **Para saber mais acesse**
* **Recurso:** Recusos das instituições de ensino.

Processo de reserva de recursoProcessoReservaRecursotruePessoa responsável e Plano de aulaPrimeiro passo - Pessoa responsável e Plano de aula

Neste passo, deve selecionar a pessoa responsável pela reserva.

Lista de pessoas disponíveis

A lista de pessoas disponíveis para selecionar será conforme a opção "**Tipo pessoa**" selecionada no cadastro da atividade agendada.

Todos

Todos os alunos e professores disponíveis na instituição

Aluno

Todos os alunos disponíveis na instituição

Professor

Todos os professores disponíveis na instituição

Plano de aula

Caso deseja, poderá selecionar a professor na turma/disciplina para a qual a reserva está sendo feita e o plano de aula correspondente a data em que a aula será realizada no local desejado.

Plano de aula com a data superior a data atual

O sistema irá listar apenas os planos de aula em que a data é superior a data atual

Período e lista de esperaSegundo passo - Período da reserva

Neste passo, deve selecionar o período que compreende a reserva, o horário, os dias da semana em questão e em caso de feriados, considerar ou não de acordo com calendário parametrizado. Existe a possibilidade de o usuário incluir a Recurso em uma lista de espera caso ela já esteja reservada por outro usuário.

Período da reserva

Existe a possibilidade de se incluir vários horários distintos. Para a inclusão de várias período, informe uma data de início e fim, hora de início e fim, dias da semana e clique no botão "Adicionar horário" para cada reserva de dia e horário que desejar. Caso deseje remover algum dos horários incluídos na lista, basta selecionar o horário e clicar em "Remover horário".

Dia e hora específica

O sistema permite que realizar a reserva para os dias da semana em um intervalo de datas e horários específica. Neste caso a opção "Reservar período contínuo", deverá ficar **desmarcada.**

Podendo atender as seguintes situações:

* Apenas um dia e hora específica
* Vários dias diferentes com o mesmo horário ou o mesmo dia com horários diferentes

Período contínuos

O sistema permite que realizar a reserva por todo período definido. Neste caso a opção "Reservar período contínuo", deverá ficar **marcada.**

Incluir na lista de espera

O sistema possui a opção "**Incluir lista de espera se a reserva não for possível**", que **marcada** pelo usuário, ao final do processo caso a **recurso selecionada no período informado já esteja reservada para outra pessoa**, o sistema automaticamente irá inclui-lo em uma lista de espera para esta reserva de recurso. **Para saber mais acesse**

Parâmetro "Utilizar lista de espera para recurso / instalação"

Para que esta funcionalidade esteja disponível, será necessário que o parâmetro "**Utilizar lista de espera para recurso / instalação**" esteja **marcado** em: **Configurações | Parâmetros | Secretaria | Geral 6/7**

RecursoTerceiro passo - Recurso da reserva

Neste passo, deve selecionar tipo de recurso e recurso (se disponível) da reservada.

Recurso disponível

Para que seja possível selecionar o recurso no processo de reserva de recurso é **necessário** que o parâmetro "**Permite seleção dos usuários**" esteja **marcado** em: **Configurações | Parâmetros | Secretaria | Geral 6/7**

Informações adicionaisQuarto passo - Informações adicionais

Neste passo é possível informações adicionais à reserva.

AnexoQuinto passo - Anexo

Neste passo é possível incluir um ou mais arquivos à reserva.

Parametrização de armazenamento

Para o correto funcionamento do anexo, será necessário informar as extensões permitidas e o tamanho máximo do arquivo em: **Configurações | Parâmetros | Secretaria | Geral 6/7**

Extensões de arquivos permitidas

Caso o campo "Extensões de arquivos permitidas" esteja vazio, o sistema irá permitir **todas** as extensões possíveis.

Usuários da agendaSexto passo - Usuários da agenda

Neste passo é possível inserir os usuários que terão a reserva de instalações associadas à agenda. Para acessar **Gestão | Utilitários | Agenda.**

Permite exportação para agenda global

Para que este passo seja exibido no processo de reserva de recurso é **necessário** que a opção "**Permite exportação para agenda global**" esteja **marcado** no cadastro da atividade agendada

Permite seleção dos usuários

Para que seja possível selecionar os usuários no processo de reserva de recurso é **necessário** que a opção "**Permite seleção dos usuários**" esteja **marcado** no cadastro da atividade agendada.

Finalizar processo

Após as configurações, o processo pode ser executado e a recurso será reservada no período informado para a pessoa escolhida no início do processo.

Enviar notificação

Ao final do processo, caso exista o tipo de mensagem "**Confirmar reservas de instalações**" configurada no cadastro de mensagens de notificações, o sistema irá enviar automaticamente a mensagem de notificação para o usuário da reserva. Para saber mais acesse: .

Usuário vinculado a pessoa

Para que o envio de notificações funcione corretamente é necessário que a **pessoa da reserva possua um usuário vinculado a ela**.

Lista de espera

Ao final do processo, caso a opção "**Incluir lista de espera se a reserva não for possível**" foi **marcada** pelo usuário, caso a **recurso** **selecionada no período informado já esteja reservada para outra pessoa**, o sistema automaticamente irá inclui-lo em uma lista de espera para esta reserva de recurso. **Para saber mais acesse .**

Cancelar reserva

Para realizar o cancelamento da reserva de recurso, deve-se utilizar o processo de cancelar reserva de recurso.

Lista de espera de instalação

No caso de **cancelamento da reserva da recurso no período desejado,** o sistema verifica se existe alguma solicitação na lista de reserva, e caso exista ele irá gerar automaticamente uma reserva para este solicitante que estava na espera.  **Para saber mais acesse****.**

Visualizar/Editar reserva

Para poder acessar a reserva realizadas e também, caso desejar editar as informações da reserva realizada. A **edição** irá obedecer **todas configurações** relacionadas à atividade agendada que a reserva está associada.

Data reserva maior que a data atual

A reserva só poderá ser editada se a data da reserva for maior ou igual a data atual.

Choque do horário

Em caso de choque de horário, deve-se verificar a permissão especial para superalocar salas ou recursos. Se o usuário possuir esta permissão, será emitida uma mensagem exibindo o choque e solicitando a confirmação da alteração.
