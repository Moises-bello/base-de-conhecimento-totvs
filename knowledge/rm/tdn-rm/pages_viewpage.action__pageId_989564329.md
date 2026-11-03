---
content_hash: 79152bb19b132fa4661fef0e658a8404c432c2e601d729001e3e01e2b31d4302
fetched_at: '2026-06-29T00:12:16.435986+00:00'
page_id: '989564329'
product: rm
source: tdn-rm
title: Grupo de informações de compras governamental (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564329
version: 2
---

# gTribCompraGov - Grupo de informações da composição do valor do IBS e da CBS em compras governamental

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gTribCompraGov** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **0-1** | **Grupo** | **Grupo de informações da composição do valor do IBS e da CBS em compras governamental**  Este grupo será gerado sempre que o grupo ide.gCompraGov for gerado |
| pAliqIBSUF | gTribCompraGov | 1-1 | Elemento | gIBSUF.pIBSUF |
| vTribIBSUF | gTribCompraGov | 1-1 | Elemento | gIBSCBS.vBC \* pAliqIBSUF |
| pAliqIBSMun | gTribCompraGov | 1-1 | Elemento | gIBSMun.pIBSMun |
| vTribIBSMun | gTribCompraGov | 1-1 | Elemento | gIBSCBS.vBC \* pAliqIBSMun |
| pAliqCBS | gTribCompraGov | 1-1 | Elemento | gCBS.pCBS |
| vTribCBS | gTribCompraGov | 1-1 | Elemento | gIBSCBS.vBC \* pAliqCBS |
