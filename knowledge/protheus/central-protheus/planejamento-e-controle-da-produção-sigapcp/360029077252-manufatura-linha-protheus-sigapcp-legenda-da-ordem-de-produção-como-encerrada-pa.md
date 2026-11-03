---
article_id: 360029077252
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 31b8ecb553b2b0e1c8ddbcf0d655698248d5b6031c4f0b385c1b3ae132a3b096
fetched_at: '2026-06-28T22:42:43.503043+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Legenda da ordem de produção como encerrada
  parcialmente
type: support-article
updated_at: '2021-11-05T20:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029077252-Manufatura-Linha-Protheus-SIGAPCP-Legenda-da-ordem-de-produ%C3%A7%C3%A3o-como-encerrada-parcialmente
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Dúvida**Quando a **OP - Ordem de Produção** fica com o **status** ou **legenda** de **Encerrada Parcialmente** na rotina **MATA650 - Ordens de Produção**?   
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema considera a **OP** como **Encerrada Parcialmente**quando a quantidade produzida é menor do que a quantidade da **OP**que foi encerrada.   
  
**Exemplo**  
Uma **OP**cuja quantidade são 80 peças. A **OP** teveapontamento total de 51,50 e uma perda de 28,50.  
Neste caso, como a **OP** possui perda, o Sistema irá considerar como **Encerrada Parcialmente**, já que o que foi produzido é inferior à quantidade da **OP**.
