---
content_hash: 0822d757e8e85ec21d1eb92f7e8414d884f7d5d9ee79464676885cf537cc13c5
fetched_at: '2026-06-29T00:09:18.092723+00:00'
page_id: '421388662'
product: rm
source: tdn-rm
title: Estrutura XML de Registro Online para Boletos existentes.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388662
version: 10
---

A estrutura XML abaixo é um exemplo para uso do Web Service para Registrar Online o boleto incluído na base e não enviado para o banco. As Tags em negrito, são as principais para identificar o boleto desejado e realizar o processo de Registro Online:

XML simplificado para registrar os boletos existentes na base que possuam lançamentos com o convênio parametrizado para o registro online:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
   <soapenv:Header/>  
   <soapenv:Body>  
      <tot:ExecuteWithParams>  
         <!--Optional:-->  
         <tot:ProcessServerName>**FinBoletoRegistroOnLineTBCData**</tot:ProcessServerName>  
         <!--Optional:-->  
         <tot:strXmlParams>

         <![CDATA[<?xml version="1.0" encoding="utf-16"?>  
         <FinBoletoRegistroOnLineParamsProc>

**<CodAplicacaoOrigem>F</CodAplicacaoOrigem>  
         <DataSistema>2017-09-28T00:00:00-03:00</DataSistema>**

         <ListaBoleto>  
                <FinBoletoOnLineParamsProc>  
                   <CanParallelize>false</CanParallelize>  
                   <CanSendMail>false</CanSendMail>  
                   <CanWaitSchedule>false</CanWaitSchedule>  
                   <DisableIsolateProcess>false</DisableIsolateProcess>  
                   <ExecutionId>44a10a5e-3096-4203-bff5-84fd8066e708</ExecutionId>  
                   <FailureMessage>Processo executado com sucesso</FailureMessage>  
                   <HideProgressDialog>false</HideProgressDialog>  
                   <Initialized>false</Initialized>  
                   <IsolateProcess>false</IsolateProcess>  
                             <JobID>  
                                     <Children />  
                                     <ExecID>-1</ExecID>  
                                     <ID>-1</ID>  
                                     <IsPriorityJob>false</IsPriorityJob>  
                             </JobID>  
                   <MaximumQuantityOfPrimaryKeysPerProcess>1000</MaximumQuantityOfPrimaryKeysPerProcess>  
                   <MinimumQuantityOfPrimaryKeysPerProcess>1</MinimumQuantityOfPrimaryKeysPerProcess>  
                   <NotifyEmail>false</NotifyEmail>  
                   <NotifyFluig>false</NotifyFluig>  
                   <OnlineMode>false</OnlineMode>  
                   <QuantityOfSplits>0</QuantityOfSplits>  
                   <SaveLogInDatabase>true</SaveLogInDatabase>  
                   <SaveParamsExecution>false</SaveParamsExecution>  
                   <ScheduleDateTime>2017-09-28T15:29:34.1170233-03:00</ScheduleDateTime>  
                   <Scheduler>JobMonitor</Scheduler>  
                   <SendMail>false</SendMail>  
                   <ShouldParallelize>false</ShouldParallelize>  
                   <SuccessMessage>Processo executado com sucesso</SuccessMessage>  
                   <SyncExecution>false</SyncExecution>  
                   <UseJobMonitor>true</UseJobMonitor>  
                   <WaitSchedule>false</WaitSchedule>  
**<CodColigada>1</CodColigada>  
                   <IdBoleto>8185</IdBoleto>**  
                </FinBoletoOnLineParamsProc>  
         </ListaBoleto>  
</FinBoletoRegistroOnLineParamsProc>]]>

</tot:strXmlParams>  
     </tot:ExecuteWithParams>  
       </soapenv:Body>  
        </soapenv:Envelope>

\* XML Completo do processo de registro online de boletos já existentes na base:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
   <soapenv:Header/>  
   <soapenv:Body>  
      <tot:ExecuteWithParams>  
         <!--Optional:-->  
         **<tot:ProcessServerName>FinBoletoRegistroOnLineTBCData</tot:ProcessServerName>**  
         <!--Optional:-->  
         <tot:strXmlParams>

