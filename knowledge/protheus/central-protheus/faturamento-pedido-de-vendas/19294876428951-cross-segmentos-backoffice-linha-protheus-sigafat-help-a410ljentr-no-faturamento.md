---
article_id: 19294876428951
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1a2f73e8473d6b7e62d21f7978a8ef43e30f866350bc8341c4fd5835ca059379
fetched_at: '2026-06-28T22:38:42.507162+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help: A410LJENTR
  no Faturamento'
type: support-article
updated_at: '2023-11-24T12:04:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19294876428951-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-A410LJENTR-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19294891688599) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como solucionar o Help A410LJENTR no Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**O erro o só ocorre quando o valor dos campos estão em memória:

* O campo C5\_CLIENT está vazio e o C5\_LOJAENT preenchido
* O campo C5\_CLIENT está preenchido e o C5\_LOJAENT vazio

**OBS:** Cheque se não há gatilhos personalizados invertendo os pares corretos de código e loja de faturamento e entrega.

Exemplo correto de par:

> Par 1: C5\_CLIENTE + C5\_LOJACLI
>
> Par 2: C5\_CLIENT + C5\_LOJAENT

Exemplo incorreto de par:

> Par 1: C5\_CLIENTE + C5\_LOJAENT
>
> Par 2: C5\_CLIENT + C5\_LOJACLI
