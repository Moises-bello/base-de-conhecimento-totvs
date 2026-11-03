---
article_id: 4414622313623
category: NFe - Nota Fiscal Eletrônica
content_hash: 62350d8fe03fc3fc9b99f3c530991526e56bce92c99f125d5c4c7078df6c482c
fetched_at: '2026-06-28T22:40:07.200219+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - WSCERR063 / Argument
  error : Missing field ENVIACCEPDF'
type: support-article
updated_at: '2025-06-30T19:23:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414622313623-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-WSCERR063-Argument-error-Missing-field-ENVIACCEPDF
---

**Dúvida**Como solucionar o erro WSCERR063 / Argument error : Missing field ENVIACCEPDF   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao tentar transmitir o exportar o XML ocorre o erro ***WSCERR063 / Argument error : Missing field ENVIACCEPDF***

***1. Aplique a**patch no Protheus de acordo com sua release:*

*Patch Protheus 12.1.2210 - <https://suporte.totvs.com/portal/p/10098/download#detail/1081419>*

*Patch Protheus 12.1.2310 -*<https://suporte.totvs.com/portal/p/10098/download#detail/1124963>

*Patch Protheus 12.1.2410 - <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>*

*2. Realize atualização do **TSS de acordo com a sua release:**  
  
[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)*

3. Após isso, ***transmita ou exporte a CC-e.***
