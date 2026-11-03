---
content_hash: e300230539fe6dda4e5e2cb6376089898c6b88aec3f8f00e090d678bbadeec39
fetched_at: '2026-06-29T00:09:17.794685+00:00'
page_id: '421388652'
product: rm
source: tdn-rm
title: Baixa de 2 Lançamentos, utilizando valores alfa opcionais diferentes para cada
  lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388652
version: 13
---

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header/>  
<soapenv:Body>  
<tot:ExecuteWithParams>  
<!--Optional:-->  
<tot:ProcessServerName>FinTBCBaixaDataProcess</tot:ProcessServerName>  
<!--Optional:-->  
<tot:strXmlParams>  
<![CDATA[  
<FinTBCBaixaParamsProc>

<Context>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODSISTEMA>F</CODSISTEMA>  
</Context>  
<CodColigada>1</CodColigada>   
<DataBaixa>2016-09-16</DataBaixa>   
<CodMoeda>R$</CodMoeda>   
<HistoricoBaixa>Teste SOAP</HistoricoBaixa>   
<UsarDataDefaultBaixa>false</UsarDataDefaultBaixa>   
<TipoGeracaoExtratoBaixa>ExtratoParaCadaLancamento</TipoGeracaoExtratoBaixa>  
<CodUsuario>mestre</CodUsuario>   
<Lancamentos>   
<FinTBCBaixaLancamento>  
<CampoAlfaOp1>100</CampoAlfaOp1>  
<CampoAlfaOp2>200</CampoAlfaOp2>  
<CampoAlfaOp3>300</CampoAlfaOp3>   
<CodColigada>1</CodColigada>   
<IdLan>13034</IdLan>   
<Pagamentos>   
<FinTBCBaixaPagamento>   
<CodColigada>1</CodColigada>  
<IdFormaPagamento>007</IdFormaPagamento>  
<IdPagto>1</IdPagto>   
<Valor>150</Valor>   
<CodColCxa>1</CodColCxa>   
<CodCxa>0001</CodCxa>  
</FinTBCBaixaPagamento>  
</Pagamentos>  
</FinTBCBaixaLancamento>   
<FinTBCBaixaLancamento>  
<CampoAlfaOp1>400</CampoAlfaOp1>  
<CampoAlfaOp2>500</CampoAlfaOp2>  
<CampoAlfaOp3>600</CampoAlfaOp3>   
<CodColigada>1</CodColigada>   
<IdLan>13035</IdLan>  
<Pagamentos>   
<FinTBCBaixaPagamento>  
<CodColigada>1</CodColigada>  
<IdFormaPagamento>011</IdFormaPagamento>  
<IdPagto>5</IdPagto>   
<Valor>200</Valor>   
<CodColCxa>1</CodColCxa>   
<CodCxa>0001</CodCxa>  
</FinTBCBaixaPagamento>  
</Pagamentos>   
</FinTBCBaixaLancamento>   
</Lancamentos>   
</FinTBCBaixaParamsProc>   
]]>  
</tot:strXmlParams>  
</tot:ExecuteWithParams>  
</soapenv:Body>  
</soapenv:Envelope>
