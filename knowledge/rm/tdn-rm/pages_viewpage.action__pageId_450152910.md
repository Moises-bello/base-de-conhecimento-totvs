---
content_hash: 9a75761daca674120fd8447146b4c2831c6bd582a3627695faaa8de40d8b5e74
fetched_at: '2026-06-29T00:09:55.815310+00:00'
page_id: '450152910'
product: rm
source: tdn-rm
title: Cancelamento apenas do id de baixa informado 1278 do lançamento 12930
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152910
version: 3
---

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
<IdLan>12930</IdLan>  
<idbaixa>1278</idbaixa>   
</FinLanBaixaPKPar>   
</ListIdlanIdBaixa>  
</FinLanCancelamentoBaixaParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
