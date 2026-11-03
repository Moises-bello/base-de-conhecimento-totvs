---
content_hash: f48ee75caa8635b2754791ed82540f3ae90b964a06d3a2e2fa5b1c6c3187d041
fetched_at: '2026-06-29T00:10:25.281138+00:00'
page_id: '502453088'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Agendamento > Agenda de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502453088
version: 20
---

O processo de agendamento permite o controle e marcação de agendas de médicos e exames.

Pré-requisitos necessários para utilizar a funcionalidade do agendamento.



Antes de iniciar a parametrização das Agendas de Atendimento, é importante que se defina quais serão as Agendas que deverão ser criadas e as características do processo de agendamento dos Tipos de Agenda que serão abertas.IMPORTANTE!

AGENDAMENTO1AGENDAMENTO DE ATENDIMENTOS

Nesta tela você poderá visualizar todas as Agendas de Atendimentos filtradas por tipo e Unidade de Atendimento, visualizar uma Agenda específica de um profissional ou sala selecionando-a no menu a esquerda da tela, visualizar dias em que a Agenda funciona e que tem horários livres em verde no calendário. Ao lado do calendário, foi implementada a opção de se visualizar fotos dos pacientes cadastrados no momento do Registro de Atendimento (Externo e Interno).Caso haja arquivo de foto associado ao paciente, quando o mesmo for carregado na funcionalidade, a imagem será carregada. 

## 

#### Na parte de cima da tela temos algumas ferramentas como:

| Campo | Descrição |
| --- | --- |
| Visualizar | Gera um relatório simples da Agenda selecionada por período, mostrando todos os horários livres e ocupados. |
| Opções | Acessa as Propriedades da Agenda de Atendimento selecionada. |
| Localizar | Caixa de texto onde é possível pesquisar, pelo nome da especialidade, sala ou profissional do qual se deseja encontrar a Agenda de Atendimento. |
| Pesquisar | Chama a tela de Pesquisa Paciente, onde é possível visualizar todos os agendamentos existentes incluindo os futuros, para o paciente pesquisado. |
| Atend. Externo | Permite Registrar um Atendimento Externo para o paciente selecionado. |
| Prontuário | Permite acessar o Prontuário Eletrônico do Paciente através da Agenda de Atendimentos. Observação: Para que esse botão seja habilitado, é necessário que o usuário tenha permissão de acesso ao PEP no Cadastro de Prestador e tenha perfil de Médico definido em Parâmetros Gerais/Prontuário Eletrônico além de o paciente em questão ter um Registro de Atendimento. |

#### No calendário à direita da tela

Após ser escolhido uma agenda, os dias com horários livres passam a ser coloridos de verde, já os dias sem horários livres ficarão em branco.  
Mostra também agendamentos da data selecionada, na grade de horários localizada na parte inferior dessa tela, sendo possível incluir ou editá-los clicando 2 vezes em cima da linha da grade.

Não será possível incluir e nem editar agendamentos em dias que já se passaram.Atenção:

#### Acima da grade de horários temos uma barra de tarefas que realiza operações nos agendamentos que são:

