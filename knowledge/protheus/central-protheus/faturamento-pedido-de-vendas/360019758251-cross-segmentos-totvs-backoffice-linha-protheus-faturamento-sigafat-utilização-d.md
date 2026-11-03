---
article_id: 360019758251
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c7507fe41ab414cdd30f3ba4b7fbe3d877d95980927ffbe0f9eb605f06acbe85
fetched_at: '2026-06-28T22:38:41.058038+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Utilização da Rotina Controle de Reservas (MATA430)
type: support-article
updated_at: '2024-01-25T20:41:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019758251-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Utiliza%C3%A7%C3%A3o-da-Rotina-Controle-de-Reservas-MATA430
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**

Utilização da Rotina Controle de Reservas (**MATA430**)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 11.80  
  
  
**Solução**

A rotina Controle de reservas tem o objetivo de reservar quantidades de estoque de determinados produtos para que possam ser utilizadas nos pedidos de venda.

Geralmente, este recurso é utilizado para garantir a disponibilidade de estoque de determinado item antes da colocação dos pedidos de venda. Quando a reserva é colocada, a quantidade solicitada é empenhada nas tabelas de saldo de estoque, impedindo que o saldo seja consumido por outros processos que baixam ou reservam quantidades no estoque (pedidos, reservas, produções, movimentos internos entre outros).

A reserva pode ser efetuada **manualmente**, inserindo o registro no cadastro de reservas(**mata430**) e depois associando ao pedido através do campo **c6\_reserva**, ou efetuada de forma automática com o uso dos parâmetros **mv\_resest** (produtos sem lote) e **mv\_resaut** (produtos com lotes), geralmente utilizados para quando há bloqueio de crédito cliente, mas precisa garantir o produto para a venda.

Com relação a reserva de lotes, o sistema só permite reservar de forma manual um único lote por reserva, da mesma forma que no pedido somente uma reserva será associada por linha de item, através do campos c6\_reserva. Caso seja necessário vários lotes para compor a quantidade a ser vendida, valide a possibilidade do uso do **mv\_resaut** para reserva automática, após a liberação do pedido.

**Obs: Atendendo a este conceito, não é possível gerar reserva para Produto que não possui saldo em estoque.**

**Saiba Mais:**  
**[MATA430 Controle de Reservas B2\_RESERVA](https://tdn.totvs.com/x/P5AjDw)**
