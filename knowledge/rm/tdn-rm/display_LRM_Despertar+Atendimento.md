---
content_hash: 67843377d930a45601ece0578d6179297e3323e35a0e3e54d4afd9d140f30db2
fetched_at: '2026-06-29T00:09:33.970758+00:00'
page_id: '425459098'
product: rm
source: tdn-rm
title: Despertar Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Despertar+Atendimento
version: 1
---

**Despertar Atendimento**   
O Serviço de Despertar Atendimentos é utilizado para atualizar os status (situação) dos atendimentos de acordo com as datas de "Prazo Limite" e "Data que os atendimentos deverão Despertar".Trata-se de um processo que pode ser executado de acordo com a parametrização.  
**Hora da Execução**  
A hora da execução deve ser realizada de acordo com as necessidades da empresa.  
**Agora:** Deseja executar o processo uma única vez e imediatamente na data corrente.  
**Executar em:** Deseja executar o processo uma única vez e em uma data especifica de acordo com a data escolhida. Esse controle vem como padrão a data corrente do dia, sendo possível escolher uma data e hora especifica.  
**Sob Demanda:** Deseja executar o processo de forma recorrente.  
**Repetir a execução**  
Ela apresenta as seguintes opções:  
• **Semanal:** Todas as semanas no mesmo horário e no(s) dia(s) de acordo com o definido.   
• **Mensal:** Todos os meses, no mesmo horário e no(s) dia(s) de acordo com o definido.  
• **Diário:** Diariamente, a cada intervalo (em horas) de acordo com o definido.  
Ao executar o processo e dependendo da periodicidade escolhida o processo será executado atualizando os status dos atendimentos que se encontram nas seguintes situações:  
"Agendado a Responder", "Agendado Respondido", "Despertado", "Concluídos a responder" e "Concluído Respondido" respeitando como critério as datas "Prazo Limite" e "Data em que o(s) atendimentos deverá (ao) Despertar" selecionadas ao se executar o processo "Agendar Atendimento".  
Os atendimentos que estão com o status de "Agendado Respondido" e que a data "agendado para" seja menor que a data corrente do servidor serão atualizados para o status de "Despertado". Os atendimentos que estão com os status de "Despertado" e que a data "Prazo Limite" seja menor que a data corrente do servidor serão atualizados para o status de "Em andamento". Os atendimentos que estão com o status de "Concluido Respondido", serão atualizado para o status "Concluido Automatico pelo Sistema", desde que a data corrente do servidor seja maior que o resultado da soma da data de fechamento mais o valor do parâmetro "Conclusão Automática de Atendimento" localizado nos parâmetros.  
Os atendimentos que estão com o status de "Concluido a Responder", serão atualizado para o status "Concluido Automatico pelo Sistema", desde que a data corrente do servidor seja maior que o resultado da soma da data em que ele foi colocado no status   "Concluido a Responder".  
Os atendimento que estão com o status "Agendado a Responder" , serão atualizados para o status "Agendado Respondido" , desde que a data corrente do servidor seja maior que o resultado da soma da data em que ele foi colocado no status  "Agendado a Responder".  
O sistema também irá gravar na discussão do atendimento um texto informando que o status do atendimento foi alterado, pois o cliente não respondeu a tempo.  
Vale ressaltar que o agendamento do Serviço de Despertar com recorrência (Executar em com a repetição marcada), permite apenas uma instância para este serviço, caso mais de um agendamento seja feito, o sistema apresenta uma mensagem de alerta:  
**Mensagem de Alerta:** Já existe um JOB "Despertar Atendimento" agendado. O sistema irá substituir o processo antigo pelo novo criado. Deseja continuar?  
Caso a resposta seja positiva (Sim): O sistema substitui o antigo agendamento pelo novo informado.  
Caso a resposta seja negativa (Não): O sistema aborta o agendamento  e a tela de Jobs é apresentada, para que o agendamento anterior seja visualizado.  
**Observação.:**  
Caso o número de dias referente ao prazo do atendimento não esteja configurado, os atendimentos não serão despertados.   
Para especificar o horário que o serviço de despertar será executado (recomendável para organizações que trabalham com turnos de funcionários) basta realizar configuração do parâmetro: "Utilizar data/hora do momento da execução do serviço".  
Veja maiores detalhes nos parâmetros gerais do sistema: Clique aqui.  
**Exemplo 1:**  
Dessa forma quando o serviço de despertar estiver sendo executado, caso o parâmetro esteja marcado ele irá verificar se a data de despertar é menor igual (<=)do que a data corrente ( Data/hora no momento da execução do serviço).  
Data Despertar: 01/04/2011 10:00:00  
Data Corrente: 01/04/2011 09:00:00  <-- Momento em que o serviço foi executado.  
**Exemplo 2:**    
Caso o parâmetro esteja desmarcado o sistema irá verificar se a data de despertar é menor do que a maior data possível de um dia    
Data Despertar: 01/04/2011 10:00:00  
Data Corrente: 01/04/2011 23:59:59 <- Maior data possível do dia da execução do processo.
