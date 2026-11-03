---
content_hash: f001e10b388f960d36cb9f94c66779e693dd3c2e394a8daec80b3260d682fb95
fetched_at: '2026-06-29T00:08:25.767951+00:00'
page_id: '270925808'
product: rm
source: tdn-rm
title: RMEDU00003_WebService - Geração de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270925808
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.14 |
| **Observações:** | WebService |

Como configura o WebService e Obter as chaves primarias.

[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=189307798)

Após configurar o ambiente acessar o link abaixo e validar a conexão

<http://localhost:8051/wsPageIndex/>

Onde Localhost deve ser igual ao servidor onde o WebService foi configurado

Ao acessar o Link a tela abaixo deve ser exibida

Clicar na Opção Processos

A tela abaixo deve ser exibida

Testar o link de processo no Soap Ui

**Para consumir os WebServices, utilize um aplicativo que faça uso do protocolo Soap nas chamadas. Indicamos o SoapUI.**

****Para baixar o software, [Clique aqui](https://sourceforge.net/projects/soapui/files/)****

Nomear o Novo Projeto e inserir o Link recuperado

<http://localhost:8051/wsProcess/MEX?wsdl>

Acessar opções RM\_IwsProcess | ExecuteWithXmlParams | Request1

Excluir o conteúdo apresentando na tela e informar o modelo abaixo.

O Codigo da Coligada e o Identificador da parcela são obrigatórios, itens identificados em vermelho no modelo abaixo.

.

Modelo de XML

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

   <soapenv:Header/>

   <soapenv:Body>

      <tot:ExecuteWithXmlParams>

         <!--Optional:-->

         <tot:ProcessServerName>EduGerarLancFromParcelaData</tot:ProcessServerName>

         <!--Optional:-->

         <tot:strXmlParams><![CDATA[<?xml version="1.0" encoding="utf-16"?>

<EduGeraLancParamsProc z:Id="i1" xmlns="<http://www.totvs.com.br/RM/>" xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:z="<http://schemas.microsoft.com/2003/10/Serialization/>">

  <ActionModule xmlns="<http://www.totvs.com/>">S</ActionModule>

  <ActionName xmlns="<http://www.totvs.com/>">EduGerarLancFromParcela</ActionName>

  <CodUsuario xmlns="<http://www.totvs.com/>">mestre</CodUsuario>

  <Context z:Id="i2" xmlns="<http://www.totvs.com/>" xmlns:a="<http://www.totvs.com.br/RM/>">

    <a:\_params xmlns:b="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$EXERCICIOFISCAL</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">22</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODLOCPRT</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">12</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODTIPOCURSO</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">1</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$EDUTIPOUSR</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">A</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODUNIDADEBIB</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">5</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODCOLIGADA</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">1</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$RHTIPOUSR</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">01</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODIGOEXTERNO</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">-1</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODSISTEMA</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">S</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODUSUARIOSERVICO</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>" />

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODUSUARIO</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">mestre</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$IDPRJ</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">2</b:Value>

      </b:KeyValueOfanyTypeanyType>

     <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CHAPAFUNCIONARIO</b:Key>

        <b:Value i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">00027</b:Value>

      </b:KeyValueOfanyTypeanyType>

      <b:KeyValueOfanyTypeanyType>

        <b:Key i:type="c:string" xmlns:c="<http://www.w3.org/2001/XMLSchema>">$CODFILIAL</b:Key>

        <b:Value i:type="c:int" xmlns:c="<http://www.w3.org/2001/XMLSchema>">1</b:Value>

      </b:KeyValueOfanyTypeanyType>

    </a:\_params>

    <a:Environment>DotNet</a:Environment>

  </Context>

  <PrimaryKeyList xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">

    <a:ArrayOfanyType>

      <a:anyType i:type="b:short" xmlns:b="<http://www.w3.org/2001/XMLSchema>">1</a:anyType>

      <a:anyType i:type="b:int" xmlns:b="<http://www.w3.org/2001/XMLSchema>">35223</a:anyType>

    </a:ArrayOfanyType>

  </PrimaryKeyList>

  <PrimaryKeyNames xmlns="<http://www.totvs.com/>" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>">

    <a:string>CODCOLIGADA</a:string>

    <a:string>IDPARCELA</a:string>

  </PrimaryKeyNames>

  <ClausulaFiltroRa i:nil="true" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

  <CodCurso i:nil="true" />

  <CodGrade i:nil="true" />

  <CodHabilitacao i:nil="true" />

  <CodSentencaSql i:nil="true" />

  <CodTurma i:nil="true" />

  <CodTurno>0</CodTurno>

  <ParamsGeraLanc z:Id="i3">

    <AgrupamentoBoleto i:nil="true" />

    <BoletoPorServico i:nil="true" />

    <CampoAlfaOp1 i:nil="true" />

    <CampoAlfaOp2 i:nil="true" />

    <CampoAlfaOp3 i:nil="true" />

    <CnabCarteira i:nil="true" />

    <CodCCusto i:nil="true" />

    <CodCfo i:nil="true" />

    <CodColCfo>0</CodColCfo>

    <CodColCxa i:nil="true" />

    <CodColCxaAPagar i:nil="true" />

    <CodColNatFinanceira i:nil="true" />

    <CodColigada>1</CodColigada>

    <CodColigadaConta>0</CodColigadaConta>

    <CodContrato i:nil="true" />

    <CodCxa i:nil="true" />

    <CodCxaAPagar i:nil="true" />

    <CodDepto i:nil="true" />

    <CodEvento i:nil="true" />

    <CodFilial>1</CodFilial>

    <CodMoeda i:nil="true" />

    <CodNatFinanceira i:nil="true" />

    <CodTabOp1 i:nil="true" />

    <CodTabOp2 i:nil="true" />

    <CodTabOp3 i:nil="true" />

    <CodTabOp4 i:nil="true" />

    <CodTabOp5 i:nil="true" />

    <CodTipoCurso>1</CodTipoCurso>

    <CodTipoDocumento i:nil="true" />

    <CodTipoDocumentoAPagar i:nil="true" />

    <CodUsuario>mestre</CodUsuario>

    <ContratoHabNull i:nil="true" />

    <CotaFinal i:nil="true" />

    <CotaInicial i:nil="true" />

    <DataCompetencia i:nil="true" />

    <DataFinal i:nil="true" />

    <DataInicial i:nil="true" />

    <DataOp1 i:nil="true" />

    <DataOp2 i:nil="true" />

    <DataOp3 i:nil="true" />

    <DataOp4 i:nil="true" />

    <DataOp5 i:nil="true" />

    <DataVencimento>0001-01-01T00:00:00</DataVencimento>

    <Historico i:nil="true" />

    <IncluirExcluirBolsaRetroativa>Inclusao</IncluirExcluirBolsaRetroativa>

    <IsIncluirExcluirBolsaRetroativa>false</IsIncluirExcluirBolsaRetroativa>

    <IsSimulaLancamento>false</IsSimulaLancamento>

    <ListaAlunos xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaContaCorrente />

    <ListaHabilitacaoFilial xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaIdParcela xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaPeriodoLetivo xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaPlanosPgto xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaServicos xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

    <ListaTipoContrato xmlns:a="<http://schemas.datacontract.org/2004/07/RM.Edu.Consts>" />

    <ListaTipoParcela xmlns:a="<http://schemas.datacontract.org/2004/07/RM.Edu.Consts>" />

    <NroConta i:nil="true" />

    <NumAgencia i:nil="true" />

    <NumAgenciaAPagar i:nil="true" />

    <NumBanco i:nil="true" />

    <NumBancoAPagar i:nil="true" />

    <OperacaoBolsaRetroativa i:nil="true" />

    <OrigemParcela i:nil="true" />

    <ParcelaFinal i:nil="true" />

    <ParcelaInicial i:nil="true" />

    <PermiteAtualizarContaCorrente>true</PermiteAtualizarContaCorrente>

    <TipoCob i:nil="true" />

    <TipoContaCaixa i:nil="true" />

    <TipoContabilLan i:nil="true" />

    <TipoContabilLanAPagar i:nil="true" />

    <TipoSelecaoParcela>IdParcela</TipoSelecaoParcela>

   <ValorBolsaRetroativa>0</ValorBolsaRetroativa>

    <ValorOriginal>0</ValorOriginal>

  </ParamsGeraLanc>

  <RA i:nil="true" />

  <SalvarParams>false</SalvarParams>

  <TipoFiltro>Nenhum</TipoFiltro>

 <ValorParamsConsultaSql i:nil="true" xmlns:a="<http://schemas.microsoft.com/2003/10/Serialization/Arrays>" />

</EduGeraLancParamsProc>]]></tot:strXmlParams>

      </tot:ExecuteWithXmlParams>

   </soapenv:Body>

</soapenv:Envelope>

Definir autenticação

Clicar na opção “Auth”

Inserir um usuário do sistema com acesso a geração de lançamentos “neste modelo utilizaremos o mestre”

Lançamento gerado com sucesso.
