---
article_id: 360025224412
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6633bbaeeafb02d877228620911e5b65541654f3a8addc34781cf5bf56f2c342
fetched_at: '2026-06-28T22:38:38.523656+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Finalidade da
  rotina de Liberação de Pedido de Venda-Desconto em Cascata
type: support-article
updated_at: '2023-08-15T14:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025224412-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Finalidade-da-rotina-de-Libera%C3%A7%C3%A3o-de-Pedido-de-Venda-Desconto-em-Cascata
---

**Dúvida**

O sistema não está aplicando o desconto em cascata no orçamento ou pedido de venda, utilizando os campos de cabeçalho do pedido.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**  
Para que o sistema aplique o desconto em cascata, seja no orçamento (mata415) ou no pedido de venda (mata410), utilizando os campos de cabeçalho (CJ\_DESC1 a 4 ou C5\_DESC1 a 4), é necessário que haja preço de lista, seja no produto (B1\_PRV1) ou utilizando tabela de preço (OMSA10) no orçamento ou pedido de venda.

A utilização do preço de lista será demonstrada através dos campos CK\_PRUNIT ou C6\_PRUNIT.

Uma vez que o campo de preço de lista está preenchido, o sistema acatará o percentual de desconto para o orçamento ou pedido.
