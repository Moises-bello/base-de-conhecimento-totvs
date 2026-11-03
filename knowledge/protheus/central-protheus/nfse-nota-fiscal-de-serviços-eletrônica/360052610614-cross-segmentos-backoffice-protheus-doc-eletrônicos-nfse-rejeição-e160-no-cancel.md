---
article_id: 360052610614
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 250217f8ca5258cd798d5024b8dc1e4d210a53fb30f110a01294be992d15971b
fetched_at: '2026-06-28T22:39:58.457150+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  E160 no Cancelamento de Ribeirão Preto
type: support-article
updated_at: '2025-06-25T20:57:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052610614-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-E160-no-Cancelamento-de-Ribeir%C3%A3o-Preto
---

**Dúvida**Ao transmitir um cancelamento para o município de Ribeirão Preto, ocorre a rejeição:  
E160 - ARQUIVO ENVIADO FORA DA ESTRUTURA DO ARQUIVO XML DE ENTRADA  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse erro está ocorrendo pois o código do cancelamento está vazio no XML\_LOTE da tabela SPED053:  
<tc:CodigoCancelamento></tc:CodigoCancelamento>  
  
Realize o procedimento abaixo para envio do código do cancelamento:  
[MP - NFSE - MV\_CODCANC e MV\_MOTCNFS (Códigos de Cancelamento)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046961634-MP-NFSE-MV-CODCANC-e-MV-MOTCNFS-C%C3%B3digos-de-Cancelamento-?source=search)
