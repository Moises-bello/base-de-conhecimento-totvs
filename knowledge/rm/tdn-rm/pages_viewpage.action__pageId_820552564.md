---
content_hash: 81d2737a5cdf85bf9f52e5609ddda237aa43f30a6372ad8067d189db3a16503d
fetched_at: '2026-06-29T00:11:45.598591+00:00'
page_id: '820552564'
product: rm
source: tdn-rm
title: DT - Importação de Fotos - Mudança de Comportamento em Webservice e Fórmula
  Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820552564
version: 15
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Importação de Fotos - Mudança de Comportamento em Webservice e Fórmula Visual |
| País: | Brasil |
| Ticket: | [#18717809](https://totvssuporte.zendesk.com/agent/tickets/18717809 "Visualizar o Ticket no portal do Zendesk") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8264](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8264) |

## **02.** **VERSÕES**

**A partir dos patches:**

* 12.1.2302.254
* 12.1.2306.210
* 12.1.2310.143 e Superiores.

## **03. SITUAÇÃO/REQUISITO**

Ao realizar o processo de importação de foto via fórmula visual ou via Webservice utilizando o Dataserver "FopImportacaoImagemProcess" o sistema está se comportando de maneira  diferente a partir do release 12.1.2306.

## **04. SOLUÇÃO**

Aprimoramos o recurso de WebService e Formula Visual para que no XML seja realizado a importação de foto no formato Base64 Encoded String.

**ATENÇÃO:** A imagem deve ser convertida para formato Base64 Encoded String. Para isso sugerimos que realize a conversão através deste link <https://www.base64encoder.io/image-to-base64-converter/>

Após a conversão da imagem em Base64 Encoded String, basta inserir na TAG <imagem> conforme abaixo:

É imprescindível que contenha a TAG *<UploadViaWebService>true</UploadViaWebService>* no XML, caso contrário a importação não será realizada:

**OBSERVAÇÕES:**

1. A tag <guid>, precisa estar com o valor "<guid>00000000-0000-0000-0000-000000000000</guid>", pois agora ela será desconsiderada caso o processo seja chamado via webservice e se estiver vazia, ocorrerá erro no SOAP Ui devido formato inválido de GUID.
2. A tag <FilePath> será ignorada caso o processo FopImportacaoImagemProcess seja chamado via webservice ou formula visual, pois o processo irá considerar somente Base64 Encoded String para a importação da imagem.
3. É necessário fazer importação das fotos por coligada, as chapas informadas precisam ser de funcionários da coligada informada.

Segue exemplo do XML para Formula visual e XML utilizado no SOAP Ui:

**XML para Formula Visual:**

> ###### <?xml version="1.0" encoding="utf-16"?> <FopImportacaoImagemParams z:Id="i1" xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">   <ActionModule xmlns="http://www.totvs.com/">P</ActionModule>   <ActionName xmlns="http://www.totvs.com/">FopImportacaoImagemAction</ActionName>   <CanParallelize xmlns="http://www.totvs.com/">true</CanParallelize>   <CanSendMail xmlns="http://www.totvs.com/">false</CanSendMail>   <CanWaitSchedule xmlns="http://www.totvs.com/">false</CanWaitSchedule>   <CodUsuario xmlns="http://www.totvs.com/">mestre</CodUsuario>   <ConnectionId i:nil="true" xmlns="<http://www.totvs.com/>" />   <ConnectionString i:nil="true" xmlns="<http://www.totvs.com/>" />   <Context z:Id="i2" xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>">     <a:\_params xmlns:b="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EXERCICIOFISCAL</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">2</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODLOCPRT</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODTIPOCURSO</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EDUTIPOUSR</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUNIDADEBIB</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODCOLIGADA</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$RHTIPOUSR</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODIGOEXTERNO</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODSISTEMA</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">P</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIOSERVICO</b:Key>         <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>" />       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIO</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">mestre</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$IDPRJ</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CHAPAFUNCIONARIO</b:Key>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>       </b:KeyValueOfanyTypeanyType>       <b:KeyValueOfanyTypeanyType>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODFILIAL</b:Key>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>       </b:KeyValueOfanyTypeanyType>     </a:\_params>     <a:Environment>WebServices</a:Environment>   </Context>   <CustomData i:nil="true" xmlns="<http://www.totvs.com/>" />   <DisableIsolateProcess xmlns="http://www.totvs.com/">false</DisableIsolateProcess>   <DriverType i:nil="true" xmlns="<http://www.totvs.com/>" />   <ExecutionId xmlns="http://www.totvs.com/">8e9a93d1-1ddb-4721-a9b3-07bbd0a830a6</ExecutionId>   <FailureMessage xmlns="http://www.totvs.com/">Falha na execução do processo</FailureMessage>   <FriendlyLogs i:nil="true" xmlns="<http://www.totvs.com/>" />   <HideProgressDialog xmlns="http://www.totvs.com/">false</HideProgressDialog>   <HostName xmlns="http://www.totvs.com/">**SEU\_HOSTNAME**</HostName>   <Initialized xmlns="http://www.totvs.com/">true</Initialized>   <Ip xmlns="http://www.totvs.com/">**SEU\_IP**</Ip>   <IsolateProcess xmlns="http://www.totvs.com/">false</IsolateProcess>   <JobID xmlns="<http://www.totvs.com/>">     <Children />     <ExecID>1</ExecID>     <ID>105638</ID>     <IsPriorityJob>false</IsPriorityJob>   </JobID>   <JobServerHostName xmlns="http://www.totvs.com/">**SEU\_HOSTNAME**</JobServerHostName>   <MasterActionName i:nil="true" xmlns="<http://www.totvs.com/>" />   <MaximumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1000</MaximumQuantityOfPrimaryKeysPerProcess>   <MinimumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1</MinimumQuantityOfPrimaryKeysPerProcess>   <NetworkUser xmlns="http://www.totvs.com/">usuário</NetworkUser>   <NotifyEmail xmlns="http://www.totvs.com/">false</NotifyEmail>   <NotifyEmailList i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />   <NotifyFluig xmlns="http://www.totvs.com/">false</NotifyFluig>   <OnlineMode xmlns="http://www.totvs.com/">false</OnlineMode>   <PrimaryKeyList xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />   <PrimaryKeyNames i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />   <PrimaryKeyTableName i:nil="true" xmlns="<http://www.totvs.com/>" />   <ProcessName xmlns="http://www.totvs.com/">ImportacaoImagem</ProcessName>   <QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>   <SaveLogInDatabase xmlns="http://www.totvs.com/">true</SaveLogInDatabase>   <SaveParamsExecution xmlns="http://www.totvs.com/">false</SaveParamsExecution>   <ScheduleDateTime xmlns="http://www.totvs.com/">2023-12-29T10:38:36.6078464-03:00</ScheduleDateTime>   <Scheduler xmlns="http://www.totvs.com/">JobMonitor</Scheduler>   <SendMail xmlns="http://www.totvs.com/">false</SendMail>   <ServerName xmlns="http://www.totvs.com/">FopImportacaoImagemProcess</ServerName>   <ServiceInterface i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.datacontract.org/2004/07/System>" />   <ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>   <ShowReExecuteButton xmlns="http://www.totvs.com/">true</ShowReExecuteButton>   <StatusMessage i:nil="true" xmlns="<http://www.totvs.com/>" />   <SuccessMessage xmlns="http://www.totvs.com/">Processo executado com sucesso</SuccessMessage>   <SyncExecution xmlns="http://www.totvs.com/">false</SyncExecution>   <UseJobMonitor xmlns="http://www.totvs.com/">true</UseJobMonitor>   <UserName xmlns="http://www.totvs.com/">mestre</UserName>   <WaitSchedule xmlns="http://www.totvs.com/">false</WaitSchedule>
>
> ###### <Altura>200</Altura>   <CodColigada>1</CodColigada>   <DadosArquivo>     <FopPropertiesImagemParams>       <chapa>00004</chapa>       <guid>00000000-0000-0000-0000-000000000000</guid>       <imagem>       /9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCACFAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9PaKKKACiivjf9v39vgfsp2+n+GvDWn2+r+OtUg+0r9sJNvYW+4qJHUEF2Yhgq5A+UkngBgD7GmmS3ieWV1jiRSzO5wFA5JJ7CviX4uf8FbPg78Odau9I0S31bxzd2sjRSXGlRpHab1OCBLIRuGQfmVWU9QSMGvzi+JX/AAUZ+OfxW8G6z4X1vxLbpo+rR+TcxWNjHbuY8glA6jcFOMEZ5BIPBNfM1AH7C+Gf+C0Xw01C7SLW/BPiXR4mOPPt2gulX3I3IfyBr6x+CX7WHwr/AGhLf/iivF1lf36jL6VcH7Pep0yfJfDEDP3lBX3r+cmrGm6ld6PfQXthdTWN7A4khuLaQxyRsOjKwIIPuKAP6iqK/OL/AIJv/wDBQzVPiprFt8LfibfLdeI3jP8AYuuS4V77YpJgmwMGXaCVfq2CDlsFv0doAKKKKACiiigAooooAK/n/wD+CjXiC68RftnfEqS5kkcWt3DZQo5JEccVvEgCg9ASC3Hdie9f0AV+Iv8AwVj+FM3hH9rCXW7WJmtvGFjb3saqvHnoot5EGO58tG+shoA+UPAfwr8X/FC6uLfwn4c1HX5bdd8wsYGcRj/aPQZ7DvVzXfgj8QvDEZfVvA/iHTk/vXGmTIPzK1+yv7O/wb034F/CnRfDVjbrHdrCs2o3AHzXF0ygyOT9eAOygCvS+vWvlamdOM2oQvE+rp5IpU05ztI/nqYFSQRgjgg0V+5PxS/Zt+G/xjhk/wCEn8K2Nzeuu0albxiG7X0/erhjjPAbI9q8a8Uf8E/fB/iDTfDv2lEvNV026Fvd36KLeTUrBiUzPs4NxHGwYSgfO0Q3D5jjqp5zRkveTRyVMlrRfutM/LnwD4wvPh/440DxNp7Ml7pF9DfRFTg7o3DAZ98Y/Gv6b7S6jvrWG5hbdDMiyI3qpGQfyr+cv49fs66/8DfiuPBtwG1Fbx0bSr1Yyq3kbttQgdmDfKy5OCPQg1/RfpNgulaXZ2SHKW0KQqfZVA/pXuwnGpFTi7pnhThKnJwmrNFqiiirICiiigAooooAK+Kv2uPhafjN8RvAF7dRlp/Cnia1u0XHW081DMmPQ7I2P+6fWvtWuS8Y/D+38SzR3kTC3v48Hfjh8dj/AI15WY0q9Smnh3qnt3R62W1cPTqNYlaNWv2Z5fRTpI2ikZHG1lOCPQ02vgj78KKKckZbscUAeKftGfBuP4oa18MNS8lTL4f8Rx3ss7D7luI3kcf8CeKEfUg9q+yfA+rXGt+GbO7ueZ2BDN64JGa880DwYfFzHfIYbOFl3sOpPoPfH869as7OHT7WK2t4xFBEoVEXoAK+syinX+OT9y1ku7vufI5vUw9uSK/eXu32Vtiaiiivpj5gKKKKACiiigAooooA80+IPhtrO8bUYE/0eY/vMfwP6/Q/zrja96mhS4ieKVFkjYYZWGQRXiPjb7J4c8TT2KB1hCLIpJzjIzivi82waoP28X7rf4n2uUYyWIX1eSvJL8CnViytpr+4jtreMyTSHaoH6/5+tZEmtW0a5DFz6KK9b+GNjbN4dt9SEQF1c7tzk5IAYgAeg4rzcDQWMrezT836HqY+u8HR9rKPkvU6HQNHTQ9LhtEO4ry7Y+8x6mtCiiv0OEY04qEVoj85nOVSTnLdhRRRVkBRRRQAUUUUAFU7zVrexO123P8A3F5NU9a1c2+YIDiTHzMP4fYe9c9y7cnk96dhGxL4mlYny4lUf7Rya4jx54Xi8QQTa015DZTwxFpnnbbDsUElif4cDnPTiugbHSvM/wBpTT21b4C+NbYXUtoBYmfdEcFjGyuEP+y+3afZjXJi8PTxFGUKiuj1MrqTjjaUYT5eZpXtfRtLbqcX8LfEHh34ta1dadoev2k8tp88qfMsjR5xvjVgN65wMjpkZ6jP0VplwPDdjBp1oqm3gXaN+SSepJPuSa/OH9i7Tph8f9IuGeSD7NbXUgVW4lJhZdreo+bd9VFfokSScnk15uVYOjh4OcFq9L+R9ZxnTeExscLCbcOVSt5u6+e342OhtfEkbcTxmM/3l5Fa8MyTxh42DqehFcPVixv5bGXdGcj+JT0Ne9Y/P7nZUVFa3KXcKyxnKt+ntUtSMKKKKACorq4+y20kp52rmpaz9eYLpsgPG4gfrQBy7M00jOxyzHJNDccVHcP5cLsOqqTS1ZIteX/tOX32D4E+LXzgvBFD/wB9zxp/7NXqFeN/tcy+X8B9dXOPMmtV/wDJhG/pWNb+HL0Z7GSxU8zw0X/PD/0pHyv+yfeiz+PXhtScCdbqE/jbSkfqBX6GV+anwD1AaX8afBc5OA2pxQ5/66Zj/wDZ6/SuuPAv9215n23iBTtmNKp3gvwlL/MKKKYz7ZEU/wAQNekfmBt+HLox3DQH7sgyPqP/AK1dFXH6W2zUID/tYrsKllIKKKKQwrI8StizjX1k/oa16w/E7fLbr7k/ypiOcuebeUD+4f5Utu26CNvVQf0pZhmJwOu00yzbdZ25HIMan9BVCJq8L/bMuDD8F5UHSa/t0P4Fm/pXulfPn7bVwIvhLYx55l1WJfyjlP8ASufEfwpH0XDsebN8Mv7yPjn4eTC2+IXhWcnAh1ezlz/uzof6V+pNflJokxt9ZsJQdpS4jYH0wwNfq0rblB9RmuLAbSR934hx/e4aXlL9P8xarXDFbm0H952H/jjH+lWaqXjFbvTwBndMy/T905/pXqn5EaFq3lzRyf3WB/Wu1rhlYrXbW7+ZBG/95Qf0qWND6KKKQxFbcM1z/iZv9IhX0Un9f/rVu2/MYrnPEUm7UMf3UA/mf600JmWehqvpn/INtP8Arin/AKCKs1U0k7tLsz/0xT+QqiS3XzP+3ZPt8CeGoM/f1QyY/wB2Fx/7PX0xXyj+3ne7bLwTaZ5kkvJsf7ohH/s9cmKdqMj67hOHPnWHXm390Wz5FEhh/eDqvzD8K/V7SrgXWl2c46Swo4/FQa/KA8giv1F+Gd+NW+HHhO9ByLjSLSbP+9AhriwD1kj73xChelhp9nJffb/I6QDNU9SbbdaXjg/aSP8AyDJV7jHBrM1Y/wCkaV/19/8AtKSvYPxU0a7DS38zT4D/ALOK4+uq0GTfpsY/ukj9c/1pMEaFFFFSUR2/EYpslnBK5d4UZj1JHNFFADf7Ptv+eEf/AHyKSPS7SNFRLaJVUYChRgCiigBf7Ptv+eEf/fIrF8Q/Drwv4teBta8P6dqrW4YRG8tkk2BsbsZHGcD8hRRSeujLhUnSlz03Z91oZH/Ci/h3/wBCToX/AIAR/wCFdVp+gabpNjBZWVjb2tpbosUUMUYVEUDAUAdABRRSUUtka1MRWrK1Wbl6tsn/ALPtv+eEf/fIpr6VZyFC1rExRty5QcHBGfyJ/OiiqOcd/Z9t/wA8I/8AvkVLFCkC7Y0VFznCjFFFAD6KKKAP/9k=       </imagem>     </FopPropertiesImagemParams>     <FopPropertiesImagemParams>       <chapa>00005</chapa>       <guid>00000000-0000-0000-0000-000000000000</guid>       <imagem>       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       </imagem>     </FopPropertiesImagemParams>   </DadosArquivo>   <FilePath></FilePath>   <Largura>200</Largura>   <ManterOriginal>false</ManterOriginal>   <Qualidade>170</Qualidade>   <SobrescreverAtual>true</SobrescreverAtual>   <UploadViaWebService>true</UploadViaWebService> </FopImportacaoImagemParams>

XML para SOAP Ui:

> <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
>    <soapenv:Header/>  
>    <soapenv:Body>  
>       <tot:ExecuteWithXmlParams>  
>          <!--Optional:-->  
>          <tot:ProcessServerName>FopImportacaoImagemProcess</tot:ProcessServerName>  
>          <!--Optional:-->  
>          <tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>  
> <FopImportacaoImagemParams z:Id="i1" xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">  
>   <ActionModule xmlns="http://www.totvs.com/">P</ActionModule>  
>   <ActionName xmlns="http://www.totvs.com/">FopImportacaoImagemAction</ActionName>  
>   <CanParallelize xmlns="http://www.totvs.com/">true</CanParallelize>  
>   <CanSendMail xmlns="http://www.totvs.com/">false</CanSendMail>  
>   <CanWaitSchedule xmlns="http://www.totvs.com/">false</CanWaitSchedule>  
>   <CodUsuario xmlns="http://www.totvs.com/">mestre</CodUsuario>  
>   <ConnectionId i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <ConnectionString i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <Context z:Id="i2" xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>">  
>     <a:\_params xmlns:b="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EXERCICIOFISCAL</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">2</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODLOCPRT</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODTIPOCURSO</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$EDUTIPOUSR</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUNIDADEBIB</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODCOLIGADA</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$RHTIPOUSR</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODIGOEXTERNO</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODSISTEMA</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">P</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIOSERVICO</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>" />  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIO</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">mestre</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$IDPRJ</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CHAPAFUNCIONARIO</b:Key>  
>         <b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">-1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>       <b:KeyValueOfanyTypeanyType>  
>         <b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODFILIAL</b:Key>  
>         <b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
>       </b:KeyValueOfanyTypeanyType>  
>     </a:\_params>  
>     <a:Environment>DotNet</a:Environment>  
>   </Context>  
>   <CustomData i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <DisableIsolateProcess xmlns="http://www.totvs.com/">false</DisableIsolateProcess>  
>   <DriverType i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <ExecutionId xmlns="http://www.totvs.com/">8e9a93d1-1ddb-4721-a9b3-07bbd0a830a6</ExecutionId>  
>   <FailureMessage xmlns="http://www.totvs.com/">Falha na execução do processo</FailureMessage>  
>   <FriendlyLogs i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <HideProgressDialog xmlns="http://www.totvs.com/">false</HideProgressDialog>  
>   <HostName xmlns="http://www.totvs.com/">**SEU\_HOSTNAME**</HostName>  
>   <Initialized xmlns="http://www.totvs.com/">true</Initialized>  
>   <Ip xmlns="http://www.totvs.com/">**SEU\_IP**</Ip>  
>   <IsolateProcess xmlns="http://www.totvs.com/">false</IsolateProcess>  
>   <JobID xmlns="<http://www.totvs.com/>">  
>     <Children />  
>     <ExecID>1</ExecID>  
>     <ID>105638</ID>  
>     <IsPriorityJob>false</IsPriorityJob>  
>   </JobID>  
>   <JobServerHostName xmlns="http://www.totvs.com/">**SEU\_HOSTNAME**</JobServerHostName>  
>   <MasterActionName i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <MaximumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1000</MaximumQuantityOfPrimaryKeysPerProcess>  
>   <MinimumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1</MinimumQuantityOfPrimaryKeysPerProcess>  
>   <NetworkUser xmlns="http://www.totvs.com/">usuário</NetworkUser>  
>   <NotifyEmail xmlns="http://www.totvs.com/">false</NotifyEmail>  
>   <NotifyEmailList i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
>   <NotifyFluig xmlns="http://www.totvs.com/">false</NotifyFluig>  
>   <OnlineMode xmlns="http://www.totvs.com/">false</OnlineMode>  
>   <PrimaryKeyList xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
>   <PrimaryKeyNames i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />  
>   <PrimaryKeyTableName i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <ProcessName xmlns="http://www.totvs.com/">ImportacaoImagem</ProcessName>  
>   <QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>  
>   <SaveLogInDatabase xmlns="http://www.totvs.com/">true</SaveLogInDatabase>  
>   <SaveParamsExecution xmlns="http://www.totvs.com/">false</SaveParamsExecution>  
>   <ScheduleDateTime xmlns="http://www.totvs.com/">2023-12-29T10:38:36.6078464-03:00</ScheduleDateTime>  
>   <Scheduler xmlns="http://www.totvs.com/">JobMonitor</Scheduler>  
>   <SendMail xmlns="http://www.totvs.com/">false</SendMail>  
>   <ServerName xmlns="http://www.totvs.com/">FopImportacaoImagemProcess</ServerName>  
>   <ServiceInterface i:nil="true" xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.datacontract.org/2004/07/System>" />  
>   <ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>  
>   <ShowReExecuteButton xmlns="http://www.totvs.com/">true</ShowReExecuteButton>  
>   <StatusMessage i:nil="true" xmlns="<http://www.totvs.com/>" />  
>   <SuccessMessage xmlns="http://www.totvs.com/">Processo executado com sucesso</SuccessMessage>  
>   <SyncExecution xmlns="http://www.totvs.com/">false</SyncExecution>  
>   <UseJobMonitor xmlns="http://www.totvs.com/">true</UseJobMonitor>  
>   <UserName xmlns="http://www.totvs.com/">mestre</UserName>  
>   <WaitSchedule xmlns="http://www.totvs.com/">false</WaitSchedule>  
>   <Altura>200</Altura>  
>   <CodColigada>1</CodColigada>  
>   <DadosArquivo>  
>     <FopPropertiesImagemParams>  
>       <chapa>00004</chapa>  
>       <guid>00000000-0000-0000-0000-000000000000</guid>  
>       <imagem>  
>       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  
>       </imagem>  
>     </FopPropertiesImagemParams>  
>     <FopPropertiesImagemParams>  
>       <chapa>00005</chapa>  
>       <guid>00000000-0000-0000-0000-000000000000</guid>  
>       <imagem>  
>       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  
>       </imagem>  
>     </FopPropertiesImagemParams>  
>   </DadosArquivo>  
>   <FilePath></FilePath>  
>   <Largura>200</Largura>  
>   <ManterOriginal>false</ManterOriginal>  
>   <Qualidade>170</Qualidade>  
>   <SobrescreverAtual>true</SobrescreverAtual>  
> </FopImportacaoImagemParams>]]>  
> </tot:strXmlParams>  
>       </tot:ExecuteWithXmlParams>  
>    </soapenv:Body>  
> </soapenv:Envelope>

## **05. DEMAIS INFORMAÇÕES**
