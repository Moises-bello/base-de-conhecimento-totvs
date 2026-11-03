---
content_hash: a634239c417409b602569b572063db4906c1f595c2ca2e7943fcaa3dce1282f6
fetched_at: '2026-06-29T00:11:46.549277+00:00'
page_id: '822688930'
product: rm
source: tdn-rm
title: trib/tribFed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688930
version: 10
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **trib** | **DPS/infDPS/valores** | **Sim** | **Grupo** | **Grupo de informações dos tributos do serviço prestado.** |
| **tribFed** | **DPS/infDPS/valores/trib** | **Não** | **Grupo** | **Grupo de informações de outros tributos relacionados ao serviço prestado** |
| vRetCP | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/ | Não | Valor do tributo INSS informado no item do movimento.  TTRBITEM.VALOR | No item do movimento deve existir a linha do tributo INSS com Alíquota e valor. |
| vRetIRRF | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/ | Não | Valor do tributo IRRF ou IRRF PJ informado no movimento.  TTRBMOV.VALOR  Obs: Não busca informações de tributos no item. | Valor monetário do IRRF (R$). |
| vRetCSLL | NFSe/infNFSe/DPS/infDPS/valores/trib/tribFed/ | Não | Valor do tributo CSLLRF informado no movimento.  TTRBMOV.VALOR  Obs: Não busca informações de tributos no item. | Somatório do Valor monetário dos tributos PISRF, COFINSRF e/ou CSLLRF (R$). |
