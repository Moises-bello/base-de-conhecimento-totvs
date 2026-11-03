---
article_id: 20265962060183
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7fe3532732dcf0a698a7552b937fc4813d2218ab5aebec36625599f21bc556f6
fetched_at: '2026-06-28T22:42:44.616506+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - No estorno do apontamento via Execauto
  o saldo endereçado volta para o endereço original
type: support-article
updated_at: '2024-01-02T19:04:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20265962060183-Manufatura-Linha-Protheus-SIGAPCP-No-estorno-do-apontamento-via-Execauto-o-saldo-endere%C3%A7ado-volta-para-o-endere%C3%A7o-original
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20265962021399)***Tempo aproximado para leitura: **00:00:34 min  
  
Dúvida**Ao estonar o **apontamento de produção** através do **Execauto** da rotina, a quantidade requisitada volta para o endereço original?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para que o produto retorne ao endereço original, é preciso configurar o parâmetro **MV\_PDEVLOC -Define o tratamento quando ocorrer um estorno de movimento com controle de localização**, como **1 - Localização****original.**
