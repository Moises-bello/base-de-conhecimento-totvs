---
content_hash: 958b2b686a9168f7f52432258082e571926ce427ef94ab931e24dcf9a0b1e36c
fetched_at: '2026-06-29T00:09:45.458574+00:00'
page_id: '433250912'
product: rm
source: tdn-rm
title: DT Vínculo via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433250912
version: 3
---

# Realizar vínculo via WebService no Gestão Financeira

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Vínculo | Vincular Lançamentos. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Baixar Lançamentos | Baixar Lançamento | |
| **Cadastros Iniciais:** | Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito. |
| **Parâmetro(s):** | Informe os parâmetros utilizados. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-9068> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | FLAN |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Possibilidade de criar vínculo com lançamentos de devolução, nota de crédito e de nota de crédito de adiantamento através de Web Services.

## Procedimento para Utilização

Preencher o xml de acordo com as informações.

RMSDataProcess para inclusão de vínculo: **FinInclusaoVinculoTBCData**

RMSDataProcess para inclusão de vínculo: **FinExclusaoVinculoTBCData**

#### Realizando o Vínculo

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
 <soapenv:Header/>  
 <soapenv:Body>  
 <tot:ExecuteWithParams>  
 <!--Optional:-->  
 <tot:ProcessServerName>FinInclusaoVinculoTBCData</tot:ProcessServerName>  
 <!--Optional:-->  
 <tot:strXmlParams>  
 <![CDATA[<FinInclusaoVinculoTBCParamsProc>  
 <Coligada>1</Coligada>  
 <CodUsuario>mestre</CodUsuario>  
 <ExibirLogComoExcecao>true</ExibirLogComoExcecao>  
 <ListaVinculos>  
 <FinLancamentoTBCParamsProc>

<ReferenciaLancamento>6961</ReferenciaLancamento>  
 <TipodoVinculo>VinculoDevolucao</TipodoVinculo>  
 <ListaLancamentosASeremVinculados>  
 <FinLancamentoASerVinculadoTBCParamsProc>  
 <ReferenciaLancamentoASerVinculado>6960</ReferenciaLancamentoASerVinculado>  
 <ValordoVinculo>300</ValordoVinculo>  
 </FinLancamentoASerVinculadoTBCParamsProc>  
 </ListaLancamentosASeremVinculados>  
 </FinLancamentoTBCParamsProc>  
 </ListaVinculos>  
</FinInclusaoVinculoTBCParamsProc>]]>  
 </tot:strXmlParams>  
 </tot:ExecuteWithParams>  
 </soapenv:Body>  
</soapenv:Envelope>

#### Desfazendo o Vínculo

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
 <soapenv:Header/>  
 <soapenv:Body>  
 <tot:ExecuteWithParams>  
 <!--Optional:-->  
 <tot:ProcessServerName>FinExclusaoVinculoTBCData</tot:ProcessServerName>  
 <!--Optional:-->  
 <tot:strXmlParams>  
 <![CDATA[<FinExlusaoVinculoTBCParamsProc>  
 <Coligada>1</Coligada>  
 <CodUsuario>mestre</CodUsuario>  
 <ExibirLogComoExcecao>true</ExibirLogComoExcecao>  
 <ListaVinculos>  
 <FinVinculoTBCParamsProc>   
 <ReferenciaLancamento>6961</ReferenciaLancamento>  
 <TipodoVinculo>VinculoDevolucao</TipodoVinculo>  
 <ReferenciaLancamentoVinculado>6960</ReferenciaLancamentoVinculado>  
 </FinVinculoTBCParamsProc>  
 </ListaVinculos>  
</FinExlusaoVinculoTBCParamsProc>]]>  
 </tot:strXmlParams>  
 </tot:ExecuteWithParams>  
 </soapenv:Body>  
</soapenv:Envelope>

### Exemplos com vários (des)vínculos por vez:

### Fazer vários Vínculos

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
 <soapenv:Header/>  
 <soapenv:Body>  
 <tot:ExecuteWithParams>  
 <!--Optional:-->  
 <tot:ProcessServerName>FinInclusaoVinculoTBCData</tot:ProcessServerName>  
 <!--Optional:-->  
 <tot:strXmlParams>  
 <![CDATA[<FinInclusaoVinculoTBCParamsProc>

<Coligada>1</Coligada>  
 <CodUsuario>mestre</CodUsuario>  
 <ExibirLogComoExcecao>true</ExibirLogComoExcecao>  
 <ListaVinculos>  
 <FinLancamentoTBCParamsProc>

<ReferenciaLancamento>14421</ReferenciaLancamento>  
 <TipodoVinculo>VinculoDevolucao</TipodoVinculo>  
 <ListaLancamentosASeremVinculados>  
 <FinLancamentoASerVinculadoTBCParamsProc>  
 <ReferenciaLancamentoASerVinculado>14422</ReferenciaLancamentoASerVinculado>  
 <ValordoVinculo>100</ValordoVinculo>  
 </FinLancamentoASerVinculadoTBCParamsProc>  
 </ListaLancamentosASeremVinculados>

</FinLancamentoTBCParamsProc>  
 </ListaVinculos>  
</FinInclusaoVinculoTBCParamsProc>]]>

</tot:strXmlParams>  
 </tot:ExecuteWithParams>  
 </soapenv:Body>  
</soapenv:Envelope>

### Desfazer vários Vínculos

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
 <soapenv:Header/>  
 <soapenv:Body>  
 <tot:ExecuteWithParams>  
 <!--Optional:-->  
 <tot:ProcessServerName>FinExclusaoVinculoTBCData</tot:ProcessServerName>  
 <!--Optional:-->  
 <tot:strXmlParams>  
 <![CDATA[<FinExlusaoVinculoTBCParamsProc>

<Coligada>1</Coligada>  
 <CodUsuario>mestre</CodUsuario>  
 <ExibirLogComoExcecao>true</ExibirLogComoExcecao>  
 <ListaVinculos>  
 <FinVinculoTBCParamsProc>

<ReferenciaLancamento>14421</ReferenciaLancamento>  
 <TipodoVinculo>VinculoDevolucao</TipodoVinculo>  
 <ReferenciaLancamentoVinculado>14422</ReferenciaLancamentoVinculado>

</FinVinculoTBCParamsProc>

<FinVinculoTBCParamsProc>

<ReferenciaLancamento>144121</ReferenciaLancamento>  
 <TipodoVinculo>VinculoDevolucao</TipodoVinculo>  
 <ReferenciaLancamentoVinculado>14422</ReferenciaLancamentoVinculado>

</FinVinculoTBCParamsProc>  
 </ListaVinculos>  
</FinExlusaoVinculoTBCParamsProc>]]>

</tot:strXmlParams>  
 </tot:ExecuteWithParams>  
 </soapenv:Body>  
</soapenv:Envelope>

## Vídeo

250
