---
content_hash: 6121675e33346cfaa1eebf2df997774278615c258f2dbd0a811f42dd82bc07ed
fetched_at: '2026-06-29T00:12:15.807955+00:00'
page_id: '982918187'
product: rm
source: tdn-rm
title: Grupo de informações do IBS/CBS de competência do município - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982918187
version: 9
---

# gIBSMun - Grupo de informações do IBS/CBS de competência do município

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gIBSMun** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=981794544)** | **1-1** | **Grupo** | **Grupo de informações do IBS/CBS de competência do município** |
| pIBSMun | gIBSMun | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Municipal definido no Movimento   * Se o Grupo **gTribRegular** for gerado este campo deve ser zerado; (ou seja, caso esteja informada a regra para Regra Tributária Regular) |
| **gDif** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo IBS Municipal   * O percentual do diferimento no Movimento for maior que zero (TTRBMOV.PCTDIFERIMENTO para IBSMUN); ou * O tipo de tributação for "Diferido" na Regra de Tributação (DREGRATRIBUTARIADETALHETRIBUTO.TIPOTRIBUTACAO = "F" para IBSMUN) |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do IBS Municipal definido no Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do IBS Municipal definido no Movimento |
| **gDevTrib** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gIBSMun** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota (TTRBMOV.PCTREDUCAOALIQUOTA) estiver preenchido para o tributo IBS Municipal definido no Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Municipal definido no Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do IBS Municipal definido no Movimento |
| vIBSMun | gIBSMun | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do IBS Municipal definido no Movimento |
