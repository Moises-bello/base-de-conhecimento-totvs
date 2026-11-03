---
article_id: 4412151531415
category: Rescisão
content_hash: 9bd4c29664e83d7107f4203afb7242975e107412d9da5a91de3385071789282a
fetched_at: '2026-06-28T22:46:54.474466+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Data de vencimento não pode ser menor do que a data
  do sistema'
type: support-article
updated_at: '2024-10-23T22:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412151531415-RH-RM-FOP-GRRF-Data-de-vencimento-n%C3%A3o-pode-ser-menor-do-que-a-data-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo Totvs Folha de Pagamento, ao gerar a rotina GRRF com lançamento financeiro, ocorre o seguinte erro: **Data de vencimento não pode ser menor do que a data do sistema.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Ocorre quando a data de vencimento, em lançamentos financeiros está menor que a data do sistema e em **BackOffice | Gestão financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira | Manutenção de lançamentos | Inclusão**, o flag **Permite data de vencimento menor que a data do sistema** está desmarcado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **BackOffice | Gestão financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira | Manutenção de lançamentos | Inclusão.****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8868167741975/mceclip0.png)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8868319179159/mceclip1.png)  
  
2. Na aba **Inclusão**, marque a flag **Permite data de vencimento menor que a data do sistema.**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8868324108055/mceclip2.png)  
  
3. Após realizar os passos 1 e 2, gere novamente a GRRF.

**Saiba Mais**[GRRF - Guia de Recolhimento Rescisório do FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=452719518)
