---
article_id: 4420207290647
category: Materiais - Compras (SIGACOM)
content_hash: 88bb170794a7186e4a2f21adcdb70b6a6118c17c4347051abce89ad912821b15
fetched_at: '2026-06-28T22:41:13.003741+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  HELP A120IERSC ao
  excluir um Pedido de Compras
type: support-article
updated_at: '2022-01-25T17:55:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420207290647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A120IERSC-ao-excluir-um-Pedido-de-Compras
---

**Ocorrência**Ao tentar excluir um pedido de compras ou deletar um item do Pedido apresenta a mensagem com o HELP A120IERSC, como corrigir?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420222371863/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Causa**O sistema exibe esse help A120IERSC, quando o Pedido de Compras estiver vinculado a uma SC na qual tenha sido executada a rotina de eliminação de resíduo, ou seja, quando o campo SC1->C1\_RESIDUO estiver diferente de vazio o help será apresentado. Nesse caso o PC não poderá ser excluído ou alterado, mas sim eliminado o resíduo.  
  
**Solução**Nesse caso o PC não poderá ser excluído ou alterado, mas sim eliminado o resíduo apenas.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
