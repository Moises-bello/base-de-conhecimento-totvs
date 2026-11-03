---
content_hash: 785e0f7287313827efa8ff0ae9005932bd1b8701c7d031163c279a7c157b9879
fetched_at: '2026-06-29T00:12:15.763856+00:00'
page_id: '981791028'
product: rm
source: tdn-rm
title: Informações da Carga do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981791028
version: 2
---

# infCarga - Informações da Carga do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infCarga** | **[infCTeNorm](https://tdn.totvs.com/pages/viewpage.action?pageId=981002639)** | **1-1** | **Grupo** | **Informações da Carga do CT-e** |
| vCarga | infCarga | 0-1 | Elemento | ITMOV.VALORMERCADORIAS |
| proPred | infCarga | 1-1 | Elemento | TMOV.CAMPOLIVRE3 ou TPRD.NOMEFANTASIA |
| xOutCat | infCarga | 0-1 | Elemento | TMOV.NATUREZAVOLUMES |
| **infQ** | **infCarga** | **1-n** | **Grupo** | **Informações de quantidades da Carga do CTe** |
| cUnid | infQ | 1-1 | Elemento | TMOV.UNCALCULO |
| tpMed | infQ | 1-1 | Elemento | TMOV.ESPECIE |
| qCarga | infQ | 1-1 | Elemento | TMOV.QUANTIDADE |
| vCargaAverb | infQ | 0-1 | Elemento | Não será gerado |
