---
content_hash: 3c12236d8e3316e5d6f89c3b33f39861894a352a5ccb840f37e0de05c54c18d7
fetched_at: '2026-06-29T00:12:16.419576+00:00'
page_id: '989564181'
product: rm
source: tdn-rm
title: Grupo de informações da CBS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564181
version: 5
---

# gCBS - Grupo de informações da CBS

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gCBS** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **1-1** | **Grupo** | **Grupo de informações da CBS** |
| pCBS | gCBS | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do CBS definido no Item do Movimento   * Se o Grupo **gTribRegular** for gerado este campo deve ser zerado; |
| **gDif** | **gCBS** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo CBS   * O percentual do diferimento no Item do Movimento for maior que zero; ou * O tipo de tributação for "Diferido" na Regra de Tributação |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do CBS definido no Item do Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do CBS definido no Item do Movimento |
| **gDevTrib** | **gCBS** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gCBS** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota estiver preenchido para o tributo CBS definido no Item do Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do CBS definido no Item do Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do CBS definido no Item do Movimento |
| vCBS | gCBS | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do CBS definido no Item do Movimento |
