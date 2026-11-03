---
content_hash: 62fdfd1f3a1476472777f44f3837cf73b58310f6c196f39fe261af0d839da9e5
fetched_at: '2026-06-29T00:09:04.064197+00:00'
page_id: '382547177'
product: rm
source: tdn-rm
title: 3225795 FINANCEIRO01-7832 DT Baixa Web Service
type: documentation
url: https://tdn.totvs.com/display/LRM/3225795+FINANCEIRO01-7832+DT+Baixa+Web+Service
version: 1
---

# Baixa WebService

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa - WebService |
| **Situação/Requisito:** | Não é possível informar as tabelas opcionais ao utilizar a baixa web service. |
| **Solução/Implementação:** | Adicionado as propriedades CodTb1Flx, CodTb2Flx, CodTb3Flx, CodTb4Flx, CodTb5Flx a classe de parâmetros FinTBCBaixaParamsProc que é utilizada para baixa via Web Service. Dessa forma, pode ser alterada a tabela opcional ao executar a baixa.  <FinTBCBaixaParamsProc> <CodColigada>1</CodColigada>  <DataBaixa>2016-09-16</DataBaixa>  <CodMoeda>R$</CodMoeda>  <HistoricoBaixa>Teste SOAP</HistoricoBaixa>  <UsarDataDefaultBaixa>false</UsarDataDefaultBaixa>  <TipoGeracaoExtratoBaixa>ExtratoParaCadaLancamento</TipoGeracaoExtratoBaixa> <CodUsuario>mestre</CodUsuario>  <Lancamentos>  <FinTBCBaixaLancamento> <CampoAlfaOp1>100</CampoAlfaOp1> <CodTb1Flx>200</CodTb1Flx> <CodTb3Flx>300</CodTb3Flx>  <CodColigada>1</CodColigada>  <IdLan>13034</IdLan>  <Pagamentos>  <FinTBCBaixaPagamento>  <CodColigada>1</CodColigada> <IdFormaPagamento>007</IdFormaPagamento> <IdPagto>1</IdPagto>  <Valor>150</Valor>  <CodColCxa>1</CodColCxa>  <CodCxa>0001</CodCxa> </FinTBCBaixaPagamento> </Pagamentos> </FinTBCBaixaLancamento>   </FinTBCBaixaParamsProc> |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000040. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
