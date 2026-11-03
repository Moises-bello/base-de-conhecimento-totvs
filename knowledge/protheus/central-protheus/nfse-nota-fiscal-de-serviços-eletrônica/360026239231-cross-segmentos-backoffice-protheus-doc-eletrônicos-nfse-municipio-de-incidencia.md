---
article_id: 360026239231
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b1155af78717b74810580dcf4b044a55ec82968b1921d2c4bc26c7fa881e8e20
fetched_at: '2026-06-28T22:39:57.545557+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Municipio
  de Incidencia '
type: support-article
updated_at: '2025-10-16T20:31:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026239231-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Municipio-de-Incidencia
---

**Dúvida**Onde informar o município de Incidência para destaque no XML da NFSe?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Crie um campo na tabela SC5 para informar o município de incidência de acordo com o IBGE, 7 dígitos.  
Informe o nome desse campo dentro do parâmetro MV\_NFSEINC com o tipo Caractere.

**Importante:** O município de incidência, será destacado apenas no XML das prefeituras que possuem essa informação no layout webservice.

**Caso não tenha o parâmetro, poderá criar conforme exemplo abaixo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16748399397783)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16748444551191)**
