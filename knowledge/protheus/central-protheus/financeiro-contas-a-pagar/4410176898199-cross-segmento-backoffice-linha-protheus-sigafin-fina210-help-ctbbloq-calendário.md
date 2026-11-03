---
article_id: 4410176898199
category: Financeiro - Contas a Pagar
content_hash: ad48c5b2536e5e1900a5d8c96c69dc684ce07670951a97aab267109da34367ec
fetched_at: '2026-06-28T22:38:08.284046+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - BackOffice Linha Protheus - SIGAFIN - FINA210 - HELP CTBBLOQ:
  Calendário Contábil Bloqueado. Verifique o Processo'
type: support-article
updated_at: '2022-04-28T17:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410176898199-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA210-HELP-CTBBLOQ-Calend%C3%A1rio-Cont%C3%A1bil-Bloqueado-Verifique-o-Processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar o recalculo dos saldos bancários pela rotina FINA210, é apresentada o help **CTBBLOQ: Calendário Contábil Bloqueado Verifique o Processo** 

![HELP_CTBBLOQ.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410169392151/HELP_CTBBLOQ.png)  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o período informado no recalculo está bloqueado por processo pela rotina **CTBA010 - Calendário Contábil**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a rotina **CTBA010 - Calendário Contábil**e localizar o período.  
2. Clicar em **Outras Ações > Bloqueio de Processo**   
3. Alterar o processo para "**Aberto**"  
4. Recalcular novamente os saldos bancários.

**Saiba mais:**  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010 - Como funciona a funcionalidade - Bloqueio por Processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035066073-MP-SIGACTB-CTBA010-Como-funciona-a-funcionalidade-Bloqueio-por-Processo-)  
[Cross Segmentos - Backoffice Linha Protheus - HELP - DTMOVFIN e utilização dos parâmetros MV\_DATAFIN e MV\_BXDTFIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020859271)
