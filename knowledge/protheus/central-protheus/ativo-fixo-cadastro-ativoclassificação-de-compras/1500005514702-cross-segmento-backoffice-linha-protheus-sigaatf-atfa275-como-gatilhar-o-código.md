---
article_id: 1500005514702
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 5b4c525f57f77037819c5a9356cdecc1237aae57a342a0f052ba994c4809b4f8
fetched_at: '2026-06-28T22:41:48.400192+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA275 - Como gatilhar
  o código (N1_CBASE)  sequencial automaticamente no ATFA012
type: support-article
updated_at: '2023-11-30T17:01:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005514702-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA275-Como-gatilhar-o-c%C3%B3digo-N1-CBASE-sequencial-automaticamente-no-ATFA012
---

**Dúvida**  
Como gatilhar o código (N1\_CBASE) sequencial automaticamente no ATFA012?

**Ambiente**MP - SIGAATF - ATFA275

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. **Na rotina ATFA275, INCLUA UM GRUPO:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007493441)  
2. Ao incluir um bem na rotina ATFA012, utilizando o grupo 002, no exemplo acima, o próximo código será: "003"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007493661)

Saiba Mais:

<https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa275_config_grupo.htm>
