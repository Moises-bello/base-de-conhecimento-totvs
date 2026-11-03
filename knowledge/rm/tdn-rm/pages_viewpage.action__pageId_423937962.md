---
content_hash: df184836cd11fd290fcca31efccc0afa40678e4d91ef361af30b0833b0e171f1
fetched_at: '2026-06-29T00:09:24.559295+00:00'
page_id: '423937962'
product: rm
source: tdn-rm
title: Incluir Movimento através de XML Cupom Fiscal com Integração TOTVS Business
  Connect e SOAPUI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937962
version: 11
---

O TOTVS Business Connect (TBC) contém Web Services que podem ser acessados por outros aplicativos para integração com a Linha RM.   
Através de uma ferramenta SOAP, (Simple Object Access Protocol) que é padrão universal utilizado para a troca de mensagens entre as aplicações consumidoras e o Web Service, nesse caso SoapUI, esses WebServices são consumidos e testados.  
Para iniciar o processo é preciso verificar se os serviços web do TBC estão disponíveis, através do link <http://localhost/TOTVSBusinessConnect/> no navegador.   
Um dos serviços é o DataServer, que disponibiliza acesso direto aos objetos de negócio RM (DataServer).   
No SoapUI, ao criar um projeto, em Initial WSDL informar o WSDL do Data Server. Ao clicar em Ok, um projeto será criado na ferramenta.   
No projeto temos 3 menus. Nesse caso, será utilizado o RM\_IwsDataServer. Ao expandi-lo temos algumas funções.  
Uma delas é a SaveRecord é a utilizada para Salvar (incluir) o movimento no TOTVS Gestão de Estoque, Compras e Faturamento. Ao expandir SaveRecord, temos Request1.   
Ao clicar duas vezes, é aberta a tela para informar o XML, nesse caso um XML Cupom Fiscal que terá as informações do cupom fiscal para inserir no movimento. Também é necessário que em Request Properties seja preenchidos os values do Property Username e Passoword, com usuário e senha, assim a ferramenta irá conseguir autenticar o usuário da operação.   
Para efetuar a inclusão, é necessário preencher de forma correta as tags utilizadas no processo. Segue abaixo as orientações:

1. A tag <tot:DataServerName>?</tot:DataServerName> deve-se informar o Nome do Data Server;
2. Na tag <tot:XML>?</tot:XML> será incluso o XML, com tags informando os dados para que o sistema inclua o movimento. Entre o XML deve informar a tag <![CDATA ]]>.;
3. Na tag <tot:Contexto>?</tot:Contexto> será informado o Código da Coligada, Usuário e o Código do Sistema que serão utilizados para realizar a inclusão;
4. Inserido o XML, com as tags do mesmo com dados coerentes com a base de dados, basta executar;
5. O SoapUI irá exibir uma mensagem informando se foi incluído ou se há alguma inconsistência. Se houver, a mesma deve ser corrigida para efetuar a inclusão;
6. Incluído com sucesso, basta acessar o banco de dados ou a própria aplicação para conferir o movimento foi gerado.

Exemplo de um esquema para Incluir Movimento a partir de XML Cupom Fiscal:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

  < soapenv:Header/>

  < soapenv:Body>

      <tot:SaveRecord>

        < !-Optional:->

        < tot:DataServerName>MovCupomFiscalData</tot:DataServerName>

        < !-Optional:->

        < tot:XML><![CDATA[<MovCupomFiscal>

<TCUPOMFISCAL>

   < CODCOLIGADA>1</CODCOLIGADA>

   < IDCUPOM>-1</IDCUPOM>

   < PONTOVENDA>9</PONTOVENDA>

    <CRO>2</CRO>

   < NUMERO>80073</NUMERO>

    <COO>80065</COO>

   < DATAEMISSAO>2014-04-03T00:00:00</DATAEMISSAO>

   < HORARIO>2014-04-03T00:00:00</HORARIO>

   < CODCOLCFO>0</CODCOLCFO>

   < CODCFO>00029869</CODCFO>

   < VALORLIQUIDO>1.70</VALORLIQUIDO>

   < DESCONTO>0.00</DESCONTO>

   < ACRESCIMO>0.00</ACRESCIMO>

   < VALORRECEBIDO>1.70</VALORRECEBIDO>

    <CAIXA>3</CAIXA>

   < IDREDUCAOZ>924</IDREDUCAOZ>

   < CANCELADO>0</CANCELADO>

    <STATUS>C</STATUS>

    <TIPO>V</TIPO>

</TCUPOMFISCAL>

<TCUPOMFISCALITM>

   < CODCOLIGADA>1</CODCOLIGADA>

   < IDCUPOM>-1</IDCUPOM>

   < NUMEROITEM>1</NUMEROITEM>

   < IDPRD>110904</IDPRD>

   < QUANTIDADE>1.000</QUANTIDADE>

   < PRECOUNITARIO>1.700</PRECOUNITARIO>

   < VALORBRUTO>1.70</VALORBRUTO>

    <DESCONTO>0.00</DESCONTO>

   < ACRESCIMO>0.00</ACRESCIMO>

   < RATEIODESCONTO>0.00</RATEIODESCONTO>

   < RATEIOACRESCIMO>0.00</RATEIOACRESCIMO>

   < VALORLIQUIDO>1.70</VALORLIQUIDO>

   < CANCELAMENTO>0.00</CANCELAMENTO>

   < TRIBUTACAOECF>II</TRIBUTACAOECF>

    <IDNAT>41</IDNAT>

   < ALIQUOTA>0.00</ALIQUOTA>

    <CST>040</CST>

   < CANCELADO>0</CANCELADO>

    <CODUND>UN</CODUND>

</TCUPOMFISCALITM>

<TCUPOMFISCALFIN>

   < CODCOLIGADA>1</CODCOLIGADA>

   < IDCUPOM>-1</IDCUPOM>

   < NUMEROPARCELA>80733</NUMEROPARCELA>

   < DEBITOCREDITO>C</DEBITOCREDITO>

    <VALOR>1.70</VALOR>

   < DATAVENCIMENTO>2013-11-01T00:00:00</DATAVENCIMENTO>

   < IDFORMAPAGTO>1</IDFORMAPAGTO>

   < CODCOLCXA>1</CODCOLCXA>

   < CODCXA>CX-011</CODCXA>

</TCUPOMFISCALFIN>

</MovCupomFiscal>]]></tot:XML>

        < !-Optional:->

         <tot:Contexto>CODCOLIGADA=1;CODUSUARIO=mestre;CODSISTEMA=T</tot:Contexto>

      </tot:SaveRecord>

  < /soapenv:Body>

</soapenv:Envelope>
