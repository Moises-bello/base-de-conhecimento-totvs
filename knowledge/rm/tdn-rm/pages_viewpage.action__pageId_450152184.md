---
content_hash: 3a10d9486d6f4172dfe21958ed651a8ca830fe2d2ce7f02c44bd105390f48915
fetched_at: '2026-06-29T00:09:55.789454+00:00'
page_id: '450152184'
product: rm
source: tdn-rm
title: Cancelamento de Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152184
version: 2
---

## **XML com exemplo de Cancelamento de Lançamento, utilizando o ProcessServer FinLanCancelamentoData, via ExecuteWithParams.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinLanCancelamentoData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>  
<FinLanCancelamentoParamsProc>  
<CodColigada>1</CodColigada>  
<DataCancelamento>2018-02-07T00:00:00-02:00</DataCancelamento>  
<Historico>[HIS]</Historico>  
<ListaDeLancamentos>  
<int>12919</int>  
<int>12920</int>  
<int>12921</int>  
<int>12922</int>  
</ListaDeLancamentos>  
</FinLanCancelamentoParamsProc>]]></tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
