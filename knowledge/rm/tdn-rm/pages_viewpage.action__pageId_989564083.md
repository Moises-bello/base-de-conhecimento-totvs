---
content_hash: 77e2eed8890f38be858f674e02f5067bd6451148452c1c8b67ec065a1cb4ad32
fetched_at: '2026-06-29T00:12:16.406998+00:00'
page_id: '989564083'
product: rm
source: tdn-rm
title: Informações do IBS/CBS de competência das Unidades Federadas (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564083
version: 3
---

# gIBSUF - Grupo de informações do IBS/CBS de competência das Unidades Federadas

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gIBSUF** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **1-1** | **Grupo** | **Grupo de informações do IBS/CBS de competência das Unidades Federadas** |
| pIBSUF | gIBSUF | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do IBS Estadual definido no Item do Movimento   * Se o Grupo **gTribRegular** for gerado este campo deve ser zerado |
| **gDif** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo IBS Estadual   * O percentual do diferimento no Item do Movimento for maior que zero; ou * O tipo de tributação for "Diferido" na Regra de Tributação |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do IBS Estadual definido no Item do Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do IBS Estadual definido no Item do Movimento |
| **gDevTrib** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gIBSUF** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota estiver preenchido para o tributo IBS Estadual definido no Item do Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do IBS Estadual definido no Item do Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do IBS Estadual definido no Item do Movimento |
| vIBSUF | gIBSUF | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do IBS Estadual definido no Item do Movimento |
