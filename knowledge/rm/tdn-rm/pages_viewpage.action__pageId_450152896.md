---
content_hash: d9d955488d19fe082e2f7dff91300a3702272737a1ccac71347069af8cb6b5aa
fetched_at: '2026-06-29T00:09:55.810039+00:00'
page_id: '450152896'
product: rm
source: tdn-rm
title: Baixa de 2 Lançamentos, Três Meios de Pagamento. Um extrato para cada lançamento
  e contabilização através de tabela opcional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152896
version: 6
---

## **(http://localhost:8051/wsProcess/IwsProcess)**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>"  
                  xmlns:tot="<http://www.totvs.com/>">  
    <soapenv:Header/>  
    <soapenv:Body>  
        <tot:ExecuteWithParams>  
            <!--Optional:-->  
            <tot:ProcessServerName>FinLanBaixaTBCData</tot:ProcessServerName>  
            <!--Optional:-->  
            <tot:strXmlParams>  
<![CDATA[  
<FinLanBaixaTBCParamsProc>  
<Context>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODSISTEMA>F</CODSISTEMA>  
</Context>

   <CodColigada>1</CodColigada>  
    <CodUsuario>Mestre</CodUsuario>  
    <DataBaixa>2014-02-28</DataBaixa>  
    <DataSistema>2014-02-28</DataSistema>  
    <CodMoeda>R$</CodMoeda>  
    <HistoricoBaixa/>  
    <CotacaoBaixa>0</CotacaoBaixa>  
    <UsarDataVencimentoBaixa>false</UsarDataVencimentoBaixa>  
    <TipoGeracaoExtrato>ExtratoParaCadaLancamento</TipoGeracaoExtrato>  
    <ContabilizarPosBaixa>false</ContabilizarPosBaixa>  
    <Pagamentos>  
        <FinPagamentoBaixaTBCParamsProc>  
            <ListIdLan>  
                <int>12929</int>  
                <int>12930</int>  
            </ListIdLan>  
            <MeioPagamento>  
                <Cheque/>  
                <CodColigada>1</CodColigada>  
                <IdFormaPagto>1</IdFormaPagto>  
                <Valor>30,00</Valor>  
                <CodColCxa>1</CodColCxa>  
                <CodCxa>0002</CodCxa>  
            </MeioPagamento>  
        </FinPagamentoBaixaTBCParamsProc>  
    </Pagamentos>  
    <Pagamentos>  
        <FinPagamentoBaixaTBCParamsProc>  
            <ListIdLan>  
                <int>12929</int>  
            </ListIdLan>  
            <MeioPagamento>  
                <Cheque/>  
                <Cartao>  
                    <FinCartaoBaixaParamsProc>  
                        <CartaoAutorizacao>35353535345345</CartaoAutorizacao>  
                        <CartaoBandeira>1</CartaoBandeira>  
                        <CartaoNsu>2423423423</CartaoNsu>  
                        <CartaoNumParcela>1</CartaoNumParcela>  
                        <CartaoOperadora>7</CartaoOperadora>  
                        <CartaoTid>34535345345345</CartaoTid>  
                        <IdPagto>1</IdPagto>  
                    </FinCartaoBaixaParamsProc>  
                </Cartao>  
                <CodColigada>1</CodColigada>  
                <IdFormaPagto>4</IdFormaPagto>  
                <Valor>60,00</Valor>  
                <CodColCxa>1</CodColCxa>  
                <CodCxa>0002</CodCxa>  
            </MeioPagamento>  
        </FinPagamentoBaixaTBCParamsProc>  
    </Pagamentos>  
    <ValoresAlteracao>  
        <FinValoresAlteracaoTBCParamsProc>  
            <CodColigada>1</CodColigada>  
            <IdLan>12930</IdLan>  
            <ValorJuros>2,00</ValorJuros>  
            <ValorDesconto>5,00</ValorDesconto>  
            <ValorMulta>6,00</ValorMulta>  
        </FinValoresAlteracaoTBCParamsProc>  
    </ValoresAlteracao>  
</FinLanBaixaTBCParamsProc>  
]]></tot:strXmlParams>  
        </tot:ExecuteWithParams>  
    </soapenv:Body>  
</soapenv:Envelope>

**Obs.:**

**Tags de meios de pagamento:**

Neste exemplo de tag de <pagamento> foi informado duas referência de lançamento: (8930 e 8931) e o valor de baixa 30,00. Ao executar o serviço o valor será proporcionalizado para os dois lançamentos por estar na mesma tag de <pagamentos>.   
Ou seja, será realizado uma baixa para cada lançamento no valor de 15,00. Os valores podem ser alterados mediante particularidades de cada lançamento, juros, multa, desconto, tributos etc.

<Pagamentos>  
    <FinPagamentoBaixaTBCParamsProc>  
        <ListIdLan>  
            <int>8930</int>  
            <int>8931</int>  
        </ListIdLan>  
        <MeioPagamento>  
            <Cheque/>  
            <CodColigada>1</CodColigada>  
            <IdFormaPagto>1</IdFormaPagto>  
            <Valor>30</Valor>  
            <CodColCxa>1</CodColCxa>  
            <CodCxa>0002</CodCxa>  
        </MeioPagamento>  
    </FinPagamentoBaixaTBCParamsProc>  
</Pagamentos>

Na tag abaixo foi informado apenas uma referência de lançamento: (8932) e o valor de baixa 60, então será realizada apenas uma baixa no valor de 60,00:

<Pagamentos>  
    <FinPagamentoBaixaTBCParamsProc>  
        <ListIdLan>  
            <int>8932</int>  
        </ListIdLan>  
        <MeioPagamento>  
            <Cheque/>  
            <CodColigada>1</CodColigada>  
            <IdFormaPagto>4</IdFormaPagto>  
            <Valor>60</Valor>  
            <CodColCxa>1</CodColCxa>  
            <CodCxa>0002</CodCxa>  
        </MeioPagamento>  
    </FinPagamentoBaixaTBCParamsProc>  
</Pagamentos>

**Tags valores de alteração**

Na tag abaixo será adicionado apenas para a referência de lançamento (8930) o valor informado nas tags de valor de juros, valor de desconto e valor de multa:

<ValoresAlteracao>  
    <FinValoresAlteracaoTBCParamsProc>  
        <CodColigada>1</CodColigada>  
        <IdLan>8930</IdLan>  
        <ValorJuros>2</ValorJuros>  
        <ValorDesconto>5</ValorDesconto>  
        <ValorMulta>6</ValorMulta>  
    </FinValoresAlteracaoTBCParamsProc>  
</ValoresAlteracao>

**Tags dado do cartão**

Os dados do cartão devem ficar dentro da TAG <MeioPagamento>

 <Cartao>  
    <FinCartaoBaixaParamsProc>  
        <CartaoAutorizacao>35353535345345</CartaoAutorizacao>  
        <CartaoBandeira>1</CartaoBandeira>  
        <CartaoNsu>2423423423</CartaoNsu>  
        <CartaoNumParcela>1</CartaoNumParcela>  
        <CartaoOperadora>7</CartaoOperadora>  
        <CartaoTid>34535345345345</CartaoTid>  
        <IdPagto>1</IdPagto>  
    </FinCartaoBaixaParamsProc>  
</Cartao>
