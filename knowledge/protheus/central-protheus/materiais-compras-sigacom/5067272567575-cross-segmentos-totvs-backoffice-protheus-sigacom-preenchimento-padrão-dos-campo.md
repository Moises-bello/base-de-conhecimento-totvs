---
article_id: 5067272567575
category: Materiais - Compras (SIGACOM)
content_hash: ffb2e313bdbcba47b806fe40beaa526bc362a7d8cc55077a573960594d777f28
fetched_at: '2026-06-28T22:41:24.065257+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preenchimento padrão
  dos campos no pedido de compra C7_CC / C7_CONTA / C7_ITEMCTA '
type: support-article
updated_at: '2022-03-28T12:26:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5067272567575-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Preenchimento-padr%C3%A3o-dos-campos-no-pedido-de-compra-C7-CC-C7-CONTA-C7-ITEMCTA
---

**Dúvida**

Ao alterar o código de um produto, o sistema não limpa os dados do código do produto anterior nos campos **C7\_CC**, **C7\_CONTA** e **C7\_ITEMCTA**.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras- Todas as versões  
  
**Solução**

O preenchimento padrão dos campos no item do pedido de compra obedece as seguintes regras:

1) Se o campo estiver vazio, ele é preenchido com o conteúdo do campo do cadastro de Produto (SB1).

2) Se já estiver preenchido, ao alterar o produto do item do pedido de compra, o conteúdo dos campos **C7\_CC, C7\_CONTA**, **C7\_ITEMCTA** é mantido conforme o que já estava preenchido.

Esse tratamento é regra do sistema e **não pode ser alterado** devido a pontos de entradas e customizações já existentes.

Para os casos onde as entidades contábeis são informadas direto no cadastro do produto, deve-se utilizar os parâmetro **MV\_PRODCTB**.

Ver link: [395938 MMAN5773 DT Parâmetro MV\_PRODCTB](https://tdn.totvs.com/pages/viewpage.action?pageId=271181501)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
