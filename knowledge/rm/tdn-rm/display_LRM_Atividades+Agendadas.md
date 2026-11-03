---
content_hash: 74543a938a1ab5d876feae0428b4aac0cad659bc66b1b5524b8f817022e4d4c4
fetched_at: '2026-06-29T00:09:38.084888+00:00'
page_id: '425459710'
product: rm
source: tdn-rm
title: Atividades Agendadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividades+Agendadas
version: 4
---

Esta funcionalidade é um anexo de cadastros do Processo Seletivo e permite que uma ou mais atividades agendadas sejam incluídas e configuradas para o processo seletivo. Para excluir uma atividade, esta não deve estar vinculada a horários já agendados. Se houver vínculos com horários (e ainda não vinculados a candidatos) será necessário rodar o processo de  para excluir a atividade agendada do processo seletivo. No momento em que uma atividade agendada for cadastrada para um processo seletivo, este terá características de Processo Seletivo com atividades agendadas sendo obrigatório disponibilizar horários e recursos para cada atividade agendada de um processo seletivo através do processo   . A partir da visão será possível incluir, editar e excluir atividades agendadas.   O cadastro "Atividades Agendadas" contém os campos:

Ordem: no ato do cadastro de atividades agendadas será definida automaticamente pelo sistema a ordem de realização de cada atividade que o candidato terá que realizar no processo seletivo.

Tipo de atividade: lookup que permite selecionar um tipo de atividade pré-cadastrado ou incluir um novo tipo.

Antecedência de agendamento: campo numérico que define o número de dias mínimo para agendamento da atividade. Por exemplo, se o valor for 1, o candidato deverá agendar a atividade no mínimo 1 dia antes. O valor default é 0 e se for mantido, a atividade poderá ser agendada para ser realizada no mesmo dia em que está sendo feito o agendamento.

Intervalo após atividade anterior: campo numérico que define o número de horas mínimo entre uma atividade e a sua atividade precedente. Só é possível definir esse intervalo para atividades posteriores à 1ª atividade agendada. Essa configuração irá permitir que um candidato agendado na primeira atividade às 14h00min e termine as 15h00min não consiga agendar para iniciar a segunda atividade imediatamente às 15h01min.

***Validações para salvamento***:  
 Na lista de atividades de um processo seletivo não poderão existir atividades repetidas, isto será verificado pelo código da atividade. Para cada inscrição de processo seletivo agendado, será necessário ter horário e recursos disponíveis para receber cada inscrição. Lembrando que a alocação de recursos e horarios é por cada atividade. Deve ser permitido incluir atividades agendadas antes e durante o período de inscrições. Após o término do período de inscrição o cadastro poderá ser aberto apenas em modo de leitura. No ato da inscrição do candidato em processo seletivo agendado, abrirá uma aba de agendamentos.

Importante Quando o Processo Seletivo estiver integrado com o Totvs Educacional, a visão de "Atividades agendadas" exibirá somente as atividades agendadas que pertençam a processos seletivos da filial logada e dos processos seletivos que são visíveis para todas as filiais.

 Veja também

---
