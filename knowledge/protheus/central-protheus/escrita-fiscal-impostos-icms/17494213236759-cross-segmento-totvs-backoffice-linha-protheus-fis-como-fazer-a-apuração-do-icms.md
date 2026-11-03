---
article_id: 17494213236759
category: Escrita Fiscal - Impostos - ICMS
content_hash: b8ab50dbf1c6dee9038a27ab36ca03bdd357b74564a0f12adda83fd590321184
fetched_at: '2026-06-28T22:39:24.057549+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS-  Como fazer a apuração
  do ICMS base dupla em SP?
type: support-article
updated_at: '2024-05-21T13:17:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17494213236759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-fazer-a-apura%C3%A7%C3%A3o-do-ICMS-base-dupla-em-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17494235145495) Tempo aproximado para leitura: **05:00 min** **Dúvida**Como fazer a apuração do ICMS base dupla em SP?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Calculo do Diferencial de alíquota com base dupla na apuração do ICMS no estado de SP

MV\_ESTADO = SP

MV\_USASPED = .T.

MV\_P9SPED = .F.

MV\_P9AUTO = F

MV\_ART117 = .F.

MV\_BASDENT = SP

Fornecedor = Fora do estado

MG

TES

Calcula icms = sim

L fiscal icms = outros

Sit trib icm = 90

Calc dif icm = sim

Mat consumo = sim

Calc difal = não

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631520526103)

Conteúdo do Reflexo

0000010 - padrão gerado pelo U\_IMPSPED

![](https://totvssuporte.zendesk.com/attachments/token/dar1Lqlw7bFrEHa7ANfAHoPui/?name=image.png)

0000207 - inserido de forma manual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631520537879)

Documento de entradas

![](https://totvssuporte.zendesk.com/attachments/token/0r3tu7kDmSzbFJVBaerhWiKLW/?name=image.png)

Lançamento de apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631520543383)

Apuração do ICMS

![](https://totvssuporte.zendesk.com/attachments/token/zeHw2qfSegr1uuUyqk85P7rM2/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/W4VYhKv8Ju0fn3Yf7KV3Pddcv/?name=image.png)

Boletim da apuração.

<https://tdn.totvs.com/pages/releaseview.action?pageId=270894388>

Boletim do Reflexo

<https://tdn.totvs.com/pages/releaseview.action?pageId=640907320>

Obs.: O P9autotext.SP não trata a base dupla e nesse caso precisamos configurar o reflexo na TES, para notas fiscais onde o campo F3\_ICMSCOM estiver preenchido, após alteração da TES, fazer o reprocessamento de dados para criar os lançamento de apuração.
