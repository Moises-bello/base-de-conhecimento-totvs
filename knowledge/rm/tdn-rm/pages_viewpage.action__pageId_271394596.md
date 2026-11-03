---
content_hash: 9233d861aefc035c83442b98d6df0e8620e51f59be3e28e6970fa91e5066c88b
fetched_at: '2026-06-29T00:08:27.170249+00:00'
page_id: '271394596'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-227_JobPrioritário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271394596
version: 101
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Job Server |
| **Segmento Executor** | Framework | | |
| **Projeto1** | Framework BH - 004 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | FRW\_FRW002-227 | **Subtarefa1** | FRW\_FRW002-229 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Revisar o enfileiramento de processos viabilizando o "fura fila" no JobServer.

Os Jobs prioritários devem ser executados imediatamente quando requisitados, ou o mais imediatamente possível. Isto significa que o Host App não irá mais executar os Jobs marcados como prioritário e deverá solicitar a execução imediata para um Host Job Server com maior disponibilidade no momento.

## Definição da Regra de Negócio

# Passo a passo da solução

* No método SubmitJob da classe RMSJobData, recebe como parâmetro um objeto da classe RMSParamsProc que contém uma propriedade chamada OnlineMode que define se o processo será executado no seu modo Online, ou seja, imediatamente sem aguardar pela latência e processamento da fila do JobServer. Esta propriedade é utilizada para marcar o Processo como "Prioritário Fura-Fila"
* Desmembrar a lógica para execução prioritária e execução em ambientes que NÃO são TRÊS CAMADAS  
  A variável isPrioritaryJob não pode ser utilizada juntamente com !IsThreeTier()
* Criar um novo método na classe RMSJobData chamado StartPriorityJob(job.JobID)  
  Deverá descobrir qual é o melhor JobServer disponível para execução do job e chamá-lo diretamente  
    

  SELECT TOP 1  
    NOMESERVIDOR,  
    NUMJOBS,  
    MAXJOBS,  
    (MAXJOBS - NUMJOBS) AS DISPONIBILIDADE  
   FROM  
    GJOBSERVER (NOLOCK)  
   ORDER BY  
    DISPONIBILIDADE DESC

    
  Se não retornar nenhum registro, ABORTAR

  

* Criar um novo método estático na classe RMSJobServer para retornar uma nova instância semelhante ao GetServerInstance do RMSBroker, chamado GetDirectServetInstance passando o nome do Job Server como parâmetro. Esse nome pode conter porta ou não e vem da query acima (NOMESERVIDOR). O conteúdo do método deverá ser:

  string host;  
   int port;  
   int portIndex = jobServerName.IndexOf(":");  
   if (portIndex > 0)  
   {  
    host = jobServerName.Substring(0, portIndex);  
    port = Convert.ToInt32(jobServerName.Substring(portIndex + 1));  
   }  
   else  
   {  
    host = jobServerName;  
    port = RMSBroker.Params.Port;  
   }

  RMSHostConnection hostConnection = new RMSHostConnection(host, port);  
   IRMSJobServer jobServer = (IRMSJobServer)RMSBroker.GetServerInstance(typeof(IRMSJobServer), "RMSJobServer", false, hostConnection);  
   return jobServer;

  A chamada deverá ser:

  using (IRMSJobServer directJobServer = RMSJobServer.GetDirectServetInstance("BHD00008051:3000"))  
   {  
    directJobServer.StartJob(jobID);  
   }

* O método StartJob(job.JobID) na classe RMSJobData deve ser chamado caso o ambiente NÃO seja TRÊS CAMADAS
* O método StartPriorityJob(job.JobID) na classe RMSJobData deve ser chamado caso o Job seja Prioritário (OnlineMode)
* Retirar o código abaixo do método chamado StartJob(job.JobID) da classe RMSJobServer

  if (RMSJobUtils.IsThreeTier())  
   {  
    // pede para cada JobExecutor válido (em execução e sem finalização pendente) executar o job  
    foreach (RMSJobExecutor jobExecutor in RMSJobServer.JobExecutors.Values)  
    {  
      if (jobExecutor.IsRunning && !jobExecutor.IsFinalizing)  
       {  
         jobExecutor.StartJob(jobID);

        RMSSysLogTrace.WriteLine(RMSSyslogGlobal.Facility.Local0,  
         RMSSyslogGlobal.Level.Information, "RMSJobServer", RMSSyslogGlobal.Group.Schedule,  
         transactionID, RMSSyslogGlobal.Category.Engine, RMSSyslogGlobal.Step.End, string.Empty, null, null, "Fim start job. (Start Job) Id. Rotina: " + this.GetType().Name, ListParams); //donotlocalize  
         return;  
       }  
     }  
   }

  Este código não é mais necessário ou redundante e pode ser retirado
* Alterar o método NotifyServerForNewJobs(string jobServerName) da classe RMSJobExecutor para utilizar o método estático RMSJobServer.GetDirectServerInstance(jobServerName) recém criado

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
