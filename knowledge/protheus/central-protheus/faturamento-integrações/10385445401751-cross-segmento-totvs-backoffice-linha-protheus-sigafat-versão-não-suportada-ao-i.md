---
article_id: 10385445401751
category: Faturamento - Integrações
content_hash: f9fe3b8ae99629de95ad41a24638eaaba1eda5d722a564db4035bc80a223085a
fetched_at: '2026-06-28T22:38:26.628863+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Versão não suportada
  ao integrar Pedido de Vendas entre TOTVS Gestão Hospitalar x Back Office Protheus
  via XML
type: support-article
updated_at: '2022-11-21T19:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10385445401751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Vers%C3%A3o-n%C3%A3o-suportada-ao-integrar-Pedido-de-Vendas-entre-TOTVS-Gest%C3%A3o-Hospitalar-x-Back-Office-Protheus-via-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao integrar Pedido de Vendas entre TOTVS Gestão Hospitalar x Back Office Protheus via XML é apresentada a mensagem de versão não suportada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**O erro ocorre quando o sistema não encontra o cliente do pedido no Protheus e ao tentar incluir o cliente não localiza o adapter correspondente, no Configurador será necessário a inclusão do adapter CRMA980 (CUSTOMERVENDOR) para que a mensagem deixe de ocorrer no momento de integrar.
