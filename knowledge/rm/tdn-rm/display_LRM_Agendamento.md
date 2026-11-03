---
content_hash: 278b4d9643aceaaf26011643a424723959ecb32d3c5b4a982e8ac7857837ef29
fetched_at: '2026-06-29T00:10:25.241038+00:00'
page_id: '502446539'
product: rm
source: tdn-rm
title: Agendamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Agendamento
version: 27
---

## **CONTEÚDO**

1. **Visão geral**
2. **Configuração de Dias e Horários de Funcionamento de Agenda**
3. **Realizando agendamento de atendimento**
4. **Realizando agendamento de exames**
5. **Realizando agendamento de cirurgia**
6. **Layout grade de agendamentos**
7. **Pesquisar / Reagendar**
8. **Mensagens de confirmação da Agenda**
9. **Tempo de Execução dos Exames da Agenda**
10. **Envio de e-mail**

sumarioVisão Geral

# **01.** **Visão geral**

LGPD - Lei Geral de Proteção de Dados

Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

O processo de agendamento permite o controle e marcação dos seguintes tipos de agenda:

* Agenda de médicos.
* Agenda de salas cirúrgicas para realização de procedimentos.
* Agenda de coletas de exames.

Para utilizar a funcionalidade realize a parametrização dos campos descritos em [Parametrização da Agenda](https://tdn.totvs.com/pages/viewpage.action?pageId=301188982).

Para realizar o cadastro de agenda acesse [Cadastros | Agenda](http://tdn.totvs.com/display/LR/Cadastros+%7C+Agenda).

Configuração de Dias e Horários de Funcionamento de Agenda

# **02. Configuração de Dias e Horários de Funcionamento de Agenda**

Para configurar uma agenda, acesse Atendimento / Agendamento / Agenda de Atendimentos, selecione a unidade que deseja realizar a configuração da agenda, clique sobre agenda que deseja configurar e, em seguida em Opções.

Critérios para elaboração de agendas

Alguns critérios deverão ser observados na montagem da agenda tais como:

* Dias da Semana: definição dos dias de atendimento do profissional (de segunda a Domingo) Ex.: Atendimentos somente às segundas, quartas e sextas.
* Flexibilidade nos horários diários de atendimento: informar dentro do(s) dia(s) da semana definidos, os horários de atendimento do profissional e o intervalo entre um atendimento e outro (Ex.: Atendimento de 20 em 20 minutos).
* Tipo de Atividade/Consulta: pode-se criar vários Tipos de Atividades/Consulta. As atividades são pré cadastradas pelos usuários através do menu Cadastros / Uso Geral / Agendamento / Atividades.
* Número máximo de consultas por Tipo de Atividade/Consulta: pode-se definir/limitar por exemplo, o número máximo de quatro consultas do tipo retorno por dia.

1. Aba Períodos acessada no menu Atendimento/Agendamento/Agenda de Atendimentos, nesta aba parametriza-se as informações específicas no tempo em que esta agenda irá vigorar, bem como a sua data máxima para agendamento e a antecedência máxima.
2. Clique no Ícone de Página para incluir o períodos de vigência da configuração da agenda e também períodos de funcionamento da agenda.
3. Informe a data máxima para agendamento, por exemplo, até 23 de dezembro para prestadores que não trabalham no natal.
4. Informe a antecedência mínima em dias para agendamento.
5. Informe a duração da consulta em minutos.
6. Informe a especialidade que deseja para o período (opcional)
7. Acesse a tela de inclusão de períodos da agenda.
8. Em Horário - De preencha o início do horário da vigência da configuração da agenda.
9. Em Horário - Até preencha o fim do horário da vigência da configuração da agenda.
10. Clique no Ícone de Página para incluir os horários do período.
11. Acesse a tela de inclusão de horários do período.
12. Selecione o dia da semana referente à configuração.
13. Preencha o horário de funcionamento da agenda no dia da semana em questão.
14. Preencha a duração do atendimento.
15. Caso sejam permitidos encaixes, informe quantos serão permitidos.
16. Informe qual a sala de realização do atendimento (não obrigatório).
17. Acesse a tela de inclusão de atividades na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Atividades. Na aba Atividades, escolhemos as atividades que esta agenda irá realizar (as atividades são pré cadastradas pelo usuário). Para cada atividade, pode-se definir uma quantidade máxima de agendamentos.
18. Clique no ícone para incluir uma atividade.
19. Informe a atividade.
20. Atribua uma quantidade máxima a aquela atividade e caso necessário adicione dias restritos para esta atividade.
21. Informe a quantidade máxima de integrantes do grupo.
22. Caso marcada a caixa Não permite agendamentos após exceder limites, não será possível realizar agendamentos para esta agenda quando os limites configurados forem excedidos.
23. Clique no ícone da página em branco para adicionar restrições ao dia da semana, para uma atividade específica.
24. Acesse a tela de inclusão de especialidades que a agenda atende, para acessá-la, na tela inicial de configuração das agendas, clique na guia Especialidades.
25. Clique no ícone de Página para incluir uma atividade.
26. Selecione a(s) especialidade(s) do prestador.
27. Esta parametrização é muito importante caso a agenda seja de Plantonista.
28. Acesse a tela para configurar um período de bloqueio na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Bloqueios.
29. Informe o período do bloqueio.
30. Informe o horário bloqueado.
31. Selecione uma justificativa e informe o motivo.
32. Caso esteja relacionado a um feriado, marque a caixa correspondente.

    Exemplo

    Na aba **Períodos**, foi parametrizado que, nas quintas-feiras, o medico atende das 08:00 até as 16:00. Todavia, em uma quinta-feira específica do mês, por motivos médicos, o mesmo só irá atender até meio dia. Esta parametrização é feita nos períodos especiais.
33. Acesse a tela de inclusão de períodos especiais na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Períodos Especiais.
34. Informe a data.
35. Informe a a duração em minutos
36. Informe o horário.
37. Selecione uma justificativa e informe o motivo.
38. Acesse a tela de impressão de relatórios da agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Impressão.
39. Principais Campos e Parâmetros:
40. Selecione o relatório.
41. Clique em Imprime para realizar a impressão após selecionar o relatório.
42. Acesse a tela de remarcação de agendamentos, para acessá-la, na tela inicial de configuração das agendas, clique na guia Reagendar.
43. Selecione o período.
44. Clique em Raio para realizar a pesquisa do período, os registros existentes serão listados, em seguida, selecione o agendamento e realize a alteração.
45. Acesse a tela de inclusão de período reservado, para acessá-la, na tela inicial de configuração das agendas, clique na guia Reservas. Esta guia possibilita que o médico reserve um horário para uma atividade específica. Ao criar uma reserva, a grid de agendamento manterá-se com uma coloração verde durante o período selecionado.
46. Informe a data a ser reservada.
47. Informe o horário.
48. Informe a atividade que será realizada durante o período da reserva e selecione os dias.
49. Selecione os dias da semana que serão reservados.
50. Acesse a tela de cadastro de exames e serviços que estarão vinculados a agenda (atendidos pelo médico), para acessá-la, na tela inicial de configuração das agendas, clique na guia Exames.
51. Selecione o exame e, preencha as informações conforme solicitado.
52. No campo Qtde Horários (Duração), significa a quantidade de horarios esse exame irá ocupar na agenda.  
    Obs: Essa configuração só é utilizada para exames de imagens.
Realizando agendamento de atendimento

# **03. Realizando agendamento de atendimento**

1. Para realizar agendamentos acesse menu Atendimento/Agendamento/Agenda de Atendimentos.
2. No campo Unidade do Agendamento selecione a Unidade do agendamento.
3. Em Localizar escolha a Especialidade, Nome (Profissional), Sala/Exame ou Agente de Coleta, referente ao procedimento que deseja realizar. O Calendário será atualizado. Nele pesquise as datas com horários disponíveis (que estão com marcação em verde) e selecione o dia.
4. Na tela do calendário da agenda de atendimentos, dê duplo clique no horário desejado, para realizar o agendamento.
5. Na tela para marcação, realize o preenchimento das informações do paciente para agendamento. Nesta guia é possível incluir/ alterar o endereço do paciente.
6. Caso selecione o profissional de tendo da pasta de especialidade (Ex: Clinica medica, ortopedia, cardiologista e etc) o RM deixará como default a especialidade escolhida.
7. Selecione o paciente que será atendido.
8. Selecione o convênio do paciente.
9. Selecione a atividade (exemplo: consulta, retorno).
10. Selecione a especialidade.
11. Selecione o procedimento a ser realizado (não obrigatório).
12. Cadastro de tipo de indicação do paciente, as opções são pré cadastradas em Cadastro de Tipos de Indicação.
13. Cadastro de indicação do paciente, as opções são pré cadastradas em Cadastro de Indicação.
14. Cadastro de atividade da agenda, pré cadastrado em Cadastro de Atividades da Agenda.
15. Cadastro de status do agendamento, pré cadastrado em Cadastro de Status do Agendamento.
16. Cadastro de motivos do atendimento, pré cadastrado em Cadastro de Motivos de Atendimento.
17. Na guia Exames é possível lançar exames no agendamento.
18. Clique em ... para selecionar um exame.
19. Após selecionar o exame, clique em Adicionar, ele será adicionado na lista dos Exames agendados.
20. Selecione o exame e clique em remover, para remove-lo da lista.  
      
    1. Na guia Campos Complementares é possível utilizar campos complementares (pré cadastrados em Cadastros / Campos Complementares / Agenda de Atendimentos) para atender a necessidade específica de cada hospital.
    2. Para os dias com todos os horários bloqueados e/ou reservados será representado pela cor laranja no calendário
21. Quando chegar o dia agendado, os atendentes iniciam o Atendimento do paciente através do botão “Atend. Externo”.
22. Após criado o atendimento, se o convênio for do tipo particular, o sistema irá criar o item de débito. Para mais informações acessar
23. Após registrado o atendimento, através da ordem de horários, os médicos iniciam o atendimento clínico ao paciente através do botão "Prontuário", o mesmo fica habilitado apenas caso o usuário esteja parametrizado como Perfil Médico em "Opções / Parâmetros / Parâmetros Gerais / Aba Prontuário Eletrônico / Sub Aba Geral / Perfil Médico".
24. O botão Lista de Espera, realiza o cadastro de uma fila de espera para casos de desistência.
25. Ao ser acionado, será impresso um relatório com a relação dos retornos de pacientes no período selecionado.
Realizando agendamento de exames

# **04. Realizando agendamento de exames**

A agenda de exames, tem como finalidade agendar os exames específicos, sem ter uma visão de “Agendas médicas”, verificando os horários disponíveis de todos os médicos que atendem determinados exames.  
Consulte em [Assistente de agendamento](https://tdn.totvs.com/display/LRM/Assistente+de+Agendamento)

Realizando agendamento de cirurgia

# **05. Realizando agendamento de cirurgia**

1. Acesse a agenda de cirurgias no menu Atendimento/Agendamento/Agenda de Cirurgias.  
   Consulte em [Agenda de Cirurgia](https://tdn.totvs.com/display/LRM/Agenda+de+Cirurgia)
2. Clique no ícone de página em branco para adicionar um agendamento.
3. Ao clicar no Mapa da Agenda será aberta a tela do mapa da agenda cirúrgica.
4. Acesse a tela de identificação do paciente na agenda de cirurgias, no menu Atendimento/Agendamento/Agenda de Cirurgias ao clicar em Incluir.
5. Clique no botão Paciente para pesquisar o paciente.
6. Clique em Paciente para pesquisar o atendimento referente à cirurgia.
7. Selecione a unidade de atendimento.
8. Selecione o convênio do paciente.
9. Selecione o Plano do paciente.
10. Selecione o tipo de cirurgia.
11. Informe o período de duração da cirurgia.
12. Selecione a sala da cirurgia.
13. Selecione o Status do agendamento, pré cadastrado em Cadastro de Status do Agendamento.
14. Tela de para inclusão do procedimento no agendamento na agenda de cirurgias, acessada no menu Atendimento/Agendamento/Agenda de Cirurgias na aba Procedimentos.
15. Na guia Identificação são preenchidas as informações do paciente e cirurgia.
16. Na guia Profissionais é possível adicionar informações dos profissionais relacionados a este procedimento.
17. Na guia Solicitação e Reservas é possível realizar solicitações e/ou reservas de itens, por exemplo: bolsa de sangue, plasma, reserva de UTI, etc.
18. Tela de para inclusão de recursos para a cirurgia na agenda de cirurgias, acessada no menu Atendimento/Agendamento/Agenda de Cirurgias na aba Recursos.
19. Confira os recursos que foram previamente cadastrados ao informar a cirurgia a ser realizada. Acrescente e/ou exclua algum recurso se necessário.
20. Na tela de para inclusão de informações de anestesia (como tempo de duração, Classificação ASA e Técnica.) para cirurgia na agenda de cirurgias, acessada no menu Atendimento/Agendamento/Agenda de Cirurgias na aba Anestesia, informe:
    1. O tempo de duração da anestesia.
    2. A classificação do estado físico de acordo com a classificação da ASA.
    3. A técnica utilizada para a anestesia (Geral ou Condutiva). De acordo com a seleção deste campo, serão abertos outros campos de seleção.
Layout grade de agendamentos

# **06. Layout grade de agendamentos**

A grade de agendamentos pode ser configurada quanto a exibição e ordenação de colunas por usuário.

Após clicar no botão de ordenação de colunas ()será exibido a tela abaixo para realizar a configuração por usuário.

Pesquisar / Reagendar

# **07. Pesquisar / Reagendar**

Clique no botão Pesquisar, dentro da Agenda de atendimentos.

Filtros

Pesquisar no Log:

Em vez de pesquisar na tabela SZAGENDAMENTO, passa a pesquisar na tabela SZLOGAGENDAMENTO.

Unid.Atendimento:

No lookup de **Unid.Atendimento** é possível filtrar os agendamentos apenas da unidade de atendimento selecionada.  
Caso não selecione uma unidade, os agendamentos de todas irão aparecer, respeitando os outros filtros.

Pesquisar por:

No campo “**Pesquisar por**” é possível escolher o **Campo Consulta** (Código ou Nome Cliente) e filtrar a pesquisa pelo paciente / cliente.

Agenda pertencente a:

É possível filtrar pela agenda medica, se a unidade de atendimento tiver sido selecionada.

Protocolo de Agendamento:

Pesquisar por um sequencial / protocolo de agendamento especifico.

Período:

Informar o período de busca dos agendamentos.

Botões

Pesquisar:

Pesquisa utilizando os filtros informados nos outros campos.

Pesquisa Padrão:

Este botão pesquisa primeiramente o paciente no sistema para posteriormente pesquisar os agendamentos dele utilizando os filtros.

Pesquisa

Após pesquisar, uma lista com todos os agendamentos filtrados irá aparecer contendo informações como Especialidade, Exames atrelados ao agendamento, agenda, data e horário.

Com um click sobre uma das linhas é possível selecionar a mesma e informações sobre o agendamento serão mostradas na parte inferior da tela,

incluindo **Observações** e **Log de Reagendamento**, caso exista.

Ao apertar o botão OK o usuário será direcionado na agenda para a página de agendamento que contém o item selecionado.

Botão Reagendar:

Os agendamentos do dia e agendamentos futuros possuirão um checkbox [ x ] que permite que sejam marcados para reagendamento.

Ao apertar o botão Reagendar, tendo itens com checkbox marcado, o assistente de agendamento será aberto.

O assistente abrirá já com as informações do Paciente, a Atividade, a Especialidade e as Informações complementares carregadas, ele utiliza as informações do agendamento mais recente que consta no sistema.

Dos agendamentos selecionados para reagendar, o assistente irá identificar quais deles possuem exames com **AGENDA ABERTA** e inserir cada um dos exames como um novo agendamento na Aba de Exames, para ser preenchido.  
Já agendamentos sem exames, são percebidos como Consultas e serão incluídos na Aba Consultas pela Especialidade caso exista **AGENDA ABERTA**.

Exemplo

Caso eu tente reagendar um agendamento que possua dois exames: Creatinina e Hemograma, porém a Creatinina não possua agenda aberta, apenas o Hemograma será inserido no assistente e um alerta será mostrado para avisar ao usuário sobre a possibilidade de remarcação da Creatinina.

Observação

Agendamentos que possuem exames sem agenda aberta e com agenda aberta, terão os exames **COM** agenda aberta remarcados e excluídos do agendamento original.

O agendamento original será mantido, pois os exames que não foram reagendados permanecerão em aberto.

Caso não haja exames sem agenda aberta e TODOS os agendamentos tenham sido remarcados, o agendamento original é cancelado e inserido no Log.

Para agendamentos de consultas, caso tenha agenda aberta e a remarcação seja concluída com sucesso, o agendamento original será cancelado e inserido no Log.

É possível existir exames e consultas iguais. 

O usuário pode incluir exames e consultas novas para fazer agendamentos.

A partir deste ponto, o comportamento do assistente de agendamento será padrão.

Utilize a documentação <https://tdn.totvs.com/display/LRM/Assistente+de+Agendamento> em caso de dúvidas.

Mensagens de confirmação da Agenda

# **08. Mensagens de confirmação da Agenda**

Copiar todos agendamentos, para uma data no qual o médico não tem horário disponível

No exemplo abaixo o médico Bernard na segunda-feira tem horário apenas pela manhã

Mais por algum motivo vai ser necessário colar os agendamentos

E o dia selecionado foi na sexta feira onde ele inicia o atendimento as 10

Mas como os horários não são compatíveis e é mostrado a mensagem abaixo

Copiar todos os agendamentos do período

Será perguntado se você confirma

Você não pode escolher um período maior de 30 dias

Dara uma mensagem, informando que não podem

Caso você tenha selecionado um número maior de agendamento para o horário do dia selecionado, ele irá informar

Vou precisar colar no dia 11 de agosto os agendamentos do dia 01 a 03 de agosto

No dia 11 temos apenas o Frederico agendado as 08:45

No dia 1º de agosto temos a Pamela

No dia 03 temos 2 agendamentos as 08:45 do Marcos e da Joana Darc as 10:15, a ideia é que no dia 11,

pegue os primeiros horários livres, não necessariamente vai ocorrer de pegar o horário antigo.

Selecionei o Período

Cliquei em colar e assim ficou nossa agenda

Copiar Todos Agendamentos

Vou copiar todos os agendamentos do dia 07/08 onde o médico tem 03 pacientes

As 08:00 Jose Carlos da Silva, 08:45 Jose Maria Rodrigues da Rosa e as 09:00 Jose Ferreira.

Vou colar no dia 09/08

Onde ele tem apenas a Daiane Pedroso as 08:45

Ao copiar os agendamentos ele me pergunta se eu quero fazer a operação

Colar Agendamento

Como o horário do Jose Maria está ocupado com a Daiane, ele me pergunta se quero continuar

Como eu escolhi continuar o sistema colou todos os horários que estavam disponíveis

Só lembrando que na operação de colar todos, você terá que apagar na mão os outros agendamentos.

Os agendamentos que tinham horários livres foram excluídos, ficando apenas o do Jose Maria

Mover todos os Agendamentos

No meu exemplo vou mover todos os agendamentos que o médico tem no dia 8 de agosto para o dia 11.

No dia 08 ele tem duas consultas agendas Leandro as 09:30 e Fernanda as 10:15

No dia 17 tem apenas o André as 08:45

Ao clicar em Mover todos os agendamentos

É feito uma pergunta, caso você responda não, nada é feito.

Mas eu escolhi sim e selecionei o dia que eu quero e clico em colar

Agendamentos colados com sucesso. Não permanece o horário antigo, mais pega os primeiros horários livres na agenda

A agenda do dia 08 foi liberada

Copiar os agendamentos quando tem encaixe

03 Agendamentos Comuns e 2 agendamentos de encaixe (06:10 Marcelo e 06:15 Pedro Pereira)

Para a terça dia 22 de agosto

Todos os 5 agendamentos foram colados com sucesso

Colar como encaixe

Caso eu use a opção de (Copiar todos Agendamentos, copiar todos Agendamentos do Período ou Mover todos Agendamentos)

e tente colar como encaixe

Será apresentada a seguinte mensagem

Tempo de Execução dos Exames da Agenda

# **09. Tempo de Execução dos Exames da Agenda**

Existem dois cenários a serem considerados: Agenda do tipo SALA e agenda de MEDICO.

Para agendas do tipo SALA é importante poder definir horários específicos para os exames realizados nela,

pois o equipamento presente na sala pode ser mais rápido para realizar o exame, dessa forma os horários da agenda podem ser em intervalos menores.

Para agendas do tipo MEDICO é importante poder definir horários específicos para os exames,

pois existem médicos mais experientes que realizam os exames mais rápido que outros e, por eles receberem por exame,

é importante que eles possam maximizar sua produtividade.

Como nas agendas é possível ter vários exames, o usuário poderá definir DENTRO das opções de AGENDA, na aba de Exames,

quantos intervalos da agenda a execução de cada exame dura.

A coluna **Qtde Horários** foi adicionada, onde fica indicado quantos horários o exame irá ocupar na agenda.

## **Observação**:

* A duração de cada exame é determinada na seguinte ordem:

1. Caso possua Quantidade de Horários determinada para o exame nas Opções da Agenda
2. Caso possua Duração preenchida na tela de Cadastro do Exame
3. Duração do período especificado para a Agenda em questão.
4. Tempo padrão de duração da agenda

* Na aba de exames do agendamento, caso o parâmetro do DELPHI **Exibe exames configurados por Agenda** esteja marcado,

somente irão aparecer os exames adicionados nas Opções da Agenda.

### Exemplo 1:

Se cada intervalo tem uma hora, e o exame Hemograma dura 3 intervalos (3 horas).

Se eu criar um agendamento 12:00 com este exame dentro.

O agendamento ocupará os 3 horários indicados pelo exame.

### Exemplo 2:

Caso você queira fazer um agendamento com 3 exames:

* Hemograma – Qtde Horários: 3 intervalos

Colesterol Total – Duração no cadastro do Exame: 02:00h

* Colesterol Hdl – Sem duração de exame definida, irá considerar a duração padrão da agenda: 01:00h

Consequentemente o agendamento ocupará Totalizando 6 horas (horários);

Envio de e-mail

# **10. Envio de e-mail**

Após a finalização do agendamento, é possível enviar um e-mail para o contato informado no campo conforme imagem.

O botão de envio somente será habilitado após o salvamento da agenda e o envio será realizado apenas para agendas que contenham exames.

Informação

O texto não pode ser customizado

O TOTVS RM Saúde utiliza o processo padrão de envio de e-mails do TOTVS RM.

Para mais detalhes sobre a configuração do envio de e-mails, consulte a documentação: [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001046067-Framework-Linha-RM-Frame-Configurar-Envio-de-E-mail)
