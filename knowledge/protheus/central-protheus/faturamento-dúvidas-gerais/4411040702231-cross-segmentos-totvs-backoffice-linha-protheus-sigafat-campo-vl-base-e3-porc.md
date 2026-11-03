---
article_id: 4411040702231
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4a4e844107531ab758d1d9d606d2c1e3ab6deb471ac937b9ba52b0ec6992f5d0
fetched_at: '2026-06-28T22:38:29.949141+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campo Vl. Base
  E3_PORC
type: support-article
updated_at: '2021-10-19T14:58:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411040702231-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-Vl-Base-E3-PORC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Gravação do campo Vl. Base E3\_PORC  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411034123927/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- a partir da versão 12.  
  
**Solução**O cálculo do campo Vl. Base E3\_PORC é preenchido com a porcentagem proporcional do valor da comissão calculada.

Exemplo:

Comissão inserida na linha do pedido de venda onde cada item tem uma porcentagem diferente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411034823191/mceclip1.png)

A porcentagem da comissão na SE3 deste pedido de venda calculada é 6,89%:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411030841239/mceclip2.png)

Por que o sistema vai gravar a porcentagem baseado no total do valor da comissão:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411031176855/mceclip4.png)  
  
Cálculo do Total Vlr Comissão \* Total Vlr Itens para obter a porcentagem:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411035447319/mceclip5.png)

**Saiba mais na documentação:**  
**[Configuração das Comissões dos Vendedores](https://tdn.totvs.com/x/efIKDg)**
