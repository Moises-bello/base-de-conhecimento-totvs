---
content_hash: 232049003ebd1ea1a6dba93faed164a4dc875de9354a7540940286e0db42743d
fetched_at: '2026-06-29T00:08:19.265831+00:00'
page_id: '266981857'
product: rm
source: tdn-rm
title: Gerando um relatório via Job
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266981857
version: 18
---

Existem três formas de gerar um relatório via job:

# **1- Classe RptExecutorClient**

Esta API deverá ser utilizada para requisições de geração de relatório realizadas da camada Cliente (RM.exe). As propriedade relacionadas à execução de relatório via job são:

* ***ExecuteOnJobServer***: Se true o relatório será gerado via job. Caso contrário o relatório será gerado diretamente pelo AppServer que receber a requisição.  
  Valor Default: false
* ***OnlineMode***: Se true indica que, caso ExecuteOnJobServer seja  true, o job de geração do relatório deverá ser executado diretamente pelo AppServer e não entrará na fila de jobs do JobServer. Este é uma forma de dar prioridade à execução do job mas deve ser utilizada em casos muito especiais onde justifique que o job do relatório seja executado sem passar pela fila de jobs.  
  Valor Default: false
* ***TimeoutMillisec***: Indica quanto tempo (em millisegundos) deve-se aguardar que o relatório seja gerado quando ExecuteOnJobServer = true. Se esse período for ultrapassado será lançada uma exceção.  
  Valor Default: int.MaxValue

c#1Exemplo RptExecutorClienttrue

# **2- RMSServer RptExecutorOnJobServer**

Este server deve ser utilizado na camada Server mas não deverá ser utilizada de dentro de um RMSProcess pelo fato que ele mesma gerará um processo a ser executado como job.

Os principais métodos deste server são:

* ***SubmitReport***: Submete um relatório para ser executado em JobServer.
* ***Wait***: Aguarda o retorno do JobServer até que ocorra um timeout.
* ***SubmitReportAndWait***: Submete um relatório para ser executado em jobserver e aguarda o retorno do JobServer até que ocorra um timeout.

c#1Exemplo RptExecutorOnJobServertrue("RptExecutorOnJobServer"))
{
int timeoutMillisec = 600000;
RMSJobID jobId = executorJobServer.SubmitReport(\_CodColigada, \_IdReport, \_CodUsuario, executorParams, onlineMode, scheduleTo, recurrencePattern);
execReturn = executorJobServer.Wait(timeoutMillisec, jobId);
}]]>

# **3- Processo de Produto**

Uma outra forma de gerar o relatório via job é criando um RMSProcess e à partir dele chamar o server RptExecutor. Este procedimento é  geralmente realizado pelo produto em seus processos quando existe a necessidade de geração de relatório.

c#1Exemplo RMSProcesstrue("RptExecutorServer"))
{
executorReturn = executorServer.ExecuteReport(paramsProc.CodColigada,
paramsProc.IdReport, paramsProc.CodUsuario, paramsProc.ExecutorPar);
}
...]]>
