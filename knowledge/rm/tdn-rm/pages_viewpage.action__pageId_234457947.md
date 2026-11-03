---
content_hash: 38cc81d5ffc17ae5ecef758ae30713a33e6bd8f4a76aedabc6c6a5f993afea16
fetched_at: '2026-06-29T00:06:29.324907+00:00'
page_id: '234457947'
product: rm
source: tdn-rm
title: DT_MensageriaTotvs (RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234457947
version: 135
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Framework Bh* |
| **Módulo:** | *EAI* |
|  |  |
|  |  |

## Descrição

Esse documento tem como objetivo descrever as novas funcionalidades agregadas ao modelo atual de "mensagem única", procurando atender a definição de que “o vertical deve ser o dono da integração”.

Foram criados mecanismos que de acordo com o padrão de cada aplicativo, disponibilize seus “objetos de negócios” como *BusinessContent.*

Essas alterações não têm como objetivo substituir o modelo de mensageria única e sim agregar novas funcionalidades e recursos ao mesmo.

Para fins de adequação, para esse novo modelo adotaremos o nome de "MENSAGERIA TOTVS".

## Importante

As equipes responsáveis pelos produtos Totvs deverão desenvolver serviços a serem expostos por webServices.  As estruturas desses serviços (schemas ou contratos) devem ser expostos através do formato de xsd's .

Isso permitirá que os produtos possam enviar dados no formato de xml (BusinessContent) contendo informações já no formato nativo dos objetos de negócio (sem necessidade de transformação).

As estruturas de DataServers e Process serão expostos através das suas interfaces públicas IRMSDataServer e IRMSProcess.

## Definições

 

* Na tag “transaction” poderá ser enviado o nome do objeto de negócio responsável pelo processamento da mensagem. Atualmente, somente nomes de mensagens únicas são enviadas nessa tag.

                       Exemplo: <transaction>RM/FinCFODataBR<transaction>

**Mensageria Totvs:** Nesse exemplo o nome do objeto de negócio foi enviado.

                       Exemplo: <transaction>CUSTOMERVENDOR<transaction>

**Mensageria Única**: Nesse exemplo o nome da mensagem única foi enviado

* No recebimento de uma determinada mensagem, será determinado automaticamente pelo EAI receptor o tipo de processamento da mensagem (processamento por um módulo “Vertical” ou “ERP”).
* Em se tratando de mensagens nativas (não utilizando mensageria única), no atributo “transaction”, deve ser incluído obrigatoriamente o nome do ERP (RM/ ou Protheus/ ou DataSul/ ou /Logix) antes do nome do objeto de negócio.   
  No recebimento dessa mensagem, o EAI receptor verificará se o nome incluído emparelha com seu ERP. Caso positivo, trata-se de um receptor ERP. Caso negativo, trata-se de um receptor vertical.  
    
  Exemplo:

  | <MessageInformation version="12.1.9">    <UUID>578458748541574578548487</UUID>    <Type>BusinessMessage</Type>    <Transaction>Protheus/ObjetoDeNegocioProtheus</Transaction>    <StandardVersion>1.0</StandardVersion>    <SourceApplication>SourceApplication</SourceApplication>    <CompanyId>CompanyId</CompanyId>    <Product name="Any" version="Any"/>    <GeneratedOn>2016-02-04T11:00:00</GeneratedOn>    <DeliveryType>Assync/Sync</DeliveryType>  </MessageInformation> |
  | --- |
* Na tag “Identification” não será enviada nenhuma informação (em caso de mensagens nativas). O envio dessa informação só faz sentido em caso de mensagens únicas;  
    
  Exemplo

| BusinessMessage>    <BusinessEvent>      <Entity>**Protheus/ObjetoDeNegocioProtheus**</Entity>      <Event>upsert|delete</Event>  **<Identification>**  **</Identification>**    </BusinessEvent>    <BusinessContent>      ...    </BusinessContent>  </BusinessMessage> |
| --- |

* Na tag “ReturnContent” da mensagem de resposta “ResponseMessage” não será retornada a lista de internalsIds (em caso de mensagens nativas), visto que para esse tipo de mensagem o ERP não mais armazenará os internalsIds dos verticais;

| <ResponseMessage>    <ReceivedMessage>          <SentBy>client</SentBy>          <UUID>94551485144878487457857454</UUID>          <MessageContent><![CDATA[                 <TOTVSMessage>...</TOTVSMessage>          ]]>          </MessageContent>    </ReceivedMessage>    <ProcessingInformation>          <ProcessedOn>2001-12-31T12:00:03</ProcessedOn>          <Status>OK</Status>          <ListOfMessages>            <Message type="WARNING" code="c1">msg1</Message>            <Message type="ERROR" code="c2">msg2.</Message>          </ListOfMessages>    </ProcessingInformation>    <ReturnContent>    </ReturnContent>  </ResponseMessage> |
| --- |

 

* Foi criada uma nova tag chamada “*XMLContent”*filha de ReturnContent”. Nessa nova tag será enviado o xml contendo o resultado da informação após seu processamento pelo receptor. Através dessa informação, o EAI vertical saberá os valores exatos das chaves geradas. Possibilitando portanto a inclusão desses valores nas tabelas de De/Para.

  | <ResponseMessage>    <ReceivedMessage>          <SentBy>client</SentBy>          <UUID>94551485144878487457857454</UUID>  **<MessageContent><![CDATA[**  **<TOTVSMessage>...</TOTVSMessage>**  **]]>**          </MessageContent>    </ReceivedMessage>    <ProcessingInformation>          <ProcessedOn>2001-12-31T12:00:03</ProcessedOn>          <Status>OK</Status>          <ListOfMessages>            <Message type=*"WARNING"* code=*"c1"*>msg1</Message>            <Message type=*"ERROR"* code=*"c2"*>msg2.</Message>          </ListOfMessages>    </ProcessingInformation>    <ReturnContent>  **<XMLContent>**  **...**  **</XMLContent>**  </ReturnContent>  </ResponseMessage> |  |
  | --- | --- |

  Nas mensagens de Requests, ao enviar o o nome do Process da RM, será retornado na tag "xmlContent" a classe de parâmetros do processo contendo informações geradas após seu processamento.

 

* Em mensagens de exclusão, as informações excluídas também serão retornadas nessa tag para recuperação correta do De/Para nos aplicativos verticais.
* Objetos de negócio nos aplicativos verticais deverão “emparelhar” com seus respectivos objetos de negócios no ERP.

Exemplo: Atualmente no RM existem 4 objetos de negócios diferentes responsáveis pela inclusão dos dados bancários (banco, agencia, conta e conta caixa). No Protheus existe apenas um único objeto de negócio para inclusão dessas informações.

             Sendo assim, deve ser criado pela equipe de segmentos do RM um único objeto de negócio capaz de receber todas as informações bancárias de uma única vez.

             Esse novo objeto de negócio a ser criado pelo RM “*orquestrará*” as chamadas aos objetos de negócio nativos do segmento;

 

* Em caso de mensagens assíncronas, o originador da mensagem deve observar o conteúdo da tag "**ReceivedMessage\MessageContent**" para a montagem do "**DE-PARA**" no retorno da mensagem. Não consideramos prudente buscar o valor diretamente da fila pelo fato de ser impossível garantir a existência da mensagem.

## Mensagens utilitárias

 

* ## Whois:

  mensagem utilizada para retornar os nomes das mensagens únicas parametrizadas no EAI ou retornar os nomes de todos os objetos de negócio expostos como webServices (dataservers ou process).

            Exemplo de mensagem de entrada:

| <TOTVSMessage>  <MessageInformation version="1.001">  <UUID>bb9dd43c-9dcd-a056-c3c7-d78f038d2779</UUID>  <Type>BusinessMessage</Type>  <Transaction>WHOIS</Transaction>  <StandardVersion>1.000</StandardVersion>  <SourceApplication>PR11\_BRA</SourceApplication>  <CompanyId>18</CompanyId>  <BranchId>D MG 01</BranchId>  <Product name="PROTHEUS" version="11" />  <GeneratedOn>2015-09-22T19:46:09</GeneratedOn>  <DeliveryType>Sync</DeliveryType>  </MessageInformation>  <BusinessMessage>  <BusinessRequest>  <Operation>WhoIs</Operation>  </BusinessRequest>  <BusinessContent>  <RequestType BusinessObjectOnly="true" />  </BusinessContent>  </BusinessMessage> </TOTVSMessage> |
| --- |

Caso o atributo "BusinessObjectOnly" esteja configurado com o valor "true" será retornado os nomes dos serviços (objetos de negócio). Caso seja marcado como "false", terá o mesmo comportamento da mensagem Whois 1.000, ou seja, retornará somente as mensagens mapeadas para o modelo de mensageria única

Exemplo de mensagem de saída:

| <ProcessingInformation> <ProcessedOn>2016-03-23T17:13:51</ProcessedOn> <Status>OK</Status> </ProcessingInformation>  <ReturnContent> <Transaction><Name>Autenticacao</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbDuplicVersaoEstudoProcess</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbEstudoData</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbEstudoServer</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbFaseData</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbSituacaoData</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbTipoEstudoData</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>AvbVersaoEstudoData</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction><Name>BaseScript</Name><Mode>BOTH\_ENABLED</Mode><Version>1.000</Version></Transaction><Transaction> </ReturnContent> |
| --- |

Será retornada uma mensagem do tipo "ResponseMessage" contendo todos os nomes dos servers disponíveis na RM. Por questão de tamanho da mensagem, no exemplo abaixo será retornado somente alguns serviços, visto que, existem milhares de serviços disponíveis na arquitetura RM.

* ## GetSchema:

  Mensagem utilizada para retornar o schema do serviço em questão. Através desse retorno, os outros sistemas poderão enviar xml de entrada no formato desse schema.

  Exemplo1: cadastro de cliente fornecedor (Mensagem de Event). Será utilizado o serviço "FinCFODataBR".

  | <TOTVSMessage>  <MessageInformation version="1.000">  <UUID>bb9dd43c-9dcd-a056-c3c7-d78f038d433/</UUID>  <Type>BusinessMessage</Type>  <Transaction>GETSCHEMA</Transaction>  <StandardVersion>1.000</StandardVersion>  <SourceApplication>P12\_INTX</SourceApplication>  <CompanyId>T1</CompanyId>  <BranchId>D MG 01</BranchId>  <CompanySharingMode>E</CompanySharingMode>  <BusinessUnitySharingMode>E</BusinessUnitySharingMode>  <BranchSharingMode>E</BranchSharingMode>  <Product name="PROTHEUS" version="12" />  <GeneratedOn>2015-10-30T14:18:11</GeneratedOn>  <DeliveryType>Sync</DeliveryType>  </MessageInformation>  <BusinessMessage>  <BusinessRequest>  <Operation>GetSchema</Operation>  </BusinessRequest>  <BusinessContent>  <Adapter>FinCFODataBR</Adapter>  </BusinessContent>  </BusinessMessage> </TOTVSMessage> |
  | --- |

  Será retornada uma mensagem do tipo "ResponseMessage" contendo o schema do serviço em questão.

  | <ProcessingInformation> <ProcessedOn>2016-03-23T17:43:55</ProcessedOn> <Status>OK</Status> </ProcessingInformation> <ReturnContent ><XSD> <Adapter>FinCFODataBR</Adapter> <Schema>&lt;FinCFOBR xmlns="http://tempuri.org/FinCFOBR.xsd"&gt;  &lt;xs:schema id="FinCFOBR" targetNamespace="<http://tempuri.org/FinCFOBR.xsd>" xmlns:mstns="<http://tempuri.org/FinCFOBR.xsd>" xmlns="<http://tempuri.org/FinCFOBR.xsd>" xmlns:xs="<http://www.w3.org/2001/XMLSchema>" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" attributeFormDefault="qualified" elementFormDefault="qualified"&gt;  &lt;xs:element name="FinCFOBR" msdata:IsDataSet="true" msdata:UseCurrentLocale="true" msdata:EnforceConstraints="False"&gt;  &lt;xs:complexType&gt;  &lt;xs:choice minOccurs="0" maxOccurs="unbounded"&gt;  &lt;xs:element name="FCFO"&gt;  &lt;xs:complexType&gt;  &lt;xs:sequence&gt;  &lt;xs:element name="CODCOLIGADA" msdata:Caption="Coligada" type="xs:short" /&gt;  &lt;xs:element name="CODCFO" msdata:Caption="Cliente/Fornecedor"&gt;  &lt;xs:simpleType&gt;  &lt;xs:restriction base="xs:string"&gt;  &lt;xs:maxLength value="25" /&gt;  &lt;/xs:restriction&gt;  &lt;/xs:simpleType&gt;  &lt;/xs:element&gt;  &lt;xs:element name="NOMEFANTASIA" msdata:Caption="Nome Fantasia"&gt;  &lt;xs:simpleType&gt;  &lt;xs:restriction base="xs:string"&gt;  &lt;xs:maxLength value="100" /&gt;  &lt;/xs:restriction&gt;  &lt;/xs:simpleType&gt;  &lt;/xs:element&gt;  &lt;xs:element name="NOME" msdata:Caption="Nome"&gt;  &lt;xs:simpleType&gt;  &lt;xs:restriction base="xs:string"&gt;  &lt;xs:maxLength value="100" /&gt;  &lt;/xs:restriction&gt;  &lt;xs:selector xpath=".//mstns:FCFOCOMPL" /&gt;  &lt;xs:field xpath="mstns:CODCOLIGADA" /&gt;  &lt;xs:field xpath="mstns:CODCFO" /&gt;  &lt;/xs:keyref&gt;  &lt;/xs:element&gt;  &lt;/xs:schema&gt; &lt;/FinCFOBR&gt; </Schema> </XSD> </ReturnContent> |
  | --- |

  Exemplo2: retorna o schema da classe de parâmetros do processo

  | <TOTVSMessage>  <MessageInformation version="1.000">  <UUID>bb9dd43c-9dcd-a056-c3c7-d78f038d4279/</UUID>  <Type>BusinessMessage</Type>  <Transaction>GETSCHEMA</Transaction>  <StandardVersion>1.000</StandardVersion>  <SourceApplication>P12\_INTX</SourceApplication>  <CompanyId>T1</CompanyId>  <BranchId>D MG 01</BranchId>  <CompanySharingMode>E</CompanySharingMode>  <BusinessUnitySharingMode>E</BusinessUnitySharingMode>  <BranchSharingMode>E</BranchSharingMode>  <Product name="PROTHEUS" version="12" />  <GeneratedOn>2015-10-30T14:18:11</GeneratedOn>  <DeliveryType>Sync</DeliveryType>  </MessageInformation>  <BusinessMessage>  <BusinessRequest>  <Operation>GetSchema</Operation>  </BusinessRequest>  <BusinessContent>  <Adapter>ConExecuteQueueProcess</Adapter>  </BusinessContent>  </BusinessMessage> </TOTVSMessage> |
  | --- |

  Mensagem de resposta:

  | <ProcessingInformation> <ProcessedOn>2016-03-23T18:36:37</ProcessedOn> <Status>OK</Status> </ProcessingInformation> <ReturnContent> <XSD> <Adapter>ConExecuteQueueProcess</Adapter> <Schema>&lt;?xml version="1.0" encoding="utf-16"?&gt; &lt;ConExecuteQueueParams xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" z:Id="i1" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>" xmlns="http://www.totvs.com/"&gt;  &lt;Context xmlns:d2p1="<http://www.totvs.com.br/RM/>" z:Id="i2"&gt;  &lt;d2p1:\_params xmlns:d3p1="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" /&gt;  &lt;d2p1:Environment&gt;Delphi&lt;/d2p1:Environment&gt;  &lt;/Context&gt;  &lt;PrimaryKeyList xmlns:d2p1="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" /&gt;  &lt;PrimaryKeyNames xmlns:d2p1="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" i:nil="true" /&gt; &lt;/ConExecuteQueueParams&gt; </Schema> </XSD> </ReturnContent> |
  | --- |

Ao chamar a mensagem "GetSchema" para processo qualquer, será retornado o objeto RMSParamsProc relacionado ao processo em questão de forma serializada.

**3) Direção das mensagens**

