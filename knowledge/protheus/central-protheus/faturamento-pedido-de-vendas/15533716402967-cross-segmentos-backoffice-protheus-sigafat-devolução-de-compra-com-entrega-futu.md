---
article_id: 15533716402967
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: cbfb32d8fb751b77e3d0e0ff71d7fabd1be91b3b734916a9d84d7372ec64a4b0
fetched_at: '2026-06-28T22:38:39.771114+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Devolução de Compra com Entrega
  Futura (tabela DHQ)
type: support-article
updated_at: '2026-03-12T18:51:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15533716402967-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Devolu%C3%A7%C3%A3o-de-Compra-com-Entrega-Futura-tabela-DHQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15533730502679) Tempo aproximado para leitura: **2:00 min**  
  
**Dúvida**  
Qual o tratamento da devolução de NF gerada pela Compra com Entrega Futura (tabela DHQ)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
  
Existe no módulo Compras o processo de Compra com Entrega Futura:  
  
[**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada - Processo de Compra com Entrega Futura (tabela DHQ)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021818751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Processo-de-Compra-com-Entrega-Futura-tabela-DHQ?source=search)  
  
A movimentação da tabela DHQ é somente no módulo Compras (entrada).  A rotina que grava a tabela DHQ na entrada é o "Documento de Entrada (MATA103)" e o relatório "Relatório de controle de compras com entrega futura (COMR103)". O relatório informado não possui dados de nota de devolução (SD2).  
  
A devolução de uma NF que gerou movimentação da tabela DHQ é feita da mesma forma que uma devolução normal de compras e não há qualquer alteração na tabela DHQ e na NF de Origem (entrada):  
  
[**Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer uma devolução de compras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022341592-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uma-devolu%C3%A7%C3%A3o-de-compras)
