---
article_id: 360027015632
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e069db4bddb782454bf5e0ea2c4bf0af80ad494c3f2aba425a27e6038a2a936a
fetched_at: '2026-06-28T22:39:57.515005+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - IPM: 00154
  - TRIBUTA_MUNICIPIO_PRESTADOR '
type: support-article
updated_at: '2021-10-06T17:40:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027015632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-IPM-00154-TRIBUTA-MUNICIPIO-PRESTADOR
---

**Dúvida**Qual campo deve ser preenchido para alimentar a tag <tributa\_municipio\_prestador>?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**De acordo com o manual IPM:  
  
*"Esta tag serve para informar onde será recolhido o imposto e deve ser preenchida*  
*com "0" ou "N" quando NÃO TRIBUTAR P/ PRESTADOR e "1" ou "S" quando TRIBUTAR P/ PRESTADOR."*Se o campo F4\_ISSST for preenchido com 1 (Dentro do município), a tag <tributa\_municipio\_prestador> será gerada com S.  
Se o campo F4\_ISSST possuir conteúdo diferente de 1, a tag <tributa\_municipio\_prestador> será gerada com N.