****a) Origem –> ERP  /   Destino -> Vertical****

**Detalhamento dos processos:**

* Origem da mensagem:
  + O aplicativo do ERP chama o EAI(ERP) passando as seguintes informações:
    - Nome da mensagem (mensagem única ou mensagem nativa);
      * Deve ser adicionado no início do nome da mensagem o “nome do ERP” separado por “/”.
        + Ex: Protheus/MATA010, sendo:
          - Protheus -> nome do ERP;
          - MATA010 -> nome do objeto de negócio;
    - Versão da mensagem (somente em caso de mensagens únicas);
    - Xml dos dados no formato do ERP.
  + O EAI(ERP) inclui a mensagem na fila;
  + O EAI(ERP) recupera a mensagem da fila;
  + O EAI(ERP) cria a mensagem *TotvsMessage* (incluindo na tag “*BusinessContent”* o xml recebido com os dados no formato nativos do ERP);
  + O EAI(ERP) envia para o WebServices EAI(Vertical) a mensagem no formato “*TotvsMessage”*;
* Destino da mensagem:
  + O EAI (vertical) inclui a mensagem na fila;
  + O EAI(Vertical) recupera a mensagem da fila;
  + O EAI(Vertical) recupera a primeira parte do nome da mensagem (até a posição da barra “/”) recuperando com isso o nome do ERP. Se o mesmo emparelhar com o nome do ERP em questão, trata-se de um receptor ERP. Caso contrário, trata-se de um vertical;
  + O EAI(vertical) solicita os seguintes serviços do seguimento vertical:
    - Execução do serviço de transformação da mensagem (formato nativo do ERP) para o formato nativo do segmento vertical;
    - Execução do objeto de negócio do segmento mapeado com o nome do objeto de negócio enviado pelo ERP;
    - Atualização dos valores de De/Para contendo informações das chaves de origem/destino;
      * Deve ser localizado na própria mensagem de origem os valores das chaves;
    - Retorno para o EAI(vertical) um xml contendo os dados atuais após a execução do objeto de negócio;

      A partir de agora, os EAI’s não serão mais responsáveis em transformar mensagens e controlar informações de De/para. Esses serviços serão de responsabilidade dos diversos seguimentos.

      Serviços genéricos poderão ser disponibilizados no EAI para facilitar o trabalho dos segmentos.

