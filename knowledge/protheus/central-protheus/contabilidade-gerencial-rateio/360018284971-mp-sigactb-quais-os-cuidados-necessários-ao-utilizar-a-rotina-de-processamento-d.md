---
article_id: 360018284971
category: Contabilidade Gerencial - Rateio
content_hash: ac163f21f207242be6fbf4c143c1b773675ce8a331f233b461df6baeafee4437
fetched_at: '2026-06-28T22:40:35.586640+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: 'MP - SIGACTB: Quais os cuidados necessários ao utilizar a rotina de processamento
  do Rateio Offline'
type: support-article
updated_at: '2021-04-28T15:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018284971-MP-SIGACTB-Quais-os-cuidados-necess%C3%A1rios-ao-utilizar-a-rotina-de-processamento-do-Rateio-Offline
---

**Dúvida**Quais os cuidados necessários ao utilizar a rotina de processamento do Rateio Offline

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

Ao processar rateio offline com entidade, e a conta contábil na grid **Origem** estiver em branco é utilizado para composição do saldo, as tabelas de saldos compostos,  conforme tópico do help online [Parâmetros de saldo](https://www.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/ctba130_parametros_de_saldo.htm), em que o saldo composto **NUNCA** é atualizado online, portanto ao utilizar rotina de rateio offline é necessário previamente reprocessar os saldos.

A rotina para reprocessamento está localizada em **Miscelânea/ Refaz Saldo / Reprocessamento**, que atualizam tanto [saldos básicos como saldos compostos](https://www.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/ctba130_detalhamento_tecnico.htm).

**Importante:**

Caso o parâmetro **MV\_ATUSAL** esteja com o conteúdo **N**, é necessário utilizar a rotina de reprocessamento de saldos antes da execução do processamento do rateio off-line
