---
article_id: 28273192090135
category: Escrita Fiscal - Configurador de Tributos
content_hash: 0ab7c63a67161ab54c64171622bdd6d79885960494ecc4adf874acee73d42dc0
fetched_at: '2026-06-28T22:39:18.437425+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  PIS-COFINS Apuração utilizando o Configurador de Tributos para notas de entrada
  e saída.
type: support-article
updated_at: '2025-11-04T21:37:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273192090135-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176632087) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como calcular PIS/COFINS Apuração utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do PIS/COFINS Apuração.

**Segue exemplo de cadastros de Regra de Base de Cálculo:**

FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

**1)** FISA710 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273192043159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273192045591)

 

**2)** FISA710 - **Regras Fiscais** > Perfis > **Perfil de Participante:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176639383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176645399)

**3)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176648215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176657303)

**4)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273192057495)**

 

Segue exemplo de cadastro do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273176660119)

Segue exemplo de cadastro do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273192062103)

**5)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Escrituração:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273192068375)

Segue exemplo de cadastro do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273376226583)

Segue exemplo de cadastro do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357606807)

**6)** FISA710 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273376232343)

 

Segue exemplo de cadastro do PIS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273376235415)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357615127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273376240791)

Segue exemplo de cadastro do COFINS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357622295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357624215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273376250263)

 

**7)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com impostos nos valores de PIS = 16,50, COFINS = 76,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357628311)

**9)** Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com impostos nos valores de PIS = 16,50, COFINS = 76,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273357630615)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
