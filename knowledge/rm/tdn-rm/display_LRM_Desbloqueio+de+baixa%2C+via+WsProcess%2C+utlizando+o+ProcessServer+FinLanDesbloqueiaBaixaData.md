---
content_hash: 1983c6d27ac38c40d9c08db39279ef4121e1e07c18a10b91176485782e8c4d60
fetched_at: '2026-06-29T00:09:55.817574+00:00'
page_id: '450152915'
product: rm
source: tdn-rm
title: Desbloqueio de baixa, via WsProcess, utlizando o ProcessServer FinLanDesbloqueiaBaixaData
type: documentation
url: https://tdn.totvs.com/display/LRM/Desbloqueio+de+baixa%2C+via+WsProcess%2C+utlizando+o+ProcessServer+FinLanDesbloqueiaBaixaData
version: 3
---

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinLanDesbloqueiaBaixaData</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams>  
<![CDATA[                      
<RMSParamsProc>

<Context>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODSISTEMA>F</CODSISTEMA>  
</Context>                                  
<PrimaryKeyList>1|13563</PrimaryKeyList>                                
<CodUsuario>mestre</CodUsuario>  
</RMSParamsProc>]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
