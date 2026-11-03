---
article_id: 28273997578391
category: Escrita Fiscal - Configurador de Tributos
content_hash: 0a4bd0e488c9848cf792c355fb228d1a3a35d49f66b3db7563f5f2f6b17d9ad2
fetched_at: '2026-06-28T22:39:18.459883+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como deduzir
  o valor do ICMS na base do PIS/COFINS Apuração utilizando o Configurador de Tributos.
type: support-article
updated_at: '2024-12-04T17:10:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273997578391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-deduzir-o-valor-do-ICMS-na-base-do-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997542679) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como ajustar a base de calcular PIS/COFINS Apuração quando o valor do ICMS deve ser deduzido utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para deduzir o valor do ICMS na base do PIS/COFINS Apuração, deve ser ajustado a Regra da Base de Cálculo. Segue exemplo de cadastros de Regra de Base de Cálculo:

FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

**1)** Valor do ICMS deduzido na base do PIS/COFINS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997543575)

Ajuste o campo **Valor de Origem** = 11 – Fórmula Manual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997547543)

Acesse a aba Detalhamento da Fórmula de Cálculo.

Para iniciar, clique em Editar Fórmula e seguir os passos abaixo;

* No campo “Consulta de Regra” = O:VAL\_MERCADORIA (Adicionar):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997548439)

* Informe menos (-);
* No campo “Tipo de Regra a ser consultada” = 05 – Regra de Tributo, no campo “Tributo para filtrar a consulta” informe a Regra de Cálculo criada do ICMS, após selecione VAL:(a Regra de Cálculo do ICMS):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997552407)

 

**2)** **Valor do ICMS não incide na base do PIS/COFINS Apuração:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273997553943)

Ajuste o campo **Valor de Origem** = 01 – Valor da Mercadoria:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28273973498263)

**Importante:** Todos os impostos relacionados (ICMS, PIS Apuração e COFINS Apuração) devem ser calculados utilizando o Configurador de Tributos (FISA170).

 

[CFGTRIB - Dedução somente do ICMS Próprio da base de cálculo de PIS e base de cálculo de COFINS](https://tdn.totvs.com/pages/releaseview.action?pageId=720356042#CFGTRIBDedu%C3%A7%C3%A3osomentedoICMSPr%C3%B3priodabasedec%C3%A1lculodePISebasedec%C3%A1lculodeCOFINS,emopera%C3%A7%C3%A3ocomc%C3%A1lculodeFECPPr%C3%B3prio-Defini%C3%A7%C3%A3odeRegradeC%C3%A1lculo-PIS)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
