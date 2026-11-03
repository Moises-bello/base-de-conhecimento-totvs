---
content_hash: 6faa390b81a72ecb101242ec3c1e8368e925129a0b22a915cc2153ee50b7770a
fetched_at: '2026-06-29T00:12:16.217927+00:00'
page_id: '982927054'
product: rm
source: tdn-rm
title: Grupo de informações da CBS - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982927054
version: 6
---

# gCBS - Grupo de informações da CBS

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gCBS** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=981794544)** | **1-1** | **Grupo** | **Grupo de informações da CBS** |
| pCBS | gCBS | 1-1 | Elemento | TTRBMOV.ALIQUOTACHEIA  Busca do CBS definido no Movimento |
| **gDif** | **gCBS** | **0-1** | **Grupo** | **Grupo de campos do diferimento**  Este grupo deverá ser gerado sempre que uma das condições abaixo for verdadeira para o tributo CBS   * O percentual do diferimento no Movimento for maior que zero (TTRBMOV.PCTDIFERIMENTO para CBS); ou * O tipo de tributação for "Diferido" na Regra de Tributação (DREGRATRIBUTARIADETALHETRIBUTO.TIPOTRIBUTACAO = "F" para CBS) |
| pDif | gDif | 1-1 | Elemento | TTRBMOV.PCTDIFERIMENTO  Busca do CBS definido no Movimento |
| vDif | gDif | 1-1 | Elemento | TTRBMOV.TRIBUTODIFERIDO  Busca do CBS definido no Movimento |
| **gDevTrib** | **gCBS** | **0-1** | **Grupo** | **Grupo de informações da devolução de tributos**  Não será gerado |
| vDevTrib | gDevTrib | 1-1 | Elemento | Não será gerado |
| **gRed** | **gCBS** | **0-1** | **Grupo** | **Grupo de informações da redução de Alíquota**  Este grupo deverá ser gerado sempre que o percentual de redução de alíquota estiver preenchido para o tributo CBS definido no Movimento |
| pRedAliq | gRed | 1-1 | Elemento | TTRBMOV.PCTREDUCAOALIQUOTA  Busca do CBS definido no Movimento |
| pAliqEfet | gRed | 1-1 | Elemento | TTRBMOV.ALIQUOTA  Busca do CBS definido no Movimento |
| vCBS | gCBS | 1-1 | Elemento | TTRBMOV.VALOR - gDevTrib.vDevTrib  Busca do CBS definido no Movimento |
