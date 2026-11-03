---
article_id: 8029430206871
category: Call Center - Televendas
content_hash: de7940c18686c6346b5f49660d7a3a21bf5b1a0c9626131c1c7cf1fad58abe27
fetched_at: '2026-06-28T22:41:30.198097+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como imprimir
  um pedido gerado pelo Atendimento Televenda Call Center
type: support-article
updated_at: '2022-08-08T18:36:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8029430206871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-imprimir-um-pedido-gerado-pelo-Atendimento-Televenda-Call-Center
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como imprimir um pedido gerado pelo Atendimento Televenda Call Center?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**

O pedido vendas gerado pelo call center possui um relatório no momento de sua interação que é o tmkr03, conforme a documentação: **[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Alterações-na-Impressão-do-Atendimento-Televendas-TMKA271-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044381274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Altera%C3%A7%C3%B5es-na-Impress%C3%A3o-do-Atendimento-Televendas-TMKA271-)**

A partir da release 27, é necessário compilar o fonte em questão, para que ocorra a impressão.

Uma vez que não foi impresso neste momento, não há como imprimir o browser do atendimento e ter a visão do pedido em questão.

Fora esta opção, somente terá a consulta genérica da tabela SUA, onde constará o número do pedido no campo UA\_NUMSC5 -Número do pedido de venda gerado no Sigafat.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8029366465687/mceclip0.png)
