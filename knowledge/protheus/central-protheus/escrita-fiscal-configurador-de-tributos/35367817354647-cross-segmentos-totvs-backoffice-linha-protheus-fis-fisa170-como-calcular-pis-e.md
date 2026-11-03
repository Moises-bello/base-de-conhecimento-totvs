---
article_id: 35367817354647
category: Escrita Fiscal - Configurador de Tributos
content_hash: 3b9ce4ee98dde2a86eb852867ffc8705bfdfb25102dcca6bf3d5593275a2e91c
fetched_at: '2026-06-28T22:39:17.674251+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - FISA170 - Como calcular
  PIS e COFINS alíquota zero?
type: support-article
updated_at: '2025-11-04T22:23:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35367817354647-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-e-COFINS-al%C3%ADquota-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801603351) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como realizar o calculo do PIS/COFINS Alíquota zero nas notas de entrada e saída  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo doPIS/COFINS alíquota zero**.**

**Segue exemplo de cadastros de Regra de Base de Cálculo:**

**1)** FISA710 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801606551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801607575)

**2)** FISA710 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801608471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801609239)

**3)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817296535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801613975)

**4)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

Campo **Valor de Origem** deve estar como 06 - Formula Manual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801616791)

Acesse a aba **Detalhamento da Formula de Cálculo**, no campo **Tipo de Regra a ser considerada** = 01 - Valor de Origem e o campo **Consulta da Regra** = O:ZERO, após Adicione e Salve:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817300119)

**5)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Escrituração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801620247)

Segue exemplo de cadastro do PIS alíquota zero:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801621271)

* Utilize o CST = 04 ou 06 para notas de saída

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801622807)

* Utilize o CST = 73 para notas de entrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817307031)

Segue exemplo de cadastro do COFINS alíquota zero:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817308695)

* Utilize o CST = 04 ou 06 para notas de saída:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801626391)

* Utilize o CST = 73 para notas de entrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817312151)

**6)** FISA710 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817313303)

* Segue exemplo de cadastro do PIS alíquota zero:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801632791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817316503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801636247)

* Segue exemplo de cadastro do COFINS alíquota zero:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817321495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801639575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801636247)

**7)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367801640599)

**8)** Inclusão da Nota pelo Compras – Documento de Entrada no valor de R$ 1.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35367817324055)

**Documentos relacionados:**

[Escrita Fiscal - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26791332087191-Escrita-Fiscal-Configurador-de-Tributos)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
