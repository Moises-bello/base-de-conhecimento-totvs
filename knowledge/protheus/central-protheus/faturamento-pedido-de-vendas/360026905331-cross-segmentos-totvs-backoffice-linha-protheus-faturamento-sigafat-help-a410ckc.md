---
article_id: 360026905331
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0648db6dcfd553eacf1e877a5479f42386841c15e5e6e2e7579673a33ab42084
fetched_at: '2026-06-28T22:38:41.030675+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Help A410CKCLRA no faturamento
type: support-article
updated_at: '2022-10-14T12:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026905331-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-A410CKCLRA-no-faturamento
---

**Ocorrência**

Help A410CKCLRA no faturamento

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) – A partir da versão 11.80  
  
**Causa**

Ao realizar a inclusão de um pedido de venda, o sistema retorna o Help **A410CKCLRA** informando que não é possível alterar o cliente/loja do Pedido de Vendas, pois o mesmo possui adiantamentos (RA) vinculados. Desvincule os adiantamentos antes de alterar o cliente/loja do Pedido de Vendas.

Essa mensagem ocorre por que existe Recebimento Antecipado vinculado ao cliente na tabela **SE1**.  
  
**Solução**

Para solucionar essa ocorrência, no Contas a Receber **FINA040** desvincule o RA do pedido de venda.

**Saiba Mais:**  
**[Vincular ou Desvincular R.A. à um Pedido de Vendas pela Rotina MATA410](http://tdn.totvs.com/pages/releaseview.action?pageId=267796506)**
