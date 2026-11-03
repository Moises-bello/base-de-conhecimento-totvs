---
article_id: 360020061332
category: ADVPL - Rotina Automática
content_hash: d09322dbb48a6abcd39dabd908d18be854ea08da70ff6a53820e70e0e33c1e74
fetched_at: '2026-06-28T22:40:25.032646+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  MATA310
type: support-article
updated_at: '2021-08-26T17:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020061332-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-MATA310
---

**Dúvida**Gostaria de um exemplo da função MsExecAuto para a MATA310 - Transferência entre Filiais  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

A rotina Mata310 não está preparada para ExecAuto, pois a MATA310 já é um agrupador de diversas rotinas automáticas que centraliza todos os eventos sistêmicos necessários para realização da transferência entre filiais. Desta forma, realizar rotina automática deste processo é o mesmo que realizar rotina automática das rotinas que este processo utiliza.

Assim, para realizar uma rotina automática de transferência, deve-se utilizar os seguintes processos:

1) Geração do pedido de venda na filial de origem para transferência à filial destino.  
2) Geração de nota fiscal de saída com base no pedido de venda gerado anteriormente na filial de origem para transferência à filial destino.  
3) Geração de pré-nota ou nota fiscal de entrada na filial destino com base nos dados gerados na filial de origem.
