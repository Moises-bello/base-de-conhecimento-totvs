---
article_id: 360026099252
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7e507bae24c9ff00ebe12cee0a29c406bb9115739c4408b8b70e8a8b68df6e4b
fetched_at: '2026-06-28T22:39:56.472266+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:
  INVALID PROPERTY CODMUNSIAFI '
type: support-article
updated_at: '2025-07-08T20:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026099252-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-INVALID-PROPERTY-CODMUNSIAFI
---

**Dúvida**Ao transmitir um RPS é apresentado em tela "INTERNAL SERVER ERROR : INVALID PROPERTY \_CODMUNSIAFI"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O erro ocorre quando o campo A1\_CODSIAF está em branco.  
Algumas prefeituras trabalham com o código do município de acordo com o SIAFI, portanto há necessidade de preenchimento do campo A1\_CODSIAF com o município do tomador conforme a tabela do SIAFI.  
Para **tomadores estrangeiros** preencha o campo com **9999.**  
Prefeituras que trabalham com os provedores DSFNET e IPM se enquadram nessa condição.
