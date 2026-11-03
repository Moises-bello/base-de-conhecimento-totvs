---
article_id: 28279954561559
category: Escrita Fiscal - Configurador de Tributos
content_hash: 4bb6fc403f48864361e6590b7d12c4c00a6e1c0029ece29f20e2340d63992322
fetched_at: '2026-06-28T22:39:18.464843+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como deduzir
  o valor do ISS da base somente do PIS/COFINS Apuração utilizando o Configurador
  de Tributos
type: support-article
updated_at: '2024-12-04T21:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28279954561559-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-deduzir-o-valor-do-ISS-da-base-somente-do-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28279954514583) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como ajustar a base de cálculo do PIS/COFINS Apuração quando o valor do ISS deve ser deduzido utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para deduzir o valor do ISS na base do PIS/COFINS Apuração, deve ser ajustado a Regra da Base de Cálculo:

* Lembrando que, deverá ser criada Regra de Documento Fiscal para o ISS além do PIS e COFINS apuração.

**1)** Valor do ISS deduzido na base do PIS/COFINS Apuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279954518039)

Ajuste o campo **Valor de Origem** = 11 – Fórmula Manual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279954521879)

Acesse a aba Detalhamento da Fórmula de Cálculo.

Para iniciar, clique em Editar Fórmula e seguir os passos abaixo;

* No campo “Consulta de Regra” = O:VAL\_MERCADORIA (Adicionar):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279954524055)

* Informe menos (-);
* No campo “Tipo de Regra a ser consultada” = 05 – Regra de Tributo, no campo “Tributo para filtrar a consulta” informe a Regra de Cálculo criada do ISS, após selecione VAL:(a Regra de Cálculo do ISS):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279994194071)

**2)** **Valor do ISS não incide na base do PIS/COFINS Apuração:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279954518039)

Ajuste o campo **Valor de Origem** = 01 – Valor da Mercadoria:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28279994198679)

OBS: Todos os impostos relacionados (ISS, PIS Apuração e COFINS Apuração) devem ser calculados pelo Configurador de Tributos (FISA170).

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular PIS-COFINS Apuração utilizando o Configurador de Tributos para notas de entrada e saída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273192090135-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-Apura%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
