---
content_hash: 135b4925983979da6610ca455be77cf0ae32334121a164d676aaffa914adf30a
fetched_at: '2026-06-29T00:12:15.801878+00:00'
page_id: '982917588'
product: rm
source: tdn-rm
title: Informações do IBS/CBS de competência das Unidades Federadas - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982917588
version: 17
---

# gIBSUF - Grupo de informações do IBS/CBS de competência das Unidades Federadas

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gIBSUF** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=981794544)** | **1-1** | **Grupo** | **Grupo de informações do IBS/CBS de competência das Unidades Federadas** |
| pIBSUF | gIBSUF | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Estadual definido no Movimento   * Se o Grupo **gTribRegular** for gerado este campo deve ser zerado (ou seja, caso esteja definida a regra para Regra Tributária Regular) |
| **gDif** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo IBS Estadual   * O percentual do diferimento no Movimento for maior que zero (TTRBMOV.PCTDIFERIMENTO para IBSUF); ou * O tipo de tributação for "Diferido" na Regra de Tributação (DREGRATRIBUTARIADETALHETRIBUTO.TIPOTRIBUTACAO = "F" para IBSUF) |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do IBS Estadual definido no Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do IBS Estadual definido no Movimento |
| **gDevTrib** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota (TTRBMOV.PCTREDUCAOALIQUOTA) estiver preenchido para o tributo IBS Estadual definido no Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Estadual definido no Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do IBS Estadual definido no Movimento |
| vIBSUF | gIBSUF | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do IBS Estadual definido no Movimento |
