---
article_id: 8286690423319
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c5b85361f944d9bd2191a1a9fdc234d043d58975f8de3ac154d9e305b3c6cf35
fetched_at: '2026-06-28T22:42:42.187979+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Descontar a perda da quantidade no
  apontamento
type: support-article
updated_at: '2022-08-19T17:41:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8286690423319-Manufatura-Linha-Protheus-SIGAPCP-Descontar-a-perda-da-quantidade-no-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Ao informar uma **Perda** no **MATA250** o Sistema desconta essa informação do campo **Quantidade**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No campo **D3\_QUANT** a deve ser informado a quantidade de peças/unidades... produzidas.  
E no campo **D3\_PERDA** a quantidade que foi perdida.  
Esses campos trabalham de forma individual, ou seja, a quantidade informada no campo **D3\_PERDA** não irá descontar da informada no campo **D3\_QUANT.**  
  
**Glossário**  
**D3\_QUANT** - Quantidade  
**D3\_PERDA** - Perda  
**MATA250** - Produção Simples
