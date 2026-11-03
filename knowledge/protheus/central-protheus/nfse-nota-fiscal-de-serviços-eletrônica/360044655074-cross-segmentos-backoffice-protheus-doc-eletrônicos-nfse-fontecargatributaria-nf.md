---
article_id: 360044655074
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 4a7948b7afa5b71b9babc9ccbc8b876ed522f237ac4fe065fb5e527557fef7b7
fetched_at: '2026-06-28T22:39:57.443297+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - FonteCargaTributaria
  NFSE de São Paulo-SP
type: support-article
updated_at: '2025-07-08T19:41:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044655074-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-FonteCargaTributaria-NFSE-de-S%C3%A3o-Paulo-SP
---

**Dúvida**Qual o procedimento para preenchimento da tag FonteCargaTributaria da NFSE de São Paulo-SP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O parâmetro MV\_CRGTRIB deve ser habilitado.  
O Parâmetro MV\_MSGTRIB deve possui conteúdo 1 ou 3.  
A fonte deve ser informada no MV\_FNTCTRB, mas se o parâmetro estiver sem conteúdo, a tag será gerada com conteúdo default IBPT.
