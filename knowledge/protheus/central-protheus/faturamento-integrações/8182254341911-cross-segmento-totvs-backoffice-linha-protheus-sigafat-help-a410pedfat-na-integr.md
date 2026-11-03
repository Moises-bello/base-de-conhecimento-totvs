---
article_id: 8182254341911
category: Faturamento - Integrações
content_hash: 9589c1b8ce768992b06d419342f9c00076c5ed529cd3292f1bd25bf09463db10
fetched_at: '2026-06-28T22:38:26.614456+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - HELP A410PEDFAT
  NA INTEGRAÇÃO EAI VIA XML
type: support-article
updated_at: '2022-08-15T14:23:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8182254341911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-HELP-A410PEDFAT-NA-INTEGRA%C3%87%C3%83O-EAI-VIA-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03:00:00 min****Dúvida**Como solucionar o **Help A410PEDFAT** ao tentar incluir o pedido de venda via **Integração EAI (XML)**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Sistema está informando que **já existe** um **pedido de venda faturado** com a mesma numeração que está tentando incluir.  
  
Para **permitir alterar** um pedido de venda que já está faturado altere o parâmetro (**MV\_ALTPED = S**).  
  
Para verificar a qual pedido no Protheus o help se refere, verifique no **XML** de envio a **TAG <InternalId>** e na tabela "**XXF**" no Protheus os campos "**XXF\_EXTVAL**" e "**XXF\_INTVAL**".  
  
**- XXF\_EXTVAL:** Código do pedido na Aplicação de Origem, TAG <InternalId>

**- XXF\_INTVAL:** Número do pedido no Protheus (C5\_NUM)  
  
**Saiba Mais: [MP-FAT-MV\_ALTPED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025018113-MP-FAT-MV-ALTPED)**
