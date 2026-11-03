---
article_id: 4558111401111
category: Financeiro - Movimentação Bancária
content_hash: 06ec616182e907420c796e735b3b737f0a98f9591a720f35013170cd8a369052
fetched_at: '2026-06-28T22:38:19.392502+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100  -  HELP:INVTRF
  na transferência bancária '
type: support-article
updated_at: '2023-01-25T22:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4558111401111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-HELP-INVTRF-na-transfer%C3%AAncia-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min****Ocorrência:**No módulo Financeiro ao realizar uma transferência Bancária (FINA100) apresentou a mensagem HELP:INVTRF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4557939223831/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA100  - Todas as versões  
  
**Solução**

Validar se o banco utilizado está no parâmetro **MV\_CXFIN** ou contém na **SX5** **tabela 23** irá apresentar a mensagem "INVTRF - Somente é possível transferir valores de um caixa para um banco utilizado a transferência em dinheiro ou cartões."  
Quando o banco é informado neste parâmetro, o sistema o considera como Caixa, impossibilitando a transferência do **tipo TB**  
  
**Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=501480542>
