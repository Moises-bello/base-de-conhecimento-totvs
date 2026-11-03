---
article_id: 360052697193
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 828c2e44abdd40233b18a5b8a98f8a24ef0f9487e0426a2283d1bd16a027e836
fetched_at: '2026-06-28T22:39:56.344567+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - CANCELAMENTO
  EM AMBIENTE DE HOMOLOGAÇÃO (São Paulo)
type: support-article
updated_at: '2025-06-20T11:54:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052697193-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-CANCELAMENTO-EM-AMBIENTE-DE-HOMOLOGA%C3%87%C3%83O-S%C3%A3o-Paulo
---

**Dúvida**Ao transmitir um cancelamento para São Paulo-SP em ambiente de homologação ocorre a rejeição abaixo:  
1106 - NFS-e não encontrada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Não há possibilidade de transmitir um **cancelamento em ambiente de homologação** para prefeitura de São Paulo-SP, isso porque na emissão da nota a prefeitura não converte em NFSe o RPS transmitido, portanto não retorna o número da NFSe.  
A transmissão do cancelamento exige o envio do numero da nota gerada na prefeitura, como em homologação não efetiva a nota, não há como cancelar.
