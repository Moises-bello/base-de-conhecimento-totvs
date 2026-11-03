---
article_id: 34973653322903
category: Financeiro - Configurador de Tributos
content_hash: 4d5c2f7ba26f7bb95d19d88267c15102bb877a2d1ae0a9483a9d0b762492f303
fetched_at: '2026-06-28T22:37:45.822369+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Aplicação
  de retenção em título de adiantamento
type: support-article
updated_at: '2025-11-05T17:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34973653322903-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Aplica%C3%A7%C3%A3o-de-reten%C3%A7%C3%A3o-em-t%C3%ADtulo-de-adiantamento
---

**Dúvida:**  
Como vincular a regra financeira em um título de adiantamento?  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução:**

No **cadastro de regras financeiras** no **Configurador de Tributos (FISA170)**, o campo **“Antecipações”** deve estar configurado como **“Retém”**.

Dessa forma, ao realizar a amarração entre o fornecedor e a regra financeira configurada, o sistema aplicará automaticamente a retenção nos títulos de adiantamento (**PA** e **RA)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34973653303831)

Para que o tipo seja exibido como **TXA** no financeiro, é preciso ajustar o campo **“Tipo Título”** para **TXA** na regra de título, conforme ilustrado no exemplo anexo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36128336183063)

Acesse o **HOW TO - Aplicação de retenção em título de adiantamento:**

**Saiba Mais**

[SIGAFIN - Configurador de Tributos - How to](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configurador-de-Tributos-How-to)

[SIGAFIN - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
