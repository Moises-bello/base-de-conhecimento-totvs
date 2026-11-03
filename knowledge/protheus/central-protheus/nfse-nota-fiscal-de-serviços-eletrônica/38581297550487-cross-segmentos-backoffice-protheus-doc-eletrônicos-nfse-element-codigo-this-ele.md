---
article_id: 38581297550487
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6da1e7ebccb8746472ae5e57834773823bf9d48426cd8baf0186b7435d9b8d73
fetched_at: '2026-06-28T22:39:57.389521+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element
  ''codigo'': This element is not expected. Expected is one of ( construcao, impostos,
  impostosbcs, ISTot, ISBCSTot, totTrib )'
type: support-article
updated_at: '2026-04-27T19:03:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38581297550487-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-codigo-This-element-is-not-expected-Expected-is-one-of-construcao-impostos-impostosbcs-ISTot-ISBCSTot-totTrib
---

**Ocorrência**  
Ao realizar a transmissão de uma NFSE, ocorre a falha de schema abaixo:

> **------------------ ERRO SCHEMA - XML UNICO ------------------**  
> **Element 'codigo': This element is not expected. Expected is one of ( construcao, impostos, impostosbcs, ISTot, ISBCSTot, totTrib ).**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Causa**  
Essa falha de schema ocorre pela **falta da abertura e fechamento da tag <impostosbcs>** no campo XML\_TSS da SPED051, montado pelo Protheus.  
  
Para correção, o ambiente deverá estar com o fonte **backoffice.fiscal.tss.xml.tlpp** igual ou superior a 21/01/2026:  
- 12.1.2410: <https://r.totvs.io/p/1247193> ou 12.1.2510: <https://r.totvs.io/p/1247194>.  
  
Portanto, basta aplicar o pacote acima no RPO do Protheus e realizar novos testes.
