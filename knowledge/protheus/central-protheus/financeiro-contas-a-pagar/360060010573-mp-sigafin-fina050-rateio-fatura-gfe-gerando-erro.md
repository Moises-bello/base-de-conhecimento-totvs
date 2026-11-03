---
article_id: 360060010573
category: Financeiro - Contas a Pagar
content_hash: 1f2afeec04a8637a49c28072cbe1b40b0a0d3cf7d1028866e121ffc3c336e53d
fetched_at: '2026-06-28T22:38:09.870462+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA050 – Rateio Fatura GFE gerando erro
type: support-article
updated_at: '2021-04-28T15:18:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060010573-MP-SIGAFIN-FINA050-Rateio-Fatura-GFE-gerando-erro
---

**Ocorrência**

Temos uma fatura no GFE que possui rateio contábil, ao tentar atualizar

invalid field name in Alias TMP->CTJ\_DEBITO on FA050TUDCT

E2\_RATEIO := S < -- Invalido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098567734/mceclip0.png)  
  
  
  
**Ambiente**Microsiga Protheus - Financeiro - A partir da versão 12.1.17  
  
**Causa**

**Falta de preencher parâmetro F12 rotina FINA050,** terceira pergunta (FIN0503) Informação de contas no rateio

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

Acessar a rotina **FINA050,** pressionar **F12** na rotina:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098567774/mceclip1.png)

Deixar a terceira pergunta (FIN0503) Informação de contas no rateio, como sim.

Dessa forma não apresentara o erro acima na rotina da fatura de frete.
