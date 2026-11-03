---
article_id: 8494058806295
category: Financeiro - Contas a Pagar
content_hash: 88445be03e3dc4ac7e0775aad21c1dc6fd2202cb0c3e34ea7d8cc7d126d74a0f
fetched_at: '2026-06-28T22:38:09.687162+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA390 - HELP: HA_REDEPOS'
type: support-article
updated_at: '2023-01-25T21:53:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8494058806295-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA390-HELP-HA-REDEPOS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05 min****Ocorrência**Ao cancelar a baixa, aparece a mensagem de HELP: HA\_REDEPOS

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8493971115415/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA390 - Todas as versões  
  
**Causa**Esse incidente ocorre, pois já existe redeposito para este cheque, e não é permitido o cancelamento do cheque.

**Solução**Para estornar completamente o movimento deste cheque, efetue o **redeposito** do restante do cheque atrelados aos títulos pela rotina FINA390 **Outras ações** -> **Redeposito**.  
**Redeposito**: Gera cancelamento do cheque e o movimento de estono nas movimentações Financeiras e exibi o valor de retorno no **extrato bancário**.  
**Cancelamento**: Apaga a movimentação do cheque e não exibi o estorno nos relatórios de **movimento** **bancário.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8494490989591/mceclip0.png)  
  
**Saiba mais**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA390 - Qual o conceito do redepósito de cheque a pagar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021075832)   
[Cheque sobre títulos - FINA390 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=499095374)
