---
article_id: 360028246611
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 577fa4614fb90e550bc99a5c6d950311d4af21d67d575c37bcfb18bbb26c0143
fetched_at: '2026-06-28T22:39:52.256249+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEIC - É possível vincular
  tabela de preço na solicitação de importação?
type: support-article
updated_at: '2025-04-08T18:24:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028246611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-%C3%89-poss%C3%ADvel-vincular-tabela-de-pre%C3%A7o-na-solicita%C3%A7%C3%A3o-de-importa%C3%A7%C3%A3o
---

**Dúvida**É possível vincular a tabela de preço na Solicitação de Importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Na solicitação de importação não é possível realizar vinculação da tabela de preços, porém na rotina Produto x Fornecedor (MATA061) pode-se informar o campo Vlr.Cotaçao (A5\_VLCOTUS).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028183892/mceclip1.png)

Para preencher o mesmo é necessário informar o campo Moeda Utiliz (A5\_MOE\_US):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028184172/mceclip2.png)

Ao incluir a Solicitação de Importação (EICSI400), informe a Moeda, Produto, Fornecedor e Fabricante desta forma o campo Preco Unit**.** (W1\_PREÇO) será preenchido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028184972/mceclip3.png)

**Observação:** Caso não tenha o campo Moeda informado na Solicitação de Importação (EISI400), ao incluir a Purchase Order e informar o campo Moeda (W2\_MOEDA), o Preco Unit**.** (W3\_PRECO) do item será preenchido automaticamente.
