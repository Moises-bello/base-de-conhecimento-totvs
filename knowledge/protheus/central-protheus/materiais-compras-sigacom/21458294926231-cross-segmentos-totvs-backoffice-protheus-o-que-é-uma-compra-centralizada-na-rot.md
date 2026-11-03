---
article_id: 21458294926231
category: Materiais - Compras (SIGACOM)
content_hash: 1f14a17dca7a7790c357b212554c2d87fa3a5dfebecf93c3227b4ae149fb2231
fetched_at: '2026-06-28T22:41:12.886302+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - O que é uma Compra Centralizada
  na rotina MATA110?
type: support-article
updated_at: '2024-02-19T16:41:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21458294926231-Cross-Segmentos-Totvs-Backoffice-Protheus-O-que-%C3%A9-uma-Compra-Centralizada-na-rotina-MATA110
---

**Dúvida**

O que é uma Compra Centralizada na rotina MATA110?

**Ambiente**

Protheus – Compras – A partir da versão 12

**Solução**

A Compra Centralizada permite centralizar o processo de compra de uma ou várias filiais em uma única filial.

Para realizar uma Compra Centralizada deve existir ao menos duas Filiais no sistema (onde uma será denonimada matriz, ou filial centralizadora). Por exemplo as Solicitações de Compra de uma determinada filial poderão ser centralizada em outra (Conceito de Matriz), logo a responsável por todo o processo de cotação e compra do Produto será a Matriz.

**Passo 1 - Crie uma Solicitação de Compra:**

Observe que a SC abaixo foi criada para a Matriz.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458284729879)**

**Passo 2 - Selecione a empresa Centralizadora:**

A empresa centralizadora é a empresa que ficará responsável por todo o processo de compra do produto.

![GIF-‐-Feito-com-o-Clipchamp.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21458294895383)

**Passo 3 - Valide que após Centralizar a Compra será gerada uma nova SC para a empresa centralizadora e a SC que foi gerada anteriormente ficará com a legenda roxa.**

No teste foi criada a SC 000006 a partir da centralização da SC 000036, porém observe que a filial de entrega da SC 000006 é o código da empresa que gerou a solicitação inicialmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458284731799)

Na imagem abaixo é possível visualizar a filial de entrega da SC 000006:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21458294898327)

Após o processo informado acima, deve ser realizada a cotação normalmente, Gerando a Cotação, Atualizando e por fim Analisando a cotação, para que o processo seja finalizado.

A filial para qual o pedido será criado irá depender do conteúdo do Parâmetro MV\_COTFIAP, que Indica se os pedidos gerados por cotações em compra centralizada serão administrados pela filial de compra (C) ou pela filial de entrega (E).

***Saiba Mais :***

*[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*

*[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*
