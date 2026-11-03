---
content_hash: 8891dfacb6dc96965385692ec6940b97bf553d9721b2e2c8cd5bf2b8297732f2
fetched_at: '2026-06-29T00:12:16.381038+00:00'
page_id: '985681140'
product: rm
source: tdn-rm
title: Grupo de informações do CTe OS  Normal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=985681140
version: 7
---

# infCTeNorm  - Grupo de informações do CTe OS Normal

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **infCTeNorm** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo de Escolha** | **Grupo de informações do CTe Normal e Substituto** |
| **infServico** | **infCTeNorm** | **1-1** | **Grupo** | **Informações da Prestação do Serviço** |
| xDescServ | infServico | **1-1** | Elemento |  |
| **infQ** | **infCTeNorm** | **0-1** | **Grupo** | **Informações de quantidades da Carga do CTe** |
| qCarga | infQ | 1-1 | Elemento | TMOV.QUANTIDADE |
| **infDocRef** | **infCTeNorm** | **0-1** | **gRUPO** | **Informações dos documentos referenciados** |
| nDoc | infDocRef | 1-1 | Elemento | TCTRC.NUMERODOC |
| serie | infDocRef | 0-1 | Elemento | TCTRC.SERIEDOC |
| subserie | infDocRef | 0-1 | Elemento | Não obrigatório |
| dEm | infDocRef | 1-1 | Elemento | TCTRC.DATAEMISSAO |
| vDoc | infDocRef | 0-1 | Elemento | TCTRC.VALORTOTAL |
| chBPe | infDocRef | 0-1 | Elemento | TCTRC.CHAVEACESSONFE |
| **seg** | **infCTeNorm** | **0-1** | **gRUPO** | **Informações de Seguro da Carga** |
| respSeg | seg | 1-1 | Elemento | TCTESEGURO.RESPONSAVEL |
| xSeg | seg | 0-1 | Elemento | TCTESEGURO.SEGURADORA |
| nApol | seg | 0-1 | Elemento | TCTESEGURO.APOLICE |
| **infModal** | **infCTeNorm** | **1-1** | **Grupo** | **Informações do modal** |
| versaoModal | infModal | 1-1 | Atributo | TPARFILIAL.VERSAOCTE |
| xs:any | infModal | 1-1 | Elemento | No caso do RM, somente o Modal Rodovíário está disponível.  Os campos desse modal estão descritos no grupo N - Modal Rodoviário |
| **infCteSub** | **infCTeNorm** | **0-1** | **Grupo** | **Informações do CTe de substituição** |
| chCte | infCteSub | 1-1 | Elemento | TCTEOS.CHAVEACESSO |
| refCTeCanc | infCteSub | 0-1 | Elemento | Não obrigatório |
