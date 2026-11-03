---
article_id: 17213269376279
category: SIGAEST - INVENTÁRIO
content_hash: 668bc98d52a4a7971b4666c50db5dbf9ba28ab49352953885a6a61b5a0a6e8d1
fetched_at: '2026-06-28T22:38:50.333988+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 - B7_DTVALID
  - Como informar a Data de Validade  para um novo Lote na rotina?
type: support-article
updated_at: '2023-09-01T19:37:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17213269376279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-B7-DTVALID-Como-informar-a-Data-de-Validade-para-um-novo-Lote-na-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17213254177047) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

O campo ***Data de Validade (B7\_DTVALID)*** não permite digitar uma nova Data para um Lote ainda não existente no ambiente. Como informar a Data de Validade para um novo Lote na rotina?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17213675502743)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão para inclusão de novos Lotes, o sistema **considera a Data Base do ambiente**. Referente ao campo Data de Validade (B7\_DTVALID), no padrão vem configurado com a propriedade (X3\_VISUAL) igual a Visualizar, é possível alterar a **propriedade (X3\_VISUAL)** do campo para **Alterar**.

Salve as alterações e acesse a rotina novamente. Após esse processo o campo esta liberado para DIgitações.

Veja um passo a passo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17214117265943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17214213289495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17214392880535)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre INVENTÁRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)
