---
article_id: 360059254893
category: Escrita Fiscal - Impostos - ICMS
content_hash: 14de94e56b984c4636f932b99a84bcb6c0cf122f32147b102526ecac4590d9cf
fetched_at: '2026-06-28T22:39:26.010072+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Sistema não considera
  alíquotas da nota fiscal de entrada para calculo do diferencial de alíquotas, o
  que verificar? 
type: support-article
updated_at: '2021-07-20T13:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059254893-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Sistema-n%C3%A3o-considera-al%C3%ADquotas-da-nota-fiscal-de-entrada-para-calculo-do-diferencial-de-al%C3%ADquotas-o-que-verificar
---

**Dúvida** Sistema não considera aliquotas da Nota fiscal de entradas para calculo do diferencial de aliquotas o que verificar?   
  
  
**Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
  
**Solução**Para o calculo do diferencial de aliquotas das compras para uso / consumo ou ativo de fora do estado

configuramos na TES

Calcula icms = sim

l fiscal icms = outros

Calc dif icms = sim

Mat. consumo = sim

No calculo com base simples o sistema considera a diferença entre a alíquota interna e alíquota interestadual.

exemplo MV\_estado = SP compra de SC

 mercadoria nacional

1000,00

Alíquota interestadual = 12% = 120,00

Alíquota interna = 18% = 180,00

Valor do diferencial = 60,00

Mercadoria importada

Alíquota interestadual = 4% = 40,00

Alíquota interna = 18% = 180,00

Valor do diferencial = 140,00

Se as aliquotas forem diferentes dos exemplos acima mencionados, verificar

MV\_DIFALIQ = em branco

MV\_CPMALIQ = .F.

MV\_BASDENT = em branco
