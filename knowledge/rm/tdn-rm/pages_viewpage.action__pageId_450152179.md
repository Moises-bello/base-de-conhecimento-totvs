---
content_hash: 8fc892e5eedb416f5fa5bbaab0bc51859607f574df90c9512ab0cb74f2dc616b
fetched_at: '2026-06-29T00:09:55.786328+00:00'
page_id: '450152179'
product: rm
source: tdn-rm
title: Inclusão de lançamento a receber, do tipo contábil e com evento contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152179
version: 2
---

## **XML com exemplo de Inclusão de Lançamento a receber, do tipo contábil e com evento contábil. Utilizando o DataServer FinLanDataTBC.**

## **(<http://localhost:8051/wsDataServer/IwsDataServer>)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:SaveRecord>  
<!--Optional:-->  
<tot:DataServerName>FinLanDataTBC</tot:DataServerName>  
<!--Optional:-->  
<tot:XML><![CDATA[<FinLAN>  
<FLAN>  
<CODCOLIGADA>1</CODCOLIGADA>  
<IDLAN>-7</IDLAN>  
<NFOUDUP>2</NFOUDUP>  
<CLASSIFICACAO>0</CLASSIFICACAO>  
<PAGREC>1</PAGREC>  
<STATUSLAN>0</STATUSLAN>  
<CODAPLICACAO>F</CODAPLICACAO>  
<DATAVENCIMENTO>2015-02-10T00:00:00</DATAVENCIMENTO>  
<DATAEMISSAO>2014-08-11T00:00:00</DATAEMISSAO>  
<DATAPREVBAIXA>2014-09-10T00:00:00</DATAPREVBAIXA>  
<VALORORIGINAL>145.00</VALORORIGINAL>  
<CODCOLCFO>1</CODCOLCFO>  
<CODCFO>C00313</CODCFO>  
<CODCOLCXA>1</CODCOLCXA>  
<CODCXA>0001</CODCXA>  
<CODTDO>09</CODTDO>  
<CODFILIAL>1</CODFILIAL>  
<SERIEDOCUMENTO>@@@</SERIEDOCUMENTO>  
<CODMOEVALORORIGINAL>R$</CODMOEVALORORIGINAL>  
<USUARIO>mestre</USUARIO>  
<USUARIOCRIACAO>mestre</USUARIOCRIACAO>  
<PreencherRatCCusto>true</PreencherRatCCusto>  
<PreencherRatDepto>true</PreencherRatDepto>  
<VALORDEDUCAODEPENDENTES>0.0000</VALORDEDUCAODEPENDENTES>  
<TIPOCONTABILLAN>1</TIPOCONTABILLAN>  
<CodEvento>54</CodEvento>  
</FLAN>   
</FinLAN>]]></tot:XML>  
<!--Optional:-->  
<tot:Contexto>CODCOLIGADA=1;CODUSUARIO=mestre;CODSISTEMA=F</tot:Contexto>  
</tot:SaveRecord>  
</soapenv:Body>  
</soapenv:Envelope>
