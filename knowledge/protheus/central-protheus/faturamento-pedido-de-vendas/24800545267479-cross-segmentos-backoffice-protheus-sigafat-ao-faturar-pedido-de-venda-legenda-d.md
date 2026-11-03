---
article_id: 24800545267479
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4166e3c6205be8f62d6b8dca4c70dbff1886d1b8a1c7bd2abe48e2b9e9b48faf
fetched_at: '2026-06-28T22:38:39.644128+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ao faturar pedido de venda,
  legenda do pedido de venda não ficou vermelha
type: support-article
updated_at: '2024-07-11T11:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24800545267479-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ao-faturar-pedido-de-venda-legenda-do-pedido-de-venda-n%C3%A3o-ficou-vermelha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24800545211543) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Ao faturar pedido de venda, legenda do pedido de venda não ficou vermelha, por quê?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O pedido de venda nem sempre ficará vermelho ao faturar. Isso ocorre, pois, o pedido de venda só ficara com a legenda "vermelha" se todos os seus itens, estiverem com o campo "Qtd. Vendida (C6\_QTDVEN)" igual a "Qtd. Entregue (C6\_QTDENT)", que é a quantia já faturada.

O pedido de venda após faturar pode ficar com a legenda amarela (caso uma parcela de itens esteja bloqueado por crédito ou estoque) ou verde (caso só uma parcela dos itens foi submetida a liberação e faturamento e a outra parte não).

**Exemplo 1:**

Pedido de venda:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 0
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 0

Ao liberar somente o item da linha 2 e só faturar ele:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 1
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 0

Resultado do Status do pedido de venda: **Verde** (nem todos os itens estão com a quantidade de venda igual a quantidade entregue)

**Exemplo 2:**

Pedido de venda:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 0
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 0

Ao liberar todos os itens de uma vez só, porém ao faturar, um item tinha em estoque e o outro não então ficou liberado, mas bloqueado por crédito, então só o item 1 foi faturado:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 1
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 0

Resultado do Status do pedido de venda: **Amarelo** (nem todos os itens estão com a quantidade de venda igual a quantidade entregue, mas todos os itens foram submetidos a liberação)

**Exemplo 3:**

Pedido de venda:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 0
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 0

Foi liberado todos os itens de uma vez só e todos foram faturados:

* Linha 1: C6\_QTDVEN = 1 | C6\_QTDENT = 1
* Linha 2: C6\_QTDVEN = 1 | C6\_QTDENT = 1

Resultado do Status do pedido de venda: **Verde** (Todos os itens estão com a quantidade de venda igual a quantidade entregue/faturada)
