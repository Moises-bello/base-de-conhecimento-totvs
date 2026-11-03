---
content_hash: 8fc4f7b950aa18c1de5d2fcbd2d1933c19e6c01f16217cc7d7397f4c22e381f4
fetched_at: '2026-06-29T00:09:18.039092+00:00'
page_id: '421388655'
product: rm
source: tdn-rm
title: Inclusão de boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388655
version: 9
---

## **Exemplo de xml para inclusão de boleto.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinBoletoInclusaoData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<FinBoletoParamsProc>  
<CodColigada>1</CodColigada>  
<CodUsuario>Mestre</CodUsuario>  
<DataSistema>2016-05-05T00:00:00</DataSistema>  
<OpcaoGeracao>2016-05-05T00:00:00</OpcaoGeracao>  
<listaLan>  
<FinLanBoletoParamsProc>  
<CodColigada>1</CodColigada>  
<IdLan>12929</IdLan>  
<CodCfo>C00313</CodCfo>  
<DataVencimento>2018-09-09T00:00:00</DataVencimento>  
</FinLanBoletoParamsProc>  
</listaLan>  
<ListaAgrupamento>  
<FinAgrupamentoParamsProc>  
<CodColigada>1</CodColigada>  
<IdLan>12929</IdLan>  
<CodColCliFor>1</CodColCliFor>  
<CodCliFor>C00313</CodCliFor>  
<Vencimento>2018-09-09T00:00:00</Vencimento>  
<ContraApresentacao>false</ContraApresentacao>  
<TipoBoleto>BoletoCobranca</TipoBoleto>  
<CodUsuario>Mestre</CodUsuario>  
</FinAgrupamentoParamsProc>  
</ListaAgrupamento>  
</FinBoletoParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
