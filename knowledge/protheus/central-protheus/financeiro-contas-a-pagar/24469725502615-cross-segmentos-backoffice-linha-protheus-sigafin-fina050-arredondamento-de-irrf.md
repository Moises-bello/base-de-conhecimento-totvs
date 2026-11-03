---
article_id: 24469725502615
category: Financeiro - Contas a Pagar
content_hash: f5d4cc447c82001eb5d3219d2ad32b379d461f6c7327abb301e2d5476c429b34
fetched_at: '2026-06-28T22:38:08.532296+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: CROSS Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - arredondamento
  de IRRF na inclusão de um título a pagar
type: support-article
updated_at: '2024-08-01T19:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24469725502615-CROSS-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-arredondamento-de-IRRF-na-inclus%C3%A3o-de-um-t%C3%ADtulo-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24469725490199) Tempo aproximado para leitura: **05:00 min** **Dúvida**Qual é o parâmetro de arredondamento do imposto IRRF na inclusão de um título no contas a pagar?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Qual é o parâmetro de arredondamento do imposto IRRF na inclusão de um título no contas a pagar?

Para tratar o arredondamento de **IRRF** na inclusão de **título no Contas a Pagar** utilize os dois

parâmetros a seguir:

**MV\_RNDIRRF** = Defina o critério de arredondamento do IR. (.F. = Trunca ,  Default  .T. = Arredonda)

**MV\_RNDIRF** = Informe o critério de arredondamento do IRRF (Default .F. = Trunca,  .T. = Arredonda)

**Saiba mais**

[Arredondamento de Impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023920652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arredondamento-de-Impostos)
