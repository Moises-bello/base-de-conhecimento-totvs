---
article_id: 4417311815575
category: Faturamento - Integrações
content_hash: f6cd611095d1df1412236e6b8242c4de1afb469e8ac6cee98492f3c3df58cfdd
fetched_at: '2026-06-28T22:38:26.403802+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Falha na gravação!
  Código do item não encontrado
type: support-article
updated_at: '2021-12-28T14:09:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417311815575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Falha-na-grava%C3%A7%C3%A3o-C%C3%B3digo-do-item-n%C3%A3o-encontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao importar o XML pelo Importador XML para geração do pedido, gera a mensagem no arquivo Order:

**Falha na gravação! Código do item não encontrado**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417332085783/mceclip0.png)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - a partir da release 12.1.25.  
  
**Solução**A mensagem ocorre por que na integração, o sistema verifica se o **código de barras do produto**  ou a **amarração de produto x cliente** está igual ao que o XML está informando para integrar o pedido.

No xml vem definido o tipo do código do produto através da **tag typecodprod**, se estiver como **EN**' ou '**UP**' - Busca o produto por meio do **código de barra**s (**B1\_CODBAR**), se estiver como '**BP**' - Busca pela amarração de **clientes x produtos** (**A7\_PRODUTO**).

Exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417317766039/mceclip1.png)

Neste exemplo, o tipo do código do produto é definido como **EN - código da barras**, então o código trazido na **tag ItemCode** deve ser a mesma no campo **B1\_CODBAR** do cadastro do produto para que a mensagem deixe de ocorrer.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417311738007/mceclip2.png)
