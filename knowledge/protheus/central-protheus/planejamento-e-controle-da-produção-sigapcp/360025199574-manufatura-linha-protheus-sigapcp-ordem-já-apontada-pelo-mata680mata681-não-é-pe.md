---
article_id: 360025199574
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: deb1a4dbd9d19fc96a9b01efe6a5ac71243a30becae302685079f1aac2742aa6
fetched_at: '2026-06-28T22:42:44.706783+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ordem já apontada pelo MATA680/MATA681
  não é permitido realizar o apontamento
type: support-article
updated_at: '2022-10-11T18:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025199574-Manufatura-Linha-Protheus-SIGAPCP-Ordem-j%C3%A1-apontada-pelo-MATA680-MATA681-n%C3%A3o-%C3%A9-permitido-realizar-o-apontamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Na rotina de apontamento de produção é apresentada a mensagem **Ordem já apontada pelo MATA680/MATA681. Não é permitido realizar o apontamento**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem é apresentada ao tentar realizar o apontamento de produção simultaneamente nas rotinas **MATA680 - Apontamento de Produção Mod I**/**MATA681****- Apontamento de Produção Mod II**e **MATA250 - Produção Simples**.  
  
**Solução**Não é permitido o apontamento de quantidade produzida por mais de uma rotina de apontamento de produção, deve-se definir por qual rotina será realizado o apontamento de produção e usar somente esta para todo os apontamentos da **OP - Ordem de Produção**.  
  
**Importante**  
É permitido apontar apenas tempo pelo **MATA680/MATA681** e quantidade produzida pelo **MATA250**.
