---
content_hash: 0d675e139054b31b71c438dc5fb53b9e9186b84c0d2f62a190d4a092d3427388
fetched_at: '2026-06-29T00:09:55.812668+00:00'
page_id: '450152904'
product: rm
source: tdn-rm
title: Cancelamento de Baixa, utilizado o processServer FinLanBaixaCancelamentoData
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+Baixa%2C+utilizado+o+processServer+FinLanBaixaCancelamentoData
version: 4
---

## **Exemplo de cancelamento de todas as baixas realizada para o lançamento 12929:**

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinLanBaixaCancelamentoData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams>  
<![CDATA[<FinLanCancelamentoBaixaParamsProc>

<Context>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODSISTEMA>F</CODSISTEMA>  
</Context>

<CodUsuario>mestre</CodUsuario>   
<Origem>Baixa</Origem>  
<DescompensarExtrato>false</DescompensarExtrato>   
<DataCancelamento>2016-05-05T00:00:00</DataCancelamento>  
<CodSistema>F</CodSistema>   
<TipoCancelamentoBaixaExtrato>CancelaSomenteItensSelecionados</TipoCancelamentoBaixaExtrato>   
<ListIdlanIdBaixa>  
<FinLanBaixaPKPar>  
<CodColigada>1</CodColigada>  
<IdLan>12929</IdLan>   
</FinLanBaixaPKPar>   
</ListIdlanIdBaixa>  
</FinLanCancelamentoBaixaParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
