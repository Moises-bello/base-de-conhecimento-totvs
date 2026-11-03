---
article_id: 360034528753
category: Call Center - Telecobrança
content_hash: b0afd7e80a9796a253c8f3b9e43e41ee68ca5c240852c106035084512c9e88a7
fetched_at: '2026-06-28T22:41:28.681535+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Televendas - Gerando
  SL4 '
type: support-article
updated_at: '2022-06-22T17:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034528753-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Televendas-Gerando-SL4
---

**Dúvida :**

Geração de registro na tabela **SL4** mesmo sem a integração com o Loja.

**Ambiente :**Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A partir da Versão 12.1.17.

**Solução :**

Independente do parâmetro **MV\_TMKLOJ** estar ativo ou não, para a integração do **TMK** com o SIGALOJA,  o atendimento precisa gravar dados na tabela **SL4**, os quais são necessários por exemplo na hora de alterar um atendimento e trocar a forma de pagamento de uma condição de pagamento parcelada.

Sem esses registros não seria possível identificar as formas de pagamento escolhidas.
