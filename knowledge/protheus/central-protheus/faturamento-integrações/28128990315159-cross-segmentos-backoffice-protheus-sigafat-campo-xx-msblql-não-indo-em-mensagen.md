---
article_id: 28128990315159
category: Faturamento - Integrações
content_hash: dd567b3b855cc8f4d6c89a1976ff135d9da96f5466e96bbbe028ee9e1f894b30
fetched_at: '2026-06-28T22:38:26.472855+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Campo XX_MSBLQL não indo
  em mensagens EAI MATI360
type: support-article
updated_at: '2024-11-28T15:05:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28128990315159-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Campo-XX-MSBLQL-n%C3%A3o-indo-em-mensagens-EAI-MATI360
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28128993902871) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que o campo  XX\_MSBLQL não está indo em mensagens EAI no Protheus Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

A tag "RegisterSituation" foi uma melhoria implementada para tratar o campo "E4\_MSBLQL" na Mensagem Única EAI Condição de Pagamento (PaymentCondition) utilizando JSON.

Toda a melhoria para EAI é feita no formato mais atual e, por isso, foi criada somente para a integração JSON.

Caso necessite que esta tag seja implementada para as mensagens XML, deve ser aberto uma solicitação de melhoria na central de colaborativa.

**Saiba mais:**

[DT Mensagem Única EAI PaymentCondition - Criação da Tag RegisterSituation](https://tdn.totvs.com/pages/viewpage.action?pageId=715150303)
