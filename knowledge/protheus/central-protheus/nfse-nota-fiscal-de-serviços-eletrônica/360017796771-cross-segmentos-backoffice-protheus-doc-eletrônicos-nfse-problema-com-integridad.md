---
article_id: 360017796771
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d5bbb888351dbdb0dc882a05104196f7708134f6ba04b97528e441766639d4f4
fetched_at: '2026-06-28T22:39:56.207139+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Problema
  com integridade do arquivo :: INVALIDO_NAO_INTEGRO'
type: support-article
updated_at: '2025-07-18T14:40:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017796771-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Problema-com-integridade-do-arquivo-INVALIDO-NAO-INTEGRO
---

**Ocorrência**  
Rejeição ocorrida na transmissão de uma NFSE para a Prefeitura de Florianópolis: Problema com integridade do arquivo :: INVALIDO\_NAO\_INTEGRO

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**A rejeição ocorre devido conter carácteres especiais no conteúdo do XML, caracteres estes que a Prefeitura não consegue fazer a devida conversão.  
  
**Solução**É necessário remover os caracteres especiais contidos nos cadastros utilizados na nota. Feito isso, é necessário refazer o documento de saída e retransmitir a nota.
