---
article_id: 32369017561367
category: eConsignado (Crédito do Trabalhador)
content_hash: 6c5c7f9713c2bd88477b9cdf86f372941691338ccaa6d5987fa11598dc11cd84
fetched_at: '2026-06-28T22:43:07.192173+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo eConsigando rescisão não apresenta valor
  desconto
type: support-article
updated_at: '2026-02-06T19:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32369017561367-RH-Linha-Protheus-GPE-C%C3%A1lculo-eConsigando-rescis%C3%A3o-n%C3%A3o-apresenta-valor-desconto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32368994887831) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Por que cálculo eConsigando rescisão não apresenta valor desconto?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O cálculo eConsigando rescisão não apresenta valor desconto devido não ter base para calculo margem (sem base INSS).

**Exemplo:**

Em valores futuros verba 502 (verba natureza 9253) valor parcela 178,68.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32368994888727)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32369017549335)

Em rescisão saldo salário sim INSS 2.631,19 e valor desconto sim INSS 3.062,57 (soma desconto falta e desconto DSR). Como o desconto é superior ao provento, a rescisão não possui base INSS e por isso o cálculo não apresenta o valor desconto.

**Rescisão sem verba 502.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32369017549591)

**Saiba Mais:**Para adquirir maior conhecimento acesse o link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>
