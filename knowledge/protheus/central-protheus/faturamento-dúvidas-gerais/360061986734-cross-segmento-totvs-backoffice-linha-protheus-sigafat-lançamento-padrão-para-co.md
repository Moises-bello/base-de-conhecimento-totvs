---
article_id: 360061986734
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0182da51b891167dc67e8e3a9d07fc6cf1a60f986a6da4a21c87019db2599f3c
fetched_at: '2026-06-28T22:38:28.591171+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Lançamento padrão
  para contabilizar a nota após a transmissão
type: support-article
updated_at: '2023-07-05T16:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061986734-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Lan%C3%A7amento-padr%C3%A3o-para-contabilizar-a-nota-ap%C3%B3s-a-transmiss%C3%A3o
---

**Dúvida**Existe Lançamento Padrão pra fazer contabilização depois que a nota fiscal já tenha sido transmitida?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Não existe, o que se tem é o uso da contabilização off line (**ctbanfs**) que pode ser efetuada tanto após a preparação da nota ou após a transmissão da nota, mas não há LP´s específicos, serão utilizados ou 610 para contabilização por item de nota  ou 620 para contabilização por nota, e nas queries dos lançamentos deverá especificar sua necessidade para que haja a contabilização.  
  
Saiba mais: **[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Lançamento Padrão - para contabilizar no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017692191-MP-FAT-LP-Lan%C3%A7amento-Padr%C3%A3o-para-contabilizar-o-Faturamento?source=search)**
