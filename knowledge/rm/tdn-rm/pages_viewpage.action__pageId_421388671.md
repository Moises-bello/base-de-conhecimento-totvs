---
content_hash: 554e34241060dd53a302e9fcc686e34ce155372462165606d011d6c7bc80f501
fetched_at: '2026-06-29T00:09:18.111886+00:00'
page_id: '421388671'
product: rm
source: tdn-rm
title: Alteração global de cli/for, para o CAMPOLIVRE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388671
version: 10
---

Para fazer alteração de um campo para vários Cli/For basta adiciona lós no primarykeylist.

**(http://localhost:8051/wsProcess/IwsProcess)**

Para fazer alteração de um campo para vários Cli/For basta adiciona lós no primarykeylist.

<?xml version="1.0" encoding="UTF-8"?>

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

   <soapenv:Header/>

   <soapenv:Body>

      <tot:ExecuteWithParams>

         <!--Optional:-->

         <tot:ProcessServerName>FinCFOAlteracaoGlobalServer</tot:ProcessServerName>

         <!--Optional:-->

         <tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>

<GlbParamsProcMultiUpdate>

  <PrimaryKeyList>0|0</PrimaryKeyList>

  <DataServerName>FinCFODataBR</DataServerName>

  <FieldName>CAMPOLIVRE</FieldName>

  <FieldValue>0</FieldValue>

  <IsChangingByPercentage>false</IsChangingByPercentage>

  <IsUpdateFullDetermined>false</IsUpdateFullDetermined>

  <OriginFieldName>CAMPOLIVRE</OriginFieldName>

  <OriginTableName>FCFO</OriginTableName>

  <OtherTables>FCFOCOMPL</OtherTables>

  <TableName>FCFO</TableName>

</GlbParamsProcMultiUpdate>]]></tot:strXmlParams>

      </tot:ExecuteWithParams>

   </soapenv:Body>

</soapenv:Envelope>
