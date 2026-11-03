---
article_id: 360033097354
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2ac43a925e3c5d4e7affbf409a1e8132ccc04346afa7ebccc7f913fc2abeb644
fetched_at: '2026-06-28T22:42:42.242769+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Empenho do mesmo produto a ser produzido
  na OP
type: support-article
updated_at: '2022-11-07T14:50:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033097354-Manufatura-Linha-Protheus-SIGAPCP-Empenho-do-mesmo-produto-a-ser-produzido-na-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Como empenhar o mesmo produto a ser produzido através da **OP - Ordem de Produção?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12.  
  
**Solução**Para permitir o empenho do mesmo produto execute os passos abaixo:  
1. Altere o conteúdo do parâmetro **MV\_EMPDOP - Indica se será permitido incluir no empenho o mesmo produto da OP** para **.T.**  
2. Acesse as rotinas **MATA380 - Empenho Simples** ou **MATA381 - Empenho Múltiplo**  
3. Inclua o empenho do item.
