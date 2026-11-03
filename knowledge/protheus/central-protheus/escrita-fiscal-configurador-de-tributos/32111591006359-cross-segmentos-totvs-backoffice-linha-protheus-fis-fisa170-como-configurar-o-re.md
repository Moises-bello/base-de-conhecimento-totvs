---
article_id: 32111591006359
category: Escrita Fiscal - Configurador de Tributos
content_hash: 72f8995bbc354954f6fafc7dca61ba67ddf9910dc1f817c89af2c7f5f7a905fb
fetched_at: '2026-06-28T22:39:17.766508+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como configurar
  o reflexo sobre o Diferencial de alíquotas calculado pelo Configurador de Tributos?
type: support-article
updated_at: '2025-09-12T21:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32111591006359-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-reflexo-sobre-o-Diferencial-de-al%C3%ADquotas-calculado-pelo-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604431895) Tempo aproximado para leitura: 00:05**min** **Dúvida**Como configurar o reflexo sobre o Diferencial de aliquotas calculado pelo Fisa170?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal  
  
**Solução**Nesse exemplo:

MV\_estado = SP

Fornecedor = MG

No fisa170, acessar:

Regras de Ajuste de lançamento

Cadastro da mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604434583)

Para o lançamento do código SP10090718 - vamos utiliza a regra de calculo do ICMS 000041

Valor da mercadoria \*12%

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/32109854540695-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Como-calcular-o-Diferencial-de-al%C3%ADquotas-base-dupla-no-Fisa170](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26791332087191-Escrita-Fiscal-Configurador-de-Tributos)

Para o lançamento do código SP40090207 - vamos utilizar a regra de calculo do CMP3 000043

Valor da mercadoria - ICMS /0,82 \*18%

Imposto auxiliar somente para calculo do valor diferencial de alíquotas + icms, sem ID tributo amarrado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111590937239)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111590938391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111590940055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111590943127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604444695)

Regra de Ajuste de lançamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604446871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604447895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604450967)

Ao lançar o documento de entrada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604451735)

aba lançamentos de apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111590955031)

Apuração do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32111604456983)
