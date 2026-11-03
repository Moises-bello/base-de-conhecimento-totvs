---
article_id: 22536600641815
category: Materiais - Compras (SIGACOM)
content_hash: 8c1f857be63c350fdf7dbade0f168113e92a1e2ac631416ac204be40849bc33e
fetched_at: '2026-06-28T22:41:15.980718+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como mudar o fornecedor
  e/ou loja na alteração do pedido de compras?
type: support-article
updated_at: '2024-04-03T20:18:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22536600641815-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-mudar-o-fornecedor-e-ou-loja-na-altera%C3%A7%C3%A3o-do-pedido-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22536591146519) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como mudar o código do fornecedor e/ou código da loja durante a alteração de um pedido de compras?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22536600535063)  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.33  
  
**Solução**Por padrão não temos como alterar o fornecedor na opção de alterar no pedido de compras. Porém abaixo existem dois cenários, onde temos processos padrão para executá-los. Verifique em seu processo, se a necessidade de se alterar os fornecedor e loja do pedido de compras, é por conta de alguma das situações abaixo ?  
  
O primeiro cenário é se comprou de uma filial do seu fornecedor, mas na hora da entrega/emissão da nota é outra filial do fornecedor que entrega. Temos um pergunte no F12 da MATA140 (pré-nota, caso em seu ambiente a nota seja incluída primeiro pela pré-nota) e também na MATA103 ( documento de entrada ), onde podemos configurar, para que o sistema localize o PC somente pelo código do fornecedor, sem considerar a loja. No entanto, essa regra só é aplicável se o código do fornecedor for o mesmo utilizado, mudando apenas o código da loja. Abaixo documento sobre :  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como vincular um pedido de compras de outra loja do fornecedor?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19603901438615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-vincular-um-pedido-de-compras-de-outra-loja-do-fornecedor?source=search)

O segundo cenário é se a nota estiver com um CNPJ totalmente diferente, caracterizando uma outra empresa do grupo, por exemplo. Nessa caso, temos o processo de entrega por terceiros. Segue documento abaixo sobre esse processo.  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Processo de Entrega Por Terceiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Processo-de-Entrega-Por-Terceiros?source=search)  
  
Utilizando um dos dois processos, não é necessário efetuar alteração no código do fornecedor loja no pedido de compra já incluído.

**Saiba Mais:**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
