---
article_id: 360025024033
category: Materiais - Compras (SIGACOM)
content_hash: c82b3033dbc2a05cb15fc3a28fd709b745f717649ffe6ce6811d5b4b37bbe935
fetched_at: '2026-06-28T22:41:17.335432+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  - Frete no total da nota de Devolução
type: support-article
updated_at: '2021-11-22T18:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025024033-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Frete-no-total-da-nota-de-Devolu%C3%A7%C3%A3o
---

**Dúvida**

Como incluir o valor do frete no total da nota de Devolução?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**

Por padrão, ao efetuar o lançamento de uma nota de devolução, o frete não será somado automaticamente no total da nota.

Através do parâmetro MV\_DEVTOT, o frete poderá ser considerado na base de cálculo do ICMS, pois o valor do Imposto a se creditar deverá ser o mesmo valor debitado na saída da nota.

Porem, caso necessite que o frete seja composto no total do documento de devolução deverá utilizar o parâmetro MV\_NFEAFSD = 110

[MV\_NFEAFSD - Parâmetro para definir Frete Seguro ou Despesa na Devolução de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=237388656)

***Saiba Mais :***

[MP - SIGACOM - Pontos de entrada do Documento de Entrada - MATA1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
