---
content_hash: fa3ea362414811d6566a9ce3d5310bc067a020f618f7860c129810368834d353
fetched_at: '2026-06-29T00:10:33.320995+00:00'
page_id: '528470363'
product: rm
source: tdn-rm
title: Baixa de lançamento utilizando o método 'ExecuteWithXmlParams'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528470363
version: 4
---

Exemplo de Baixa via Web service utilizando o método ExecuteWithXmlParams:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
<soapenv:Header />  
<soapenv:Body>  
<tot:ExecuteWithXmlParams xmlns:tot="<http://www.totvs.com/>">  
<tot:ProcessServerName>FinTBCBaixaDataProcess</tot:ProcessServerName>  
<tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-8"?>  
<FinTBCBaixaParamsProc xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">  
<ActionModule xmlns="http://www.totvs.com/">F</ActionModule>  
<ActionName xmlns="http://www.totvs.com/">FinTBCBaixaAction</ActionName>  
<CanParallelize xmlns="http://www.totvs.com/">true</CanParallelize>  
<CanSendMail xmlns="http://www.totvs.com/">false</CanSendMail>  
<CanWaitSchedule xmlns="http://www.totvs.com/">false</CanWaitSchedule>  
<CodUsuario xmlns="http://www.totvs.com/">mestre</CodUsuario>  
<ConnectionId i:nil="true" xmlns="<http://www.totvs.com/>" />  
<ConnectionString i:nil="true" xmlns="<http://www.totvs.com/>" />  
<Context xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>">  
<a:\_params xmlns:b="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODCOLIGADA</b:Key>  
<b:Value i:type="c:int" xmlns:c="http://www.w3.org/2001/XMLSchema">1</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODSISTEMA</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">F</b:Value>  
</b:KeyValueOfanyTypeanyType>  
<b:KeyValueOfanyTypeanyType>  
<b:Key i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">$CODUSUARIO</b:Key>  
<b:Value i:type="c:string" xmlns:c="http://www.w3.org/2001/XMLSchema">mestre</b:Value>  
</b:KeyValueOfanyTypeanyType>  
</a:\_params>  
<a:Environment>DotNet</a:Environment>  
</Context>

<PrimaryKeyList xmlns:d2p1='<http://schemas.microsoft.com/2003/10/Serialization/Arrays>' xmlns='<http://www.totvs.com/>'>  
<d2p1:ArrayOfanyType>  
<d2p1:anyType xmlns:d4p1='<http://www.w3.org/2001/XMLSchema>' i:type='d4p1:short'>1</d2p1:anyType>  
<d2p1:anyType xmlns:d4p1='<http://www.w3.org/2001/XMLSchema>' i:type='d4p1:int'>22752</d2p1:anyType>  
</d2p1:ArrayOfanyType>  
</PrimaryKeyList>  
<PrimaryKeyNames xmlns:d2p1='<http://schemas.microsoft.com/2003/10/Serialization/Arrays>' xmlns='<http://www.totvs.com/>'>  
<d2p1:string>CODCOLIGADA</d2p1:string>  
<d2p1:string>IDLAN</d2p1:string>  
</PrimaryKeyNames>  
<CodColigada>1</CodColigada>  
<CodMoeda>R$</CodMoeda>  
<CodUsuario>mestre</CodUsuario>  
<ContabilizarPosBaixa>false</ContabilizarPosBaixa>  
<CotacaoBaixa>0</CotacaoBaixa>  
<DataBaixa>2019-12-19</DataBaixa>  
<Lancamentos>  
<FinTBCBaixaLancamento>

<CampoAlfaOp1>teste</CampoAlfaOp1>  
<CodColigada>1</CodColigada>

<CodTb1Flx>01</CodTb1Flx>

<DataOp1>2025-11-24</DataOp1>  
<IdLan>22752</IdLan>  
<Pagamentos>  
<FinTBCBaixaPagamento>  
<CodColCxa>1</CodColCxa>  
<CodColigada>1</CodColigada>  
<CodCxa>0004</CodCxa>  
<Contabilizacao>  
<FinTBCBaixaContabilizacao />  
</Contabilizacao>  
<IdFormaPagamento>1</IdFormaPagamento>  
<IdPagto>1</IdPagto>  
<Valor>100</Valor>  
</FinTBCBaixaPagamento>  
</Pagamentos>  
<ValorDesconto>0</ValorDesconto>  
<ValorJuros>0</ValorJuros>  
<ValorMulta>0</ValorMulta>

<ValorOp1>0</ValorOp1>  
</FinTBCBaixaLancamento>  
</Lancamentos>  
<TipoGeracaoExtratoBaixa>ExtratoParaCadaLancamento</TipoGeracaoExtratoBaixa>  
<UsarDataDefaultBaixa>false</UsarDataDefaultBaixa>  
<UsarDataVencimentoBaixa>false</UsarDataVencimentoBaixa>

</FinTBCBaixaParamsProc>]]></tot:strXmlParams>  
</tot:ExecuteWithXmlParams>  
</soapenv:Body>  
</soapenv:Envelope>
