---
article_id: 13312495571735
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9d1bb5884a8937bb67529979f9034602de8afc1f1354cc0dd4617c4a3dd2431f
fetched_at: '2026-06-28T22:38:42.762628+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pedido "Tipo
  D - Devolução de compra" não gera título no "Contas a Receber"
type: support-article
updated_at: '2023-03-23T20:41:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13312495571735-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pedido-Tipo-D-Devolu%C3%A7%C3%A3o-de-compra-n%C3%A3o-gera-t%C3%ADtulo-no-Contas-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por qual motivo pedidos do "Tipo D - Devolução de compra" não estão gerando título no "Contas a Receber"?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões

**Solução**A devolução de compras (C5\_TIPO = D), ao faturar (com a **TES do pedido com o campo "F4\_DUPLIC = Sim")** gera títulos [SE2] no "Contas A Pagar".

Quando a mercadoria entra no Protheus pelo documento de entrada, é gerado um título no "Contas A Pagar" do tipo "NF".

Quando devolvemos essa entrada, é gerado também um par atrelado no "Contas A Pagar", só que agora do tipo "NDF" de mesmo valor para abater o saldo e ajustar:

![ExemploNDF.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13312300515479)

O sistema internamente abate o valor que saiu com o que entrou, baixando o saldo (NDF - NF = 0).

**OBSERVAÇÃO:** "NDF" significa "Nota de Devolução ao Fornecedor".
