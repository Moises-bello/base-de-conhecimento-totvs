---
article_id: 28280530067479
category: Escrita Fiscal - Configurador de Tributos
content_hash: e2da265626bc8f041e127dacc275f72f5da88aa3d2c9e096766dd8f0b20f79dc
fetched_at: '2026-06-28T22:39:18.477260+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Valor do
  ICMS ST na base do PIS/COFINS Apuração utilizando o Configurador de Tributos.
type: support-article
updated_at: '2024-12-04T21:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28280530067479-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Valor-do-ICMS-ST-na-base-do-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28280530033047) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como ajustar a base de calcular PIS/COFINS Apuração quando incide o valor do ICMS ST utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para determinar o valor do ICMS ST na base do PIS/COFINS Apuração, deve ser ajustado a regra da Base de Cálculo indicando como deve ser realizado o comportamento:

**Segue exemplo de cadastros de Regra de Base de Cálculo:**

FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

**1)** Valor do ICMS ST soma na base do PIS/COFINS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280548453783)

Ajuste o campo **Valor de Origem** = 11 – Fórmula Manual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280548454935)

Acesse a aba Detalhamento da Fórmula de Cálculo.

Para iniciar, clique em Editar Fórmula e seguir os passos abaixo:

* No campo “Consulta de Regra” = O:VAL\_MERCADORIA (Adicionar)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280530037655)

* Informe menos (-);
* No campo “Tipo de Regra a ser consultada” = 05 – Regra de Tributo, no campo “Tributo para filtrar a consulta” informe a Regra de Cálculo criada do ICMS ST, após selecione VAL:(a Regra de Cálculo do ICMS ST):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280548458519)

**2)** **Valor do ICMS ST não incide na base do PIS/COFINS Apuração:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280548453783)

Ajuste o campo **Valor de Origem** = 01 – Valor da Mercadoria:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280548459159)

Obs.: Todos os impostos relacionados (ICMS ST, PIS Apuração e COFINS Apuração) devem ser calculados pelo Configurador de Tributos (FISA170).

 

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular o ICMS ST?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17802352397591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ICMS-ST)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular PIS-COFINS Apuração utilizando o Configurador de Tributos para notas de entrada e saída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273192090135-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como deduzir o valor do ICMS na base do PIS/COFINS Apuração utilizando o Configurador de Tributos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273997578391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-deduzir-o-valor-do-ICMS-na-base-do-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos)
