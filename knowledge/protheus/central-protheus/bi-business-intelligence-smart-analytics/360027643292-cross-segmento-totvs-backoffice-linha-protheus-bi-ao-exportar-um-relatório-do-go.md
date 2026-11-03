---
article_id: 360027643292
category: BI - Business Intelligence - Smart analytics
content_hash: 9d0dc6c47669fb873559b05692983321d70422d56cc5b6bfdcbc19387fee1970
fetched_at: '2026-06-28T22:37:04.086296+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Ao exportar um relatório
  do Gooddata em PDF, ele tráz virgulas ao invés de pontos separando os números
type: support-article
updated_at: '2022-07-27T18:02:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027643292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Ao-exportar-um-relat%C3%B3rio-do-Gooddata-em-PDF-ele-tr%C3%A1z-virgulas-ao-inv%C3%A9s-de-pontos-separando-os-n%C3%BAmeros
---

**Ocorrência**Quando exporto um relatório do Gooddata em PDF, ele retorna os números separados por vírgulas ao invés de pontos, não obedecendo o padrão de minha customização da Dashboard.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027709791/mceclip1.png)**->PDF**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027709891/mceclip2.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – GoodData – A partir da versão 12  
  
**Causa**Este comportamento é causado devido a configuração regional dos números, já que cada usuário pode customizar de forma individual sua visualização nos relatórios. No entanto, o código do lado do servidor que cuida das exportações, não tem acesso às configurações do usuário, portanto, os valores exportados usarão sempre a formatação padrão, no caso a americana.
