---
content_hash: b195adaf96b8820dfb04ca412058a193f08499ba0f3d83fd367e8570b6a1bf09
fetched_at: '2026-06-29T00:12:16.424738+00:00'
page_id: '989564221'
product: rm
source: tdn-rm
title: Grupo de informações da Tributação Regular (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564221
version: 4
---

# gTribRegular - Grupo de informações da Tributação Regular

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gTribRegular** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **0-1** | **Grupo** | **Grupo de informações da Tributação Regular.** **Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva.**  Este grupo será gerado sempre que na Regra Tributária estiver definida uma Regra indicando a Tributação Regular |
| CSTReg | gTribRegular | 1-1 | Elemento | DREGRATRIBUTARIA.SITUACAOTRIBUTARIA  Situação tributária definida na Regra Tributária Regular, do cadastro da Regra Tributária informada no Item do Movimento |
| cClassTribReg | gTribRegular | 1-1 | Elemento | DREGRATRIBUTARIA.CLASSTRIB  cClassTrib definida na Regra Tributária Regular, do cadastro da Regra Tributária informada no Item do Movimento |
| pAliqEfetRegIBSUF | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA \* TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Estadual definido no Item do Movimento |
| vTribRegIBSUF | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegIBSUF |
| pAliqEfetRegIBSMun | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA \* TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Municipal definido no Item do Movimento |
| vTribRegIBSMun | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegIBSMun |
| pAliqEfetRegCBS | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA \* TTRBMOV.PCTREDUCAOALIQUOTA  Busca do CBS definido no Item do Movimento |
| vTribRegCBS | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegCBS |
