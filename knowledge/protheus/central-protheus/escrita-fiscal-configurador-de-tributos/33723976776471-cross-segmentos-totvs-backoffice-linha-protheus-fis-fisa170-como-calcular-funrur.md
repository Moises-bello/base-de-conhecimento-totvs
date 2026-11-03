---
article_id: 33723976776471
category: Escrita Fiscal - Configurador de Tributos
content_hash: 5fe8b1bd9f118fc5278a5d93d17a31aab5a5ad2253f5ca3ef0d51ffb4db60811
fetched_at: '2026-06-28T22:39:18.403844+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  FUNRURAL utilizando o Configurador de Tributos para notas de entrada e saída.
type: support-article
updated_at: '2025-07-25T20:41:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33723976776471-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-FUNRURAL-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33725021929111) Tempo aproximado para leitura: **00:20 min**  
  
**Dúvida**  
Como calcular o FUNRURAL (INSS, GILRAT e SENAR) utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**  
Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do FUNRURAL (INSS, GILRAT e SENAR).

**Segue exemplo de cadastros:**

**1)** FISA710 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987593495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976697495)

**2)** FISA710 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987596183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976701463)

**3)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987597335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987599127)

**4)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976706071)

Segue exemplo de cadastro do INSS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987603735)

Segue exemplo de cadastro do GILRAT:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987605399)

Segue exemplo de cadastro do SENAR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987607831)

**5)** FISA710 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987611927)

Segue exemplo de cadastro do INSS:

 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987613079)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976717847)

 

Segue exemplo de cadastro do GILRAT:

 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976719383)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976717847)

Segue exemplo de cadastro do SENAR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987622807)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723976717847)

**6)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com impostos nos valores de INSS = 110,00, GILRAT = 22,00 e SENAR = 2,00.

 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987625111)

**7)** Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com impostos nos valores de INSS = 110,00, GILRAT = 22,00 e SENAR = 2,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987626775)

**OBS:** para geração dos títulos do INSS, GILRAT e SENAR serão no Contas a Pagar ou Contas a Receber, deve ser vinculado uma Regra Financeira na **Regra de Cálculo - Documentos Fiscais** ou gerar os títulos utilizando o Configurador de Tributos (FISA170) > Apuração de Tributos Genéricos.

**Campos preenchidos nas notas de saída:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987628951)**

**Campos preenchidos nas notas de entrada:**

 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723987631511)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[CFGTRIB - FUNRURAL](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+FUNRURAL#CFGTRIBFUNRURAL-RegradeEscritura%C3%A7%C3%A3o)
