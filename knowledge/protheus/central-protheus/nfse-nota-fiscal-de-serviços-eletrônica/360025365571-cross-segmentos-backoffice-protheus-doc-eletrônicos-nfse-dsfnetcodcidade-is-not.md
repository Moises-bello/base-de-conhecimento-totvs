---
article_id: 360025365571
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 36bc9b4715580e5873f8af13e771470cfe3599133a31f41a8bbb4ef362778f9e
fetched_at: '2026-06-28T22:39:56.477416+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:''codcidade''_is_not_valid '
type: support-article
updated_at: '2025-07-08T19:59:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025365571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-codcidade-is-not-valid
---

**Dúvida**

Ao transmitir uma nota para prefeitura com provedor DSFNET ocorre o erro abaixo:

ERRO VALIDACAO XSD: (400)error: org.xml.sax.SAXParseException: cvc-type.3.1.3: The value '' of element 'codcidade' is not valid.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**

A tag <CodCidade> pertence ao cabeçalho do lote que está na tabela SPED053, campo XML\_LOTE. Se essa tag estiver vazia será apresentado o erro mencionado acima.

Para correção do erro, é preciso reconfigurar o wizard.config e preencher o campo 'Codigo SIAFI' .

Em seguida faça retransmissão e monitoramento da nota.
