---
content_hash: 6436d77e95c846498eae4480cb8e3f825090d569a1b15a810b0bf1cfbef0319b
fetched_at: '2026-06-29T00:09:27.869394+00:00'
page_id: '423938548'
product: rm
source: tdn-rm
title: Agendamento de Processos 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938548
version: 5
---

Os produtos da linha RM que trabalham com *JobServer* configurado para executar em modo 3 Camadas podem utilizar do recurso de **Agendamento**, que consiste em agendar para determinado dia/hora a execução de determinados processos, podendo ainda se desejar, criar recorrências ou repetições para estes agendamentos, conseguindo uma otimização de tempo e recursos.

Exemplo de utilização do ***Agendamento*** no processo de Geração de Lançamentos Periódicos:

Trabalhando em ambiente 3 Camadas, o processo de Geração de Lançamentos Periódicos será acrescido de mais uma *etapa* onde você poderá utilizar do recurso de **Agendamento** citado acima e agendar a execução deste processo para outro momento, basta para isto selecionar as opções disponíveis para o agendamento, mas se desejar que a geração dos lançamentos seja imediata selecione então a opção *Agora*.

Também para ambiente 3 Camadas, na tela do cadastro de estruturas, está disponível em ***Anexos*** a opção ***Agendamento***. Através desta opção você poderá consultar, acompanhar e gerenciar todas as gerações executadas por estrutura sejam elas executadas imediatamente ou agendadas.

Multicoligada

Assim como a tela de **Lançamentos Periódicos**, o processo de **Geração**, são multicoligada, podendo assim selecionar e executar o **Processo** ou o **Agendamento** para outro momento e ate mesmo, uma recorrência para uma ou mais coligada. Com tudo, ao **desabilitar** ou **habilitar** o Job agendado, o comando será valido para ambas as coligadas associadas.

Para obter mais informações sobre as opções disponíveis para a parametrização do
