---
article_id: 33702907793175
category: Escrita Fiscal - Configurador de Tributos
content_hash: f9ec84493eb0c1896d3a4e9c1141214b0727ab715193123b9216f6f1de51c98c
fetched_at: '2026-06-28T22:39:18.418854+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  o INSS utilizando o Configurador de Tributos para notas de entrada e saída.
type: support-article
updated_at: '2025-11-03T18:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33702907793175-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-INSS-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930161559) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como calcular INSS utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do INSS.

Segue exemplo de cadastros:               

**1)** FISA710 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907768343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907768599)

**2)** FISA710 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930163479)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907770135)

**3)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930165143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907770903)

**4)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930166935)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930168855)

**5)** FISA710 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907772055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930169879)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930170903)

**6)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com imposto de INSS no valor de R$ 110,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907773079)

**7)** Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com imposto de INSS no valor de R$ 110,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702930172951)

**OBS:** para geração dos títulos do INSS no Contas a Pagar ou Contas a Receber, deve ser vinculado uma Regra Financeira na **Regra de Cálculo - Documentos Fiscais.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar o imposto INSS com a regra financeira?](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/32524692208535-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-INSS-com-a-regra-financeira)

**Campos preenchidos nas notas de entrada:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907774743)

**Campos preenchidos nas notas de saída:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33702907774871)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
