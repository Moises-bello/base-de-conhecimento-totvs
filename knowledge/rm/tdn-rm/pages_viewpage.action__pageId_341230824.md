---
content_hash: a663223fc6157a8964f02a1bd81f0bb02b472b8a2689c3b925ea53d7fb436b70
fetched_at: '2026-06-29T00:08:52.611212+00:00'
page_id: '341230824'
product: rm
source: tdn-rm
title: 2283656 FISCAL01-3660 DT Envio da NF-e Rejeição Schema  tag vIss
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341230824
version: 1
---

# Envio da NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** |  |
| **Módulo:** | Informe o módulo. |
| **Função:** | Informe a função. |
| **Situação/Requisito:** | Ao enviar uma NF-e para Brasilia, onde a tributação é pelo ISS é apresentado a mensagem:  Não foi possível enviar a nota.    Enviar NF-e: Erro no envio da NF-e.    TSS - Erro na validação desta nota.    Motivo:Campo: vBC': Conteúdo do campo não obedece ao Esquema da NF-e. O valor '0.00' não é aceito pelo padrão estabelecido pela SEFAZ: '0\.[0-9]  {1}[1-9]{1}  |0\.[1-9]  {1}[0-9]{1}  |[1-9]  {1}[0-9]{0,12}(\.[0-9]{2})?'.  Campo: vBC': '0.00' is not a valid value of the atomic type '{<http://www.portalfiscal.inf.br/nfe}TDec_1302Opc>'.  Campo: vISS': Conteúdo do campo não obedece ao Esquema da NF-e. O valor '0.00' não é aceito pelo padrão estabelecido pela SEFAZ: '0\.[0-9]{1}  [1-9]  {1}|0\.[1-9]{1}  [0-9]  {1}|[1-9]{1}  [0-9]  {0,12}(\.[0-9]{2})?'.  Campo: vISS': '0.00' is not a valid value of the atomic type '{<http://www.portalfiscal.inf.br/nfe}TDec_1302Opc>'.      Mensagem Original:    Element '{<http://www.portalfiscal.inf.br/nfe}vBC>': [facet 'pattern'] The value '0.00' is not accepted by the pattern '0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}  (\.[0-9]  {2})?'. Element '{<http://www.portalfiscal.inf.br/nfe}vBC>': '0.00' is not a valid value of the atomic type '{<http://www.portalfiscal.inf.br/nfe}TDec_1302Opc>'.  Element '{<http://www.portalfiscal.inf.br/nfe}vISS>': [facet 'pattern'] The value '0.00' is not accepted by the pattern '0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2}  )?'.  Element '  {<http://www.portalfiscal.inf.br/nfe>}  vISS': '0.00' is not a valid value of the atomic type '  {<http://www.portalfiscal.inf.br/nfe>}  TDec\_1302Opc'. |
| **Solução/Implementação:** | Envio da NF-e Padrão Sefaz    As tags abaixo foram tratadas quando o valor apresentar 0.00 então a tag não será gerada:    tag de Valor da Duplicata: vDup    As tags pertencem ao grupo de Totalizador do ISSQN tag "ISSQNtot": vServ, vBC, vISS, vPIS, vCOFINS e vOutro.    Para correto envio da NF-e 4.0 foi removido o tratamento nas tags cEAN e cEANTrib onde escreve "SEM GTIN" quando a tag está vazia. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000071 |
| **Documento de Referência:** |  |
