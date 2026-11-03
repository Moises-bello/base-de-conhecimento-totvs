---
content_hash: 5f3d5bee537bd4a3c81acc4f089f3432151e3b72a22b6575112dd903a3e72f16
fetched_at: '2026-06-29T00:05:59.723346+00:00'
page_id: '191469341'
product: rm
source: tdn-rm
title: TBC - Web Service Process
type: documentation
url: https://tdn.totvs.com/display/LRM/TBC+-+Web+Service+Process
version: 31
---

## **Introdução**

---

O Web Service **wsProcess**é o responsável pela execução de processos do sistema

## **Como funciona**

---

   Estão expostos no **wsProcess**alguns serviços, onde para consumi-los é necessário enviar através de uma requisição um envelope SOAP, passando os parâmetros de cada serviço.

 

### Serviços Disponíveis

---

ExecuteWithXmlParamsServiço responsável por executar processos com parâmetros XML.1

Os parâmetros solicitado pelo ExecuteWithXmlParams são:

ProcessServerName tipo **String**

strXmlParams tipo **String**

Parâmetro strXmlParams

Para pegar o parâmetro XML é necessário executar o processo através da biblioteca.

2Passo 1

Acesse a biblioteca e execute o processo que deseja utilizar

3Selecionar Processo

No exemplo foi utilizado o processo de **Cópia de Consultas SQL entre Coligadas**

Parâmetros da Cópia

Selecionar para qual Coligada deseja copiar a consulta SQL e execute o processo.

Processo Executado

Após o processo ter sido executado com sucesso siga para o passo 2

Passo 2

Agora é necessário pegar o ID do Job que foi gerado pelo processo

Acesse o menu "Ambiente | Gerenciamento de Jobs"

Após saber qual é o ID do Job siga para o Passo 3

Passo 3

Sabendo qual é o ID do Job é necessário obter o XML de processo. Ele pode ser obtido de duas formas:

* Utilizando a ferramenta **TotvsWSClient**, como descrito no Passo 4
* Localizando o ID do Job na tela de **XML de Parâmetros de Jobs**, na MDI, como descrito no .

Informação

Saiba como configurar e utilizar a ferramenta através do link  

Passo 4

Após executar o TotvsWsClient acesse a visão de processos

8ProcessosInformar o Job

Informe o Job do processo e clique em carregar

Será exibido o registro equivalente ao ID Job informado

Dê dois cliques no registro e siga para o próximo passo

Visualizar Parâmetro XML

Após abrir o registro serão exibidos os dados do registro, Propriedades e o **XML**

Acesse a Aba XML, clique na opção de "Codificar como CDATA" e copie o XML, pois é ele que será passado como parâmetro do processo

Passo 53Requestxml




GlbProcCopyConsSQL

<?xml version="1.0" encoding="utf-16"?>
<GlbParamsProcCopyColig xmlns:i="http://www.w3.org/2001/XMLSchema-instance" z:Id="i1" xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/" xmlns="http://www.totvs.com.br/RM/">
<CanParallelize xmlns="http://www.totvs.com/">true</CanParallelize>
<Context xmlns:d2p1="http://www.totvs.com.br/RM/" z:Id="i2" xmlns="http://www.totvs.com/">
<d2p1:\_params xmlns:d3p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODUNIDADEBIB</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">1</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CHAPAFUNCIONARIO</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">00001</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$EXERCICIOFISCAL</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">2</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODFILIAL</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">1</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$RHTIPOUSR</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">01</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODCOLIGADA</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">1</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$EDUTIPOUSR</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">F</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODLOCPRT</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">5</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODUSUARIO</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">mestre</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODUSUARIOSERVICO</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string"></d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODSISTEMA</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">G</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODTIPOCURSO</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">2</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$CODIGOEXTERNO</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">-1</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
<d3p1:KeyValueOfanyTypeanyType>
<d3p1:Key xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:string">$IDPRJ</d3p1:Key>
<d3p1:Value xmlns:d5p1="http://www.w3.org/2001/XMLSchema" i:type="d5p1:int">2</d3p1:Value>
</d3p1:KeyValueOfanyTypeanyType>
</d2p1:\_params>
<d2p1:Environment>DotNet</d2p1:Environment>
</Context>
<Initialized xmlns="http://www.totvs.com/">true</Initialized>
<IsolateProcess xmlns="http://www.totvs.com/">false</IsolateProcess>
<MaximumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1000</MaximumQuantityOfPrimaryKeysPerProcess>
<MinimumQuantityOfPrimaryKeysPerProcess xmlns="http://www.totvs.com/">1</MinimumQuantityOfPrimaryKeysPerProcess>
<PrimaryKeyList xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns="http://www.totvs.com/">
<d2p1:ArrayOfanyType>
<d2p1:anyType xmlns:d4p1="http://www.w3.org/2001/XMLSchema" i:type="d4p1:short">1</d2p1:anyType>
<d2p1:anyType xmlns:d4p1="http://www.w3.org/2001/XMLSchema" i:type="d4p1:string">G</d2p1:anyType>
<d2p1:anyType xmlns:d4p1="http://www.w3.org/2001/XMLSchema" i:type="d4p1:string">Exemplo</d2p1:anyType>
</d2p1:ArrayOfanyType>
</PrimaryKeyList>
<PrimaryKeyNames xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns="http://www.totvs.com/">
<d2p1:string>CODCOLIGADA</d2p1:string>
<d2p1:string>APLICACAO</d2p1:string>
<d2p1:string>CODSENTENCA</d2p1:string>
</PrimaryKeyNames>
<QuantityOfSplits xmlns="http://www.totvs.com/">0</QuantityOfSplits>
<ShouldParallelize xmlns="http://www.totvs.com/">false</ShouldParallelize>
<IsReplaceExistingRecordsVisible>true</IsReplaceExistingRecordsVisible>
<ReplaceExistingRecords>false</ReplaceExistingRecords>
<TargetColigadas xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
<d2p1:int>6</d2p1:int>
</TargetColigadas>
</GlbParamsProcCopyColig>
]]>Responsexml


