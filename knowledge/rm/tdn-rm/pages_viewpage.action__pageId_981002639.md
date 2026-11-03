---
content_hash: 2abdbbd97ae6df985cef6bf2c1c21d90c2950761543202f794f8bf74e0b5df4a
fetched_at: '2026-06-29T00:12:15.656068+00:00'
page_id: '981002639'
product: rm
source: tdn-rm
title: Grupo de informações do CT-e Normal e Substituto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002639
version: 10
---

# infCTeNorm - Grupo de informações do CT-e Normal e Substituto

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infCTeNorm** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo de Escolha** | **Grupo de informações do CTe Normal e Substituto** |
| **infCarga** | **infCTeNorm** | **1-1** | **Grupo** |  |
| **infDoc** | **infCTeNorm** | **0-1** | **Grupo** |  |
| **docAnt** | **infCTeNorm** | **0-1** | **Grupo** |  |
| **infModal** | **infCTeNorm** | **1-1** | **Grupo** | **Informações do modal** |
| versaoModal | infModal | 1-1 | Atributo | TPARFILIAL.VERSAOCTE |
| xs:any | infModal | 1-1 | Elemento | No caso do RM, somente o Modal Rodovíário está disponível.  Os campos desse modal estão descritos no grupo N - Modal Rodoviário |
| **veicNovos** | **infCTeNorm** | **0-n** | **Grupo** | **Não será Gerado** |
| **cobr** | **infCTeNorm** | **0-1** | **Grupo** | **Não será Gerado** |
| **infCteSub** | **infCTeNorm** | **0-1** | **Grupo** | **Informações do CTe de substituição** |
| chCte | infCteSub | 1-1 | Elemento | Busca-se a chave de acersso do CT-e Original através da TMOVRELAC |
| indAlteraToma | infCteSub | 0-1 | Elemento | Se o cnpj do tomador do CT-e de origem for diferente do tomador do CT-e substitudo |
| **infGlobalizado** | **infCTeNorm** | **0-1** | **Grupo** | **Informações do CTe Globalizado** |
| xObs | infGlobalizado | 1-1 | Elemento | TMOVTRANSP.OBSGLOBALIZADO |
| **infServVinc** | **infCTeNorm** | **0-1** | **Grupo** | **Informações do Serviço Vinculado a Multimodal** |
| **infCTeMultimodal** | **infServVinc** | **1-n** | **Grupo** | **informações do CTe multimodal vinculado** |
| chCTeMultimodal | infCTeMultimodal | 1-1 | Elemento | TCTRC.CHAVEACESSONFE |
