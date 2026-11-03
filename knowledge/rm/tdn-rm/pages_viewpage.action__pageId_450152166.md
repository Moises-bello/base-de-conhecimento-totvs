---
content_hash: e756759964d12d34fb7f8d75e1dadea4d46666c2b0526187527b3a99e68e472c
fetched_at: '2026-06-29T00:09:55.773178+00:00'
page_id: '450152166'
product: rm
source: tdn-rm
title: Inclusão de lançamento a receber, com rateios de centro de custo e contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152166
version: 3
---

## **XML com exemplo de Inclusão de Lançamento a receber, com rateios de centro de custo e contábil. Utilizando o DataServer FinLanDataTBC.**

## (http://localhost:8051/wsDataServer/IwsDataServer)

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
<IDLAN>-6</IDLAN>  
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
<CONTABILIZACAO>  
<DATA>2015-03-22T00:00:00</DATA>  
<DESCRICAO>teste de inclusão</DESCRICAO>  
<PARTIDAS>  
<Tipo>1</Tipo>  
<CodColPartida>0</CodColPartida>  
<Partida>1.1.1.1.361</Partida>  
<CodColConta>0</CodColConta>  
<Conta>1.1.1.1.361</Conta>  
<CodFilial>1</CodFilial>  
<CodDepartamento>05</CodDepartamento>  
<CodCCusto>01.3</CodCCusto>  
<CodHistP>00001</CodHistP>  
<ComplHistorico>Teste</ComplHistorico>  
<Data>2015-02-10T00:00:00</Data>  
<Data2>2015-02-10T00:00:00</Data2>  
<Documento>0102030</Documento>  
<IdParticipante>1</IdParticipante>  
<Valor>500</Valor>  
<Valor2>12</Valor2>  
<RATEIO>  
<CodColGerencial>1</CodColGerencial>  
<CodGerencial>5.05</CodGerencial>  
<Valor>200</Valor>  
</RATEIO>  
<RATEIO>  
<CodColGerencial>1</CodColGerencial>  
<CodGerencial>5.06</CodGerencial>  
<Valor>100</Valor>  
</RATEIO>  
<RATEIO>  
<CodColGerencial>1</CodColGerencial>  
<CodGerencial>5.08</CodGerencial>  
<Valor>50</Valor>  
</RATEIO>  
<RATEIO>  
<CodColGerencial>1</CodColGerencial>  
<CodGerencial>5.09</CodGerencial>  
<Valor>50</Valor>  
</RATEIO>  
</PARTIDAS>  
<PARTIDAS>  
<Tipo>2</Tipo>  
<CodColConta>0</CodColConta>  
<Conta>1.1.1.1.360</Conta>  
<CodFilial>1</CodFilial>  
<CodDepartamento>05</CodDepartamento>  
<CodCCusto>01.3</CodCCusto>  
<CodHistP>00001</CodHistP>  
<ComplHistorico>Teste</ComplHistorico>  
<Data>2015-02-10T00:00:00</Data>  
<Data2>2015-02-10T00:00:00</Data2>  
<Documento>0102030</Documento>  
<IdParticipante>1</IdParticipante>  
<Valor>500</Valor>  
<Valor2>500</Valor2>  
<RATEIO>  
<CodColGerencial>1</CodColGerencial>  
<CodGerencial>5.05</CodGerencial>  
<Valor>500</Valor>  
</RATEIO>  
</PARTIDAS>  
</CONTABILIZACAO>  
</FLAN></FinLAN>]]></tot:XML>  
<!--Optional:-->  
<tot:Contexto>CODCOLIGADA=1;CODUSUARIO=mestre;CODSISTEMA=F</tot:Contexto>  
</tot:SaveRecord>  
</soapenv:Body>  
</soapenv:Envelope>

**Obs.:**

Contabilização está sendo informada manualmente e com rateio gerencial, nas tags **</RATEIO>** e **</PARTIDAS>**.
