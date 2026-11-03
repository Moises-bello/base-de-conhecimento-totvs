---
article_id: 28280838148503
category: Escrita Fiscal - Configurador de Tributos
content_hash: 6e2ecee87be9901b8d1259553af942e551352ab79b3fb0432680167f8daf9cc0
fetched_at: '2026-06-28T22:39:18.484527+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Valor do
  IPI na base do PIS/COFINS Apuração utilizando o Configurador de Tributos.
type: support-article
updated_at: '2024-12-04T21:06:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28280838148503-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Valor-do-IPI-na-base-do-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28280823960215) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como ajustar a base de calcular PIS/COFINS Apuração quando incide o valor do IPI utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para determinar o valor do IPI na base do PIS/COFINS Apuração, deve ser ajustado a regra da Base de Cálculo indicando como deve ser realizado o comportamento:

**Segue exemplo de cadastros de Regra de Base de Cálculo:**

FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

**1)** Valor do IPI soma na base do PIS/COFINS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280838120983)

Ajuste o campo **Valor de Origem** = 11 – Fórmula Manual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280823963543)

Acesse a aba Detalhamento da Fórmula de Cálculo.

* Para iniciar, clique em Editar Fórmula e seguir os passos abaixo;
* No campo “Consulta de Regra” = O:VAL\_MERCADORIA (Adicionar):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280823965079)

* Informe Mais (+);
* No campo “Tipo de Regra a ser consultada” = 05 – Regra de Tributo, no campo “Tributo para filtrar a consulta” informe a Regra de Cálculo criada do IPI, após selecione VAL:(a Regra de Cálculo do IPI) em Consulta de Regras:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280838131735)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280838132247)

**2)** **Valor do IPI não incide na base do PIS/COFINS Apuração:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280838120983)

 

Ajuste o campo **Valor de Origem** = 01 – Valor da Mercadoria:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28280823969815)

Obs.: Todos os impostos relacionados (ICMS, PIS Apuração e COFINS Apuração) devem ser calculados pelo Configurador de Tributos (FISA170).

 

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular PIS-COFINS Apuração utilizando o Configurador de Tributos para notas de entrada e saída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273192090135-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
