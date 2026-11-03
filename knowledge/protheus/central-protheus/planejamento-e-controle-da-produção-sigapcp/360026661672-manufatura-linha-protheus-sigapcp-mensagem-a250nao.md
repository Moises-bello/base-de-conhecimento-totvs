---
article_id: 360026661672
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d3e0adb5a773ddf73abb6a0b62d7f4c04c15667b72e4bb812bec80846be19f9c
fetched_at: '2026-06-28T22:42:43.581911+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A250NAO
type: support-article
updated_at: '2021-09-28T13:57:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661672-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A250NAO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min****Dúvida**Ao tentar estornar um apontamento de produção através da rotina **MATA250 - Produção Simples**, o usuário recebe a mensagem **A250NAO - Este movimento não é uma produção, portanto não pode ser acessado**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) -  12  
  
**Solução**Para estornar um apontamento de produção é necessário que o registro selecionado tenha o conteúdo do campo **D3\_CF - Tipo RE/DE** preenchido com **PR0**.