| Campo | Descrição |
| --- | --- |
| Dia Anterior Livre (F11) | Vai para o primeiro dia livre anterior ao dia selecionado. |
| Próximo dia livre (F12) | Vai para o primeiro dia livre posterior ao dia selecionado. |
| Inserir Encaixe (Insert) | Inserir Encaixe (Insert). Observação.: O número máximo de encaixes deve ser respeitado. |
| Remover agendamento (Del) | Exclui o agendamento selecionado. |
| Alterar agendamento (Duplo Click) | Abre o Agendamento selecionado para alterar. Observação.: Não será possível alterar agendamentos em dias que já se passaram. |
| Copiar Agendamento (Ctrl+C) | Copia o agendamento selecionado para ser colado em outro horário / dia. Observação.: No processo de cópia do agendamento, algumas regras são observadas:O Convênio de origem deve ser aceito pelo médico de destino. A Atividade de origem deve ser aceita pelo médico de destino. |
| Copiar Todos Agendamentos | Copia Todos os agendamentos do dia para ser colado em outro horário / dia, seguindo as mesmas regras da Copiar Agendamento individual. Observação: Os agendamentos que são "Encaixes" não serão copiados. |
| Mover Agendamento (Ctrl+X) | Move o Agendamento selecionado para outro horário / dia. Observação: No processo de mover agendamentos, algumas regras são observadas: O Convênio de origem deve ser aceito pelo médico de destino. A Atividade de origem deve ser aceita pelo médico de destino. |
| Mover Todos Agendamentos | Move todos os Agendamentos do dia para outro horário / dia. Observação: Os agendamentos que são "Encaixes" não serão movidos. |
| Colar Agendamento (Ctrl+V) | Cola o(s) agendamento(s) copiado(s) ou movido(s) para o novo horário. |
| Filtrar Encaixes | Exibe na grade somente os horários que são do tipo "Encaixe". |
| Número Prontuário (Ctrl+P) | Exibe na Tela o número do prontuário do paciente selecionado. |
| Log de Agendamento | Irá exibir o Log de alterações (inserção, edição, exclusão e bloqueio) realizadas na Agenda de atendimentos no dia agrupados por horário. |
| Estatísticas | Irá exibir a Tela de Estatísticas contendo alguns indicadores sobre a Agenda. |
| Atualizar Visão (F5) | Atualiza as informações da grade de Agendamentos selecionada. |
| Informações sobre Agendamento | Exibe informação sobre quando e quem realizou o primeiro agendamento, e a ultima alteração. |
| Observações da Agenda | Exibe o conteúdo do campo complementar do prestador quando preenchido. A tela contendo este campo também pode ser acessada através da tecla de atelho F10 ou clicando no ícone representado pelo "Raio amarelo". |

Para o status da agenda de atendimento mudar para atendido ao acessar o Pep o sistema deve estar parametrizado em Parametros Gerais\Prontuário Eletrônico\na Aba Geral deve estar marcado a seguinte função: Queixa principal e conduta obrigatórios.IMPORTANTE!

**Realizando agendamento de atendimento**

1. Para realizar agendamentos acesse menu Atendimento/Agendamento/Agenda de Atendimentos.
2. No campo Unidade do Agendamento selecione a Unidade do agendamento.
3. Em Localizar escolha a Especialidade, Nome (Profissional), Sala/Exame ou Agente de Coleta, referente ao procedimento que deseja realizar. O Calendário será atualizado. Nele pesquise as datas com horários disponíveis (que estão com marcação em verde) e selecione o dia.
4. Na tela do calendário da agenda de atendimentos, dê duplo clique no horário desejado, para realizar o agendamento.
5. Na tela para marcação, realize o preenchimento das informações do paciente para agendamento. Nesta guia é possível incluir/ alterar o endereço do paciente.
6. Selecione o paciente que será atendido.
7. Selecione o convênio do paciente.
8. Selecione a atividade (exemplo: consulta, retorno).
9. Selecione a especialidade.
10. Selecione o procedimento a ser realizado (não obrigatório).
11. Cadastro de tipo de indicação do paciente, as opções são pré cadastradas em Cadastro de Tipos de Indicação.
12. Cadastro de indicação do paciente, as opções são pré cadastradas em Cadastro de Indicação.
13. Cadastro de atividade da agenda, pré cadastrado em Cadastro de Atividades da Agenda.
14. Cadastro de status do agendamento, pré cadastrado em Cadastro de Status do Agendamento.
15. Cadastro de motivos do atendimento, pré cadastrado em Cadastro de Motivos de Atendimento.
16. Na guia Exames é possível lançar exames no agendamento.
17. Clique em ... para selecionar um exame.
18. Após selecionar o exame, clique em Adicionar, ele será adicionado na lista dos Exames agendados.
19. Selecione o exame e clique em remover, para remove-lo da lista.
20. Na guia Campos Complementares é possível utilizar campos complementares (pré cadastrados em Cadastros / Campos Complementares / Agenda de Atendimentos) para atender a necessidade específica de cada hospital.
21. Quando chegar o dia agendado, os atendentes iniciam o Atendimento do paciente através do botão “Atend. Externo”.
22. Após registrado o atendimento, através da ordem de horários, os médicos iniciam o atendimento clínico ao paciente através do botão "Prontuário", o mesmo fica habilitado apenas caso o usuário esteja parametrizado como Perfil Médico em "Opções / Parâmetros / Parâmetros Gerais / Aba Prontuário Eletrônico / Sub Aba Geral / Perfil Médico".
23. O botão Lista de Espera, realiza o cadastro de uma fila de espera para casos de desistência.
24. Ao ser acionado, será impresso um relatório com a relação dos retornos de pacientes no período selecionado.
TISS (SOLICITAÇÃO/CANCELAMENTO)

