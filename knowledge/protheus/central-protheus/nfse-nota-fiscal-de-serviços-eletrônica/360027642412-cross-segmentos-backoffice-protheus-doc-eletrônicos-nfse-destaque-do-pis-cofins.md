---
article_id: 360027642412
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7e81ef8e675700e2baadb24c33d8ca4bc38077312dd5efc5522367ebc08d65e5
fetched_at: '2026-06-28T22:39:56.449810+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Destaque
  do PIS, COFINS e CSLL no XML da NFSe (Retenção na Emissão)
type: support-article
updated_at: '2025-05-29T12:27:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027642412-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Destaque-do-PIS-COFINS-e-CSLL-no-XML-da-NFSe-Reten%C3%A7%C3%A3o-na-Emiss%C3%A3o
---

**Dúvida**Qual o procedimento para destacar o PIS, COFINS e CSLL no XML da NFSe, quando a retenção ocorre na Emissão da nota?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Os valores dos **impostos serão destacados nos títulos filhos** (com nomenclaturas PI- CF- CS-, através dos campos E1\_VALOR), neste caso, deverá utilizar o parâmetro como **MV\_NFSEPCC=.F.**
