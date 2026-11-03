---
article_id: 23234158462615
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93428eaadd9ef4e92185b0a762e2f32c8334938c7ebabd68888e3e96a310054c
fetched_at: '2026-06-28T22:42:45.555487+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Pedido de venda não liberado por crédito
  na importação da demanda
type: support-article
updated_at: '2024-05-06T14:13:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234158462615-Manufatura-Linha-Protheus-SIGAPCP-Pedido-de-venda-n%C3%A3o-liberado-por-cr%C3%A9dito-na-importa%C3%A7%C3%A3o-da-demanda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23234150927511)***Tempo aproximado para leitura: **00:00:53 min  
  
Dúvida**Na rotina **PCPA136 - Demandas do MRP**, ao importar demandas serão importados os **pedidos de venda** que ainda não foram submetidos à avaliação de crédito?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12

**Solução**  
Sim os **pedidos de venda** que ainda não foram liberados por crédito serão importados na demanda. Serão importados todos os **pedidos de venda** que atendam as seguintes regras:

* Possuir saldo, independente do status
* Não estar Bloqueado para tratar resíduos
* Possuir TES que controle estoque
* Não ter bloqueios de créditos

**Saiba mais**  
Para mais informações sobre a rotina de demandas, acesse: [Demandas do MRP - PCPA136](https://tdn.totvs.com/display/public/PROT/Demandas+do+MRP+-+PCPA136)
