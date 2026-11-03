---
article_id: 360055525634
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f0fb1062f5ea0f864eb163332859abacfb1b674a6a6ed46d08581d0a7e694a8f
fetched_at: '2026-06-28T22:42:40.990508+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo C2_DESTINA
type: support-article
updated_at: '2021-08-13T12:29:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055525634-Manufatura-Linha-Protheus-SIGAPCP-Campo-C2-DESTINA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Quais as opções que o campo **C2\_DESTINA - Destinação** pode assumir e quando que assume cada uma delas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo **C2\_DESTINA** pode ter os valores: **em branco**, **P - Pedido** e **E - Estoque**.

* **Em branco**: Quando a **OP - Ordem de Produção** é aberta através do **MATA650 - Ordens de Produção** manualmente, **MATA712 - MRP**;
* **P** - Quando a **OP** aberta via a opção **Vendas** através do **MATA650**;
* **E** - Quando é uma **OP intermediária**, ou que foi **aglutinada**pelo **MATA720 - Aglutinação de OPs** ou ainda foi gerada pelo **MATA760 - Ops por Ponto de Pedido**