Após salvar um agendamento, caso o convênio seja de informações TISS o botão **Solicitação/Cancelamento**ficará habilitado.  
  
  
  
Ao clicar no botão a tela abaixo será exibida para cadastro:

2AGENDAMENTO DE EXAMES

#### Realizando agendamento de exames

A agenda de exames, tem como finalidade agendar os exames específicos, sem ter uma visão de “Agendas médicas”, verificando os horários disponíveis de todos os médicos que atendem determinados exames.

1. Clique em Agendar Exames para abrir a tela de Agenda de exames.
2. Selecione o paciente.
3. Selecione a atividade Exames, pré cadastrada em Cadastro de Atividades da Agenda.
4. Selecione a especialidade do agendamento.
5. Clique em Incluir Exame para adicionar o(s) exame(s) no agendamento.
6. O campo Tipo de Indicação contrarresponde ao cadastro de tipo de indicação do paciente, as opções são pré cadastradas em Cadastro de Tipos de Indicação.
7. O campo Indicação corresponde ao cadastro de indicação do paciente, as opções são pré cadastradas em Cadastro de Indicação.
8. Selecione os horários e dia para pesquisa de horários disponíveis.
9. Clique em Incluir Agenda para incluir uma agenda para pesquisa de horários. Caso não seja preenchido, o sistema irá listar na tela seguinte todas as agendas disponíveis para o exame selecionado na tela anterior.
10. Clique em Excluir Agenda para excluir a agenda que foi incluída na listagem.
11. Clique em Avançar.
12. Na tela da agenda de exames com os dias/horários disponíveis encontrados para agendamento, selecione o dia e horário.
13. É apresentada a tela da agenda de atendimentos, com o agendamento realizado.
3OPÇÕES

#### **Propriedades da Agenda (Opções)**

Critérios para elaboração de agendas

Alguns critérios deverão ser observados na montagem da agenda tais como:

* Dias da Semana: definição dos dias de atendimento do profissional (de segunda a Domingo) Ex.: Atendimentos somente às segundas, quartas e sextas.
* Flexibilidade nos horários diários de atendimento: informar dentro do(s) dia(s) da semana definidos, os horários de atendimento do profissional e o intervalo entre um atendimento e outro (Ex.: Atendimento de 20 em 20 minutos).
* Tipo de Atividade/Consulta: pode-se criar vários Tipos de Atividades/Consulta. As atividades são pré cadastradas pelos usuários através do menu Cadastros / Uso Geral / Agendamento / Atividades.
* Número máximo de consultas por Tipo de Atividade/Consulta: pode-se definir/limitar por exemplo, o número máximo de quatro consultas do tipo retorno por dia.

Essa tela é composta pelas seguintes configurações:

OPCOESPERIODOS

**Períodos**

Na Agenda de Atendimentos, temos o botão "Opções" que abre a tela de Propriedades da Agenda, onde podemos configurar algumas opções da mesma. 

PERÍODOSPADRÕES AGENDAMENTO

#### Padrões de Agendamento e Duração

Nesta aba parametriza-se as informações específicas no tempo em que esta agenda irá vigorar, bem como a sua data máxima para agendamento e a antecedência máxima.

| Campos | Descrições |
| --- | --- |
| Data Máxima | Determina uma data máxima limite para a realização de agendamentos. |
| Antecedência Máxima | Determina em dias, um limite máximo para a realização de agendamentos, a contar do dia atual. |
| Duração da Consulta | Determina em minutos, qual será a duração padrão das consultas do médico. |

HORÁRIOS PERÍODOS

#### Horários do Período

Nesta tela será configurada os horários em que o médico irá atender durante a semana.

| Campos | Descrição |
| --- | --- |
| Dia | Selecione o dia da semana referente à configuração. |
| Horário - De / Até | Preencha o horário de funcionamento da agenda no dia da semana em questão. |
| Duração | Preencha a duração do atendimento. |
| Encaixes | Caso sejam permitidos encaixes, informe quantos serão permitidos. |
| Sala | Informe qual a sala de realização do atendimento (não obrigatório). |

ATIVIDADES

**Atividades**

Acesse a tela de inclusão de atividades na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Atividades

