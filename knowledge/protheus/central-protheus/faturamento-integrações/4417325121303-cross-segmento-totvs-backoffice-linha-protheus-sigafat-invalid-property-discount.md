---
article_id: 4417325121303
category: Faturamento - Integrações
content_hash: 361c6f38e71f1a1a4244bb969c0e018bc1cd351eacdb29f41e13d2656391e67b
fetched_at: '2026-06-28T22:38:26.421608+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - invalid property
  _DISCOUNTPERCENTAGE on MA411LEXML(MATA411.PRW) '
type: support-article
updated_at: '2021-12-28T14:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417325121303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-invalid-property-DISCOUNTPERCENTAGE-on-MA411LEXML-MATA411-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao efetuar a leitura do XML pelas tarefas do Schedule do Importador XML para pedido de venda é gerado o error.log : **invalid property \_DISCOUNTPERCENTAGE on MA411LEXML(MATA411.PRW)**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - a partir da release12.1.25.  
  
**Causa**O erro ocorre por que falta a **TAG** **DiscountPercentage** no xml importado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajuste o XMl, na parte relacionada ao item, incluindo a TAG DiscountPercentage, conforme modelo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417317182359/mceclip0.png)  
2. Posteriormente, no schedule atualize a tarefa para que XML seja lido novamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417310973591/mceclip1.png)  
3. O erro deixará de ocorrer.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417324914071/mceclip2.png)

***Obs. O erro não será mostrado no arquivo Order gerado na pasta XML da System, o erro somente é informado Console do server.ini.***
