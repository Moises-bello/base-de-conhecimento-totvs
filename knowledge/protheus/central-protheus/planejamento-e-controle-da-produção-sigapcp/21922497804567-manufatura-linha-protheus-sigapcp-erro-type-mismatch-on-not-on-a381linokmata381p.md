---
article_id: 21922497804567
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ff82f461322c58fe41234b1ad1a43190d101b0e507cd90dfb168b6227f0cddfb
fetched_at: '2026-06-28T22:42:42.282439+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro type mismatch on .NOT. on A381LINOK(MATA381.PRX)
type: support-article
updated_at: '2024-07-03T17:53:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21922497804567-Manufatura-Linha-Protheus-SIGAPCP-Erro-type-mismatch-on-NOT-on-A381LINOK-MATA381-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21922497774999) Tempo aproximado para leitura: **00:00:55 min****Ocorrência**Na rotina **MATA381 - Ajuste de Empenho** ao alterar o empenho, ocorre a mensagem **type mismatch on .NOT. on A381LINOK(MATA381.PRX)**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Todas as versões  
  
**Causa**Esta situação ocorre quando o parâmetro **MV\_EMPDOP - Indica se será permitido incluir no empenho o mesmo produto da OP (.T.) - Sim (.F.) - Não.** está definido com o **tipo** incorreto no **SIGACFG - Configurador**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **SIGACFG** e em **Base de Dados > Dicionário > Base de Dados** e em **Parâmetros** pesquise pelo código **MV\_EMPDOP**;  
2. Clique em **Alterar**;  
3. Altere o campo **Tipo** para **3 - Lógico**.
