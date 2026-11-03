---
article_id: 360019177532
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: a04100d31a73dd156de91fc146324db3e46d0fd0b81f965024306441d4d3e932
fetched_at: '2026-06-28T22:40:38.912334+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: MP - SIGACTB - CTBA350 - Relatório para identificar diferenças tipo de saldo
  9
type: support-article
updated_at: '2021-04-28T15:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019177532-MP-SIGACTB-CTBA350-Relat%C3%B3rio-para-identificar-diferen%C3%A7as-tipo-de-saldo-9
---

**Dúvida**Qual relatório apresenta identificação de diferenças do tipo de saldo 9?

**Ambiente**Protheus– Contabilidade Gerencial – A partir da versão 12.1.17

**Solução**

Não é possível reprocessar o tipo de saldo 9 porque conceitualmente não deve atualizar as tabelas CQ's.

Com isso para conferir as diferenças em um lote que foi gravado com o tipo de saldo 9, deve utilizar o relatório gerado pela própria rotina de efetivação(CTBA350), executando como simulação.

Na rotina de efetivação, selecione a opção de 'simulação e geração de relatório', assim será impresso um relatório com as diferenças ao final (sem efetivar de fato), apresentando a mensagem por exemplo "Débito e Crédito do lote não estão batendo"
