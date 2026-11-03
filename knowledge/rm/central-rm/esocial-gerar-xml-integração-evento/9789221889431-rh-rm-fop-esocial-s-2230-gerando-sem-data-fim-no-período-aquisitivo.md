---
article_id: 9789221889431
category: eSocial - Gerar XML/ Integração Evento
content_hash: a0c017ea74a2936fcd06dec6879fbd7497a703ec56cd0ea9578dba7b08d2d203
fetched_at: '2026-06-28T22:47:13.149020+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2230 Gerando sem data fim no período aquisitivo
type: support-article
updated_at: '2026-01-22T22:01:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9789221889431-RH-RM-FOP-eSocial-S-2230-Gerando-sem-data-fim-no-per%C3%ADodo-aquisitivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24346864610455) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Por qual motivo o XML S-2230 de férias gera sem a data fim no período aquisitivo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
A informação que consta no leiaute, à partir do leiaute S-1.0, é que só deverá ser gerado a tag dtFim quando o período aquisitivo for diferente de 1 ano e com data posterior a data início.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24970667513879)

Sendo assim, a tag só será gerada, quando no período aquisitivo, for diferente de 1 ano, conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24970667520535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24970697880727)
