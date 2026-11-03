---
content_hash: 1cef796e68cbcae3ea89669aa4be36f2ec1be018cef5ae972d1d708507e184aa
fetched_at: '2026-06-29T00:09:57.583634+00:00'
page_id: '450153650'
product: rm
source: tdn-rm
title: Geração de código de barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450153650
version: 1
---

## **Exemplo de xml de Geração de código de barras.**

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinBoletoGerarCodBarrasProc</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams><![CDATA[<FinBoletoParamsProc>  
<CodColigada>1</CodColigada>  
<CodUsuario>Mestre</CodUsuario>  
<CodAplicacao>F</CodAplicacao>  
<DataSistema>2018-07-02T00:00:00</DataSistema>  
<AtualizaCamposBD>true</AtualizaCamposBD>                
<ListaAgrupamento>                   
<FinAgrupamentoParamsProc>  
<CodColigada>1</CodColigada>  
<IdBoleto>10542</IdBoleto>    
<Vencimento>2018-09-09T00:00:00</Vencimento>                                                      
</FinAgrupamentoParamsProc>  
</ListaAgrupamento>  
</FinBoletoParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
