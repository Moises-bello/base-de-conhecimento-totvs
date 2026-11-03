---
article_id: 4421082604951
category: Gestão de Distribuição (SIGAOMS)
content_hash: 9d30360e8b40afd89d45e4f32ca39c50d0cbd11ae777b017a54d9620379dbe29
fetched_at: '2026-06-28T22:45:50.092561+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Quais opções para Aglutinar pedidos na rotina
  de Montagem de Carga
type: support-article
updated_at: '2022-12-01T11:15:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421082604951-Log%C3%ADstica-Linha-Protheus-OMS-Quais-op%C3%A7%C3%B5es-para-Aglutinar-pedidos-na-rotina-de-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:06 min** **Dúvida**Quais opções para **Aglutinar** pedidos na rotina de **OMSA200 - Montagem de Carga**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.1.25  
  
**Solução**Na rotina **OMSA200-Montagem de Carga** temos o **pergunte OMS200 - MV\_PAR06, com as opções abaixo:**

* **MV\_PAR06 == 1,** quando configurado por **Pedido** , irá considerar a data informada no campo **Dt. Entrega - C5\_FECENT**
* **MV\_PAR06 == 2,** quando configurado por **Itens**, irá considerar a data informada no campo **Entrega - C6\_ENTREG**
* **MV\_PAR06 == 3,** quando configurado por **Prog. Entrega**, **não considera as data de entrega acima, irá validar se o pedido está liberado na SC9 - Pedidos Liberados.**

Essa opção foi desenvolvida para atender os clientes que utilizam integração com o **Módulo Agro** em conjunto com coma rotina **OMSA200-Montagem de Carga**.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link's*:[Implementação da opção Aglutinar por? no pergunte da rotina de montagem de carga](https://tdn.totvs.com/pages/releaseview.action?pageId=522009476)  
[Montagem de Carga - OMSA200 - SIGAOMS](https://tdn.totvs.com/pages/releaseview.action?pageId=551446517)
