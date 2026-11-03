---
article_id: 35366700317719
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0480bc9762f38aa5cf6039ee79dd0c70e55765f0448866d195efa8a5b2d8db24
fetched_at: '2026-06-28T22:39:57.572951+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Natureza
  de operação no XML x Configurador de tributos
type: support-article
updated_at: '2025-10-02T19:47:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35366700317719-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Natureza-de-opera%C3%A7%C3%A3o-no-XML-x-Configurador-de-tributos
---

**Dúvida**  
Ao emitir notas usando o configurador de tributos, a natureza de operação no XML não está mais respeitando o campo F4\_ISSST.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**  
O rdmake **NFSEXMLENV de 25-07-2025** em diante, passa a ler o campo **F4\_NATOPNF** para gerar a tag <tipotrib> no xml remessa, Natureza de Operação, **para ambientes que usam o configurador de tributos**.
