---
article_id: 1500005524161
category: Faturamento - Integrações
content_hash: eb5964f33b09eae8f928a208385474a0a83c50607052a00efddc3e444b2d0769
fetched_at: '2026-06-28T22:38:26.476659+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como excluir/cancelar um
  Pedido de Venda que teve origem em uma integração EAI
type: support-article
updated_at: '2024-11-25T17:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005524161-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-excluir-cancelar-um-Pedido-de-Venda-que-teve-origem-em-uma-integra%C3%A7%C3%A3o-EAI
---

**Dúvida**

Como excluir ou cancelar um Pedido de Venda que teve origem a uma integração via EAI?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Os Pedidos de Venda que são incluídos por alguma integração EAI possuem o campo **"Origem do Pedido (C5\_ORIGEM)"** preenchido, se trata de um campo obrigatório, onde não pode haver nenhum tipo de alteração.

O sistema **não permitirá** a exclusão desse pedido via **"Outras Ações >  Excluir"**, visando manter a integridade da integração, desta forma se mantém o histórico de todos os pedidos gerados de uma integração entre outros sistemas.

Ao tentar realizar a exclusão será exibido o help abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28055049093143)

Caso haja a necessidade de exclusão do pedido, aconselhamos que esse pedido seja cancelado, selecione o pedido, clique em **"Outras Ações > Excluir > Resíduo"**.

Dessa forma o pedido continua na base de dados e o sistema grava o código de bloqueio **"****R****"** no campo **"****Status Blq (****C6\_BLQ)"** indicando que o item está bloqueado, ou seja, não será mais faturado devido à eliminação de resíduo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28055034862487)

**Saiba Mais:**

**[Eliminar Resíduo de Pedido de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=285655735)**
