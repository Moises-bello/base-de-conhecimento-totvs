---
article_id: 360027867571
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 03a8ebf6424994a3180e3add4fc774d270033178a904d30e5738e532a9caac67
fetched_at: '2026-06-28T22:39:58.480818+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Responsável
  pela retenção do ISS
type: support-article
updated_at: '2025-06-20T12:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027867571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Respons%C3%A1vel-pela-reten%C3%A7%C3%A3o-do-ISS
---

**Dúvida**O responsável pela retenção do ISS gerado no XML é extraído de qual campo do Protheus?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**O Rdmake NFSEXMLENV usa o conteúdo do campo F3\_RECISS para responsabilidade de retenção do ISS no XML.  
1 = Tomador Responsável pelo ISS   
2 = Prestador Responsável pelo ISS   
  
**OBS:** O campo F3\_RECISS terá o mesmo conteúdo do campo A1\_RECISS ou C5\_RECISS.
