---
article_id: 1500011569822
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 233e8a13c5ae9c3dbebce4b3fcb7234c3daf7a0f512abf27e372cba4c08fee28
fetched_at: '2026-06-28T22:42:45.715866+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo D4_DATA
type: support-article
updated_at: '2021-05-21T11:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011569822-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-D4-DATA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Como é preenchido o campo **D4\_DATA - Data do Empenho**, da tabela **SD4 - Requisições Empenhadas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando ocorre a inclusão automática do empenho, no registro da **OP - Ordem de Produção**, o campo **D4\_DATA** é preenchido com o mesmo conteúdo do campo **C2\_DATPRI - Previsão Inicial da OP** relacionada. Já quando ocorre a inclusão manual do empenho, através das rotinas **MATA380 - Empenho Simples** ou **MATA381 - Empenho Múltiplo** a data sugerida é a **Database**.
