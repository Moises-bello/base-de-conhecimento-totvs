---
article_id: 360035419934
category: NFe - Nota Fiscal Eletrônica
content_hash: c98b2fd3d18aa025298fa3dc6d76fb73b61629fa3a1d9942f285556fab173b9f
fetched_at: '2026-06-28T22:40:01.970349+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - type mismatch
  on + on JOBNFECAN(SPEDNFE.PRX)'
type: support-article
updated_at: '2021-07-20T20:07:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035419934--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-type-mismatch-on-on-JOBNFECAN-SPEDNFE-PRX
---

**Ocorrência**type mismatch on + on JOBNFECAN(SPEDNFE.PRX)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Causa**

Erro esta sendo gerado pois o cadastro de empresa via configurador (SIGACFG), o endereço de cobrança não esta sendo preenchido (aba endereço de cobrança).

**Solução**

No cadastro de empresa preencher o **endereço de cobrança, cidade de cobrança, estado de cobrança e cep de cobrança.**

Preencher os campos referentes ao endereço de cobrança, **M0\_ENDCOB, M0\_CIDCOB, M0\_ESTCOB e M0\_CEPCOB.**

Após preencher os campos, o erro não será mais apresentado.
