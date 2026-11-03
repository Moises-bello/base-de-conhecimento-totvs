---
content_hash: 7542115dbc81f06e9c2955fb340bb758654cc6de15922e34006a363b6375bd26
fetched_at: '2026-06-29T00:12:16.413336+00:00'
page_id: '989564131'
product: rm
source: tdn-rm
title: Grupo de informações do IBS/CBS de competência do município (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564131
version: 4
---

# gIBSMun - Grupo de informações do IBS/CBS de competência do município

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gIBSMun** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **1-1** | **Grupo** | **Grupo de informações do IBS/CBS de competência do município** |
| pIBSMun | gIBSMun | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Municipal definido no Item do Movimento   * Se o Grupo **gTribRegular** for gerado este campo deve ser zerado; |
| **gDif** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo IBS Municipal   * O percentual do diferimento no Item do Movimento for maior que zero; ou * O tipo de tributação for "Diferido" na Regra de Tributação |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do IBS Municipal definido no Item do Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do IBS Municipal definido no Item do Movimento |
| **gDevTrib** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota estiver preenchido para o tributo IBS Municipal definido no Item do Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Municipal definido no Item do Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do IBS Municipal definido no Item do Movimento |
| vIBSMun | gIBSMun | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do IBS Municipal definido no Item do Movimento |
