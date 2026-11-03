---
article_id: 360058051673
category: RH - Rescisão
content_hash: a62d831aedae517bb806a66f36c436addfcfc09243ef81beba94aa2f0156e086
fetched_at: '2026-06-28T22:43:50.993065+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: MP - GPE - Porque TRCT não demonstra verbas de férias indenizadas
type: support-article
updated_at: '2020-11-24T20:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058051673-MP-GPE-Porque-TRCT-n%C3%A3o-demonstra-verbas-de-f%C3%A9rias-indenizadas
---

**Dúvida**

MP - GPE - Porque TRCT não demonstra verbas de férias indenizadas?

**Ambiente**Microsiga Protheus - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**No TRCT o campo 66.1 não serão apresentadas verbas , pois o campo **RR\_NUMID e RR\_HORAS** não preenchem quando as verbas são informadas e este campo é o que valida para que o campo 66.1 possua informação.

No campo **RR\_NUMID ( Num Identif )**, devem ser informadas as datas inicial e final do período aquisitivo correspondente à verba lançada, no formato "AAAAMMDD - AAAAMMDD" e o campo **RR\_HORAS ( Horas ),** com a quantidade respectiva aos avos Ex: 4.12 ( 4/12 avos), para que o lançamento manual da verba de férias seja calculado e impresso corretamente no TRCT.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098392334/mceclip0.png)
