---
article_id: 360022021952
category: SIGAEST - INVENTÁRIO
content_hash: 02f2383f3220bf48b485e06c2492dbc03de82d48714880fda8b1db1712b7ad55
fetched_at: '2026-06-28T22:38:50.293272+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 HELP: A270LOTERR
  na Digitação de Inventário'
type: support-article
updated_at: '2023-04-06T14:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022021952-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-HELP-A270LOTERR-na-Digita%C3%A7%C3%A3o-de-Invent%C3%A1rio
---

**Ocorrência**Ao realizar a Digitação do Inventário (MATA270) apresenta o HELP A270LOTERR. Como corrigir?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13659896743831)

**Ambiente**ross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**O HELP A270LOTERR é apresentado devido a inexistência do saldo no local (Armazém), Endereço e/ou Lote informados na digitação do inventário.

**Solução**

Esta validação possui relação com a pergunta ***"Valida Existência do Produto?"*** onde caso esteja igual a Sim, permite apenas a inclusão de Inventários para Produtos que possuam Saldo no Local, Lote e/ou Endereço digitados.

Para que seja possível, por exemplo, a realização de inventário de um produto cujo lote seja inexistente em determinado armazém é necessário com que a pergunta **"Valida Existência do Produto?" esteja com conteúdo "Não"**. Desta forma, será criado na respectiva tabela SB8 o saldo deste novo lote criado, bem como será gravado o lote digitado e processado (B8\_LOTECTL) e sua respectiva origem (B8\_DOC), além da atualização do saldo na tabela SB2.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13659998016791)

**Saiba mais:**

*[MP - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614)*

*[Clique aqui e veja mais artigos sobre Inventário no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033402-SIGAEST-INVENT%C3%81RIO)*
