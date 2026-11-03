---
content_hash: b47ce9f7d5a94eeeee7865a2c2542871b038dd35b8d84e2d26e51b6108340d9e
fetched_at: '2026-06-29T00:08:49.575007+00:00'
page_id: '331845100'
product: rm
source: tdn-rm
title: 1898465 FISCAL01-2947 DT Envio de NF-e de serviço para Brasilia - DF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331845100
version: 1
---

# Envio de NF-e de serviço para Brasilia - DF - Tags opcionais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | Ao enviar uma NF-e de serviço para Brasilia - DF |
| **Solução/Implementação:** | Tags opcionais CNAE e cServico estão saindo no XML em branco, gerando inconsistência na validação do Schema do TSS:    \_Element '  {<http://www.portalfiscal.inf.br/nfe>}  CNAE': [facet 'pattern'] The value '' is not accepted by the pattern '[0-9]  {7}  '. Element '  {<http://www.portalfiscal.inf.br/nfe>}  CNAE': '' is not a valid value of the local atomic type. Element '  {<http://www.portalfiscal.inf.br/nfe>}  cServico': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'. Element '  {<http://www.portalfiscal.inf.br/nfe>}  cServico': '' is not a valid value of the local atomic type.\_ |
| **Conversores e Parâmetros:** | Alteração no preenchimento das tags CNAE e cServico, informações opcionais que estão sendo geradas em branco no XML gerando erro de Schema do TSS. |
