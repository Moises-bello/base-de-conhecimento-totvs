---
article_id: 360036181594
category: Financeiro - Contas a Pagar
content_hash: f67da87fe77110778edf566bdb2925c712d88159426fa17ea9fa702237fe71a2
fetched_at: '2026-06-28T22:38:06.974600+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA080 - Baixa de títulos
  em borderô
type: support-article
updated_at: '2023-08-03T14:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036181594-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Baixa-de-t%C3%ADtulos-em-border%C3%B4
---

**Dúvida**Posso fazer uma baixa manual de um titulo que se esteja em borderô?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da versão 11

**Solução**Sim, é possível baixar um título a pagar mesmo que esteja em borderô.

A rotina de Baixas Pagar Manual permite a baixa total de um título mesmo que em borderô. Antes é necessário ativar o parâmetro a seguir:

1. Na rotina de baixa a pagar – FINA080 – Pressione a tecla F12  
  
2. Altere a pergunta (Permite Baixa Bord?) Para Sim

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047340014/mceclip3.png)

Dessa forma o título vinculado ao borderô pode ser baixado normalmente. Para títulos que estejam em borderô, é permitida somente a baixa total na rotina Baixa Pagar Manual - **FINA080**.

**Importante**

Caso a pergunta esteja como Não, além do título não poder ser baixado pela rotina de baixa manual será apresentado a *HELP* abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048228153/mceclip1.png)

**Saiba mais**Baixa de títulos em borderô: <https://tdn.totvs.com/pages/releaseview.action?pageId=185731640>
