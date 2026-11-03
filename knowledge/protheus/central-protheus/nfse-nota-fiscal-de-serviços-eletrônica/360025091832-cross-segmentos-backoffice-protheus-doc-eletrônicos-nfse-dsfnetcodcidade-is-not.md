---
article_id: 360025091832
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f64af38a864fe8a318d0948933276d32a0a8fc3496a5226f8a8a62cf797f3880
fetched_at: '2026-06-28T22:39:56.479634+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:''codcidade''_is_not_valid '
type: support-article
updated_at: '2025-07-18T14:37:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025091832-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-codcidade-is-not-valid
---

**Dúvida**

Ao transmitir uma nota para prefeitura com provedor DSFNET é apresentado a rejeição abaixo:

ERRO VALIDACAO XSD: (400)error: org.xml.sax.SAXParseException: cvc-type.3.1.3: The value '' of element 'codcidade' is not valid.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
  
**Solução**

A tag <CodCidade> pertence ao cabeçalho do lote que está na tabela SPED053, campo XML\_LOTE. Se essa tag estiver vazia será apresentado o erro mencionado acima.

Para correção do erro, é preciso reconfigurar o wizard.config e preencher o campo 'Codigo SIAFI'.

Em seguida faça retransmissão e monitoramento da nota.
