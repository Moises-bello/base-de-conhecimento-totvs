---
article_id: 360025481632
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93991865f227c152a25bbf4b52e15bbe1b717a8a65ec5bf67a1f67617c7bd470
fetched_at: '2026-06-28T22:42:44.539928+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem RECNO - Não existe registro
  com arquivo em pauta
type: support-article
updated_at: '2022-11-22T14:51:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025481632-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-RECNO-N%C3%A3o-existe-registro-com-arquivo-em-pauta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min****Ocorrência**A mensagem **RECNO - Não existe registro com arquivo em pauta** é apresentada ao clicar em **salvar** na rotina **MATA720 - Aglutina OPs**, após selecionar as **OPs - Ordens de Produção** a serem aglutinadas.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
 **Causa**As **OPs** selecionadas não fazem parte do mesmo período selecionado e por isso não podem ser aglutinadas.  
  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Avalie o período para aglutinação das **OPs** e se as **OPs** selecionadas fazem parte do mesmo período.  
  
**Exemplo:**  
**OP1** - Data de entrega 02/06/2014  
 **OP2** - Data de entrega 01/07/2014  
  
No momento em que for aglutinar escolher a opção por **Semestre**, será apresentada a mensagem, pois a primeira **OP** está para o primeiro semestre e a segunda **OP** para o segundo semestre.
