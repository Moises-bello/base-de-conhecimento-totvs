---
content_hash: 6f7e8cf31215a681d1df04a40a72c6de4b967e02eec9ff0381b8b447753e1876
fetched_at: '2026-06-29T00:12:02.496274+00:00'
page_id: '901955800'
product: rm
source: tdn-rm
title: Dados dos totais da NFCom (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901955800
version: 15
---

# total - Dados dos totais da NFCom

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **total** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **1-1** | **Grupo** | **Dados dos totais da NFCom** |
| vProd | total | 1-1 | Elemento | Σ (prod.vProd) |
| **ICMSTot** | **total** | **1-1** | **Grupo** |  |
| vCOFINS | total | 1-1 | Elemento | Σ (vCOFINS dos itens) |
| vPIS | total | 1-1 | Elemento | Σ (vPIS dos itens) |
| vFUNTTEL | total | 1-1 | Elemento | Σ (vFUNTTEL dos itens) |
| vFUST | total | 1-1 | Elemento | Σ (vFUST dos itens) |
| **vRetTribTot** | **total** | **1-1** | **Grupo** |  |
| vDesc | total | 1-1 | Elemento | Σ (prod.vDesc) |
| vOutro | total | 1-1 | Elemento | Σ (prod.vOutro) |
| vNF | total | 1-1 | Elemento | TMOV.VALORLIQUIDO |
| vTotDFe | total | 0-1 | Elemento | Esta tag somente será gerada se constarem na nota os tributos IBS e CBS.  Σ (vNF)  A partir de 2027:  Σ (vNF + IBSCBSTot.gIBS.vIBS + IBSCBSTot.gCBS.vCBS) |
| **IBSCBSTot** | **total** | **0-1** | **Grupo** |  |

Exemploxml
9.99

9.99
1.00
0.00
0.00
0.00
0.00
0.00
0.00

0.00
0.00
0.00
0.00
0.00
0.00
0.00

0.00


0.00
0.00
0.00

0.00
0.00
0.00
0.00

0.00
0.00
0.00
0.00  
]]>
