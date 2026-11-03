---
article_id: 9458355337623
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 52d290519dd11c20ebe37b368ab77bc604123d2bfe19cadd9b4c96e3a98241fd
fetched_at: '2026-06-28T22:38:42.354832+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help "Pedido
  de Compra" na exclusão/alteração do Pedido de Vendas (MATA410)
type: support-article
updated_at: '2023-03-22T10:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9458355337623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Pedido-de-Compra-na-exclus%C3%A3o-altera%C3%A7%C3%A3o-do-Pedido-de-Vendas-MATA410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar incluir ou alterar um pedido de vendas (MATA410) o sistema apresenta uma mensagem "Pedido de Compra" questionando "Atualiza/exclui pedido de compra?"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**Essa mensagem deve ser apresentada sempre que houver um pedido de compras vinculado ao pedido de vendas através do campo "Ped.Compra" (**C6\_PEDCOM**).  
  
**Solução**Ao alterar o Pedido de Vendas (**MATA410**) com vínculo com o Pedido de Compras através do campo "Ped.Compra" (**C6\_PEDCOM**), o sistema questiona se deseja atualizar o pedido de compras também.

Optando por "Sim", o sistema realiza a atualização do pedido de compras automaticamente, optando por "Não", o sistema altera apenas o Pedido de Venda.

O mesmo acontece na exclusão do pedido de vendas com vínculo com o Pedido de Compras através do campo "Ped.Compra" (**C6\_PEDCOM**).
