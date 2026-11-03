---
article_id: 10822862254871
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b6c3ed49a4dbfd1b375453eb144d22c52ce52b91489693ce1e8080860283b741
fetched_at: '2026-06-28T22:38:42.592365+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Campo "C.M.V" na aba Rentabilidade da Planilha Financeira no Pedido de Vendas
type: support-article
updated_at: '2022-12-13T19:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10822862254871-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-C-M-V-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min**

**Dúvida**

Qual a base da estruturação do campo "C.M.V." na aba Rentabilidade da Planilha Financeira no Pedido de Vendas?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

A Coluna C.M.V (Custo de Mercadoria Vendida) é o custo Médio do Produto.

O valor exibido no C.M.V. é trazido de acordo com a moeda do pedido de venda.

* Se C5\_MOEDA == 1  o valor é trazido do produto B2\_CM1
* Se C5\_MOEDA == 2  o valor é trazido do produto B2\_CM2
* Se C5\_MOEDA == 3  o valor é trazido do produto B2\_CM3
* Se C5\_MOEDA == 4  o valor é trazido do produto B2\_CM4
* Se C5\_MOEDA == 5  o valor é trazido do produto B2\_CM5

**![](https://tdn.totvs.com/download/attachments/266963014/Planilha%20financeira.png?version=1&modificationDate=1475242983000&api=v2)**

**Dúvidas no cálculo gerador do campo B2\_CM1/2/3/4/5 contate a Equipe Protheus Estoque.**

**Saiba Mais:**

**[FAT0139 Processo para utilização de Rentabilidade no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/RojpDw)**
