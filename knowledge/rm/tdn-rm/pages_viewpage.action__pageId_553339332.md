---
content_hash: 3ed16399cf4f059a84651a3bcc4134ce66df166b6324a864f33790990648e57d
fetched_at: '2026-06-29T00:10:45.842297+00:00'
page_id: '553339332'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Processo de Monitoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339332
version: 1
---

5%90%Monitoria InvestigativaLevantamento de Dados ou Pré-Análise10%90%

1. **Extração de Dados**

* Os dados para a pré-análise são extraídos das ferramentas Zendesk e Jira. Para selecionar os segmentos/equipes que participarão do processo de monitoria, o Analista responsável deve avaliar os seguintes dados, conforme orientações abaixo:

**Relatórios do Zendesk:**

Acessar o Zendesk **(<https://totvssuporte.zendesk.com/agent/>)** clicar em Relatórios e em seguida em Insigths, Selecionar o dashboard QA - Monitoria, aba Pré Análise Monitoria.

|  |  |
| --- | --- |
| Satisfação dos clientes | |
| Dashboard: | QA - Monitoria Zendesk / Pré Análise Monitoria |
| Relatório: | [Monitoria] satisfação dos Clientes por Grupo de Atendimento |
| Filtros: | Date (Ticket Solved):  Últimos 3 meses  Unidade de Negócio: Segmento  Ticket Tipo:  Question (avaliar equipes de Atendimento) ou;                               Task, Incident, Problem (avaliar equipes Desenvolvimento) |

Se necessário, o resultado de Reabertura, Tempo Médio de Resolução e cumprimento da Data Acordo, que é a entrega do desenvolvimento, podem ser avaliados.

|  |  |
| --- | --- |
| Reabertura de tickets | |
| Dashboard: | QA - Monitoria Zendesk / Pré Análise Monitoria |
| Relatório: | [Monitoria] Reabertos x Fechados por Grupo de Atendimento |
| Filtros: | Date (Ticket Solved):  Últimos 3 meses  Unidade de Negócio: Segmento  Ticket Tipo:  Question (avaliar equipes de Atendimento) ou;                               Task, Incident, Problem (avaliar equipes Desenvolvimento) |

|  |  |
| --- | --- |
| Tempo Médio de Resolução | |
| Dashboard: | QA - Monitoria Zendesk / Pré Análise Monitoria |
| Relatório: | [Monitoria] Tempo Médio de Resolução por Grupo de Atendimento (Calendário) |
| Filtros: | Date (Ticket Last Updated):  Últimos 3 meses  Unidade de Negócio: Segmento  Ticket Tipo:  Question (avaliar equipes de Atendimento) ou;                               Task, Incident, Problem (avaliar equipes Desenvolvimento) |
| Observação: | Para a Monitoria é considerado apenas o resultado da mediana. |

**Relatório do Jira:**

Acessar o JIRA ****(<http://jiraproducao.totvs.com.br>)**** clicar Dashboards e em seguida em Manage Dashboards. No campo **Search** informe Desenvolvimento QA e clique no botão Search.

|  |  |
| --- | --- |
| Data Acordo da Entrega | |
| Dashboard: | Desenvolvimento QA |
| Link: | <http://jiraproducao.totvs.com.br/secure/Dashboard.jspa?selectPageId=32610> |
| Relatório: | Data Acordo Entrega - Monitoria |
| Filtros: |  |
| Observação: | Relatório considera todas as issues que tiveram a data de entrega (conclusão ou liberação emergencial) maior que a data acordada para entrega. |

* Caso sejam necessários, outros dados da **lista de verificação** podem ser avaliados na pré-seleção dos segmentos/equipes. Se as equipes já estiverem sido selecionadas, no momento da extração dos dados, faça o filtro por equipe a fim de os dados obtidos sejam somente das equipes já selecionadas.

|  |  |  |
| --- | --- | --- |
| Tipo | Item a ser avaliado | Fonte de dados / Relatório |
| Canal Telefônico | Tempo médio de espera até o atendimento da ligação. | Dígitro: 30101 - EasyCall - Disp. DAC - Chamadas, Estatística por Período   Cisco - Relatório Resumo de Fila |
| Interações | Quantidade de interações do Ticket com o cliente até envio da solução? (Até 3) | [SEG-GER] Qtd. Tickets Resolvidos / Fechados por Resposta (a partir de 0-3) |
| Pesquisa de Satisfação | Na resolução do ticket/issue, a posição do solicitante foi positiva? | [SEG-GER] Satisfação dos Clientes por Grupo de Atendimento |
| Associação | Quantidade de issues associadas | Demais Tarefas Resolvidas (tipo Associada) – Desenvolvimento Ágil  Associações – Manutenção Padrão |
| SLA | O ticket foi solucionado no prazo? | [SEG-GER] SLA Suporte Técnico por Grupo de Atendimento |
| Backlog | Quantidade de tickets a serem atendidos | [SEG-GER] Total de Backlog por Mês   SEG-GER] resolvidos / Fechados por Grupo de Atendimento   [SEG-GER] Demanda por Grupo de Atendimento |

* Com base nos dados extraídos dos relatórios do Zendesk e Jira, o Analista responsável avalia quais são os segmentos / equipes selecionadas para participar do ciclo da Monitoria, que podem ser mais os mais desafiados, mais controlados ou de diferentes perfis.

* Além dos dados, também devem ser consideradas as equipes interessadas em participar do ciclo de Monitoria e sugestões dos responsáveis (Gestor e Tribe Lead).

* Os Gestores e Tribes Leads devem aprovar as equipes pré-selecionadas para participar do ciclo de Monitoria. A formalização pode ser via email ou breve uma reunião. Devem ser aboradados no email ou reunião, os seguintes assuntos: apresentação das equipes pré-selecionadas e aprovação do responsável para que essas equipes particpem do ciclo de Monitoria. Caso não seja possível a participação das equipes pré-selecionadas no ciclo de Monitoria, o Gestor ou Tribe Lead deve indicar uma outra equipe para participar da Monitoria e justificar o motivo pelo qual as equipes pré-selecionadas não poderão participar.

Planejamento10%90%

1. **Oficializar equipes selecionadas**

* A comunicação para os segmentos deve ser oficializada por e-mail para os responsáveis de cada área.
* Para equipes de Atendimento, comunicar o Coordenador e o Gestor da área.
* Para equipes de Desenvolvimento, comunicar Tribe Lead, ScrumMaster, Agile Coach e Guild.

**2. Agendar reunião de Alinhamento**

* Avaliar quem serão os convocados para a primeira reunião. Sugere-se convocar ScrumMaster ou Líder e Equipe envolvida. Este item pode ser alinhado com os responsáveis de cada área.
* As agendas com data e horário são encaminhadas por meio da ferramenta Outlook para os envolvidos. É importante que este agendamento ocorra com antecedência para que as equipes envolvidas se organizem.
Execução10%90%

1. **Reunião de Alinhamento com o Segmento / Equipe**

* Alinhar entendimento do Processo de Monitoria.
* Avaliar os motivos de sucesso / insucesso creditados aos dados coletados e análises efetuadas;
* Avaliar se há algum impeditivo ou ação que ocasionou o sucesso / insucesso;
* Avaliar se há alguma oportunidade que o segmento / equipe queira implementar ou já esteja implementando para melhorar o cenário.
* Questionar os responsáveis sobre o acredita que, enquanto Companhia, podemos fazer diferente.

**2. Registro de Ações**

* Através da conversa com o Segmento / Equipe podem surgir algumas ações:
* O Analista responsável em conjunto com o Segmento / Equipe deve elaborar planos de ação.
* Avaliar quais são os pontos a melhorar / desenvolver (processo, instrução de trabalho, ferramenta, equipe).
* Avaliar quais são as boas práticas identificadas que podem ser replicadas para outras equipes.
* Para cada ação definida, avaliar a necessidade de abertura de ticket ou issue para outras áreas.
* Definir prazo e responsável para cada ação identificada.
* As ações devem ser registradas na  para efeito de histórico e acompanhamento futuro.
* A Ficha do Cliente deve ser armazenada no Fluig > Comunidade Engenharia Corporativa - QA > Documentos > QA - Monitoria.

Também deve ser definido:

* Quais serão os meios para acompanhamento e reporte dos dados. Alinhar com segmento/equipe qual o melhor formato se presencial, lync ou via e-mail.
* Quem será o responsável por acompanhar as ações definidas e receber o reporte dos dados.
Acompanhamento e Reporte de Dados10%90%

* O acompanhamento e reporte dos dados deve ocorrer conforme definido com o segmento / equipe (presencial, lync ou e-mail).
* Sugere-se que as reuniões presenciais ou via lync sejam planejadas para ocorrer de forma rápida e eficiente.
* O objetivo desta agenda é comunicar ao responsável do segmento / equipe a evolução dos planos de ações definidos.
* O acompanhamento e progresso das ações devem ser registrados na Ficha do Cliente para manutenção do histórico.
* O acompanhamento e reporte deve ocorrer até que os planos de ação propostos sejam finalizados ou a equipe monitorada, em conjunto com a equipe QA – Monitoria, verifique que não sejam mais necessários os planos de ação.
Encerramento10%90%

* A agenda de encerramento deve ser enviada para os mesmos envolvidos da primeira agenda.
* O objetivo desta agenda é apresentar o resultado consolidado das ações implementadas e colher o feedback do segmento / equipe e finaliza o ciclo da Monitoria.
  + Avaliar se as ações foram efetivas e se a área indicaria para outras Equipes.
  + Registrar as lições aprendidas (pontos positivos e negativos).
* As ações e o feedback deverão ser registrados na Ficha do Cliente.
5%
