---
article_id: 360047411193
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a288ce216d7897fb5db0d6b11546b900e9ec0489bc524bb1b4d4a7b7508656a2
fetched_at: '2026-06-28T22:38:38.656016+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Qual a funcionalidade
  do parâmetro MV_GERABLQ na Liberação do Pedido de Venda ?
type: support-article
updated_at: '2022-06-02T11:03:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047411193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-a-funcionalidade-do-par%C3%A2metro-MV-GERABLQ-na-Libera%C3%A7%C3%A3o-do-Pedido-de-Venda
---

**Dúvida**

Qual a funcionalidade do parâmetro MV\_GERABLQ na Liberação do Pedido de Venda ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O parâmetro **MV\_GERABLQ** determina se o sistema deve **gerar bloqueio** **de estoque** para **produtos** que **controlam rastro** ou **localização**.

Ao incluir um pedido com um produto que controle rastro ou localização, e a **quantidade inserida** for **maior** do que a **disponível em estoque**:

* **MV\_GERABLQ = S**: O sistema **libera o pedido** (**grava registro na tabela  SC9**), porém **bloqueia** o pedido por **estoque**;
* **MV\_GERABLQ = N**: O sistema **não permite** a **liberação do pedido** (**não grava registro na tabela SC9).**
