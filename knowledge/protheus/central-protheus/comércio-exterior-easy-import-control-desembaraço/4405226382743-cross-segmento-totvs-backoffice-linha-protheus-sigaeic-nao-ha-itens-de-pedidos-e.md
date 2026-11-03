---
article_id: 4405226382743
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: f367d28ec186cca46e9baf505117b0fe7e23f807e07ac5fbb161026582cf1f6f
fetched_at: '2026-06-28T22:39:50.125731+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Nao ha itens de
  pedidos e p.l.i.s para esse fornecedor e moeda
type: support-article
updated_at: '2022-07-20T21:10:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405226382743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Nao-ha-itens-de-pedidos-e-p-l-i-s-para-esse-fornecedor-e-moeda
---

**Dúvida**Ao tentar selecionar a invoice na rotina de Desembaraço o sistema exibe a mensagem "**AVG0000706 -Nao há Itens de Pedidos e P.L.I.s para esse Fornecedor e Moeda**". O que necessário para que esta mensagem não seja exibida e que seja possível incluir a invoice?

![PLI.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405226737175/PLI.PNG)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Verifique os pontos abaixo:  
- No Purchase Order se o fornecedor informado (W2\_FORN) é o mesmo informado no desembaraço.   
- Se a moeda informada no Purchase Order esta como moeda Nacional (R$) no campo Moeda (W2\_MOEDA) ou diferente da informada na Invoice.  
- Se o item na PO esta como anuente e não houve a inclusão da PLI, caso o item não seja anuente realizar a alteração na Purchase Order  
![](https://totvssuporte.zendesk.com/attachments/token/VvVy5ejUrd7XzYPkqZLvglc0o/?name=inline-638068289.png)
