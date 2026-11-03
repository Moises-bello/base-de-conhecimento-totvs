---
content_hash: afaf2e9ba191434714ea41e4f276c3fd9740390eb0c4df288c7cd74d43541ae3
fetched_at: '2026-06-29T00:11:50.419694+00:00'
page_id: '840787356'
product: rm
source: tdn-rm
title: Baixa de lançamento com dados de cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840787356
version: 3
---

DataServer: FinTBCBaixaDataProcess

Necessário informar uma forma de pagamento que seja do tipo cartão no campo IdFormaPagamento

Os dados do cartão deve ser informado no nó <Cartao>

<Cartao>  
 <FinCartaoBaixaParamsProc>  
   <CartaoAutorizacao>35353535345345</CartaoAutorizacao>  
   <CartaoBandeira>1</CartaoBandeira>  
   <CartaoEstabelecimento>123456789012345</CartaoEstabelecimento>  
   <CartaoNsu>2423423423</CartaoNsu>  
   <CartaoNumParcela>1</CartaoNumParcela>  
   <CartaoOperadora>7</CartaoOperadora>  
   <CartaoTid>34535345345345</CartaoTid>  
   <IdPagto>1</IdPagto>  
  </FinCartaoBaixaParamsProc>  
</Cartao>

Valores para bandeira <CartaoBandeira>

    1 - Visa  
    2 - Master  
    3 - ELO  
    4 - Dinners  
    5 - AmericanExpress  
    6 - Aura  
    7 - JCB  
    8 - Discover  
    9 - Hipercard  
    10 - Credz  
    11 - Cabal  
    12 - CrediShop  
    13 - SoroCred

Valores para operadora <CartaoOperadora>

    1 - Cielo,  
    2 - Rede,  
    3 - GetNet  
    7 - Adyen  
    8 - Amex  
    9 - SafraPay  
    10 - Stone  
    11 - Elavon  
    13 - Sicredi

Abaixo exemplo do XML usado via soapUI

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
    <soapenv:Header/>  
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
<DataBaixa>2024-04-29</DataBaixa>  
<Cartao>  
 <FinCartaoBaixaParamsProc>  
   <CartaoAutorizacao>35353535345345</CartaoAutorizacao>  
   <CartaoBandeira>1</CartaoBandeira>  
   <CartaoEstabelecimento>123456789012345</CartaoEstabelecimento>  
   <CartaoNsu>2423423423</CartaoNsu>  
   <CartaoNumParcela>1</CartaoNumParcela>  
   <CartaoOperadora>7</CartaoOperadora>  
   <CartaoTid>34535345345345</CartaoTid>  
   <IdPagto>1</IdPagto>  
  </FinCartaoBaixaParamsProc>  
</Cartao>  
<Lancamentos>  
    <FinTBCBaixaLancamento>  
        <CodColigada>1</CodColigada>  
        <IdLan>61955</IdLan>  
        <Pagamentos>  
            <FinTBCBaixaPagamento>  
                <CodColCxa>1</CodColCxa>  
                <CodColigada>1</CodColigada>  
                <CodCxa>0021</CodCxa>  
                <Contabilizacao>  
                    <FinTBCBaixaContabilizacao />  
                </Contabilizacao>  
                <IdFormaPagamento>5</IdFormaPagamento>  
                <IdPagto>1</IdPagto>  
                <Valor>1000</Valor>  
            </FinTBCBaixaPagamento>  
        </Pagamentos>  
        <ValorDesconto>0</ValorDesconto>  
        <ValorJuros>0</ValorJuros>  
        <ValorMulta>0</ValorMulta>  
    </FinTBCBaixaLancamento>  
</Lancamentos>  
<TipoGeracaoExtratoBaixa>ExtratoParaCadaLancamento</TipoGeracaoExtratoBaixa>  
<UsarDataDefaultBaixa>false</UsarDataDefaultBaixa>  
<UsarDataVencimentoBaixa>false</UsarDataVencimentoBaixa>

</FinTBCBaixaParamsProc>]]></tot:strXmlParams>  
        </tot:ExecuteWithXmlParams>  
    </soapenv:Body>  
</soapenv:Envelope>
