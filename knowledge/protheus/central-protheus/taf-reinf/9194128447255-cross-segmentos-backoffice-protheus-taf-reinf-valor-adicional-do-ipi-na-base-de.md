---
article_id: 9194128447255
category: TAF - REINF
content_hash: 0475e7057ee803cebd7ddb38521154d322bc2084c1bb214a305f7de03f5de322
fetched_at: '2026-06-28T22:41:34.886792+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Valor adicional  do IPI
  na base de cálculo R 2050
type: support-article
updated_at: '2022-09-28T17:29:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9194128447255-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Valor-adicional-do-IPI-na-base-de-c%C3%A1lculo-R-2050
---

**Dúvida:**

**Como desconsiderar o valor do tributo de IPI na base de calculo para o evento R 2050 ?**  
  
**Ambiente**TAF - REINF - versão 12.1.17 ou superior  
  
**Solução**

Para desconsiderar o valor do IPI deve ser feito a criação do parâmetro **MV\_2050TRB (tipo caracter)** esse parâmetro  controlará se o IPI será ou **NÃO** abatido do valor da receita bruta na apuração do evento R-2050.

Para que o valor do tributo IPI seja abatido do valor da receita bruta, é necessário configurar o parâmetro com o conteúdo 1 **(sem aspas)**:

**MV\_2050TRB := 1**
