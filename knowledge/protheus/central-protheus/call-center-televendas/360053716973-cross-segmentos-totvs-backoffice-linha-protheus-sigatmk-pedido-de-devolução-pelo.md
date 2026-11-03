---
article_id: 360053716973
category: Call Center - Televendas
content_hash: 8e0f8ec38be2ba25b1ba9a7164a27e320ee661f96a0a203587d999fcfa7192aa
fetched_at: '2026-06-28T22:41:30.316274+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Pedido de Devolução
  pelo Call Center
type: support-article
updated_at: '2022-06-22T19:03:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053716973-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Pedido-de-Devolu%C3%A7%C3%A3o-pelo-Call-Center
---

**Dúvida**

Ao efetuar um atendimento no Call Center com TES de Devolução e  integrar ao Pedido de Vendas (**MATA410**) no módulo de faturamento,  o tipo do pedido criado fica igual a Normal e não como Devolução . Como efetuar um pedido de devolução via Call Center ?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- todas as versões.  
  
**Solução**

O módulo Call Center somente efetua pedido do tipo **venda**, não há hoje, tratamento no sistema para efetuar pedido do tipo **Devolução de Compras** , a Devolução de compras somente é efetuada via pedido de venda.  
  
Conforme a própria documentação oficial do módulo, **<https://tdn.totvs.com/display/PROT/Call+Center+-+Protheus+12>****,** o objetivo do módulo Call Center é ser centro de atendimento combinando um banco de dados centralizado e um sistema de distribuição automática de chamadas. Além disso, a integração da automação de telefonia no processo de negócios e atendimento a clientes, otimizando e permitindo melhores serviços.

O atendimento **Televendas (TMKA273)** não trabalha integrado ao módulo de compras, por isso não trata devolução.

Saiba mais sobre o uso da rotina Televendas e o fluxo de processos:  
  
Televendas - Vendas por telefone gerando orçamentos, pedidos de vendas e faturamentos. ([**https://tdn.totvs.com/pages/viewpage.action?pageId=341226861**](https://tdn.totvs.com/pages/viewpage.action?pageId=341226861))  
  
Fluxo dos processos de televendas  e descrição de uso: **<https://tdn.totvs.com/pages/viewpage.action?pageId=341227201>**
