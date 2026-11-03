---
article_id: 28129449411351
category: Faturamento - Cenários de Venda
content_hash: e43d0a577c856282355fdcb8ade3d8e7b7620e4662dbbf90ad9eadcfa58f8fd4
fetched_at: '2026-06-28T22:38:33.996409+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT  - Como instituir faixa de
  valores na tabela de preço (OMSA010)
type: support-article
updated_at: '2026-06-09T18:23:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28129449411351-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-instituir-faixa-de-valores-na-tabela-de-pre%C3%A7o-OMSA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28129488661015) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como instituir faixa de valores na tabela de preço (OMSA010), de modo que posso ter valores diferentes por quantidade?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Simulando uma condição onde, mudamos o item a partir de determinado preço.

![](https://totvssuporte.zendesk.com/attachments/token/NzApxbDDEArFouKXDgprJ83bu/?name=image.png)

Para que o valor do "Preco Unitario Liquido (C6\_PRCVEN)" se torne outro valor, se a quantidade "Quantidade (C6\_QTDVEN)" estiver em alguma faixa de preço, coloque na tabela de preço (da maneira que está acima), preços "Preco de venda (DA1\_PRCVEN)" de acordo com "Faixa para o preco (DA1\_QTDLOT)".

Assim, no exemplo acima (usando a tabela de preço e o item no pedido de vendas):

* Se o item "INFINITO" for vendido acima de 200 unidades, o preço é R$2
* Se o item "INFINITO" for vendido acima de 100 unidades, o preço é R$5
* Se o item "INFINITO" for vendido acima de até 100 unidades, o preço é R$10
