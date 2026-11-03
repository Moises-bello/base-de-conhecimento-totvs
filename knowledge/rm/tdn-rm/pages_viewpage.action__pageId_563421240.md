---
content_hash: 20082a74442e3e4d7a737899dc48b6429ffaf5cbb13812140f3d693012303fcd
fetched_at: '2026-06-29T00:10:50.774715+00:00'
page_id: '563421240'
product: rm
source: tdn-rm
title: Baixa de lançamento utilizando o método 'ExecuteWithParams'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563421240
version: 19
---

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
<DataBaixa>2025-11-27</DataBaixa>  
<CodMoeda>R$</CodMoeda>  
<HistoricoBaixa>Teste</HistoricoBaixa>  
<CotacaoBaixa></CotacaoBaixa>  
<UsarDataVencimentoBaixa></UsarDataVencimentoBaixa>  
<UsarDataDefaultBaixa>false</UsarDataDefaultBaixa>  
<TipoGeracaoExtratoBaixa>ExtratoParaCadaLancamento</TipoGeracaoExtratoBaixa>  
<ContabilizarPosBaixa>false</ContabilizarPosBaixa>  
<CodUsuario>mestre</CodUsuario>  
<ValidaDataBaixaFeriadoFimDeSemana>true</ValidaDataBaixaFeriadoFimDeSemana>  
<Lancamentos>   
<FinTBCBaixaLancamento>  
<CodColigada>1</CodColigada>  
<IdLan>7673</IdLan>  
<ValorJuros></ValorJuros>  
<ValorDesconto></ValorDesconto>  
<ValorMulta></ValorMulta>  
<ValorOp1></ValorOp1>  
<ValorOp2></ValorOp2>  
<ValorOp3></ValorOp3>  
<ValorOp4></ValorOp4>  
<ValorOp5></ValorOp5>  
<ValorOp6></ValorOp6>  
<ValorOp7></ValorOp7>  
<ValorOp8></ValorOp8>  
<DataOp1>2025-11-27T00:00:00</DataOp1>  
<DataOp2></DataOp2>  
<DataOp3></DataOp3>  
<DataOp4></DataOp4>  
<DataOp5></DataOp5>  
<Pagamentos>   
<FinTBCBaixaPagamento>  
<CodColigada>1</CodColigada>  
<IdFormaPagamento>1</IdFormaPagamento>  
<IdPagto>1</IdPagto>  
<Valor>1000</Valor>  
<CodColCxa>1</CodColCxa>  
<CodCxa>0008</CodCxa>  
<DataCompensacaoExtrato></DataCompensacaoExtrato>  
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

**Observações:**

* Quando o parâmetro utilizado para validar configuração de baixa de lançamento inerente a Final de Semana e Feriado for usado no sistema, basta informar a tag: **<ValidaDataBaixaFeriadoFimDeSemana>true</ValidaDataBaixaFeriadoFimDeSemana>** conforme estrutura acima.
* Quando desejado que a data de compensação de extrato seja diferente da data de baixa, deverá ser informada a tag:   
  **<DataCompensacaoExtrato> </DataCompensacaoExtrato>**, passando como valor a data no formato yyyy-mm-dd e  
  e o parâmetro "Gerar Extrato Compensado na Baixa" deve estar marcado. Caso contrário, mesmo que passe a tag, o valor passado   
  não será utilizado e a data de compensação de extrato continuará sendo a mesma que a data da baixa.  
    
  [Menu Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Pagar > Etapa Baixa 1/6]  
    
    
    
  [Menu Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber > Etapa Baixa 1/6]

```

```