ATIVIDADESIDENTIFICAÇÃO

#### Identificação

Na aba Identificação, escolhemos as atividades que esta agenda irá realizar (as atividades são pré cadastradas pelo usuário). Para cada atividade, pode-se definir uma quantidade máxima de agendamentos.

| Campos | Descrições |
| --- | --- |
| Atividade | Informe a atividade. |
| Qtde Máxima | Atribua uma quantidade máxima a aquela atividade e caso necessário adicione dias restritos para esta atividade. |
| Qtde Máxima de integrantes do grupo | Informe a quantidade máxima de integrantes do grupo. |
| Bloqueia agendamentos após exceder limite de atividades da agenda | Caso marcada a caixa Não permite agendamentos após exceder limites, não será possível realizar agendamentos para esta agenda quando os limites configurados forem excedidos. |

RESTRIÇÕES POR FAIXA ETÁRIA

#### Restrições por Faixa Etária

Na aba Restrições por Faixa Etária informamos o período que deverá ser considerada para a restrição e qual a faixa de idades.

| Campo | Descrição |
| --- | --- |
| Período Considerado | Informe a data inicial e final para ser considerada a restrição para a agenda. |
| Faixa Etária Bloqueada | Informe a idade inicial e final para ser considerada a restrição para a agenda. |
| Impeditiva | Se desmarcada apenas irá gerar uma notificação de restrição, marque-a para impedir que o lançamento da agenda seja feito. |

ESPECIALIDADES

#### Especialidades

Acesse a tela de inclusão de especialidades que a agenda atende, para acessá-la, na tela inicial de configuração das agendas, clique na guia Especialidades. 

DECK\_ESPECIALIDADESIDENTIFICAÇÃO

#### Identificação

Esta configuração é muito importante caso a agenda seja de Plantonista.

| Campos | Descrição |
| --- | --- |
| Especialidade | Selecione a(s) especialidade(s) do prestador. |

SUBESPECIALIDADES

#### Subespecialidades

| Campos | Descrição |
| --- | --- |
| Subespecialidade | Selecione a subespecialidade do prestador. |

BLOQUEIOS

#### Bloqueios

Acesse a tela para configurar um período de bloqueio na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Bloqueios.

| Campos | Descrições |
| --- | --- |
| Período Bloqueado | Informe o período do bloqueio. |
| Horário Bloqueado | Informe o horário bloqueado. |
| Tipo de Exceção | Informe um tipo de exceção. |
| Motivo | Informe o motivo. |
| Feriado | Caso esteja relacionado a um feriado, marque a caixa correspondente. |
| Dias | Informe quais os dias da semana onde irão ocorrer os bloqueios. |

PERÍODOS ESPECIAIS

#### Períodos Especiais

Acesse a tela de inclusão de períodos especiais na agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Períodos Especiais.

falseExemplo

Na aba **Períodos**, foi parametrizado que, nas quintas-feiras, o medico atende das 08:00 até as 16:00. Todavia, em uma quinta-feira específica do mês, por motivos médicos, o mesmo só irá atender até meio dia. Esta parametrização é feita nos períodos especiais.

| Campos | Descrições |
| --- | --- |
| Data | Informe a data |
| Duração | Informa a duração em minutos. |
| Horário Liberado | Informe o horário |
| Tipo de Exceção | Selecione o tipo de exceção. |
| Motivo | Informe um motivo |

IMPRESSÃO

#### Impressão

Acesse a tela de impressão de relatórios da agenda, para acessá-la, na tela inicial de configuração das agendas, clique na guia Impressão.

| Campos | Descrições |
| --- | --- |
| Relatório a ser impresso | Selecione o relatório a ser impresso |
| Imprime | Clique em Imprime para realizar a impressão após selecionar o relatório. |

REAGENDAR

#### Reagendar

Acesse a tela de remarcação de agendamentos, para acessá-la, na tela inicial de configuração das agendas, clique na guia Reagendar.

| Campos | Descrições |
| --- | --- |
| Data | Selecione a data fina do período para realizar o reagendamento |
| Raio | Clique em Raio para realizar a pesquisa do período, os registros existentes serão listados, em seguida, selecione o agendamento e realize a alteração. |

RESERVAS

#### Reservas

