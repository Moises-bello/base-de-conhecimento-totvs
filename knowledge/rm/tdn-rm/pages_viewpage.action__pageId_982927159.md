---
content_hash: 17cd1251b08388680817aa51105adf992893034f67a4cd9c38e553710654731d
fetched_at: '2026-06-29T00:12:16.222861+00:00'
page_id: '982927159'
product: rm
source: tdn-rm
title: Grupo de informações da Tributação Regular - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982927159
version: 6
---

# gTribRegular - Grupo de informações da Tributação Regular

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gTribRegular** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=981794544)** | **0-1** | **Grupo** | **Grupo de informações da Tributação Regular.** **Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva.**  Este grupo será gerado sempre que na Regra Tributária estiver definida uma Regra indicando a Tributação Regular |
| CSTReg | gTribRegular | 1-1 | Elemento | DREGRATRIBUTARIA.SITUACAOTRIBUTARIA  Situação tributária definida na Regra Tributária Regular, do cadastro da Regra Tributária informada no Movimento |
| cClassTribReg | gTribRegular | 1-1 | Elemento | DREGRATRIBUTARIA.CLASSTRIB  cClassTrib definida na Regra Tributária Regular, do cadastro da Regra Tributária informada no Movimento |
| pAliqEfetRegIBSUF | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Estadual definido no Movimento |
| vTribRegIBSUF | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegIBSUF |
| pAliqEfetRegIBSMun | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Municipal definido no Movimento |
| vTribRegIBSMun | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegIBSMun |
| pAliqEfetRegCBS | gTribRegular | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do CBS definido no Movimento |
| vTribRegCBS | gTribRegular | 1-1 | Elemento | gIBSCBS.vBC \* pAliqEfetRegCBS |
