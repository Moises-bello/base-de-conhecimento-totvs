---
article_id: 28731556884503
category: Financeiro - Contas a Receber
content_hash: 5d47464bb5ac8e2e413807c0659a0cd21460b1f932c35b4f7553f6de39c4ac80
fetched_at: '2026-06-28T22:38:12.632941+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Preenchimento
  do Campo E1_VALLIQ
type: support-article
updated_at: '2026-03-25T18:23:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28731556884503-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Preenchimento-do-Campo-E1-VALLIQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28731493879703) Tempo aproximado para leitura: **00:09 min**  
  
**Dúvida**  
Preenchimento do Campo - **E1\_VALLIQ**?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
O campo **E1\_VALLIQ** é apenas um campo que grava a movimentação e não acumulada valores. Após o cancelamento da baixa, o campo E1\_VALLIQ fica zerado.

Exemplo:

Título no valor de R$ 1.000,00

1)      2 baixas: baixa parcial de R$ 995,00 e R$5,00

a)      Baixa parcial de R$ 995,00

**E1\_VALLIQ** = R$ 995,00

b)      Baixa no valor de R$ 5,00

**E1\_VALLIQ** = R$5,00

c) Cancelamento da Baixa R$ 5,00

**E1\_VALLIQ** = R$ 0,00

d) Cancelamento da Baixa R$ 995,00

**E1\_VALLIQ** = R$ 0,00

2)      Baixa parcial de R$ 995,00 e eliminação de resíduo de R$ 5,00

a)      Baixa parcial de R$ 995,00

**E1\_VALLIQ** = R$ 995,00

b)      Eliminação de resíduo:

**E1\_VALLIQ** = R$ 5,00

c) Cancelamento da Baixa

**E1\_VALLIQ** = R$ 0,00

**Saiba Mais**

[**E1\_VALLIQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=286004910)
