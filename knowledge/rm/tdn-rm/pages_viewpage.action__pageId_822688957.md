---
content_hash: ee9c62c51bf565275593efcedfeddcc020f41ec63143caab2b5d0a511b468b55
fetched_at: '2026-06-29T00:11:46.558200+00:00'
page_id: '822688957'
product: rm
source: tdn-rm
title: tribFed/piscofins
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688957
version: 13
---

Grupo será gerado com os Tributos PIS/COFINS ou PISRF/COFINSRF contidos na Nota Fiscal

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Descrição** |
| piscofins | **NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/** | **Não** | **Grupo** | **Grupo de informações para os Valores de PIS/COFINS** |
| CST | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  TTRBMOV.SITTRIBUTARIA | CST da Nota Fiscal  Obs.: CST deve ser igual para todas as linhas do Tributo. |
| vBCPisCofins | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  Se tributo no movimento TTRBMOV.BASEDECALCULO  Senão  somatório dos itens  TTRBMOV.BASEDECALCULO | Base de Cálculo do Tributo |
| pAliqPis | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  TTRBMOV.ALIQUOTA | Alíquota do Tributo PIS |
| pAliqCofins | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  TTRBMOV.ALIQUOTA | Alíquota do Tributo COFINS |
| vPis | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  TTRBMOV.VALOR | Valor do PIS |
| vCofins | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | Tributo do Movimento/Item do Movimento  Se tributo no movimento TTRBMOV.VALOR  Senão  somatório dos itens  TTRBMOV.VALOR | Valor do COFINS |
| tpRetPisCofins | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/piscofins/ | Sim | 0 - PIS/COFINS/CSLL Não Retidos; 1 - PIS/COFINS Retido; 2 - PIS/COFINS Não Retido; 3 - PIS/COFINS/CSLL Retidos; 4 - PIS/COFINS Retidos, CSLL Não Retido; 5 - PIS Retido, COFINS/CSLL Não Retido; 6 - COFINS Retido, PIS/CSLL Não Retido; 7 - PIS Não Retido, COFINS/CSLL Retidos; 8 - PIS/COFINS Não Retidos, CSLL Retido; 9 - COFINS Não Retido, PIS/CSLL Retidos; | O valor da tag será gerado da seguinte forma:  Se não houver os tributos IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | | --- | --- | --- | | **1** | Sim | Sim | | **2** | Não | Não |   Se houver IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** | | --- | --- | --- | --- | | **0** | Não | Não | Não | | **3** | Sim | Sim | Sim | | **4** | Sim | Sim | Não | | **5** | Sim | Não | Não | | **6** | Não | Sim | Não | | **7** | Não | Sim | Sim | | **8** | Não | Não | Sim | | **9** | Sim | Não | Sim | |
