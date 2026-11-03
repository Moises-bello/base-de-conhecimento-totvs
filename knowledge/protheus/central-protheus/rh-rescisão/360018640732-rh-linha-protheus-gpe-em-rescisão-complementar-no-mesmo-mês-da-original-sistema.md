---
article_id: 360018640732
category: RH - Rescisão
content_hash: 46257f9105e042ba66d03deb7fca87d47467f4656d99813ae95aadfcb5b519d2
fetched_at: '2026-06-28T22:43:49.712781+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Em Rescisão Complementar no mesmo mês da original,
  sistema demonstra novamente as verbas já calculadas na rescisão anterior
type: support-article
updated_at: '2025-04-16T18:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018640732-RH-Linha-Protheus-GPE-Em-Rescis%C3%A3o-Complementar-no-mesmo-m%C3%AAs-da-original-sistema-demonstra-novamente-as-verbas-j%C3%A1-calculadas-na-rescis%C3%A3o-anterior
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26561323997079)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao calcular rescisão complementar no mesmo mês da original ou uma segunda complementar no mesmo período, sistema demonstra novamente as verbas já calculadas na rescisão anterior do mesmo período.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É normal que no cálculo da rescisão complementar no mesmo mês da original ou no cálculo de uma segunda complementar no mesmo período o sistema demonstre novamente as verbas já calculadas na rescisão anterior dentro do mesmo período.

Por ser uma rescisão no mesmo período, o sistema irá demonstrar no cálculo da rescisão complementar os valores já pagos na rescisão anterior mais o que esta sendo pago na complementar, porém será calculada a verba de ID 0303-Liquido da Rescisão Anterior (Para Rescisão Complementar no Mesmo Mês da Original ou uma segunda complementar dentro do mesmo período), que é uma verba de desconto, ela terá o valor do Liquido Rescisão da rescisão original, abaixo exemplo:

Rescisão Original:

![Rescis_o_Original.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014503492)

Rescisão Complementar onde carregou todas as verbas da Rescisão Original mais a Diferença paga na complementar (verba 210) e trouxe a verba de ID 0303 no mesmo valor do Liquido da Rescisão Original (verba 522) e o Liquido Rescisão complementar (verba 428).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014549311)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
