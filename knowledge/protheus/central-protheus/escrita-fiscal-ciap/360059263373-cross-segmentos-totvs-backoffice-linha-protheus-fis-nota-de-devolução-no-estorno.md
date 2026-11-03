---
article_id: 360059263373
category: Escrita Fiscal - CIAP
content_hash: 233bba041766d41d8c7c4532e7c0f440118d544dcf3cf700bfda6caa212579f5
fetched_at: '2026-06-28T22:39:33.923871+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nota de devolução
  no estorno CIAP geração de coeficiente
type: support-article
updated_at: '2021-07-29T12:27:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059263373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-de-devolu%C3%A7%C3%A3o-no-estorno-CIAP-gera%C3%A7%C3%A3o-de-coeficiente
---

**Dúvida**Nota de devolução no estorno ciap para geração do coeficiente.  
  
**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

**1.** No Configurador**(SIGACFG)**acesse **Ambientes/ Cadastros/ Parâmetros**configure o parâmetro a abaixo:

MV\_CIAPDEV = T e MV\_MTDCOEF = 2 (para não ser considerada)  
MV\_CIAPDEV = F e MV\_MTDCOEF = 1 (para ser considerada, será descontado pois já usou a nota de origem para gerar o coeficiente).

[MP - FIS - NOVAS REGRAS CIAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028531591-MP-FIS-NOVAS-REGRAS-CIAP?source=search)

<https://tdn.totvs.com/pages/releaseview.action?pageId=187532625>
