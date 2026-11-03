---
article_id: 4406506050967
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1e4bb59d5b0cca8af399d3fffd850fccf707c6fc80b79ce8fc8e22aed7f6da2a
fetched_at: '2026-06-28T22:42:44.457416+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Essa OP é movimentada somente
  através do módulo Chão de Fábrica
type: support-article
updated_at: '2021-08-17T12:16:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406506050967-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Essa-OP-%C3%A9-movimentada-somente-atrav%C3%A9s-do-m%C3%B3dulo-Ch%C3%A3o-de-F%C3%A1brica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar apontar uma **OP - Ordem de Produção** no **MATA250 - Apontamento Simples**, **MATA680 - Apontamento Modelo I** ou **MATA681 - Apontamento Modelo II** por que o usuário recebe a mensagem **Essa OP é movimentada somente através do módulo Chão de Fábrica?**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem surge quando o parâmetro **MV\_INTSFC - Define se existe integração entre o módulo SIGASFC - Chão de Fábrica** e outros módulos, possui o conteúdo 1 e a **OP** está integrada com o **SIGASFC.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se procede a integração com o **SIGASFC**, se não proceder altere o parâmetro **MV\_INTSFC** para **0**;  
2. Se procede a integração com o **SIGASFC**, faça o apontamento através das rotinas do **SIGASFC**, **SFCA310 - Apontamento Produção Modelo 1** ou **SFCA316 - Apontamento Produção Modelo 2**.
