---
article_id: 360026776452
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 0ed74e1224b54cd4edb69f6a70e9a4003a1fc226b1d8e3db9719b7364e703439
fetched_at: '2026-06-28T22:39:20.434264+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como sistema calcula
  a base de cálculo do ICMS-ST na Importação?
type: support-article
updated_at: '2021-07-13T17:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026776452-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-sistema-calcula-a-base-de-c%C3%A1lculo-do-ICMS-ST-na-Importa%C3%A7%C3%A3o
---

**Dúvida**Como sistema calcula a Base de cálculo do ICMS-ST na Importação ?  
   
 **Ambiente**Protheus  - A partir Versão 11.8

**Solução**

Para calcular a base de cálculo do ICMS-ST na Importação sistema faz a seguinte composição:

1) Valor Aduaneiro + Pis + Cofins

2) Resultado 1 + MVA ( Margem de Lucro)

3) Resultado 2 divide pela Alíquota do ICMS-ST

Exemplo:

Valor Aduaneiro = 1.000,00

Pis = 21,00

Cofins = 96,50

1.000,00 + 21,00 + 96,50 = 1117,50

1117,50  + 50% (MVA) = 1676,25

1676,25 / 0,82 ( 1-0,18) = 2044,21
