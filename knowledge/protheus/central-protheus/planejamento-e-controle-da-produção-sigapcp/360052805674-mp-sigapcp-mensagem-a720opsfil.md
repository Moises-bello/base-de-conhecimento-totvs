---
article_id: 360052805674
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: aa69a8098ea99244173212b1a163fa985b675276b9951a862b6c4808b14c0d72
fetched_at: '2026-06-28T22:42:47.252921+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'MP - SIGAPCP - Mensagem A720OPSFIL '
type: support-article
updated_at: '2021-06-28T17:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052805674-MP-SIGAPCP-Mensagem-A720OPSFIL
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:58 min**  
**Ocorrência**Ao tentar aglutinar as **OPs** através da rotina **MATA720**o Sistema apresenta a mensagem **A720OPSFIL**.  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**Esta mensagem é apresentada, pois existem ordens que não geraram suas **OPs intermediarias** e **SCs**.  
  
**Solução**Para executar o **MATA720,** altere o parâmetro**MV\_EXPLOPU**para **N**, acesse a rotina **MATA650** e tecle **ESC**, após clique em **Sim** na mensagem para geração das **OPs intermediarias** e **SCs**.  
  
**Glossário**  
**OPs** - Ordem de Produção  
**SCs** - Solicitações de Compra  
**MATA720** - Aglutinação de OPs   
**MATA650** - Ordens de Produção  
**MV\_EXPLOPU** - Se o parâmetro estiver com o conteúdo igual a **S** serão geradas **OPs** intermediarias/**SC**, somente para o usuário corrente
