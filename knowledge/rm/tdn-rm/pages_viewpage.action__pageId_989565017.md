---
content_hash: 54759900e9386747c7d6f104df41c857a8991847868ba809f162cc2f7c80af2b
fetched_at: '2026-06-29T00:12:16.445576+00:00'
page_id: '989565017'
product: rm
source: tdn-rm
title: Grupo de informações para apuração do IBS e CBS declarado pelo contribuinte
  (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989565017
version: 7
---

# IBSCBSTot - Grupo de informações para apuração do IBS e CBS declarado pelo contribuinte

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **IBSCBSTot** | **[total](https://tdn.totvs.com/pages/viewpage.action?pageId=901955800)** | **0-1** | **Grupo** | **Grupo de informações para apuração do IBS e CBS declarado pelo contribuinte** |
| vBCIBSCBS | IBSCBSTot | 1-1 | Elemento | Σ (vBC do IBS ou CBS dos itens) |
| **gIBS** | **IBSCBSTot** | **1-1** | **Grupo** | **Totalização do IBS** |
| **gIBSUF** | **gIBS** | **1-1** | **Grupo** | **Totalização do IBS de competência da UF** |
| vDif | gIBSUF | 1-1 | Elemento | Σ (vDif do IBS\_UF dos itens) |
| vDevTrib | gIBSUF | 1-1 | Elemento | Σ (vDevTrib do IBS\_UF dos itens) |
| vIBSUF | gIBSUF | 1-1 | Elemento | Σ (vIBSUF do IBS\_UF dos itens) |
| **gIBSMun** | **gIBS** | **1-1** | **Grupo** | **Totalização do IBS de competência Municipal** |
| vDif | gIBSMun | 1-1 | Elemento | Σ (vDif do IBS\_Mun dos itens) |
| vDevTrib | gIBSMun | 1-1 | Elemento | Σ (vDevTrib do IBS\_Mun dos itens) |
| vIBSMun | gIBSMun | 1-1 | Elemento | Σ (vIBSMun do IBS\_Mun dos itens) |
| vIBS | gIBS | 1-1 | Elemento | vIBSUF + vIBSMun |
| **gCBS** | **IBSCBSTot** | **1-1** | **Grupo** | **Total do CBS** |
| vDif | gCBS | 1-1 | Elemento | Σ (vDif do CBS dos itens) |
| vDevTrib | gCBS | 1-1 | Elemento | Σ (vDevTrib do CBS dos itens) |
| vCBS | gCBS | 1-1 | Elemento | Σ (vIBSMun do CBS dos itens) |

Exemploxml
100.00


0.00
0.00
0.10

0.00
0.00
0.00
1.00

0.00
0.00
0.90
]]>
