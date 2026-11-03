---
article_id: 360011934671
category: Materiais - Compras (SIGACOM)
content_hash: a610fc5259cdb2608e1800f1886827f86265b86a1f4b87676d25d298e0b9e349
fetched_at: '2026-06-28T22:41:10.278247+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preenchimento padrão
  dos campos no Pedido de Compras
type: support-article
updated_at: '2022-05-13T11:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011934671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Preenchimento-padr%C3%A3o-dos-campos-no-Pedido-de-Compras
---

**Dúvida**Ao alterar o código de um produto, o sistema não limpa os dados do código do produto anterior.

Preenchimento padrão dos campos no Pedido de Compras  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**O preenchimento padrão dos campos no item do Pedido de Compras obedece as seguintes regras:

**1)** Se o campo estiver vazio, ele é preenchido com o conteúdo do campo do cadastro de Produto.

**2)** Se já estiver preenchido, ao alterar o produto do item do pedido de compras, o conteúdo dos campos **C7\_CC, C7\_ITEMCTA, C7\_CLVL, C7\_TES** é mantido conforme o que já estava preenchido, exceto para o campo **C7\_CONTA**. No caso do campo **C7\_CONTA**, o padrão de preenchimento é sempre sobrescrever o conteúdo do campo com àquele que corresponde ao cadastro de Produtos.

Caso regra não atenda, poderá configurar o ***MV\_PRODCTB***.

***Saiba Mais :***

[MV\_PRODCTB - Parâmetro](https://tdn.totvs.com/pages/viewpage.action?pageId=271181501)

[PCOM04012 - Preenchimento padrão dos campos no pedido de compra.](http://tdn.totvs.com/pages/viewpage.action?pageId=267793255)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
