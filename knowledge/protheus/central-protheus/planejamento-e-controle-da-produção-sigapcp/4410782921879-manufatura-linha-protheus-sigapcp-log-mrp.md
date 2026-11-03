---
article_id: 4410782921879
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5682e2d31ddf7c7625c301151413803a68555106e2c822e56f663c10351f1e5c
fetched_at: '2026-06-28T22:42:43.536494+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Log MRP
type: support-article
updated_at: '2025-10-08T17:31:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410782921879-Manufatura-Linha-Protheus-SIGAPCP-Log-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como gerar e quais os *logs* gerados pelo **MRP - Material Requiriment Planning**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para determinar se deve os *logs* do planejamento do **MRP** é necessário marcar a opção **Log de eventos no MRP**. O Sistema exibe uma lista com os produtos e os eventos a eles relacionados.  
  
Os *logs* de evento do **MRP** podem ser:

|  |  |  |
| --- | --- | --- |
| **Código** | **Evento** | **Descrição** |
| 001 | Saldo em estoque inicial menor que zero | Indica produtos que estão com saldo em estoque negativo no início do período de cálculo do **MRP**. A composição deste saldo em estoque varia de acordo com a parametrização inicial do **MRP**, podendo considerar saldo de/em terceiros, estoque de segurança etc. |
| 002 | Atrasar o documento | Indica documentos que podem ter a data ajustada para atender a uma necessidade em período anterior à data atual do documento, sem causar impactos no planejamento. Este recurso é útil, pois reduz a quantidade de documentos gerados pelo **MRP** e, conseqüentemente, os saldos em estoque e custos. |
| 003 | Adiantar o documento | Indica documentos que podem ter a data ajustada para atender a uma necessidade em período posterior à data atual do documento, sem causar impactos no planejamento. Este recurso é útil, pois reduz a quantidade de documentos gerados pelo **MRP** e, conseqüentemente, os saldos em estoque e custos |
| 004 | Data de necessidade inválida - Data anterior à *database* do cálculo | Indica necessidades que se encontram em períodos anteriores ao primeiro período calculado pelo **MRP**. Para efeito de cálculo, estas necessidades são consideradas no primeiro período do **MRP**. |
| 005 | Data de necessidade inválida - Data posterior à data limite do cálculo | Indica necessidades que se encontram em períodos posteriores ao último período calculado pelo **MRP**. Para efeito de cálculo, estas necessidades são consideradas no último período do **MRP**. |
| 006 | Documento planejado em atraso | Indica documentos já lançados na base de dados, em que a data de entrega é anterior à *database* de cálculo do **MRP**, ou seja, são documentos que estão atrasados, de acordo com a data de entrega informada nestes documentos. |
| 007 | Cancelar o documento | Indica documentos lançados na base de dados que não atendem a nenhuma necessidade, dentro do período calculado, e podem ser cancelados para não acumularem estoque. |
