---
content_hash: 8d90a4a45a4ff5197343039b722149ab1ed92e0227dee11e45e86f5182d15982
fetched_at: '2026-06-29T00:09:57.607683+00:00'
page_id: '450153667'
product: rm
source: tdn-rm
title: Inclusão de boleto registrado online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450153667
version: 1
---

## **Exemplo do xml de inclusão de boleto registrado online.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

Observação: Método utilizado ExecuteWithXmlParams

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithXmlParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinBoletoInclusaoData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>  
<FinBoletoParamsProc z:Id="i1" xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">  
<ActionModule xmlns="http://www.totvs.com/">F</ActionModule>  
<ActionName xmlns="http://www.totvs.com/">FinBoletoInclusaoAction</ActionName>  
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
<ExecutionId xmlns="http://www.totvs.com/">668f98de-dc0b-4799-b62b-c8deb5721809</ExecutionId>  
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
<ID>106854</ID>  
<IsPriorityJob>false</IsPriorityJob>  
</JobID>  
<JobServerHostName xmlns="http://www.totvs.com/">BHN0001878</JobServerHostName>  
<MasterActionName xmlns="http://www.totvs.com/">FinLanAction</MasterActionName>  
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
<a:anyType i:type="b:int" xmlns:b="http://www.w3.org/2001/XMLSchema">14335</a:anyType>  
</a:ArrayOfanyType>  
</PrimaryKeyList>  
<PrimaryKeyNames xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
<a:string>CODCOLIGADA</a:string>  
<a:string>IDLAN</a:string>  
</PrimaryKeyNames>  
<PrimaryKeyTableName xmlns="http://www.totvs.com/">FLAN</PrimaryKeyTableName>  
<ProcessName xmlns="http://www.totvs.com/">Inclusão de Boleto</ProcessName>  
<QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>  
<SaveLogInDatabase xmlns="http://www.totvs.com/">true</SaveLogInDatabase>  
<SaveParamsExecution xmlns="http://www.totvs.com/">false</SaveParamsExecution>  
<ScheduleDateTime xmlns="http://www.totvs.com/">2018-04-10T11:52:26.8415789-03:00</ScheduleDateTime>  
<Scheduler xmlns="http://www.totvs.com/">JobMonitor</Scheduler>  
<SendMail xmlns="http://www.totvs.com/">false</SendMail>  
<ServerName xmlns="http://www.totvs.com/">FinBoletoInclusaoData</ServerName>  
<ServiceInterface i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.datacontract.org/2004/07/System>" />  
<ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>  
<StatusMessage i:nil="true" xmlns="<http://www.totvs.com/>" />  
<SuccessMessage xmlns="http://www.totvs.com/">Processo executado com sucesso</SuccessMessage>  
<SyncExecution xmlns="http://www.totvs.com/">false</SyncExecution>  
<UseJobMonitor xmlns="http://www.totvs.com/">true</UseJobMonitor>  
<UserName xmlns="http://www.totvs.com/">mestre</UserName>  
<WaitSchedule xmlns="http://www.totvs.com/">false</WaitSchedule>  
<AlterarDtaVencContraApresentacao>false</AlterarDtaVencContraApresentacao>  
<AlterarDtaVencLan>false</AlterarDtaVencLan>  
<AtualizaCamposBD>false</AtualizaCamposBD>  
<CNABAceite>0</CNABAceite>  
<CNABComando i:nil="true" />  
<CNABInstrucao1 i:nil="true" />  
<CNABInstrucao2 i:nil="true" />  
<CNABInstrucao3 i:nil="true" />  
<CodAplicacao i:nil="true" />  
<CodColCxa>0</CodColCxa>  
<CodColigada>1</CodColigada>  
<CodCxa />  
<DataInstrucao1 i:nil="true" />  
<DataInstrucao2 i:nil="true" />  
<DataInstrucao3 i:nil="true" />  
<DataSistema>2018-04-10T00:00:00-03:00</DataSistema>  
<DataVencimento i:nil="true" />  
<EspecieCNAB>02</EspecieCNAB>  
<GerarBoletoParcial>false</GerarBoletoParcial>  
<IdConvenio>0</IdConvenio>  
<LancamentosValidados>false</LancamentosValidados>  
<ListaAgrupamento>  
<FinAgrupamentoParamsProc z:Id="i3">  
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
<ExecutionId xmlns="http://www.totvs.com/">8735c0f3-2e11-4cad-8598-3afda6f903e6</ExecutionId>  
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
<ScheduleDateTime xmlns="http://www.totvs.com/">2018-04-10T11:52:29.3885789-03:00</ScheduleDateTime>  
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
<CodBarras i:nil="true" />  
<CodCliFor>C00434</CodCliFor>  
<CodColCliFor>1</CodColCliFor>  
<CodColigada>1</CodColigada>  
<ContraApresentacao>false</ContraApresentacao>  
<FormaPagamento i:nil="true" />  
<IPTE i:nil="true" />  
<IdBoleto>0</IdBoleto>  
<IdConvenio>0</IdConvenio>  
<IdLan>14335</IdLan>  
<NomeCliFor>RICARDO BARBOSA DA SILVA</NomeCliFor>  
<NossoNumero />  
<NumeroDocumento>0000014335</NumeroDocumento>  
<SegundoNumero i:nil="true" />  
<StatusBoleto>EmAberto</StatusBoleto>  
<TipoBoleto>BoletoCobranca</TipoBoleto>  
<ValorBoleto>0</ValorBoleto>  
<Vencimento>2018-05-10T00:00:00</Vencimento>  
</FinAgrupamentoParamsProc>  
</ListaAgrupamento>  
<OpcaoGeracaoBoleto>UmBoletoParaCadaLancamentos</OpcaoGeracaoBoleto>  
<QtdeDiasInstrucao1 i:nil="true" />  
<QtdeDiasInstrucao2 i:nil="true" />  
<QtdeDiasInstrucao3 i:nil="true" />  
<RegistrarOnLineBoleto>true</RegistrarOnLineBoleto>  
<TipoBoleto>BoletoCobranca</TipoBoleto>  
<ValorParcial i:nil="true" />  
<listaLan>  
<FinLanBoletoParamsProc z:Id="i4">  
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
<ExecutionId xmlns="http://www.totvs.com/">73d83f1e-4bcb-4065-8fed-425d9e639c77</ExecutionId>  
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
<ScheduleDateTime xmlns="http://www.totvs.com/">2018-04-10T11:52:27.9115789-03:00</ScheduleDateTime>  
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
<BaixaPendente>Livre</BaixaPendente>  
<CarenciaJuros>0</CarenciaJuros>  
<CodCCusto i:nil="true" />  
<CodCfo>C00434</CodCfo>  
<CodColCfo>1</CodColCfo>  
<CodColCxa>1</CodColCxa>  
<CodColPgto>1</CodColPgto>  
<CodColigada>1</CodColigada>  
<CodCxa>0341</CodCxa>  
<CodDepartamento />  
<CodFilial>1</CodFilial>  
<CodIndexador i:nil="true" />  
<CodMoeda i:nil="true" />  
<CodSistema>F</CodSistema>  
<CodTabOp1>0001</CodTabOp1>  
<CodTabOp2 />  
<CodTabOp3 />  
<CodTabOp4 />  
<CodTabOp5 />  
<CodTdo>01</CodTdo>  
<Convenio>9999</Convenio>  
<ConvenioAtivo>0</ConvenioAtivo>  
<CxaAtiva>0</CxaAtiva>  
<DataOP1 i:nil="true" />  
<DataOP2 i:nil="true" />  
<DataOP3 i:nil="true" />  
<DataOP4 i:nil="true" />  
<DataOP5 i:nil="true" />  
<DataVencimento>2018-05-10T00:00:00</DataVencimento>  
<Historico />  
<IdConvenio>55</IdConvenio>  
<IdPgto>1</IdPgto>  
<Idlan>14335</Idlan>  
<JurosDia>0</JurosDia>  
<MultaDia>0</MultaDia>  
<NomeCFO>RICARDO BARBOSA DA SILVA</NomeCFO>  
<NossoNumero />  
<NumBloqueios>Sem</NumBloqueios>  
<NumeroDocumento>0000014335</NumeroDocumento>  
<PagRec>Receber</PagRec>  
<SegundoNumero />  
<StatusBol>EmAberto</StatusBol>  
<TipoFormaPagto>0</TipoFormaPagto>  
<TipoJurosDia>Taxa</TipoJurosDia>  
<ValorDesconto>0</ValorDesconto>  
<ValorJuros>0</ValorJuros>  
<ValorMulta>0</ValorMulta>  
<ValorOriginal>500.0000</ValorOriginal>  
</FinLanBoletoParamsProc>  
</listaLan>  
</FinBoletoParamsProc>]]></tot:strXmlParams>  
</tot:ExecuteWithXmlParams>  
</soapenv:Body>  
</soapenv:Envelope>