* Origem da mensagem:
  + O EAI(ERP), no retorno da mensagem, grava as informações da mensagem de resposta (ResponseMessage);

****b) - Origem –> Vertical   /   Destino -> ERP e outro Vertical****

**Detalhamento dos processos:**

* Origem da mensagem:
  + O segmento vertical chama o EAI(vertical) passando as seguintes informações:
    - Nome da mensagem (mensagem única ou mensagem nativa);
      * Deve ser adicionado no início do nome da mensagem o “nome do ERP” que receberá a mensagem separado por “/”.
        + Ex: Protheus/MATA010, sendo:
          - Protheus -> nome do ERP;
          - MATA010 -> nome do objeto de negócio;
    - Versão da mensagem (somente em caso de mensagem única);
    - Versão da mensagem (em caso de mensagem única);
    - Xml dos dados do vertical (no exemplo em questão, trata-se do formato nativo do segmento vertical).
  + O EAI(vertical) inclui a mensagem na fila;
  + O EAI(vertical) recupera a mensagem da fila;
  + O EAI(vertical) solicita os seguintes serviços do seguimento vertical:
    - Serviço de transformação da mensagem (do formato nativo do vertical) para o formato nativo do ERP;
  + O EAI(vertical) cria a mensagem *TotvsMessage* (incluindo na tag <*BusinessContent*> o xml recebido do segmento com os dados no formato ERP);
  + O EAI(vertical) envia para o WebServices EAI(ERP) a mensagem no formato <*TotvsMessage*>