<![CDATA[<?xml version="1.0" encoding="utf-16"?>  
      <FinBoletoRegistroOnLineParamsProc>  
**<CodAplicacaoOrigem>F</CodAplicacaoOrigem>  
      <DataSistema>2017-09-28T00:00:00-03:00</DataSistema>**  
      <ListaBoleto>  
      <FinBoletoOnLineParamsProc>  
      <ActionModule></ActionModule>  
      <ActionName></ActionName>  
      <CanParallelize>false</CanParallelize>  
      <CanSendMail>false</CanSendMail>  
      <CanWaitSchedule>false</CanWaitSchedule>  
      <CodUsuario></CodUsuario>  
      <ConnectionId></ConnectionId>  
      <ConnectionString></ConnectionString>  
      <Context></Context>  
      <CustomData></CustomData>  
      <DisableIsolateProcess>false</DisableIsolateProcess>  
      <DriverType></DriverType>  
      <ExecutionId>44a10a5e-3096-4203-bff5-84fd8066e708</ExecutionId>  
      <FailureMessage>Processo executado com sucesso</FailureMessage>  
      <FriendlyLogs></FriendlyLogs>  
      <HideProgressDialog>false</HideProgressDialog>  
      <HostName></HostName>  
      <Initialized>false</Initialized>  
      <Ip></Ip>  
      <IsolateProcess>false</IsolateProcess>  
         <JobID>  
         <Children />  
         <ExecID>-1</ExecID>  
         <ID>-1</ID>  
         <IsPriorityJob>false</IsPriorityJob>  
         </JobID>  
      <JobServerHostName></JobServerHostName>  
      <MasterActionName></MasterActionName>  
      <MaximumQuantityOfPrimaryKeysPerProcess>1000</MaximumQuantityOfPrimaryKeysPerProcess>  
      <MinimumQuantityOfPrimaryKeysPerProcess>1</MinimumQuantityOfPrimaryKeysPerProcess>  
      <NotifyEmail>false</NotifyEmail>  
      <NotifyEmailList></NotifyEmailList>  
      <NotifyFluig>false</NotifyFluig>  
      <OnlineMode>false</OnlineMode>  
      <PrimaryKeyList></PrimaryKeyList>  
      <PrimaryKeyNames></PrimaryKeyNames>  
      <PrimaryKeyTableName></PrimaryKeyTableName>  
      <ProcessName></ProcessName>  
      <QuantityOfSplits>0</QuantityOfSplits>  
      <SaveLogInDatabase>true</SaveLogInDatabase>  
      <SaveParamsExecution>false</SaveParamsExecution>  
      <ScheduleDateTime>2017-09-28T15:29:34.1170233-03:00</ScheduleDateTime>  
      <Scheduler>JobMonitor</Scheduler>  
      <SendMail>false</SendMail>  
      <ServerName></ServerName>  
      <ServiceInterface></ServiceInterface>  
      <ShouldParallelize>false</ShouldParallelize>  
      <StatusMessage></StatusMessage>  
      <SuccessMessage>Processo executado com sucesso</SuccessMessage>  
      <SyncExecution>false</SyncExecution>  
      <UseJobMonitor>true</UseJobMonitor>  
      <UserName></UserName>  
      <WaitSchedule>false</WaitSchedule>  
**<CodColigada>1</CodColigada>  
      <IdBoleto>8185</IdBoleto>**  
      </FinBoletoOnLineParamsProc>  
      </ListaBoleto>  
</FinBoletoRegistroOnLineParamsProc>]]>

</tot:strXmlParams>  
     </tot:ExecuteWithParams>  
      </soapenv:Body>  
        </soapenv:Envelope>

**Observação:**

 As tags acima devem ser estruturadas em ordem alfabética, caso estejam fora da ordem, o processo não será concluído ou a tag fora da ordem não será processada.
