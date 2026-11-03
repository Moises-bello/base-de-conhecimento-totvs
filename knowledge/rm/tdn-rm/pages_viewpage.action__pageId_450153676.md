---
content_hash: 29cb3a6a345a66aad1b1ca3ecddcd7cc03617ea13b5b7afb480ff98c8311be6f
fetched_at: '2026-06-29T00:09:57.622123+00:00'
page_id: '450153676'
product: rm
source: tdn-rm
title: Registro online de boleto já existente na base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450153676
version: 1
---

## **Exemplo do xml de registro online de boleto já existente na base.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

Observação: Método utilizado ExecuteWithXmlParams

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithXmlParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinBoletoRegistroOnLineTBCData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>  
<FinBoletoRegistroOnLineParamsProc z:Id="i1" xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">  
<ActionModule xmlns="http://www.totvs.com/">F</ActionModule>  
<ActionName xmlns="http://www.totvs.com/">FinBoletoRegistroOnLineAction</ActionName>  
<CanParallelize xmlns="http://www.totvs.com/">true</CanParallelize>  
<CanSendMail xmlns="http://www.totvs.com/">false</CanSendMail>  
<CanWaitSchedule xmlns="http://www.totvs.com/">false</CanWaitSchedule>  
<CodUsuario xmlns="http://www.totvs.com/">mestre</CodUsuario>  
<ConnectionId i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ConnectionString i:nil="true" xmlns="<http://www.totvs.com/>" />  
<Context z:Id="i2" xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>">  
<a:\_params xmlns:b="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EXERCICIOFISCAL</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">22</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODLOCPRT</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODTIPOCURSO</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EDUTIPOUSR</b:Key>  
<b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>" />  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUNIDADEBIB</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODCOLIGADA</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$RHTIPOUSR</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODIGOEXTERNO</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODSISTEMA</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">F</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIOSERVICO</b:Key>  
<b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>" />  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIO</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">mestre</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$IDPRJ</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">2</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CHAPAFUNCIONARIO</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODFILIAL</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
</a:\_params>  
<a:Environment>DotNet</a:Environment>  
</Context>  
<CustomData i:nil="true" xmlns="<http://www.totvs.com/>" />  
<DisableIsolateProcess xmlns="http://www.totvs.com/">false</DisableIsolateProcess>  
<DriverType i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ExecutionId xmlns="http://www.totvs.com/">23db982d-4df6-4d9e-b990-7a24f9303bd0</ExecutionId>  
<FailureMessage xmlns="http://www.totvs.com/">Falha na execução do processo</FailureMessage>  
<FriendlyLogs i:nil="true" xmlns="<http://www.totvs.com/>" />  
<HideProgressDialog xmlns="http://www.totvs.com/">false</HideProgressDialog>  
<HostName xmlns="http://www.totvs.com/">BHN0001878</HostName>  
<Initialized xmlns="http://www.totvs.com/">true</Initialized>  
<Ip xmlns="http://www.totvs.com/">192.168.25.167</Ip>  
<IsolateProcess xmlns="http://www.totvs.com/">false</IsolateProcess>  
<JobID xmlns="<http://www.totvs.com/>">  
<Children />  
<ExecID>1</ExecID>  
<ID>106869</ID>  
<IsPriorityJob>false</IsPriorityJob>  
</JobID>  
<JobServerHostName xmlns="http://www.totvs.com/">BHN0001878</JobServerHostName>  
<MasterActionName xmlns="http://www.totvs.com/">FinBoletoLanAction</MasterActionName>  
<MaximumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1000</MaximumQuantityOfPrimaryKeysPerProcess>  
<MinimumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1</MinimumQuantityOfPrimaryKeysPerProcess>  
<NetworkUser xmlns="http://www.totvs.com/">ricardo.alvarenga</NetworkUser>  
<NotifyEmail xmlns="http://www.totvs.com/">false</NotifyEmail>  
<NotifyEmailList i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
<NotifyFluig xmlns="http://www.totvs.com/">false</NotifyFluig>  
<OnlineMode xmlns="http://www.totvs.com/">false</OnlineMode>  
<PrimaryKeyList xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
<a:ArrayOfanyType>  
<a:anyType i:type="b:short" xmlns:b="http://www.w3.org/2001/XMLSchema">1</a:anyType>  
<a:anyType i:type="b:int" xmlns:b="http://www.w3.org/2001/XMLSchema">11141</a:anyType>  
</a:ArrayOfanyType>  
</PrimaryKeyList>  
<PrimaryKeyNames xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
<a:string>CODCOLIGADA</a:string>  
<a:string>IDBOLETO</a:string>  
</PrimaryKeyNames>  
<PrimaryKeyTableName xmlns="http://www.totvs.com/">FBOLETO</PrimaryKeyTableName>  
<ProcessName xmlns="http://www.totvs.com/">Registro Online de Boletos</ProcessName>  
<QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>  
<SaveLogInDatabase xmlns="http://www.totvs.com/">true</SaveLogInDatabase>  
<SaveParamsExecution xmlns="http://www.totvs.com/">false</SaveParamsExecution>  
<ScheduleDateTime xmlns="http://www.totvs.com/">2018-04-10T12:03:09.5175789-03:00</ScheduleDateTime>  
<Scheduler xmlns="http://www.totvs.com/">JobMonitor</Scheduler>  
<SendMail xmlns="http://www.totvs.com/">false</SendMail>  
<ServerName xmlns="http://www.totvs.com/">FinBoletoRegistroOnLineDataProc</ServerName>  
<ServiceInterface i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.datacontract.org/2004/07/System>" />  
<ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>  
<StatusMessage i:nil="true" xmlns="<http://www.totvs.com/>" />  
<SuccessMessage xmlns="http://www.totvs.com/">Processo executado com sucesso</SuccessMessage>  
<SyncExecution xmlns="http://www.totvs.com/">false</SyncExecution>  
<UseJobMonitor xmlns="http://www.totvs.com/">true</UseJobMonitor>  
<UserName xmlns="http://www.totvs.com/">mestre</UserName>  
<WaitSchedule xmlns="http://www.totvs.com/">false</WaitSchedule>  
<CodAplicacaoOrigem>F</CodAplicacaoOrigem>  
<DataSistema>2018-04-10T00:00:00-03:00</DataSistema>  
<ListaBoleto>  
<FinBoletoOnLineParamsProc z:Id="i3">  
<ActionModule i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ActionName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<CanParallelize xmlns="http://www.totvs.com/">false</CanParallelize>  
<CanSendMail xmlns="http://www.totvs.com/">false</CanSendMail>  
<CanWaitSchedule xmlns="http://www.totvs.com/">false</CanWaitSchedule>  
<CodUsuario i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ConnectionId i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ConnectionString i:nil="true" xmlns="<http://www.totvs.com/>" />  
<Context i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>" />  
<CustomData i:nil="true" xmlns="<http://www.totvs.com/>" />  
<DisableIsolateProcess xmlns="http://www.totvs.com/">false</DisableIsolateProcess>  
<DriverType i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ExecutionId xmlns="http://www.totvs.com/">8c381bfe-ea19-4a81-953d-04cef095d8fd</ExecutionId>  
<FailureMessage xmlns="http://www.totvs.com/">Falha na execução do processo</FailureMessage>  
<FriendlyLogs i:nil="true" xmlns="<http://www.totvs.com/>" />  
<HideProgressDialog xmlns="http://www.totvs.com/">false</HideProgressDialog>  
<HostName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<Initialized xmlns="http://www.totvs.com/">false</Initialized>  
<Ip i:nil="true" xmlns="<http://www.totvs.com/>" />  
<IsolateProcess xmlns="http://www.totvs.com/">false</IsolateProcess>  
<JobID xmlns="<http://www.totvs.com/>">  
<Children />  
<ExecID>-1</ExecID>  
<ID>-1</ID>  
<IsPriorityJob>false</IsPriorityJob>  
</JobID>  
<JobServerHostName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<MasterActionName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<MaximumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1000</MaximumQuantityOfPrimaryKeysPerProcess>  
<MinimumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1</MinimumQuantityOfPrimaryKeysPerProcess>  
<NetworkUser i:nil="true" xmlns="<http://www.totvs.com/>" />  
<NotifyEmail xmlns="http://www.totvs.com/">false</NotifyEmail>  
<NotifyEmailList i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
<NotifyFluig xmlns="http://www.totvs.com/">false</NotifyFluig>  
<OnlineMode xmlns="http://www.totvs.com/">false</OnlineMode>  
<PrimaryKeyList xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
<PrimaryKeyNames i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
<PrimaryKeyTableName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ProcessName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>  
<SaveLogInDatabase xmlns="http://www.totvs.com/">true</SaveLogInDatabase>  
<SaveParamsExecution xmlns="http://www.totvs.com/">false</SaveParamsExecution>  
<ScheduleDateTime xmlns="http://www.totvs.com/">2018-04-10T12:03:10.7935789-03:00</ScheduleDateTime>  
<Scheduler xmlns="http://www.totvs.com/">JobMonitor</Scheduler>  
<SendMail xmlns="http://www.totvs.com/">false</SendMail>  
<ServerName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ServiceInterface i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.datacontract.org/2004/07/System>" />  
<ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>  
<StatusMessage i:nil="true" xmlns="<http://www.totvs.com/>" />  
<SuccessMessage xmlns="http://www.totvs.com/">Processo executado com sucesso</SuccessMessage>  
<SyncExecution xmlns="http://www.totvs.com/">false</SyncExecution>  
<UseJobMonitor xmlns="http://www.totvs.com/">true</UseJobMonitor>  
<UserName i:nil="true" xmlns="<http://www.totvs.com/>" />  
<WaitSchedule xmlns="http://www.totvs.com/">false</WaitSchedule>  
<CodColigada>1</CodColigada>  
<IdBoleto>11142</IdBoleto>  
</FinBoletoOnLineParamsProc>  
</ListaBoleto>  
</FinBoletoRegistroOnLineParamsProc>]]></tot:strXmlParams>  
</tot:ExecuteWithXmlParams>  
</soapenv:Body>  
</soapenv:Envelope>
