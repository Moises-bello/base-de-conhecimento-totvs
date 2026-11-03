---
article_id: 360029400211
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fdf1aaf43e74767601b9c0d88e23bd661aee98310789e76ca4d338929d608b9b
fetched_at: '2026-06-28T22:42:42.182125+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Definição do número da Ordem de Produção
  quando criada por pedido de venda
type: support-article
updated_at: '2021-10-19T11:04:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029400211-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-do-n%C3%BAmero-da-Ordem-de-Produ%C3%A7%C3%A3o-quando-criada-por-pedido-de-venda
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Dúvida**Como é definido o número da **OP - Ordem de Produção** quando ela é criada pelo pedido de venda?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O processo do Sistema para definição do número da **OP** ocorre da seguinte forma:

1. Pode-se informar o número inicial no parâmetro **Numero Inicial OP?** da opção **Vendas**
2. Se não for preenchido o Sistema tentará assumir como número da **OP** o mesmo número do pedido
3. Caso encontre **OP** com o mesmo número do pedido de venda, assumirá o próximo na sequência das **OPs**.
