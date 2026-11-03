---
article_id: 360052864813
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 929fcab1d458b687d3746edebcc6bad930443014703514d95d0d007f07c408a5
fetched_at: '2026-06-28T22:42:42.179144+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Definição do item da Ordem de Produção
  quando criada por pedido de venda
type: support-article
updated_at: '2022-02-16T17:43:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052864813-Manufatura-Linha-Protheus-SIGAPCP-Defini%C3%A7%C3%A3o-do-item-da-Ordem-de-Produ%C3%A7%C3%A3o-quando-criada-por-pedido-de-venda
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:45 min  
  
Dúvida**Como é definido o item da **OP - Ordem de Produção** quando ela é criada pelo **pedido de venda**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O número do item da **OP** é definido pela quantidade de produtos cadastrados no pedido de venda. O Sistema inclui **OPs** com a mesma numeração, porém com itens diferentes.  
  
**Exemplo**Há mais de um produto no pedido de venda:Item 01: Produto AItem 02: Produto B  
  
Ao abrir a **OP** por **pedido de venda** para o **item 01** do pedido será gerado um código, por exemplo, 101010 **01** 001.  
Ao abrir a **OP** para o **item 02** do pedido será gerado um código, por exemplo, 101010 **02** 001.
