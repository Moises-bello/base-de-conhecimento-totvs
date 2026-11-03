---
article_id: 360050813633
category: ADVPL - Classe e Função
content_hash: 5dc950c82f9c86b064b8a69295ce2191a47cf5ce385f238ba34c687ea89cd946
fetched_at: '2026-06-28T22:40:14.166159+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Função Extenso
  texto no plural
type: support-article
updated_at: '2021-05-06T20:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050813633-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Extenso-texto-no-plural
---

**Dúvida**Função Extenso está retornando palavra "DOLARES" como retornar "DOLLARS".

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Utilize o parâmetro **MV\_MOEDAP2**

Para o texto (em singular) que representa a moeda serão usados os ja existentes MV\_MOEDAx (onde x de 1 a 5) e deverão ser criados mais cinco parâmetros MV\_MOEDAPx (onde x de 1 a 5) para os respectivos plurais.

**Saiba Mais**[Função genérica - Extenso](https://tdn.totvs.com/pages/releaseview.action?pageId=6070758)
