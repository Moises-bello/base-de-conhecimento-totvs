---
article_id: 35619536885015
category: Escrita Fiscal - Configurador de Tributos
content_hash: 1e97a7c9435283c6ae7f8e30505d0b19e46c7d23b5e8fc52360e44d6b7f37469
fetched_at: '2026-06-28T22:39:18.444874+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  PIS/COFINS Auto Peças utilizando o Configurador de Tributos?
type: support-article
updated_at: '2025-10-14T14:01:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35619536885015-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Auto-Pe%C3%A7as-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560677783) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar PIS/COFINS para Auto Peças utilizando o Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do PIS/COFINS Auto Peças.

**Segue exemplo de cadastros:**

**1)** FISA170 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560678039)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536844055) 

**2)** FISA170 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536844951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536845847)

 

**3)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536846871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560680727)

**4)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560681367)

Regra da Alíquota do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536850199)

Regra da Alíquota do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536851479)

**5)** FISA170 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560683927)

Segue exemplo de cadastro do PIS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560685079)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536855191)

Segue exemplo de cadastro do COFINS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560689047)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619560690711)

**6)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com impostos nos valores de PIS = 1,00, COFINS = 5,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35619536857239)

**OBS:**para geração dos títulos do PIS/COFINS no Contas a Receber, deve ser vinculado uma Regra Financeira na**Regra de Cálculo - Documentos Fiscais.**

**Documentações relacionadas:**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular PIS-COFINS Apuração utilizando o Configurador de Tributos para notas de entrada e saída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273192090135-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
