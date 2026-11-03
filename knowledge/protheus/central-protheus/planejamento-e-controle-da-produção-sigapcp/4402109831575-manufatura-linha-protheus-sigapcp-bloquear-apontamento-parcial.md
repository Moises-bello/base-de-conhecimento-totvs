---
article_id: 4402109831575
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f4c3d4f58804e02a52d784b6a1d3028779e59f7b7c75c8bef0b09ce1db9f0675
fetched_at: '2026-06-28T22:42:40.909123+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloquear apontamento parcial
type: support-article
updated_at: '2021-06-07T11:01:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402109831575-Manufatura-Linha-Protheus-SIGAPCP-Bloquear-apontamento-parcial
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**É possível bloquear o apontamento parcial de **OP  - Ordem de produção** no **MATA250 - Produção Simples**, **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Atualmente não é possível impedir que ocorra um apontamento parcial de uma OP, seria necessário implementar uma validação através de ponto de entrada.  
  
**Saiba mais**Para implementar a validação sugerimos o uso do ponto de entrada **A250ITOK** para apontamentos via **MATA250**, cuja documentação encontra-se disponível no link [A250ITOK - Permite customização antes do apontamento da produção](https://tdn.totvs.com/pages/releaseview.action?pageId=6087504)[.](https://tdn.totvs.com/pages/releaseview.action?pageId=6087504)  
Já para apontamentos via **MATA680** ou **MATA681** sugerimos o uso do ponto de entrada **MT680VAL ,** cuja documentação encontra-se disponível no link [MT680VAL - Inclusão das Produções](https://tdn.totvs.com/pages/releaseview.action?pageId=6089410).
