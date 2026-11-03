---
article_id: 4403910675607
category: Financeiro - Movimentação Bancária
content_hash: e4b5d1e198e9dde1dd74a697170178fc7d3ac777aa1330f8f3c4a3630cb37410
fetched_at: '2026-06-28T22:38:19.389518+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN -  FINA100 - HELP : SEMPERM'
type: support-article
updated_at: '2024-04-16T15:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403910675607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-HELP-SEMPERM
---

**Ocorrência**Ao Cancelar um movimento bancário a Pagar ou a Receber é apresentado o Help : SEMPERM

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403910526743/mceclip0.png)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA100 - A partir da 12.1.17  
  
**Causa**  
Esse incidente ocorre, após retirar a permissão de acesso 52 e 53 do modulo Financeiro.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403910571799/mceclip1.png)   
  
**Solução**Para que não apresente o help será necessário deixar os acessos para o usuário.

**Importante**  
Mesmo após a retirada somente do acesso **53** também será bloqueado o cancelamento de movimentações a Receber via **FINA100**, pois está tratando como movimentação bancaria.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403904315031/mceclip2.png)

**Saiba mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=221546134>
