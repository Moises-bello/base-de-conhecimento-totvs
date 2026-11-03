---
content_hash: d9fd743cae76d8623b4d0354f136cb02b599ac0e4f7173c6e3308670289810b5
fetched_at: '2026-06-29T00:10:02.068054+00:00'
page_id: '452718878'
product: rm
source: tdn-rm
title: Assistente Agendamento Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718878
version: 5
---

**Assistente Agendamento Automático**

O Assistente de Agendamento Automático agenda exames para as pessoas cadastradas no sistema de acordo com as configurações a serem definidas nos passos do assistente. O assistente apresenta os seguintes passos:

1) Opções de agendamento Neste passo o usuário deverá informar os dados do agendamento e do convênio como: data de início do agendamento, número de atendimentos por horário e as opções de convênio (menor preço, menor tempo ou informar convênio específico).

2) Seleção de Pessoas Neste passo deverão ser selecionadas as pessoas que terão exames agendados. O usuário terá a opção de criar filtros para selecionar as pessoas desejadas.

3) Seleção de Exames Neste passo deverão ser selecionados os exames para agendamento. Poderão ser selecionados por tipo de exame, os exames pendentes, ou outros exames.

4) Pessoas x Exames O sistema exibe as pessoas e os respectivos exames agendados.

5) Seleção de Médicos Nesse passo o usuário pode informar se deseja "Prosseguir o agendamento de exames sem agendar consultas clínicas" ou "Agendar consultas clínicas para análise do resultado dos exames". Caso o usuário escolha em agendar consultas clínicas, o campo "Tipo de Consulta" e "Médico" serão habilitados para preenchimento.

**Observação:**

Um mesmo médico não poderá ser agendado para atender mais de um paciente na mesma data e horário.

6) Concluir Agendamento de Exames O sistema conclui o agendamento e para cada exame agendado é salvo um registro do na agenda de exames com os respectivos dados informados no processo. Caso a opção de agendamentos de exames seja selecionada os exames serão gerados estando vinculados à uma consulta clínica para análise dos mesmos. Essa consulta irá ser criada com o status "Agendada".

**Atenção**

* Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | pasta Acesso a Menus.

* As consultas agendadas enviadas para o prontuário, através do agendamento, tem um padrão de intervalo entre as consultas de 30 minutos.
