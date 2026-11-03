---
content_hash: 36950ad8cd2c5c66f5c1d9a73e47b82522800db3b5465f5fd181e48f896a0a36
fetched_at: '2026-06-29T00:09:17.761635+00:00'
page_id: '421388640'
product: rm
source: tdn-rm
title: Estrutura XML para inclusão de Boleto Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388640
version: 9
---

A estrutura XML abaixo é um exemplo para uso do Web Service utilizando o wsProcess do TBC. Será utilizado o Processserver **FinBoletoInclusaoTBCData** para inclusão de boleto com registro online.

O Processserver foi substituído:

De "**FinBoletoInclusaoData**"

Para " **FinBoletoInclusaoTBCData** "

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
   <soapenv:Header/>  
   <soapenv:Body>  
      <tot:**ExecuteWithParams**>  
         <!--Optional:-->  
         <tot:ProcessServerName>**FinBoletoInclusaoTBCData**</tot:ProcessServerName>  
         <!--Optional:-->  
         <tot:strXmlParams>

<![CDATA[  
<FinBoletoParamsProc>  
  <CodUsuario>MESTRE</CodUsuario>  
  <CNABAceite>0</CNABAceite>  
  <CNABComando>11</CNABComando>  
  <CNABInstrucao1>1</CNABInstrucao1>  
  <CNABInstrucao2>2</CNABInstrucao2>  
  <CNABInstrucao3>3</CNABInstrucao3>  
  <CodColCxa>01</CodColCxa>  
  <CodColigada>01</CodColigada>  
  <CodCxa>00017</CodCxa>  
  <DataInstrucao1>2017-10-30T00:00:00-03:00</DataInstrucao1>  
  <DataInstrucao2>2017-10-30T00:00:00-03:00</DataInstrucao2>  
  <DataInstrucao3>2017-10-30T00:00:00-03:00</DataInstrucao3>  
  <DataSistema>2017-10-25T00:00:00-03:00</DataSistema>  
  <DataVencimento>2017-10-30T00:00:00-03:00</DataVencimento>  
  <EspecieCNAB>02</EspecieCNAB>  
  <GerarBoletoParcial>false</GerarBoletoParcial>  
  <IdConvenio>18</IdConvenio>  
  <ListaAgrupamento>  
    <FinAgrupamentoParamsProc>  
                  <CodUsuario>MESTRE</CodUsuario>  
      <CodBarras>9999999</CodBarras>  
      <CodCliFor>RM</CodCliFor>  
      <CodColCliFor>0</CodColCliFor>  
      <CodColigada>01</CodColigada>  
      <ContraApresentacao>false</ContraApresentacao>  
      <FormaPagamento>01</FormaPagamento>  
      <IPTE>9999999</IPTE>  
      <IdBoleto>0</IdBoleto>  
      <IdConvenio>18</IdConvenio>  
      <IdLan>8516</IdLan>  
      <NomeCliFor>RM SISTEMAS</NomeCliFor>  
      <NossoNumero>140000000001217050</NossoNumero>  
      <SegundoNumero>0000000123</SegundoNumero>  
      <StatusBoleto>EmAberto</StatusBoleto>  
      <ValorBoleto>300</ValorBoleto>  
      <Vencimento>2017-10-30T00:00:00-03:00</Vencimento>  
    </FinAgrupamentoParamsProc>  
  </ListaAgrupamento>  
  <OpcaoGeracaoBoleto>UmBoletoParaCadaLancamentos</OpcaoGeracaoBoleto>  
  <QtdeDiasInstrucao1>1</QtdeDiasInstrucao1>  
  <QtdeDiasInstrucao2>1</QtdeDiasInstrucao2>  
  <QtdeDiasInstrucao3>1</QtdeDiasInstrucao3>  
  <RegistrarOnLineBoleto>true</RegistrarOnLineBoleto>  
  <TipoBoleto>BoletoCobranca</TipoBoleto>  
  <ValorParcial/>  
  <listaLan>  
    <FinLanBoletoParamsProc>  
      <CodCfo>RM</CodCfo>  
      <CodColCfo>0</CodColCfo>  
      <CodColigada>01</CodColigada>  
                  <CodSistema>F</CodSistema>  
      <DataVencimento>2017-08-09T00:00:00</DataVencimento>  
                <Idlan>8516</Idlan>  
      <NossoNumero>140000000001217050</NossoNumero>  
      <SegundoNumero>0000000123</SegundoNumero>  
      <ValorOriginal>300</ValorOriginal>  
    </FinLanBoletoParamsProc>  
  </listaLan>  
</FinBoletoParamsProc>  
]]>  
         </tot:strXmlParams>  
      </tot:ExecuteWithParams>  
   </soapenv:Body>  
</soapenv:Envelope>

**Observação:**

 As tags acima devem ser estruturadas em ordem alfabética, caso estejam fora da ordem, o processo não será concluído ou a tag fora da ordem não será processada.
