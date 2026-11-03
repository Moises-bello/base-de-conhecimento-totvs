---
article_id: 360043285134
category: Gestão de Transportes (TMS)
content_hash: 0033e5233a3770d79acba9c7d7c9b0140a1c4bd5c4cd4ceea7a10dda20d14974
fetched_at: '2026-06-28T22:45:29.270120+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - HELP AT250TABFR - Tabela de Frete Inválida
type: support-article
updated_at: '2022-06-01T18:50:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043285134-Log%C3%ADstica-Linha-Protheus-TMS-HELP-AT250TABFR-Tabela-de-Frete-Inv%C3%A1lida
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:42 min**  
**Dúvida**Como resolver o *help***AT250TABFR - Tabela de Frete Inválida**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Na rotina **TECA250 - Contrato Cliente,**ao informar uma tabela de frete a pagar e clicar em **Confirmar**, é apresentado o *help***AT250TABFR - Tabela de Frete Inválida.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058537854/mceclip0.png)

Este *help*é apresentado pois esta tabela existe apenas na rotina **TMSA130 - Configuração da Tabela de Frete,**faltando ser cadastrada na rotina **TMSA790 - Tabela de Frete a Pagar.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058537934/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059441713/mceclip2.png)**

Para resolver o *help*, é necessário efetuar a inclusão da tabela de frete na rotina **TMSA790 - Tabela de Frete a Pagar.**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058538034/mceclip3.png)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058538074/mceclip4.png)**
