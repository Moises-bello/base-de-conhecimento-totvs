---
article_id: 1500005380281
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 20182d27c451970fe756a876026e2530561a4370757e32c2854951d9bee13ce4
fetched_at: '2026-06-28T22:38:41.254119+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Schedule na análise de crédito do pedido de vendas
type: support-article
updated_at: '2021-04-28T15:49:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005380281-MP-FAT-Schedule-na-an%C3%A1lise-de-cr%C3%A9dito-do-pedido-de-vendas
---

**Dúvida**

Qual a configuração para poder efetuar a análise de crédito via schedule, onde obedeça aos critérios :

01 - Liberando Pedido novos dentro do padrão configurado A1\_NIVEL Boletos em dia etc.  
02 - Bloqueando pedidos que em outro momento foi liberado por estar em dia e agora estão com algum atraso.  
  
**Ambiente**

Microsiga Protheus - todas as versões  
  
**Solução**

Primeiramente, não há como schedular a rotina de análise de crédito , nem mesmo da forma desejada com base em critérios, a rotina não está preparada para tratamento em schedule.  
  
Dentro dos critérios estabelecidos, o que poderia ser feito de forma paliativa e dentro ERP sem uso de schedule, seria mudar a forma de avaliação de crédito via ponto de entrada, podendo utilizar:

* **MAAVCRED: Ponto de entrada substitui a avaliação de credito padrão do sistema: <https://tdn.totvs.com/x/LIVn>;**
* **MAAVCRPR: Ponto de entrada pertence à rotina de avaliação de crédito de clientes (função: MaAvalCred): <https://tdn.totvs.com/x/LYVn>.**
* **MTValAvC - <https://tdn.totvs.com/pages/viewpage.action?pageId=6784433>**

A rotina de análise de crédito **(mata450/mata450a)** não possui execauto para que possa efetuá-la de forma automática.

**Saiba mais sobre análise de crédito:**

**[MP-FAT- Comportamento do parâmetro MV\_AVALCRD no Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176611-MP-FAT-Comportamento-do-par%C3%A2metro-MV-AVALCRD-no-Pedido-de-Vendas)**

**[MP - FAT -Como identificar a causa de o Pedido de Venda ter sido liberado/bloqueado por Crédito "indevidamente"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001428228-MP-FAT-Como-identificar-a-causa-de-o-Pedido-de-Venda-ter-sido-liberado-bloqueado-por-Cr%C3%A9dito-indevidamente-)**

**[MP - FAT - Pedido de Vendas está com Bloqueio de Crédito ou de Estoque, porém, na rotina de Pedido de Vendas demonstra Status Liberado (legenda verde)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019749211-MP-FAT-Pedido-de-Vendas-est%C3%A1-com-Bloqueio-de-Cr%C3%A9dito-ou-de-Estoque-por%C3%A9m-na-rotina-de-Pedido-de-Vendas-demonstra-Status-Liberado-legenda-verde-)**
