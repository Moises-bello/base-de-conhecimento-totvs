---
content_hash: 588e995ed7f1659b2a6aeac74fb8e822893592cf028781a7999bb3cbed4b6f3e
fetched_at: '2026-06-29T00:09:55.819840+00:00'
page_id: '450153122'
product: rm
source: tdn-rm
title: Alteração global de cli/for, para o NOMEFANTASIA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450153122
version: 2
---

**(http://localhost:8051/wsProcess/IwsProcess)**

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

  <FieldName>NOMEFANTASIA</FieldName>

  <FieldValue>0</FieldValue>

  <IsChangingByPercentage>false</IsChangingByPercentage>

  <IsUpdateFullDetermined>false</IsUpdateFullDetermined>

  <OriginFieldName>NOMEFANTASIA</OriginFieldName>

  <OriginTableName>FCFO</OriginTableName>

  <OtherTables>FCFOCOMPL</OtherTables>

  <TableName>FCFO</TableName>

</GlbParamsProcMultiUpdate>]]></tot:strXmlParams>

      </tot:ExecuteWithParams>

   </soapenv:Body>

</soapenv:Envelope>
