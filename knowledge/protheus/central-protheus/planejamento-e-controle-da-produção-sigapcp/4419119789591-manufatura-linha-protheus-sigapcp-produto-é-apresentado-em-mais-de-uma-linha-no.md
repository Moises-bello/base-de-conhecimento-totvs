---
article_id: 4419119789591
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3f525107e20659126240c117be749af3ac4bfec37cdd0b7bd9616556e6c94c72
fetched_at: '2026-06-28T22:42:45.753959+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Produto é apresentado em mais de uma
  linha no empenho
type: support-article
updated_at: '2022-01-14T14:20:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419119789591-Manufatura-Linha-Protheus-SIGAPCP-Produto-%C3%A9-apresentado-em-mais-de-uma-linha-no-empenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Quando o produto é apresentado em mais de uma linha no empenho numa mesma **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução** O produto é apresentado em mais de uma linha no empenho numa mesma **OP** quando o componente é um produto intermediário e tem saldo parcial, então em uma linha fica o empenho que irá consumir o saldo e em outra linha o restante para produção do item intermediário.   
Outra situação é quando o produto controla lote e existe um lote com saldo parcial, o restante da quantidade fica em outro linha que pode ser preenchido com outro lote caso tiver saldo disponível ou sem lote dependendo do cenário.
