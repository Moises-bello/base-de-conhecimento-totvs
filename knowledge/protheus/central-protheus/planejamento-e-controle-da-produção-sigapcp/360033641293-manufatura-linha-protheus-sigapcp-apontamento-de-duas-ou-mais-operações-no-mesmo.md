---
article_id: 360033641293
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cbc39bb721d9837cb1f3c4478b204835ce56f0d3d5bffa42cf0834eefa8f7711
fetched_at: '2026-06-28T22:42:40.807074+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento de duas ou mais operações
  no mesmo horário e recurso.
type: support-article
updated_at: '2021-08-13T12:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033641293-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-de-duas-ou-mais-opera%C3%A7%C3%B5es-no-mesmo-hor%C3%A1rio-e-recurso
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**É possível realizar o apontamento de duas **operações** no mesmo horário, para o mesmo **recurso**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No momento do apontamento nas rotinas de apontamento **MATA680 - Produção PCP Mod1** e **MATA681 - Produção PCP Mod2** não validam se para o **recurso** que está sendo apontado já foi realizado algum apontamento anterior para o mesmo horário. Sendo assim é possível realizar apontamentos de diversas **operações** no mesmo horário.
