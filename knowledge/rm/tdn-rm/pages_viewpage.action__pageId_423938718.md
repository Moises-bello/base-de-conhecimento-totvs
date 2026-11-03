---
content_hash: df7c7baaf8c12aa92f382a3fcd9a17b9d2f88bd445c22c87d3e1b859820247c2
fetched_at: '2026-06-29T00:09:28.584674+00:00'
page_id: '423938718'
product: rm
source: tdn-rm
title: Leitura e Montagem de XML de Cupom Fiscal com Integração TOTVS Business Connect e
  SOAPUI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938718
version: 5
---

O TOTVS Business Connect (TBC) contém Web Services que podem ser acessados por outros aplicativos para integração com a Linha RM.   
Através de uma ferramenta SOAP, (Simple Object Access Protocol) que é padrão universal utilizado para a troca de mensagens entre as aplicações consumidoras e o Web Service, nesse caso SoapUI, esses WebServices são consumidos e testados.  
Para iniciar o processo é preciso verificar se os serviços web do TBC estão disponíveis.  
Um dos serviços é o DataServer, que disponibiliza acesso direto aos objetos de negócio RM (DataServer).   
No SoapUI, ao criar um projeto, em Initial WSDL informar o WSDL do Data Server.   
Ao clicar em Ok, um projeto será criado na ferramenta. No projeto há 3 Menus. Nesse caso será utilizado o RM\_IwsDataServer. Ao expandi-lo temos algumas funções.   
Uma delas é a ReadRecord, utilizada para ler dados da base e montar o XML, nesse caso o de Cupom Fiscal.   
Ao expandir ReadRecord, temos Request1. Ao clicar duas vezes, é aberta a tela para informar os dados a serem lidos, já existente na base de dados.   
É necessário que em Request Properties seja preenchidos os values do Property Username e Passoword, com usuário e senha, assim a ferramenta irá conseguir autenticar o usuário da operação.   
Para efetuar a leitura dos dados, é necessário preencher de forma correta as tags utilizadas no processo que são:

* A tag <tot:DataServerName>?</tot:DataServerName> deve-se informar o nome do Data Server.
* Na <tot:PrimaryKey>?</tot:PrimaryKey> deve-se informar o Código da Coligada e o Identificador do Cupom Fiscal a ter sua informações copiadas.
* Na tag <tot:Contexto>?</tot:Contexto> será informado o Código da Coligada, Usuário e o Código do Sistema que serão utilizados para realizar a leitura.
* Após preencher as tags, com dados coerentes com a base de dados, basta executar. O SoapUI irá exibir o esquema com o XML do Cupom Fiscal ou se há alguma inconsistência. Se houver, a mesma deve ser corrigida para efetuar a leitura e montagem do XML. Pode-se incluir um novo movimento, utilizado esse XML. Exemplo de um esquema para ler dados da base e montar o XML Cupom Fiscal:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tot="http://www.totvs.com/">  
    < soapenv:Header/>  
    < soapenv:Body>  
       < tot:ReadRecord>  
          < !-Optional:->  
          < tot:DataServerName>MovCupomFiscalData</tot:DataServerName>  
          < !-Optional:->  
          < tot:PrimaryKey>1;202508</tot:PrimaryKey>  
          <!-Optional:->  
          < tot:Contexto>CODCOLIGADA=1;CODUSUARIO=mestre;CODSISTEMA=T</tot:Contexto>  
       </tot:ReadRecord>  
    < /soapenv:Body>  
 </soapenv:Envelope>
