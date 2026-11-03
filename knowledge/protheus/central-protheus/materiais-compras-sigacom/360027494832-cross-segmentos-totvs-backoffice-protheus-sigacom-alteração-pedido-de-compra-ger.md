---
article_id: 360027494832
category: Materiais - Compras (SIGACOM)
content_hash: 8053b7e0e67f9eed23225c726094e56d1d5965c5905dfd3e8c347acc0dd6a088
fetched_at: '2026-06-28T22:41:07.413999+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alteração Pedido de
  Compra gera inconsistência na tabela SCY
type: support-article
updated_at: '2024-12-02T13:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027494832-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Altera%C3%A7%C3%A3o-Pedido-de-Compra-gera-inconsist%C3%AAncia-na-tabela-SCY
---

**Ocorrência:**

Ao alterar pedido de compra ele grava registro na tabela SCY, e ocorre erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027426831)  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Causa**

Para manter o histórico dos dados originais do pedido, o Sistema utiliza a tabela **SCY** - (**Histórico dos Pedidos de Compras**, que sempre é atualizada quando ocorre alguma alteração no pedido).

A cada alteração no pedido de compras, será gerado um registro de histórico na tabela **SCY** (**Histórico dos pedidos de compras**), que armazena todos os dados anteriores do pedido de compra, gravando um número de identificação para cada versão no campo **Versão Manut**.

Quando o pedido de compras é alterado pela primeira vez, este campo é gravado com o conteúdo **0001**. Quando alterado pela segunda vez, será gravado com **0002** e, assim, sucessivamente.

A versão atual do pedido sempre será armazenada na tabela **SC7** (**Pedido de Compra**); se não existirem alterações no pedido de compra, não haverá registro do pedido na tabela de histórico.

Em outras palavras, a tabela SCY, pode ser uma tabela de historico, que sempre guardará a versão anterior da atualização, e a tabela SC7, a versão atual. Ou seja, a versão com a alteração mais recente.

Caso a tabela SCY guardasse o pedido atual (com as últimas alterações feitas), a tabelas SC7 perderia sua funcionalidade. Uma vez que ela é responsável por armazenar a versão mais recente e atual do pedido de compras.  
   
Para mapear qual foi a última alteração feita no pedido, basta comparar a última versão do pedido na tabela SCY, com a versão atual do pedido na tabela SC7.

É possível realizar a consulta da tabela **SCY** (**Histórico dos pedidos de compras**), por meio da rotina **Consulta Genérica**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101718893)

**Solução**

Para que não ocorra o erro, o modo de compartilhamento entre as tabelas SCY e SC7 devem ser os mesmos. Caso estejam diferentes, pode ser gerado erro de violação de chave única na tabela SCY ao tentar alterar um Pedido de Compras.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
