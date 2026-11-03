---
article_id: 360019974472
category: Call Center - Telecobrança
content_hash: b30d7306290f9ad30db19450a80edf540228686a92b0f4a5a632e33a6c51a9c0
fetched_at: '2026-06-28T22:41:28.625344+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Mensagem telelecobrança
  SetOrder - Index not found. on TK274CLIENT.
type: support-article
updated_at: '2021-11-18T14:26:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019974472-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Mensagem-telelecobran%C3%A7a-SetOrder-Index-not-found-on-TK274CLIENT
---

**Dúvida**

Na rotina de Telelecobrança é apresentada a mensagem: SetOrder - Index not found. on TK274CLIENT.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as Versões

**Causa**

A mensagem é apresentada caso não exista na tabela de índices (SIX) o índice 3 da tabela ACF.

**Solução**

Valide via configurador a existência do índice 3 na tabela ACF.

ACF\_CLIENT+ACF+LOJA+STR(ACF\_DIASDA,8,0)+STR(ACF\_HORADA,8,0)

Caso o mesmo não exista, realize a atualização do Dicionário de Dados e execute o UPDDISTR: [**Atualizador de dicionário e base de dados - UPDDISTR**](https://tdn.totvs.com/x/nJLYCg)
