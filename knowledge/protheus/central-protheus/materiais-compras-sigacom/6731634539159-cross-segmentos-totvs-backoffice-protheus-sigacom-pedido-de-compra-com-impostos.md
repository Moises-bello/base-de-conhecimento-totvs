---
article_id: 6731634539159
category: Materiais - Compras (SIGACOM)
content_hash: 0bc22e97feef6d0c564923f753fb4f4873cf518d404d81439a2ecbdd0f001d85
fetched_at: '2026-06-28T22:41:22.070415+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Pedido de Compra com
  Impostos
type: support-article
updated_at: '2022-06-13T12:18:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6731634539159-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Pedido-de-Compra-com-Impostos
---

**Dúvida**Como parametrizar para que o valor do imposto seja arredondado igualmente no pedido de compras?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**Para que ao utilizar vários itens no pedido de compras o imposto fique igual em todas as linhas é necessário desabilitar o parâmetro **MV\_RNDSOBR: .F.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6731567582359/mceclip0.png)**

1. Sempre que o **RNDSOBR** estiver como Falso, não teremos o tratamento das sobras e consequentemente os valores serão truncados por item.
2. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* também como Verdadeiro, será efetuado o tratamento de arredondamento por item.
3. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* como falso, será efetuado o tratamento de arredondamento no total do imposto (truncando por item e considerando a sobra).

OBS: parâmetro podendo ser utilizado para **IPI** E **ICMS** no pedido de compras.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Arredondamento de Impostos](https://tdn.totvs.com/display/public/PROT/FIS00024_Arredondamento_de_Impostos)
