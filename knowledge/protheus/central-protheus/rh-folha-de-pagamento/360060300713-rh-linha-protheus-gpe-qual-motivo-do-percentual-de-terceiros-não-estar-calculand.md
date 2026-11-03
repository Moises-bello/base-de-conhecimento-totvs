---
article_id: 360060300713
category: RH - Folha de Pagamento
content_hash: 7a45d1e5cf9234f863ff361124bbfccf561eac6a5195a86e576e9ba9434e361d
fetched_at: '2026-06-28T22:44:16.242932+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Qual motivo do percentual de Terceiros não estar
  calculando para a folha de pagamento, verba de ID 0149
type: support-article
updated_at: '2025-08-12T13:20:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060300713-RH-Linha-Protheus-GPE-Qual-motivo-do-percentual-de-Terceiros-n%C3%A3o-estar-calculando-para-a-folha-de-pagamento-verba-de-ID-0149
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354140712215) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Qual motivo do percentual de Terceiros não estar calculando para a folha de pagamento, verba de ID 0149?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Sistema valida o cadastro da tabela **S038 - Outras Entidades** para o cálculo do percentual de terceiros. Irá validar o percentual de Terceiros - os percentuais de Outras Entidades (SESI/SENAI/etc), ou seja, quando o percentual de terceiros está cadastrado com 5,8% e a soma dos percentuais de outras entidade também é o valor de 5,8%, o Sistema entende que já está sendo calculado o percentual de terceiros completo nas verbas de outras entidades, por este motivo a verba de ID 0149 não é gerada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101297313)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101297393)

Caso o percentual de terceiros esteja cadastrado com 5,8% e a soma dos percentuais de outras entidade der um total, por exemplo, de 3%, o sistema calculará 2,8% para o percentual de terceiros na verba de ID 0149.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000199821)![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000200161)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
