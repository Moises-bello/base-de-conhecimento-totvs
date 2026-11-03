---
article_id: 360016305732
category: ADVPL - Classe e Função
content_hash: 7c4dc1f914dccb406ef0c6903a464a2b8184318b990ac3e61fd74b00190d4ed4
fetched_at: '2026-06-28T22:40:19.457457+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função Salva e
  Criar Novo
type: support-article
updated_at: '2022-01-10T22:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016305732-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Salva-e-Criar-Novo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como inibir o botão "Salva e Criar Novo" numa customização em MVC?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.17  
  
**Solução**Para que não apresente o botão "Salvar e Criar Novo" utilize a função *FwexecView*(), no 8º parâmetro (aEnableButtons) posição [15][1] do array precisa ser .F.

**Saiba mais**Para mais detalhes da função *[FWExecView](http://tdn.totvs.com/display/public/mp/FWExecView)*
