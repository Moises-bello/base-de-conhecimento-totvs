---
article_id: 360037428353
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3ea832955944b3c25e42f6e28a78bd27b7176e7e07b2809ee5c8a735269696fe
fetched_at: '2026-06-28T22:38:41.220970+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Como considerar a quantidade disponível em estoque na inclusão do
  Pedido de Vendas
type: support-article
updated_at: '2021-04-28T15:50:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037428353-MP-FAT-Como-considerar-a-quantidade-dispon%C3%ADvel-em-estoque-na-inclus%C3%A3o-do-Pedido-de-Vendas
---

**Dúvida**

Como considerar a quantidade disponível em estoque na inclusão do Pedido de Vendas?  
  
**Ambiente**

Microsiga Protheus – A partir da versão 12.  
  
**Solução**

As informações de **bloqueio de Estoque** e Crédito são consideradas **apenas após a liberação do pedido** de vendas, porém é possível que, ao realizar a **liberação manual** o sistema não permita a liberação do pedido com uma quantidade maior que a disponível no estoque.

Para isso configure o parâmetro “**Sugere Qtde Liber.?**”, apertando a tecla F12 na tela de pedidos de venda (**MATA410**), como “Sim”:

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048296754/01.PNG)

Preencha também os parâmetros “**Sugere Qtde Liber.?**” e “**Libera so c/Estoque?**”, apertando a tecla F12 na tela de Liberação de Pedidos (**MATA440**), como “Sim”:

![02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048296834/02.PNG)

Realizando esta configuração, ao incluir o pedido, digitar a quantidade liberada no campo “**Qtd. Liberada**” (**C6\_QTDLIB**):

![03.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360049176873/03.PNG)

Ao realizar este processo, se a quantidade digitada no campo “Qtd. Liberada” (**C6\_QTDLIB**) estiver **disponível no estoque**, o pedido será criado com a **legenda amarela (Liberado)** e a quantidade será reservada no estoque.

Se a quantidade digitada no campo “Qtd. Liberada” (**C6\_QTDLIB**) **não estiver disponível** no estoque, o pedido será incluído com a **legenda verde** (Aberto).

Saiba mais: **<https://tdn.totvs.com/pages/viewpage.action?pageId=225267328>**
