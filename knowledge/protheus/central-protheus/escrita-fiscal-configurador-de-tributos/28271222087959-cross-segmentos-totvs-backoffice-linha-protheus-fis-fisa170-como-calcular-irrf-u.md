---
article_id: 28271222087959
category: Escrita Fiscal - Configurador de Tributos
content_hash: b358198458a5407b9b81bd505032f02cab6ac6c945ba2dcb88e8194c00dd2f66
fetched_at: '2026-06-28T22:39:18.412153+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  IRRF utilizando o Configurador de Tributos para notas de entrada e saída.
type: support-article
updated_at: '2025-01-14T14:01:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271222087959-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-IRRF-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222033431) Tempo aproximado para leitura: 00:05:00 min

**Dúvida**Como calcular o IRRF utilizando o Configurador de Tributos (FISA170) para notas de entrada e saída?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões.  
  
**Solução**

Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do IRRF.

Segue exemplo de cadastros:

**1)** FISA170 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222036375)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222038295)

**2)** FISA170 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222042647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208216727)

**3)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222051735)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208221079)

**4)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208226711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271222057367)

**5)** FISA170 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208234903)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208237463) 

**6)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com imposto de IRRF no valor de R$ 15,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29210400231447)

**7****)** Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com imposto de IRRF no valor de R$ 15,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28271208243607)

**OBS:** para geração dos títulos do IRRF no Contas a Pagar ou Contas a Receber, deve ser vinculado uma Regra Financeira na **Regra de Cálculo - Documentos Fiscais.**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
