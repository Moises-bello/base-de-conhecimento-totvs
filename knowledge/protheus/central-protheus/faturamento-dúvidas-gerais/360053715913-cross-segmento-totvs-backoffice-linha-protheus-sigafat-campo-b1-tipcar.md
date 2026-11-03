---
article_id: 360053715913
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3531b2b16fde831ee1f35b5a18a9499998eb2ac3a1878566f3d9bedfbb82e357
fetched_at: '2026-06-28T22:38:28.512025+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campo B1_TIPCAR
type: support-article
updated_at: '2023-05-16T14:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053715913-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-B1-TIPCAR
---

**Dúvida**

Na utilização dos pedidos de venda com montagem de carga no modulo **SIGAOMS**, é preciso informar o Tipo de carga através do campo **B1\_TIPCAR** no cadastro do produto. Existe a possibilidade de dessa informação ser exibida no Pedido de Venda (**MATA410**)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O pedido de venda não utiliza o campo **B1\_TIPCAR** no padrão de Faturamento, por isso não é apresentada a informação , e não há campo na tabela **SC6** que trate a informação em questão, o campo somente é utilizado nas rotinas de carga do OMS através da tabela **DB0**.  
  
Para utilização no pedido seria necessário a criação de um campo de usuário nos itens do Pedido e utilizar o ponto de entrada **m410liok** (**<https://tdn.totvs.com/pages/viewpage.action?pageId=6784149>**) para seu preenchimento.
