---
article_id: 4403752913687
category: Faturamento - Cadastros
content_hash: dc3ee58de833c5b2e69572ef97f07df8b017724f1295de6c334c9856a82b2b0e
fetched_at: '2026-06-28T22:38:35.291008+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help Cond.Pagto
type: support-article
updated_at: '2021-07-05T19:13:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403752913687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Cond-Pagto
---

**Dúvida**Ao preencher o campo Cond.Pagto (**E4\_COND**) com as parcelas para a condição do tipo 9, é gerado o Help: Cond.Pagto

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403752774295/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT Todas as versões  
  
**Solução**

O Help ocorre porque para a condição de pagamento tipo 9, o campo **Cond.Pagto** (**E4\_COND**) só irá receber as opções **Zero(0)** ou  **Percentual(%)**, onde:

* **Zero(0)** - para que os parcelamentos sejam considerados em valor moeda;
* **Símbolo %** - para utilizar os campos Parcelas do arquivo de Pedidos de Vendas como percentuais a serem parcelados.

As parcelas somente serão definidas no cabeçalho do **pedido de venda** (**MATA410**) ou **orçamento de venda (MATA415**).

**Saiba Mais sobre condição do tipo 9: [Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)- Condição de Pagamento Tipo 9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176512-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-9)**
