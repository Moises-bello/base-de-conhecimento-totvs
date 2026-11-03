---
article_id: 360026660293
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b05e7666298fb299ba46eb0a279cd969b9d89014d29d6b6d5a836502635720c9
fetched_at: '2026-06-28T22:38:30.082953+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - Como
  realizar a emissão de Nota Fiscal de Saída com complemento de frete?
type: support-article
updated_at: '2023-03-24T18:57:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026660293-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Como-realizar-a-emiss%C3%A3o-de-Nota-Fiscal-de-Sa%C3%ADda-com-complemento-de-frete
---

**Dúvida**

Como realizar a emissão de Nota Fiscal de Saída com complemento de frete?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

No módulo faturamento, não há a opção de Complemento de frete, o processo correto é gerar um pedido de vendas (**MATA410**) como Complemento de preço, mas não é preciso informar o valor e o tipo do frete no cabeçalho do pedido (**SC5**). 

É necessário que informe o produto utilizado na NF original e deixe o campo "Quantidade" (C6\_QTDVEN) em branco, preencha o preço unitário informando o valor que deseja, e depois preencha o campo Valor total com o mesmo valor do preço unitário, lembre-se de utilizar um **TES** que não atualiza (estoque) e por ultimo realizar amarração da nota original no pedido. 

Saiba Mais:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de Pedido de Vendas do Tipo Complemento de Preço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017608012-MP-FAT-Inclus%C3%A3o-de-Pedido-de-Vendas-do-Tipo-Complemento-de-Pre%C3%A7o?source=search)

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Nota complemento de despesas acessórias (frete, seguro,despesa) da nota de devolução de compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026549773-MP-FAT-Nota-complemento-de-frete-da-nota-de-devolu%C3%A7%C3%A3o-de-compra)**
