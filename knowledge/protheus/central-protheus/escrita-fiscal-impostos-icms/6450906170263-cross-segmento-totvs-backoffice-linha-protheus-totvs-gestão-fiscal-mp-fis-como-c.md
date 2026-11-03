---
article_id: 6450906170263
category: Escrita Fiscal - Impostos - ICMS
content_hash: f2689d99d4826023199b6ec3853512ada8d21ef05df9a6aee7a057bf8fa6c4ba
fetched_at: '2026-06-28T22:39:24.075683+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como configurar Diferencial de alíquotas base dupla em SP?
type: support-article
updated_at: '2024-06-20T18:19:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6450906170263-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-configurar-Diferencial-de-al%C3%ADquotas-base-dupla-em-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**MP FIS Como configurar Diferencial de aliquotas base dupla em SP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

* ##### Cálculo de base dupla na entrada:

Deverá configurar o parâmetro **MV\_BASDENT**, informando o estado que está entrando a mercadoria.

Exemplo

MV\_estado = SP

MV\_BASDENT = SP

TES

Calcula icms = sim

L fiscal icms = outros

Calc dif icm = sim

Mat consumo = sim

Valor de Mercadoria – R$ 1.000,00  
ICMS – 1.000,00 \* 12 = 120,00  
DIF – 1.073,17 \* 18 = 73,17

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6450077213079/mceclip0.png)

O valor de 73,17 é gravado no campo F3\_ICMSCOM
