---
content_hash: 939534e929838ff474177f3b0502fe84a05f21e5a5be3b7f5b16ed706deef2f5
fetched_at: '2026-06-29T00:12:15.778021+00:00'
page_id: '981792897'
product: rm
source: tdn-rm
title: Informações dos documentos transportados pelo CTe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981792897
version: 5
---

# infDoc - Informações dos documentos transportados pelo CT-e. Opcional para Redespacho Intermediário  e Serviço vinculado a multimodal.

infDocleftinfNF

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infDoc** | **[infCTeNorm](https://tdn.totvs.com/pages/viewpage.action?pageId=981002639)** | **0-1** | **Grupo** | **Informações dos documentos transportados pelo CT-e.**  **Opcional para Redespacho Intermediário  e Serviço vinculado a multimodal.** |
| **infNF** | **infDoc** | **1-n** | **Grupo de Escolha** | **Informações das NF** |
| nRoma | infNF | 0-1 | Elemento | Não será gerado |
| nPed | infNF | 0-1 | Elemento | Não será gerado |
| mod | infNF | 1-1 | Elemento | FTDO.CODMODDOC |
| serie | infNF | 1-1 | Elemento | TCTRC.SERIEDOC |
| nDoc | infNF | 1-1 | Elemento | TCTRC.NUMERODOC |
| dEmi | infNF | 1-1 | Elemento | TCTRC.DATAEMISSAO |
| vBC | infNF | 1-1 | Elemento | TCTRC.VLRBCICMS |
| vICMS | infNF | 1-1 | Elemento | TCTRC.VLRTOTICMS |
| vBCST | infNF | 1-1 | Elemento | TCTRC.VLRBCICMSST |
| vST | infNF | 1-1 | Elemento | TCTRC.VLRTOTICMSST |
| vProd | infNF | 1-1 | Elemento | TCTRC.VLRTOTPRODUTOS |
| vNF | infNF | 1-1 | Elemento | TCTRC.VALORTOTAL |
| nCFOP | infNF | 1-1 | Elemento | TCTRC.CODNAT |
| nPeso | infNF | 0-1 | Elemento | Não será gerado |
| PIN | infNF | 0-1 | Elemento | Não será gerado |
| dPrev | infNF | 0-1 | Elemento | TMOV.DATAENTREGA |
| **infUnidCarga** | **infNF** | **0-n** | **Grupo** | **Não será gerado** |
| **infUnidTransp** | **infNF** | **0-n** | **Grupo** | **Não será gerado** |

infNFe

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infDoc** | **[infCTeNorm](https://tdn.totvs.com/pages/viewpage.action?pageId=981002639)** | **0-1** | **Grupo** | **Informações dos documentos transportados pelo CT-e.**  **Opcional para Redespacho Intermediário  e Serviço vinculado a multimodal.** |
| **infNFe** | **infDoc** | **1-n** | **Grupo de Escolha** | **Informações das NF** |
| chave | infNFe | 1-1 | Elemento | TCTRC.CHAVEACESSONFE |
| PIN | infNFe | 0-1 | Elemento | Não será gerado |
| dPrev | infNFe | 0-1 | Elemento | TMOV.DATAENTREGA |
| **infUnidCarga** | **infNFe** | **0-n** | **Grupo** | **Não será gerado** |
| **infUnidTransp** | **infNFe** | **0-n** | **Grupo** | **Não será gerado** |

infOutros

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infDoc** | **[infCTeNorm](https://tdn.totvs.com/pages/viewpage.action?pageId=981002639)** | **0-1** | **Grupo** | **Informações dos documentos transportados pelo CT-e.**  **Opcional para Redespacho Intermediário  e Serviço vinculado a multimodal.** |
| **infOutros** | **infDoc** | **1-n** | **Grupo de Escolha** | **Informações dos demais documentos** |
| tpDoc | infOutros | 1-1 | Elemento | FTDO.CODMODDOC |
| descOutros | infOutros | 0-1 | Elemento | **Se** FTDO.DESCRICAO != 00  **Então** "OUTROS"  **Senão** FTDO.DESCRICAO |
| nDoc | infOutros | 0-1 | Elemento | TCTRC.NUMERODOC |
| dEmi | infOutros | 0-1 | Elemento | TCTRC.DATAEMISSAO |
| vDocFisc | infOutros | 0-1 | Elemento | TCTRC.VALORTOTAL |
| dPrev | infOutros | 0-1 | Elemento | TMOV.DATAENTREGA |
| **infUnidCarga** | **infNFe** | **0-n** | **Grupo** | **Não será gerado** |
| **infUnidTransp** | **infNFe** | **0-n** | **Grupo** | **Não será gerado** |
