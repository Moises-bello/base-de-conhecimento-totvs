---
article_id: 1500006455381
category: Materiais - Compras (SIGACOM)
content_hash: 732ab2f3de9f8903119ef7e9a10aa493c86bdf685941307c6d87642e0d2d235a
fetched_at: '2026-06-28T22:41:14.562981+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como dar Entrada em
  uma nota de complemento de preços de uma venda que foi recusada pelo cliente ?
type: support-article
updated_at: '2022-05-16T21:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006455381-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-dar-Entrada-em-uma-nota-de-complemento-de-pre%C3%A7os-de-uma-venda-que-foi-recusada-pelo-cliente
---

**Dúvida**

Como dar Entrada em uma nota de complemento de preços de uma venda que foi recusada pelo cliente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  Compras - A partir da versão 12.00  
  
**Solução:**

Através do documento de entrada usando um TES com o campo quantidade zerada = Sim, consegue-se dar entrada nessa nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008616821/mceclip0.png)

Nesse caso a entrada terá que ser de forma manual e não pela opção retornar.

Movimento -> documento de entrada -> Incluir

Tipo da nota = D, preenche-se o código do cliente e os demais dados da nota, digite o produto, o TES e em outra ações chama-se a opção Origem, para que o sistema localize a nota de saída( de complemento de preços ),

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008409982/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008617101/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008617321/mceclip3.png)

**Saiba Mais :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - SIGACOM ( Compras )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
