---
article_id: 360018760811
category: Call Center - Televendas
content_hash: 2405032154eef2402d59ba005633637e5879ecf06e43a81df5388f4a87a8f62e
fetched_at: '2026-06-28T22:41:30.333135+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Mensagem REGBLOQ,
  ao selecionar um Produto, no atendimento Televendas
type: support-article
updated_at: '2022-06-22T19:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760811-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Mensagem-REGBLOQ-ao-selecionar-um-Produto-no-atendimento-Televendas
---

**Dúvida**

O que avaliar na mensagem REGBLOQ, ao selecionar um Produto, no atendimento Televendas?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - a partir da versão 11.  
  
  
**Solução**

Verifique o TES (Tipo de Entrada e Saída) informado no parâmetro MV\_TESSAI;

Além do parâmetro, verifique se este TES está bloqueado;

Verifique se o Produto está bloqueado;

Verifique se o TES, informado no produto, está bloqueado.

Obs: O Televendas possui um gatilho que dispara o TES ao informar o Produto.

Este TES é selecionado pelo parâmetro MV\_TESSAI ou pelo Produto, se estiver informado.
