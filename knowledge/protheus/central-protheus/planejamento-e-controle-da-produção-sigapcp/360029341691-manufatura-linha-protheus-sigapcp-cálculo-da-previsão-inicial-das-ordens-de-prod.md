---
article_id: 360029341691
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 14e4565b322768498da0c535c43d510fcfaeaa69b4f2e1cdd5c75f5e8fac8db5
fetched_at: '2026-06-28T22:42:40.935026+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Cálculo da previsão inicial das Ordens
  de Produção Intermediárias '
type: support-article
updated_at: '2022-04-01T13:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029341691-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-previs%C3%A3o-inicial-das-Ordens-de-Produ%C3%A7%C3%A3o-Intermedi%C3%A1rias
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:40 min****Dúvida**Como o Sistema calcula a previsão inicial das **Ordens de Produção Intermediárias**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O cálculo para a previsão inicial das **Ordens de produção intermediárias** leva em consideração a previsão inicial da **OP - Ordem de Produção**pai menos o prazo de entrega do item intermediário na estrutura.   
  
Por exemplo:  
**OP** pai com previsão inicial para 25/06/2019 e item intermediário com prazo de entrega de 20 dias, neste caso a **OP** intermediária terá a previsão inicial para 05/06/2019.
