---
article_id: 360028300212
category: Materiais - Compras (SIGACOM)
content_hash: a1ae67dce8ef51d3efb3e969aaf19deb17d6068dafab86b7c301fe0d5edd15a9
fetched_at: '2026-06-28T22:41:12.835846+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus -  SIGACOM  -  Ocorrência do Erro
  ( DB error (Insert): -37 File: SCY010 ) ao tentar alterar Pedido de Compras'
type: support-article
updated_at: '2022-05-16T21:08:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028300212-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncia-do-Erro-DB-error-Insert-37-File-SCY010-ao-tentar-alterar-Pedido-de-Compras
---

**Ocorrência**Ocorrência do Erro ( ***DB error (Insert): -37 File: SCY010*** ) ao tentar alterar Pedido de Compras  
  
**Ambiente**Protheus - Compras – A partir da versão 11.80  
  
**Causa**

Ao alterar pedido de compra ele grava registro na tabela SCY, e ao tentar alterar novamente ocorre o erro.

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028867931/mceclip3.png)**

**Solução**Para manter o histórico dos dados originais do pedido, o Sistema utiliza a tabela **SCY** - (**Histórico dos Pedidos de Compras**, que sempre é atualizada quando ocorre alguma alteração no pedido).

A cada alteração no pedido de compras, será gerado um registro de histórico na tabela **SCY** (**Histórico dos pedidos de compras**), que armazena todos os dados anteriores do pedido de compra, gravando um número de identificação para cada versão no campo **Versão Manut**.

Quando o pedido de compras é alterado pela primeira vez, este campo é gravado com o conteúdo **0001**. Quando alterado pela segunda vez, será gravado com **0002** e, assim, sucessivamente.

Para que não ocorra a não conformidade é necessário que o modo de compartilhamento entre as tabelas SCY e SC7 sejam os mesmos. Caso estejam diferentes, poderá ser gerado o erro de violação de chave unica na tabela SCY 

***Saiba Mais:***

[PCOM04007 - Em qual tabela o pedido de compra grava o histórico das alterações?](http://tdn.totvs.com/pages/releaseview.action?pageId=233754761)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
