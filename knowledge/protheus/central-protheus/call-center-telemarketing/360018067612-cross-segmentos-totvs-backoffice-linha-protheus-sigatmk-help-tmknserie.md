---
article_id: 360018067612
category: Call Center - Telemarketing
content_hash: e9731642c214bba5af116d3b2b0abe2fbc64cfa3d8a13cf6f05e21ce6498cab9
fetched_at: '2026-06-28T22:41:29.417472+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- HELP TMKNSERIE
type: support-article
updated_at: '2022-06-22T18:01:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018067612-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-HELP-TMKNSERIE
---

**Dúvida**

Ao confirmar o atendimento telemarketing (**TMKA272**) para a geração da OS (**TECA450**) através do Call Center, é gerado o Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049760094/mceclip0.png)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Todas as versões  
  
**Solução**

O Help ocorre por que o produto a ser utilizado como base de atendimento precisa ter uma série informada no campo **UD\_NSERIE**(Num.Serie) , após informar a série o sistema verificará se esta série existe e caso não exista, irá exibir uma mensagem infirmando que a série será criada para poder efetuar a integração entre Call Center e Gestão de Serviços.

![UD_NSERIE_x_OS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049762114/UD_NSERIE_x_OS.gif)
