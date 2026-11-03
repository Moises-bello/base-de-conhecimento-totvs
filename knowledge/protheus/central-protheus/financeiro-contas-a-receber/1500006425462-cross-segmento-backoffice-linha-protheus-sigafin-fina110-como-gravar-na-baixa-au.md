---
article_id: 1500006425462
category: Financeiro - Contas a Receber
content_hash: 0666d20d67d8ebca1a6b954f93a5ddc313fcdec433738f8c89bb395ad92294dc
fetched_at: '2026-06-28T22:38:13.816333+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento - BackOffice Linha Protheus- SIGAFIN - FINA110 - Como gravar
  na baixa automática o campo E5_DTDISPO com D+1 '
type: support-article
updated_at: '2021-04-28T15:16:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006425462-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA110-Como-gravar-na-baixa-autom%C3%A1tica-o-campo-E5-DTDISPO-com-D-1
---

**Dúvida**Como gravar na baixa automática o campo E5\_DTDISPO com D+1 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Não é possível informar a data de disponibilidade na rotina **FINA110**.  
Para data de disponibilidade fique com D+1 verifique o cadastro do banco utilizado no campo **A6\_RETENCA = 1**.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008514421/mceclip1.png)**

e os títulos tem que estar em borderô. Na rotina **FINA060** colocar o título em borderô, verifique a pergunta parâmetro <F12> **C****onsidera Retencao Bancaria? = Sim**.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008322822/mceclip2.png)**

 E na rotina **FINA110** nos parâmetros <F12> a pergunta **C****onsidera Retenc Bancaria?** com o conteúdo  **= Sim**.

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008322882/mceclip3.png)**
