---
article_id: 360055657013
category: RH - Rescisão
content_hash: 6ad746563fd1b80be97c6421524099034b2d805fff2b674d5442dd14b6098556
fetched_at: '2026-06-28T22:43:51.939424+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de rescisão por pedido de demissão não
  apresenta saldo FGTS ID 0118, mesmo quando há histórico de valores na rotina manutenção
  saldos
type: support-article
updated_at: '2022-08-25T13:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055657013-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-por-pedido-de-demiss%C3%A3o-n%C3%A3o-apresenta-saldo-FGTS-ID-0118-mesmo-quando-h%C3%A1-hist%C3%B3rico-de-valores-na-rotina-manuten%C3%A7%C3%A3o-saldos
---

**Ocorrência**Cálculo de rescisão por pedido de demissão não apresenta saldo FGTS ID 0118, mesmo quando há histórico de valores na rotina manutenção saldos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Causa**  
Pedido de demissão não gera multa de FGTS.  
  
**Solução**O cálculo de rescisão por pedido de demissão não apresenta o saldo de FGTS no id 0118 mesmo quando há histórico de valores na rotina de manutenção saldo, pois para esse tipo de rescisão não há recolhimento de multa FGTS, assim o cálculo de rescisão não apresenta o saldo FGTS.

Para pedido de demissão, o FGTS 8% referentes ao saldo de salário e 13º salário são recolhidos em Sefip. Em rescisão sem justa causa pelo empregador, os valores de FGTS são recolhidos em GRRF e assim o saldo de FGTS é demonstrado em rescisão pelo id 0118 e lançado em GRRF.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[MP - GPE - Como realizar a manutenção de saldo FGTS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052553034-MP-GPE-Como-realizar-a-manuten%C3%A7%C3%A3o-de-saldo-FGTS-?source=search)
