---
article_id: 7466854518039
category: SIGAEST - INVENTÁRIO
content_hash: fdec4b53de559d1403e7847cd91b8b70bdbca08b1749df5fda3e3c4e505f9bc9
fetched_at: '2026-06-28T22:38:50.327076+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como saber qual usuário
  fez o Inventário ?
type: support-article
updated_at: '2022-07-14T16:52:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7466854518039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-saber-qual-usu%C3%A1rio-fez-o-Invent%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:53 min****Dúvida**Existe a possibilidade de saber qual usuário iniciou o inventário ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Como sabemos o inventário no Protheus basicamente é feito em duas etapas:

**1°** **-** Primeiro é realizado a Digitação do Inventário (MATA270);

A Digitação do Inventário (MATA270) gera informação na tabela SB7, e essa tabela não tem campo de gravação de usuário.

**2° -** Depois é realizado o Acerto de Inventário (MATA340).

Quando é realizado o Acerto do Inventário (MATA340) as quantidades são atualizadas na tabela SD3, essa tabela tem informação de usuário:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7472107641623/mceclip2.png)

Desta maneira se o acerto do inventário gerar movimentação na tabela SD3, existe a possibilidade de identificar qual usuário fez o processo de acerto do inventário.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Inventário de Estoques](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)*
