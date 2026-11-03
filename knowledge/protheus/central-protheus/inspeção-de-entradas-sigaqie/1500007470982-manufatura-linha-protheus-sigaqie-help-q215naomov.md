---
article_id: 1500007470982
category: Inspeção de Entradas (SIGAQIE)
content_hash: 044ae55caae6d3f70db6cbfac5361ee7f5cfc801eb3f58be8f8a65daffa50179
fetched_at: '2026-06-28T22:42:27.021832+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - HELP Q215NAOMOV
type: support-article
updated_at: '2021-05-06T14:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007470982-Manufatura-Linha-Protheus-SIGAQIE-HELP-Q215NAOMOV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**  
**Ocorrência**Ao tentar realizar o estorno na rotina **QIEA215 - Resultados** em **Outras Ações > Estorno C.Q.** ocorre o *help* **Q215NAOMOV - Não existe movimentação de Estoque para esta Entrada.**  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Causa**O *help* **Q215NAOMOV** ocorre quando não há integração para o documento de entrada entre o módulo de **Inspeção de Entradas** e o módulo de **Estoque**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Validar se a entrada de documento ocorreu pela rotina **MATA103 - Documento de Entrada**, caso tenha se originado na rotina **QIEA200** **- Entradas**não haverá movimentação de estoque.
