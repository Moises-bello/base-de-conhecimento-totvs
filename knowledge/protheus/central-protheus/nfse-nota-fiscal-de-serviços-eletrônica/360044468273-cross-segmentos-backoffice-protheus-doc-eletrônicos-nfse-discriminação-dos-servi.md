---
article_id: 360044468273
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 45910da3c36385644288b82725da87050be3963b4ecf5bd97ea5b9d4ee172fbb
fetched_at: '2026-06-28T22:39:56.459932+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Discriminação
  dos serviços NFTS
type: support-article
updated_at: '2025-07-18T14:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044468273-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Discrimina%C3%A7%C3%A3o-dos-servi%C3%A7os-NFTS
---

**Dúvida**Qual a origem da discriminação dos serviços gravada na NFTS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O rdmake NFSEXML102 é o responsável por montar o xml da NFTS.  
A tag **<DiscriminacaoServico>** é gerada com o conteúdo do campo **B1\_DESC**.
