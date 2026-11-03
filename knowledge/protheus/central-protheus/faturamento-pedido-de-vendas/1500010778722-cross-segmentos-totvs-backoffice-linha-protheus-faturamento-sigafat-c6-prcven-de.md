---
article_id: 1500010778722
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ddd4370fff33c8bb8c8f4e7f4fb558ad1df996030ec7f6774d05b4caa93a85e7
fetched_at: '2026-06-28T22:38:41.189563+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- Faturamento (SIGAFAT) -
  C6_PRCVEN Devolução de Compras no Faturamento '
type: support-article
updated_at: '2021-05-17T20:07:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010778722-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-C6-PRCVEN-Devolu%C3%A7%C3%A3o-de-Compras-no-Faturamento
---

**Dúvida**Quando há devolução de Compras no Faturamento, o sistema mostra o valor unitário como liquido na linha do Pedido de Vendas, diferente da Nota de entrada que é valor unitário é o bruto .  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) – A partir da release 11.80.  
  
**Solução**O Pedido de Vendas possui tanto os campos de valor unitário bruto (sem desconto) como liquido (com desconto):

* Valor bruto está no campo **C6\_PRUNIT**
* Valor liquido está no campo **C6\_PRCVEN.**

Portanto, para que possa visualizar o valor unitário da NF entrada da mesma forma no Pedido de Vendas, o campo a ser visualizado deverá ser o **C6\_PRUNIT** (**preço de lista**) e não no campo **C6\_PRCVEN** (**preço venda**).  
  
Exemplo abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018242961/mceclip0.png)
