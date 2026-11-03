---
article_id: 4418624964375
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 16c1adc33914d1c74121f3e2c3f51d5cce8171e50ef59bc75dd296832ce73bb1
fetched_at: '2026-06-28T22:42:43.618348+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A680NAOSH1
type: support-article
updated_at: '2022-01-20T10:48:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418624964375-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A680NAOSH1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**Ao realizar o apontamento via **MATA681 - Apontamento Modelo II** o usuário recebe a mensagem **A680NAOSH1 - O recurso não está cadastrado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa situação ocorre quando ao realizar o apontamento no **MATA681** o campo **H6\_RECURSO - Recurso** não está preenchido ou está preenchido com um código não cadastrado no **MATA610 - Cadastro de Recursos.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Certifique-se que o campo **H6\_RECURSO** está preenchido;  
2. Verifique no **MATA610** se esse recurso, informado no **H6\_RECURSO** está cadastrado.
