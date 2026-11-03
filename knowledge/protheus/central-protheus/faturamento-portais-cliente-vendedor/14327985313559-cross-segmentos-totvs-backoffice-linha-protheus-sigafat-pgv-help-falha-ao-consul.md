---
article_id: 14327985313559
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 569054ef3330b2493fca38988a63e04ec613a0222179e8eb48b2a8ee48f588bb
fetched_at: '2026-06-28T22:38:24.060904+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - PGV - HELP
  Falha ao Consultar Limite de Crédito
type: support-article
updated_at: '2023-05-03T13:32:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14327985313559-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-PGV-HELP-Falha-ao-Consultar-Limite-de-Cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**No **Portal Gestão de Vendas**, em "**Meus Clientes**" ao clicar em "**Visualizar Detalhes**" de um cliente é exibido o **help**:

Falha ao consultar Limite de Crédito, por favor atualize o servidor backend com último pacote de expedição contínua do Faturamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14327604805527)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Esta mensagem é apresentada quando a **API de Clientes** do Portal Gestão de Vendas **está desatualizada**, é necessário **atualizar** o servidor backend com o **último pacote** de expedição contínua do **Faturamento**.

**[Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)**

Caso a mensagem **persista** após a atualização, verifique se o ambiente **REST** é **separado** do ambiente de **produção**, nesse caso é necessário **atualizar o RPO** do ambiente **REST.**

**Saiba Mais**

**[Portal Gestão de Vendas: Guia de Referência](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=579468339)**

**[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/x/Ro2zJg)**
