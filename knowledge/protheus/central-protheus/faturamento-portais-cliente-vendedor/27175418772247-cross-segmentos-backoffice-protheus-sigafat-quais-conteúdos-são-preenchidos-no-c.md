---
article_id: 27175418772247
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 2871aee277d7e308375278615ba25c94a50c91f2f3080617f48cadc5c00ce14e
fetched_at: '2026-06-28T22:38:23.951530+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Quais conteúdos são preenchidos
  no campo A1S_MOV?
type: support-article
updated_at: '2024-10-18T21:04:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27175418772247-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Quais-conte%C3%BAdos-s%C3%A3o-preenchidos-no-campo-A1S-MOV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27175405729047) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais opções são preenchidos no campo A1S\_MOV?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Quando ocorrer um erro no registro, o sistema vai gravar o campo **A1S\_MOV** de acordo com a seguinte regra:

* Se for um pedido de venda (MATA410), grava o conteúdo = 10
* Se for um orçamento (MATA415), grava o conteúdo = 14
* Se for cadastro de cliente (MATA030), grava o conteúdo = 18
* Se for cadastro de prospect (TMKA260), grava o conteúdo = 22
* Se for cadastro de contato (TMKA070), grava o conteúdo = 26

Quando não ocorrer erro, o sistema vai gravar o registro no campo **A1S\_MOV** da seguinte forma:

**Se for um pedido de venda (MATA410):**

* Se for uma inclusão, grava o conteúdo = 7
* Se for uma alteração, grava o conteúdo = 8
* Se for uma exclusão, grava o conteúdo = 9

**Se for um orçamento (MATA415):**

* Se for uma inclusão, grava o conteúdo = 11
* Se for uma alteração, grava o conteúdo = 12
* Se for uma exclusão, grava o conteúdo = 13

**Se for um cadastro de cliente (MATA030):**

* Se for uma inclusão, grava o conteúdo = 15
* Se for uma alteração, grava o conteúdo = 16
* Se for uma exclusão, grava o conteúdo = 17

**Se for um cadastro de prospect (TMKA260):**

* Se for uma inclusão, grava o conteúdo = 19
* Se for uma alteração, grava o conteúdo = 20
* Se for uma exclusão, grava o conteúdo = 21

**Se for um cadastro de contato (TMKA070):**

* Se for uma inclusão, grava o conteúdo = 23
* Se for uma alteração, grava o conteúdo= 24
* Se for uma exclusão, grava o conteúdo = 25

**Para saber mais consulte:  
[Tabela de Notificações do Vendedor](https://tdn.totvs.com/pages/releaseview.action?pageId=579771104)**
