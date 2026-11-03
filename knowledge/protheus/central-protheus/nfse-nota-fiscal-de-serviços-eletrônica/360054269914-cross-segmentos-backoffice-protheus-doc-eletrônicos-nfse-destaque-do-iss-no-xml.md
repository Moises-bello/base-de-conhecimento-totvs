---
article_id: 360054269914
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a42ee6a2737a70dacf5893ee49db3b612e0eeb61c4f1b49bb1b80b0ed44dfd30
fetched_at: '2026-06-28T22:39:56.189896+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DESTAQUE
  DO ISS NO XML DO RPS
type: support-article
updated_at: '2025-07-08T20:03:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054269914-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DESTAQUE-DO-ISS-NO-XML-DO-RPS
---

**Dúvida**Qual a regra de destaque do ISS no XML do RPS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para **ISS retido** (F3\_RECISS=1), o rdmake NFSEXMLENV considera:  
Valor ISS = F3\_VALICM  
Alíquota ISS = D2\_ALIQISS  
  
Para **ISS a recolher** (F3\_RECISS=2), o rdmake NFSEXMLENV considera:  
Valor ISS = CD2\_VLTRIB   
Alíquota ISS = CD2\_ALIQ  
  
***Observação***  
Vale lembrar que mesmo que os valores estejam populados nas tabelas citadas, o destaque dessas tags varia de acordo com o layout de RPS e regras de legislação da prefeitura em questão.  
Exemplo: Prefeitura de São Paulo - A tag de <ValorIss> não existe no RPS, somente a <AliquotaServicos>.
