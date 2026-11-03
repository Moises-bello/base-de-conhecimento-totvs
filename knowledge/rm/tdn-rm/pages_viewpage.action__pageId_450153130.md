---
content_hash: c08b57b37b602082600d5f42d5c40dbaa025cd987fafd9ee2db191030e6e57cc
fetched_at: '2026-06-29T00:09:55.822175+00:00'
page_id: '450153130'
product: rm
source: tdn-rm
title: Alteração global de cli/for, para BLOQUEADO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450153130
version: 3
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

  <FieldName>CFOIMOB</FieldName>

  <FieldValue>0</FieldValue>

  <IsChangingByPercentage>false</IsChangingByPercentage>

  <IsUpdateFullDetermined>false</IsUpdateFullDetermined>

  <OriginFieldName>CFOIMOB</OriginFieldName>

  <OriginTableName>FCFO</OriginTableName>

  <OtherTables>FCFOCOMPL</OtherTables>

  <TableName>FCFO</TableName>

</GlbParamsProcMultiUpdate>]]></tot:strXmlParams>

      </tot:ExecuteWithParams>

   </soapenv:Body>
