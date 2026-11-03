---
article_id: 17790396964119
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: cb9cfa2a4ca824361783e3b54f9a499f1c5f50bbb151f9814068de0fece5bfd0
fetched_at: '2026-06-28T22:39:19.236661+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como calcular o Diferencial de aliquotas base dupla pela diferença de aliquotas?
type: support-article
updated_at: '2023-09-25T12:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17790396964119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-calcular-o-Diferencial-de-aliquotas-base-dupla-pela-diferen%C3%A7a-de-aliquotas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17790380457367) Tempo aproximado para leitura: **05:00min** **Dúvida**MP FIS Como calcular o Diferencial de aliquotas base dupla pela diferença de aliquotas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Exemplo de calculo:

Documento de entradas

Valor da mercadoria = 1000,00  
Base de calculo do ICMS = 1000,00 \*12% = 120,00  
Diferencial de aliquotas = 1000,000/ ( 18% -12% = 6% ) 0,94   
1000,00/0,94 = 1063,83 \*6% = 63,83

MV\_ESTADO = SE

MV\_BASDENT = SE

MV\_BASDSER = SE

MV\_CMPALIQ = .T.

Fornecedor = PE

TES

Calcula ICMS = sim

L fiscal ICMS = outros

Calc dif icm = sim

Mat consumo = sim

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17790265594263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17790303403031)

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=699818895>
