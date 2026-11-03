---
article_id: 360026099392
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2fcf6235f32d76b73aeb0d3d8602a63adcb1a60ad7041e4397ff0fad86e0f81a
fetched_at: '2026-06-28T22:39:56.470027+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:
  INVALID PROPERTY ATIVIDADE '
type: support-article
updated_at: '2025-07-18T14:37:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026099392-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-INVALID-PROPERTY-ATIVIDADE
---

**Dúvida**Ao transmitir um RPS é apresentado em tela "INTERNAL SERVER ERROR : INVALID PROPERTY \_\_ATIVIDADE"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
  
**Solução**O erro ocorre quando o campo B1\_CNAE está em branco.  
O CNAE/Atividade é obrigatório para prefeituras que trabalham com o provedor DSFNET.

Esse código deve ser válido conforme cadastro do contribuinte junto a prefeitura.