Acesse a tela de inclusão de período reservado, para acessá-la, na tela inicial de configuração das agendas, clique na guia Reservas. Esta guia possibilita que o médico reserve um horário para uma atividade específica. Ao criar uma reserva, a grid de agendamento manterá-se com uma coloração verde durante o período selecionado.

| Campos | Descrições |
| --- | --- |
| Período Bloqueado | Informe a data a ser reservada. |
| Horário Bloqueado | Informe o horário. |
| Atividade | Informe a atividade que será realizada durante o período da reserva e selecione os dias. |
| Dias | Selecione os dias da semana que serão reservados. |

EXAMES

#### Exames

Acesse a tela de cadastro de exames e serviços que estarão vinculados a agenda (atendidos pelo médico), para acessá-la, na tela inicial de configuração das agendas, clique na guia Exames.

| Campos | Descrições |
| --- | --- |
| Exame | Utilize o filtro para selecionar um exame/ serviço |
| Qtde Máxima | Informe a quantidade máxima de exames que podem ser solicitados. |
| Qtde Horários (duração) | Informe a quantidade de slots que o exame irá ocupar. |
| Sexo | Informe o sexo que é permitido para o exame. |
| Faixa etária | Informa a faixa etária para o exame ser realizado. |

Com a configuração **“Qtde Horários (duração) = 1”** e considerando agendamentos com apenas um exame, ao incluir ou movimentar um agendamento, o sistema calculará automaticamente o horário de início e fim com base na duração do slot em que o agendamento está sendo criado ou copiado.

Para exames que **não possuam a configuração “Qtde Horários (duração) = 1”**, ou em casos de agendamentos que contenham **mais de um exame ou nenhum exame**, será aplicada a regra padrão de cálculo de tempo do agendamento, utilizando a duração definida no período configurado (normal ou especial).

4ESTATÍSTICASESTATISTICAS

Acessada através do botão Estatísticas. Nesta tela, você poderá visualizar Estatísticas da Agenda de Atendimento por período e profissional. São eles:

INDICADORES

#### Indicadores

#### Acima da grade de horários temos uma barra de tarefas que realiza operações nos agendamentos que são:

| Campo | Descrição |
| --- | --- |
| Agendamentos Registrados | Exibe a quantidade de todos os agendamentos na Agenda. |
| Número de Cancelamentos | Exibe a quantidade de todos os agendamentos cujo Status seja "Cancelado". |
| Pacientes Atendidos | Exibe a quantidade de todos os agendamentos cujo Status seja "Atendido"; |
| Percentual de Ocupação da Agenda | Exibe o Percentual de Ocupação da Agenda realizando o seguinte calculo: AGENDAMENTOS REALIZADOS / TOTAL DE AGENDAMENTOS DISPONIVEIS \* 100; Exemplo: Considere uma agenda que possua 10 horários livres e realizo 6 agendamentos nessa mesma agenda. Logo o calculo de percentual de ocupação será: 6 / 10 \* 6 = 60% |
| Taxa de Efetivação de Atendimentos | Exibe o Percentual da Efetivação de Atendimentos realizando o seguinte calculo: TOTAL DE AGENDAMENTOS CUJO STATUS SEJA "ATENDIDO" / AGENDAMENTOS REALIZADOS \* 100; Exemplo: Continuando o exemplo acima, dos 6 agendamentos realizados 3 foram confirmados como "Atendido". Logo o calculo de efetivação de atendimento será: 3 / 6 \* 100 = 50% |

 

ATIVIDADE

#### Atividade

| Campo | Descrição |
| --- | --- |
| Gráfico de distribuição de Atividades do período | Exibe um gráfico em forma de "pizza", com a utilização de Atividades cadastradas na Agenda. |

CONVENIO

**Convênio**

| Campo | Descrição |
| --- | --- |
| Gráfico de distribuição de Convênios por período | Exibe um gráfico em forma de "pizza", com a utilização de Convênios informados no momento do agendamento. |

STATUS

#### Status

| Campo | Descrição |
| --- | --- |
| Gráfico de distribuição dos Status dos Agendamentos por período | Exibe um gráfico em forma de "pizza", com a utilização de Status informados no Agendamento. |

6REGRAS DE FATURAMENTO

É possível fazer o lançamento automático do **itens de débito** associados com a **Atividade** na conta do paciente ao registrar o atendimento Convênio/Particular pelo agendamento.

Para isso é necessário fazer a associação

]]>
