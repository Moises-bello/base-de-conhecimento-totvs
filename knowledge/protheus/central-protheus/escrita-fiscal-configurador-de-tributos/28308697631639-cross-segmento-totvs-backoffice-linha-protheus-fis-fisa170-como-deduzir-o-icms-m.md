---
article_id: 28308697631639
category: Escrita Fiscal - Configurador de Tributos
content_hash: 4b7a07e60dcba350a00d80f98515c7cd6dbaf07ee29acd80019a54dc9475d86e
fetched_at: '2026-06-28T22:39:17.436139+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como deduzir
  o icms monofasico da base de calculo do pis e cofins no fisa170?
type: support-article
updated_at: '2025-11-04T22:04:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28308697631639-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-deduzir-o-icms-monofasico-da-base-de-calculo-do-pis-e-cofins-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689732631) Tempo aproximado para leitura: **05:00min** **Dúvida**Como deduzir o icms monofasico da base de calculo do pis e cofins no fisa170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**.

Para o calculo do ICMS Monofasico, vamos usar o documento abaixo:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como se creditar do ICMS para as compras do CST 61?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25745226524823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-se-creditar-do-ICMS-para-as-compras-do-CST-61)

Dados do calculo  
1750,000 litros  
ICMS monofasico = 2.474,33  
Valor unitário = 5,76  
Valor da mercadoria = 10.080,00

Base de calculo do PIS/Cofins = 10080,00 - 2.474,33 = 7.605,67  
aliquotas = 1,65% e 7,6%

Id Tributos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689734423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689739159)

Regra de base de calculo pis/cofins

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308697584407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689742615)

Regra de aliquota

000021 = PIS 1,65%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308697587223)

000022 = COFINS 7,6%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689747863)

Regra de escrituração

PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689749271)

Cofins

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689751831)

Regra de Calculo Documentos Fiscais - PIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308697593751)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689756055)

Perfis os mesmo do calculo do ICMS - monofasico

Regra de Calculo Documentos Fiscais- Cofins

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308697596823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308689758615)

Perfis os mesmos

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28308697602711)
