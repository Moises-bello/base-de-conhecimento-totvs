---
article_id: 360026661992
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 732ce00a285e4efface461311dbd16bca94969cac30652198d54b2ae8bf17652
fetched_at: '2026-06-28T22:42:40.812207+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento de produção por grade
type: support-article
updated_at: '2024-01-08T22:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661992-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-de-produ%C3%A7%C3%A3o-por-grade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quando se utiliza o conceito de grade no cadastro de produtos, é necessário apontar cada **OP - Ordem de produção** individualmente ou é possível apontar toda a grade de uma única vez?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No apontamento de produção via **MATA250 - Apontamento Simples** é possível apontar o conjunto de **OPs - Ordens de Produção** em um único processo.  
  
Para isso execute os passos abaixo:  
1. No campo **D3\_OP - Ord Producao** preencha o número da **OP** composto de Número da **OP** , Item e Sequencia, sem informar a grade  
2. No campo **D3\_QUANT - Quantidade** informe a quantidade total que deseja apontar. Neste momento, o Protheus abre a tela para que seja informada a quantidade de cada grade. O total da quantidade apontada em cada grade deve corresponder à quantidade informada no campo **D3\_QUANT**.
