---
article_id: 360026177871
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9c3bf9455ec47899e9fe22f2753567bdda80da99b7988268358e28c6d9dd7771
fetched_at: '2026-06-28T22:39:58.432324+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeicao
  335: Numero do RPS deve ser subsequente ao anterior enviado.'
type: support-article
updated_at: '2025-06-25T21:01:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026177871-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejeicao-335-Numero-do-RPS-deve-ser-subsequente-ao-anterior-enviado
---

**Dúvida**Rejeição 335: Numero do RPS deve ser subsequente ao anterior enviado.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Prefeituras que trabalham com modelo [DSFNET](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340) controlam a sequencia numérica do RPS.

Se a prefeitura espera receber o RPS número 1 por exemplo, não pode ser enviado o RPS 2 ou qualquer outro que não seja o 1, caso pule a sequencia será apresentado a rejeição 335.
