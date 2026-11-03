---
content_hash: 4165fdd81b38e3b292f260d908a05854b4d198dc35b50bf99ff2d6c15c69e0fa
fetched_at: '2026-06-29T00:10:52.226913+00:00'
page_id: '571257307'
product: rm
source: tdn-rm
title: Serviço De Monitoração Da Saúde Da Integração RM x TOTVS App
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571257307
version: 22
---

## ****01. INFORMAÇÕES GERAIS****

O Serviço de monitoração da saúde da integração tem como finalidade garantir a **disponibilidade/execução** do processo que executa a integração (**ConTotvsAppExecutorProcess**).

Atenção

É necessário que o ambiente possua ao menos um JobServer Distribuído no ambiente para que a integração seja habilitada. TDN : <https://tdn.totvs.com/x/Gy8ZE>

## **02. SITUAÇÃO/REQUISITO**

Ao ativar a integração RM x TOTVS App o processo **ConTotvsAppExecutorProcess** deve ser executado respeitando a configuração de periodicidade da  integração, independentemente da arquitetura utilizada pelo sistema ( **3 Camadas**). 

Este processo não pode deixar de ser executado, pela quantidade de volume que informação que ele pode gerar e também pela criticidade das informações que são integradas.

**Ambiente 3 Camadas**

Em ambientes **3 Camadas** o processo é agendado com recursividade de acordo com a configuração de recursividade da integração. Onde o próprio **JobServer** faz o controle da **execução** e o agendamento da próxima execução.

Pensando neste cenário precisamos que caso o processo seja desabilitado/parado por motivos **diversos,** o processo precisa ser reagendado **imediatamente,**para garantir que as informações sempre estejam sendo enviadas para a Carol. (**Respeitando a configuração de recursividade da integração**)

Atenção

É necessário garantir que o processo **ConTotvsAppExecutorProcess** não seja executado **simultaneamente** por mais de um serviço.

## **03. SOLUÇÃO**

Foi criado um serviço que executa de 10 em 10 minutos que executa a rotina de verificação do processo **ConTotvsAppExecutorProcess**.

## **04.****COMO HABILITAR O SERVIÇO**

Ao Habilitar a integração através do Wizard de configuração o serviço será inicializado em todos os ambientes RM.Host , RM.Host.Service utilizados pelo sistema, somente para o **Alias** atual.

Atenção

Este serviço tem como o comportamento ser registrado durante a subida do serviço RM.Host / RM.Host.Service para cada **Alias** configurado no ambiente.

Exemplo:

1 Host + 1 Alias = 1 Serviço

2 Host's + 1 Alias = 2 Serviços

2 Host's + 2 Alias = 4 Serviços

Caso a integração **não** esteja **configurada**/**habilitada** o mesmo será finalizado, não consumindo recursos da máquina.

## **05. COMO FUNCIONA O SERVIÇO**

Existe um serviço no Host que é responsável por **executar a rotina que controlar a execução do processo** da Integração. Este serviço chamamos de **Responsável pelo Job**.

Apenas um único Host possui esta **responsabilidade****.**

É possível identificar o **Responsável pelo Job** através da tabela **GTOTVSAPP**, o campo **SERVIDOR** representa quem é o **Responsável pelo Job** do serviço, registrado com **HOSTNAME**:**PORTA**.

O **Responsável pelo Job** pode ser assumido por **qualquer** Host do parque de máquinas, que esteja com um JobServer Distribuido Habilitado.

Como funciona o mecanismo de ser ou não o **Responsável pelo Job:**

Atenção

Todas as informações significantes do processo serão escritas no arquivo de Log do sistema. (TraceFile)

truetruefalseControlador false10617

Como Funciona a **Rotina que verifica a Saúde do processo**:

truetruefalseRoutinefalse119911

Atenção

Este fluxo da saúde do processo, server para as seguintes classes de processos.

Campo - JOBID → Classe de Processos: ConTotvsAppExecutorProcess (DataSharing)

Campo - JOBIDTLC → Classe de Processos: ConTotvsAppExecutorTLCProcess (BeheviorSharing)
