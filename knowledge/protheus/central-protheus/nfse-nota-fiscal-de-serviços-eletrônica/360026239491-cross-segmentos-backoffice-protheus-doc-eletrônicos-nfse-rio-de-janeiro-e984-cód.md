---
article_id: 360026239491
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c0e3cc61f2a9cdd7c007dc93d98639328e75e21359a1185bc5ac06200c44af7f
fetched_at: '2026-06-28T22:39:58.482930+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - RIO DE JANEIRO:
  E984 - CÓDIGO DE BENEFICIO NÃO INFORMADO'
type: support-article
updated_at: '2025-07-14T21:47:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026239491-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-RIO-DE-JANEIRO-E984-C%C3%93DIGO-DE-BENEFICIO-N%C3%83O-INFORMADO
---

**Dúvida**Como corrigir a rejeição E984 - CÓDIGO DE BENEFICIO NÃO INFORMADO?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**

Nos casos em que a NFS-e a ser emitida faça jus a um benefício fiscal, o prestador deverá preencher a TAG   
“<CodigoTributacaoMunicipio>” com código do benefício e o código do serviço no município.

Exemplo:   
Código do benefício: 123   
Código do serviço no município: 070201   
Preenchimento do campo B1\_TRIBMUN=123070201  
Geração da tag: <CodigoTributacaoMunicipio>123070201</CodigoTributacaoMunicipio>

https://notacarioca.rio.gov.br/files/manuais/WsNFSeNacional.pdf
