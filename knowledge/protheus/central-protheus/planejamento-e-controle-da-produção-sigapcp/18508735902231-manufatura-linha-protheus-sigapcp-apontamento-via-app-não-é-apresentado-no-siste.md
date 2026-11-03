---
article_id: 18508735902231
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 04c060ef2f62f1dd78c42f37f047be63d78a8fa81d6ec452d44fa5ee40f0a769
fetched_at: '2026-06-28T22:42:40.824270+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento via app não é apresentado
  no Sistema
type: support-article
updated_at: '2023-10-24T12:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18508735902231-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-via-app-n%C3%A3o-%C3%A9-apresentado-no-Sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18508699020055) Tempo aproximado para leitura: **00:00:48 min****Dúvida**Ao realizar um apontamento através do *app* **Minha Produção**, o apontamento é confirmado mas não é possível visualizá-lo na rotina de apontamento.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Isso ocorre quando o parâmetro **MV\_APPENMO - Indica se utiliza conceito de apontamentos pendentes para *mobile*** possui o conteúdo **2** ou **3**, nesses casos o apontamento fica aguardando os ajustes ou confirmação na rotina **PCPA138 - Apontamento Pendente**  
Para solucionar essa situação, realize os seguintes passos:  
1. Acesse o **PCPA138** para reprocessar o movimento  
2. Avalie o preenchimento do parâmetro **MV\_APPENMO.**
