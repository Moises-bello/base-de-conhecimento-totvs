---
article_id: 360020111692
category: Materiais - Compras (SIGACOM)
content_hash: 26f1af20bdc805381ec1924c3181b50d71c3f99a4909a3413c498584f6fe01a8
fetched_at: '2026-06-28T22:41:10.425207+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quando tento excluir
  uma nota de compras pelo documento de entrada o sistema apresenta o Help A103ValExc.  '
type: support-article
updated_at: '2023-06-21T13:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020111692-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quando-tento-excluir-uma-nota-de-compras-pelo-documento-de-entrada-o-sistema-apresenta-o-Help-A103ValExc
---

**Duvida :**

Quando tento excluir uma nota de compras pelo documento de entrada o sistema apresenta o Help A103ValExc.

![A103.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016126652)

**Ambiente**Protheus – Compras – A partir da versão P12.1.17   
  
**Solução**A mensagem **A103VALEXC** é apresentada na verificação de vinculo com o pedido de venda, ou seja, em seu cenário a mensagem apresenta as informações dos campos abaixo, onde pode ter sido efetuado nota de saída de devolução para os itens, dessa forma será necessário validar os campos:  
**C6\_FILIAL+" "+C6\_NUM+" "+C6\_ITEM+" "+C6\_PRODUTO**

![A103.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016126652)

Pode-se realizar o filtro com as informações da mensagem para identificação do Pedido/Item.  
E no caso, havendo a necessidade da exclusão da NF de Entrada, deve-se desvincular essa NF de Entrada do item pedido.

**Obs:**

Para essa alteração do Pedido de Vendas, esse Pedido que possui o vinculo necessita ser alterado, e no caso se ele tenha sida Faturado, , essa NF de Saída precisa ser excluída para isso o Pedido poder ser retirado o vínculo.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM)
