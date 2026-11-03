---
content_hash: 4ab494acb45155263eba5a52e177596543c6c6b5c35afd8d6af6c9d68fdd07d7
fetched_at: '2026-06-29T00:09:55.792411+00:00'
page_id: '450152189'
product: rm
source: tdn-rm
title: Cálculo do valor líquido do Lançamento em uma data qualquer com o mesmo cálculo
  na visão ou edição de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152189
version: 3
---

**XML com exemplo de Calculo do valor líquido do Lançamento em uma data qualquer com o mesmo cálculo na visão ou edição de lançamentos. O cálculo aceita somente um registro de lançamento como entrada.**

**(http://localhost:8051/wsFin/MEX?wsdl)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

   <soapenv:Header/>

   <soapenv:Body>

      <tot:ValorLiquido>

         <!--Optional:-->

         <tot:xml><![CDATA[<?xml version="1.0" encoding="utf-16"?>

<TOTVSMessage>

<MessageInformation>

<UUID>ValorLiquido</UUID>

<Type>BusinessMessage</Type>

<Transaction> ValorLiquido </Transaction>

<StandardVersion>1160</StandardVersion>

<SourceApplication>TOTVS SA</SourceApplication>

<CompanyId>21.867.387/0001-58</CompanyId>

<Product>RM</Product>

<GeneratedOn>2010-09-06T16:25:23Z</GeneratedOn>

<DeliveryType>Sync</DeliveryType>

<QUEUETYPE>1</QUEUETYPE>

</MessageInformation>

<BusinessMessage>

<BusinessEvent>

<Entity>ValorLiquido</Entity>

<Event>upsert</Event>

<Identification>

<key name="key1">IDFLAN</key>

<key name="key2">CODCOLIGADA</key>

</Identification>

</BusinessEvent>

<BusinessContent>

<CompanyId>1</CompanyId>

<Code>6906</Code>

<CurrentDate>2011-04-07</CurrentDate>

<User>mestre</User>

</BusinessContent>

</BusinessMessage>

</TOTVSMessage>

           ]]></tot:xml>

         <!--Optional:-->

         <tot:contexto>codcoligada=1;codusuario=mestre;codsistema=f</tot:contexto>

      </tot:ValorLiquido>

   </soapenv:Body>

</soapenv:Envelope>
