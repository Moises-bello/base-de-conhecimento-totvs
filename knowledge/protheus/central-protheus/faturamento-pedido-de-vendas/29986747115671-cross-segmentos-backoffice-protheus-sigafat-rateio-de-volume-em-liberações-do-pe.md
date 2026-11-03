---
article_id: 29986747115671
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d269e4762fb87808588ed738a94bfd89f9b22f58664fe8e67cdd94f83315e33c
fetched_at: '2026-06-28T22:38:40.016005+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Rateio de volume em liberações
  do pedido de venda
type: support-article
updated_at: '2025-02-17T11:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29986747115671-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Rateio-de-volume-em-libera%C3%A7%C3%B5es-do-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29986747101847) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Cross Segmentos - Backoffice Protheus - SIGAFAT - Qual a forma do rateio de volume em liberações do pedido de venda?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Estes campos do pedido de vendas são informativos, ou seja o valor que mencionar será levado para a DANFE.

Os campos que são tratados para rateio, são os campos de despesas conforme documentação a seguir: http://tdn.totvs.com/pages/releaseview.action?pageId=239024024

Se preenchido o campo "Volume 1 (C5\_VOLUME1)", há de ser preenchido também o campo "Especie 1 (C5\_ESPECI1)" pois são pares.  
  
Supondo um pedido de venda com:  
1 Item | Quantidade: 100 | Preço: 1 | Total: 100

E com os campos preenchidos:

* "Especie 1 (C5\_ESPECI1)" = ESPECIE 1
* "Volume 1 (C5\_VOLUME1)" = 100
* "Peso líquido (C5\_PESOL)" = 100
* "Peso bruto (C5\_PBRUTO)" = 100

Ao liberar e faturar separado 50 quantidades em uma NF e 50 em outra NF, o resultado em cada uma das notas foi:

* "Especie 1 (F2\_ESPECI1)" = ESPECIE 1
* "Volume 1 (F2\_VOLUME1)" = 100
* "Peso líquido (F2\_PLIQUI)" = 100
* "Peso bruto (F2\_PBRUTO)" = 100

Não há rateio ou diferença do valor do campo "Volume 1 (F2\_VOLUME1)" em várias notas fiscais de saída do mesmo pedido de venda.

São campos de inserção manual e são espelhados da forma que foram digitados no cabeçalho do pedido de venda, não importa a quantidade de notas fiscais de saída que saírem desse mesmo pedido de venda, serão os mesmos por padrão sempre.