1
]]>ExecuteWithXmlParamsAsync

Serviço responsável por executar processos com parâmetros XML de forma assíncrona, isto é, o serviço submeterá a execução do processo e devolverá um id de job que pode ser passado como parâmetro para o serviço GetProcessStatus para consultar o andamento do processo.

Os passos a serem seguidos são idênticos ao serviço ExecuteWithXmlParams, porém o retorno do método é diferente. Disponibilizado a partir da versão 12.1.20.

1

Os parâmetros solicitado pelo ExecuteWithXmlParamsAsync são:

ProcessServerName tipo **String**

strXmlParams tipo **String**

Parâmetros

Para pegar o parâmetro XML é necessário executar o processo através da biblioteca.

2Passo 53Requestxml




GlbCopyPermisUsrProc



G
GlbActionProcCopyPermisUsr
mestre



$EXERCICIOFISCAL
22

$CODLOCPRT
12

$CODTIPOCURSO
1

$EDUTIPOUSR
A

$CODUNIDADEBIB
5

$CODCOLIGADA
1

$RHTIPOUSR
01

$CODIGOEXTERNO
-1

$CODSISTEMA
G

$CODUSUARIOSERVICO


$CODUSUARIO
mestre

$IDPRJ
2

$CHAPAFUNCIONARIO
00001

$CODFILIAL
1
DotNet


1Teste

CODUSUARIO
S
true








false
mestre
]]]]>
]]>Responsexml




104863
1
]]]]>
]]>GetProcessStatus

Serviço responsável por retornar as informações de um processo. Os parâmetros podem ser capturados pelo método ExecuteWithXmlParamsAsync.

1

Os parâmetros solicitado pelo ExecuteWithXmlParams são:

jobId tipo **String**

execId tipo **String**

Parâmetros

Para pegar o parâmetro XML é necessário executar o processo através da biblioteca.

2Passo 13Requestxml




104863

1
]]>Responsexml





104863
1

-1
Finished
]]]]>
]]>GetJobParams

Serviço responsável por retornar os dados de parâmetro de uma execução de Job.

1

Os parâmetros solicitado pelo GetJobParams são:

jobId tipo **String**

execId tipo **String**

Parâmetros

Para pegar o parâmetro XML é necessário executar o processo através da biblioteca.

2Passo 13Requestxml




103194

1
]]>Responsexml






false
false
false
mestre





$CODUSUARIO
mestre

$CODSISTEMA
G

$CODCOLIGADA
1
WebServices

false

cff807d4-5768-4007-a540-1ac36397adc1
Falha na execução do processo

false

false

false


1
103194
false
BHN050103914

1000
1

false

false
false



GlbProcClearJobs
0
true
false
2026-01-23T11:14:13.3660824-03:00
JobMonitor
false


false
true

Processo executado com sucesso
false
true
mestre
false
true
true
true
true
true
true
false
true
true
true
true
0
0
]]]]>
]]>Observação

Os outros métodos expostos foram descontinuados, e encontram-se disponíveis somente por motivo de **compatibilidade**.

---

**Para utilização dos Web Services através do aplicativo "Totvs Web Service Client", clique [aqui](http://tdn.totvs.com/x/yBdFCg).**

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX |
| **Processo** | Web Services |
| **Subprocesso** | Utilizando o Web Service wsProcess |

|  |  |
| --- | --- |
| Status do Documento: | Finalizado |
| Data: | 30/06/2015 |
| Versão: | 11.82.XX |
| Versão Anterior: | 11.82.XX |
| Autores: |  |
