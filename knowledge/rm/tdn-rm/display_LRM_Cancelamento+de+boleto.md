---
content_hash: 0814068510245d09f52370bac567a7de6afd8659bc30fec912b343c62b5c6243
fetched_at: '2026-06-29T00:09:57.585962+00:00'
page_id: '450153653'
product: rm
source: tdn-rm
title: Cancelamento de boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+boleto
version: 2
---

## **Exemplo do xml de cancelamento de boleto.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinBoletoCancelamentoData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<FinBoletoParamsProc>  
<CodColigada>1</CodColigada>  
<CodUsuario>Mestre</CodUsuario>                 
<DataSistema>2016-09-09T00:00:00</DataSistema>  
<ListaAgrupamento>                    
<FinAgrupamentoParamsProc>  
<CodColigada>1</CodColigada>  
<IdBoleto>10542</IdBoleto>    
</FinAgrupamentoParamsProc>  
</ListaAgrupamento>  
</FinBoletoParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
