---
article_id: 28271950709399
category: Escrita Fiscal - Configurador de Tributos
content_hash: 759c48c22d2366b1628f9ec9a63a6b116c3b1972e07d024f643028c2184a7a8b
fetched_at: '2026-06-28T22:39:18.453670+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  PIS/COFINS/CSLL retenção utilizando o Configurador de Tributos para notas de entrada
  e saída.
type: support-article
updated_at: '2025-11-11T21:41:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950628119) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como calcular PIS/COFINS/CSLL retenção utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do PIS/COFINS/CSLL retenção.

**Segue exemplo de cadastros:**

**1)** FISA170 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923536919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950631959) 

**2)** FISA170 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950633367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950635287)

 

**3)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923542807)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950639127)

**4)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923545879)

Segue exemplo de cadastro do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923547159)

Segue exemplo de cadastro do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923549719)

Segue exemplo de cadastro do CSLL:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950651031)

**5)** FISA170 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950657431)

Segue exemplo de cadastro do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950658199)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950659991)

Segue exemplo de cadastro do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923562263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923563927)

Segue exemplo de cadastro do CSLL:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923565463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271923566615)

**6)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com impostos nos valores de PIS = 6,50, COFINS = 30,00 e CSLL = 10,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29208874541591)

**7)** Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com impostos nos valores de PIS = 6,50, COFINS = 30,00 e CSLL = 10,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271950677143)

**OBS:** para geração dos títulos do PIS/COFINS/CSLL no Contas a Pagar ou Contas a Receber, deve ser vinculado uma Regra Financeira na **Regra de Cálculo - Documentos Fiscais.**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
