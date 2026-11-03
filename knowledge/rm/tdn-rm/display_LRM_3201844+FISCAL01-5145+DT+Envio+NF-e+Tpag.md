---
content_hash: 12fa19e048bedf0c47c46316fbbaf7e9f9f4c9804309ea4e5699ece10938f627
fetched_at: '2026-06-29T00:09:01.562069+00:00'
page_id: '373492914'
product: rm
source: tdn-rm
title: 3201844 FISCAL01-5145 DT Envio NF-e Tpag
type: documentation
url: https://tdn.totvs.com/display/LRM/3201844+FISCAL01-5145+DT+Envio+NF-e+Tpag
version: 1
---

# Envio da NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio da NF-e |
| **Situação/Requisito:** | Ao enviar uma NF-e pela visão do movimento ocorre as inconsistências abaixo:  Motivo:Campo: mod': This element is not expected. Expected is (  {<http://www.portalfiscal.inf.br/nfe>}  indPag . Campo: vFCP': This element is not expected. Expected is one of (  {<http://www.portalfiscal.inf.br/nfe>}  vFCPUFDest,  {<http://www.portalfiscal.inf.br/nfe>}  vICMSUFDest,  {<http://www.portalfiscal.inf.br/nfe>}  vICMSUFRemet,  {<http://www.portalfiscal.inf.br/nfe>}  vBCST . Campo: detPag': This element is not expected. Expected is (  {<http://www.portalfiscal.inf.br/nfe>}  tPag . |
| **Solução/Implementação:** | No envio da NF-e pela visão do movimento será carregado o código do modelo  de documento para ser utilizado posteriormente no envio da NF-e. |
| **Tickets relacionados:** | 3194609, 3199628 |
| **Requisito:** | FIS000071 |