* Destino da mensagem:
  + O EAI (ERP) inclui a mensagem na fila;
  + O EAI(ERP) recupera a mensagem da fila;
  + O EAI(ERP) recupera a primeira parte do nome da mensagem (até a posição da barra “/”) recuperando com isso o nome do ERP. Se o mesmo emparelhar com o nome do ERP em questão, trata-se de um receptor ERP. Caso contrário, trata-se de um vertical;
  + O EAI(ERP) solicita os seguintes serviços do seguimento vertical:
    - Execução do objeto de negócio para processamento da mensagem. As informações de leitura dos dados recém criados pelo objeto de negócio deverão ser retornadas.
  + O EAI(ERP) cria a mensagem de resposta “ResponseMessage” e retorna para a origem;

* Origem da mensagem:
  + O EAI(vertical), no retorno da mensagem, solicita os seguintes serviços do seguimento vertical:
    - Atualização de De/para;

    Os dados das chaves do ERP serão extraídos da tag <*XMLContext*> localizada no “ResponseMessage”;

**Procedimentos quando o RM funcionar como ERP**

* RM recebendo os dados:  
    
  + Nenhuma configuração deve ser feita no lado do RM, visto que, a mensagem de recebimento já chegará no formato nativo do objeto de negócio da RM (ex: RM / FinCFODataBR);
  + O EAI automaticamente enviará a mensagem recebida para o dataServer ou process do RM;
  + Nenhuma transformação da mensagem será feita pelo EAI da RM, visto que os dados já serão enviados no formato nativo do objeto de negócio da RM. Caso contrário, ocorrerá erro na execução  da mensagem.
  + A tabela de De/Para (HCIntegracaoID) não será atualizada nesse momento no lado da RM, visto que os dados de De/Para devem ser controlados pelo vertical (origem da mensagem);
