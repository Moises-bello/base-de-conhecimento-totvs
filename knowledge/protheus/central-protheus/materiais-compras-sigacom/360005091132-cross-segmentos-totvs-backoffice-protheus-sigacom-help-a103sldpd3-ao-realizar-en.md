---
article_id: 360005091132
category: Materiais - Compras (SIGACOM)
content_hash: a720fcaeb66a0b99bea1cc0ee6d04776285f2f76b03246c9b1984bc40cc22c73
fetched_at: '2026-06-28T22:41:08.914411+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103SLDPD3 ao
  realizar entrada de Devolução de Beneficiamento
type: support-article
updated_at: '2022-05-12T21:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005091132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A103SLDPD3-ao-realizar-entrada-de-Devolu%C3%A7%C3%A3o-de-Beneficiamento
---

**Dúvida**Como resolver o Help A103SLDPD3 ao realizar entrada de Devolução de Beneficiamento ?  
  
**Ambiente**Protheus  – Compras – A partir da versão 11.80  
  
**Solução**

O assistente é apresentado quando uma devolução de beneficiamento possui um saldo financeiro menor que a remessa.

Para desativar o assistente e liberar a inclusão do documento configure o parâmetro**“MV\_LIBESB6” com o valor “.T.”.**

Com essa configuração o valor informado no campo Quantidade (D1\_QUANT) irá zerar o saldo total em quantidade do controle de poder de terceiros, ou seja, a inclusão desse item encerra o controle de poder de terceiros e o valor informado no campo Vlr.Total (D1\_TOTAL) não irá zerar o saldo total em valor do controle de poder de terceiros.

procedimento:

***Obs. 1: Para utilizar essa funcionalidade, o parâmetro “MV\_BLOQSB6” deve esta desabilitado.***

***Obs. 2: Quando realizada a operação descrita acima os saldos em quantidade e valor da tabela de saldos de/em terceiros são encerrados com seus valores remanescentes.***

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