* RM enviando os dados:  
    
  + Formula visual:   
    A propriedade "Id.Transformação", disponibilizada na atividade de fórmula visual, deve ser configurada conforme abaixo:

    Deve ser incluída a palavra "RM" após a versão da mensagem.
  + Cadastro na tabela de integração (HCIntegracao):   
    Deve-se cadastrar algumas informações básicas nas tabelas (HCIntegracao, HCTransformacao, HCMapaIntegracao). O EAI RM precisa saber para quais webServices a mensagem será enviada.   
    No cadastro de transformação não será necessário cadastrar os xslt de transformação, conforme figuras abaixo.

**Procedimentos quando o RM funcionar como Vertical**

RM recebendo os dados:

* A configuração para a integração deve ser feita normalmente inclusive cadastrando os xslt's de transformação;
* Deve ser criado um Adapter de recebimento da mensagem na solution do segmento conforme abaixo:  
  Os procedimentos para criação das dlls de adapters foram detalhados no seguinte documento:  
  <http://tdn.totvs.com/display/LRM/DT_CENTRALIZAR_OS_CODIGOS_DE_INTEGRACAO>

* + Herdar da classe "BusinessObjectReceiveHandle". Trata-se de uma classe do EAI da framework utilizada pelos adapters de recebimento de mensagem;
  + Utilizar o atributo "AdapterAttr" informando as seguintes características:
    - TransactionType.ttObjetoNegocio: informa que o adapter resolverá uma mensagem no formato Mensageria Totvs;
    - AdapterType.atReceive: adapter de recebimento de mensagem;
    - Identificador da mensagem (TransactionID);
    - Versão da mensagem;
  + Sobrescrever o método "GetServerName" informando o nome do server que deve ser executado no lado RM;
  + Sobrescrever o método "DoExecute" para implementação de regras a serem executadas antes da execução da mensagem;
  + Sobrescrever o método "DoAfterReceive" para atualização do De/Para;

A atualização do De/Para e a transformação da mensagem será de responsabilidade dos verticais.

RM enviando os dados:

* A configuração para a integração deve ser feita normalmente inclusive cadastrando os xslt's de transformação;
* Deve ser criado um Adapter de envio da mensagem na solution do segmento conforme abaixo:

* + Criar uma classe no projeto de adapter da solution em questão;
  + Herdar da classe "BusinessObjectSendHandle". Trata-se de uma classe da framework utilizada pelos adapters de envio de mensagem;
  + Utilizar o atributo "AdapterAttr" informando as seguintes características:
    - TransactionType.ttObjetoNegocio: informa que o adapter resolverá uma mensagem no formato Mensageria Totvs;
    - AdapterType.atSend: adapter de envio de mensagem;
    - Identificador da mensagem (TransactionID);
    - Versão da mensagem;
  + Sobrescrever o método "DoExecute" para implementação de regras a serem executadas antes da execução da mensagem;
  + Sobrescrever o método "DoAfterSend" para atualização do De/Para;

divs
