---
article_id: 360026158432
category: Materiais - Compras (SIGACOM)
content_hash: ace6de91086a4b462c0b6e498f875c874fad3b9cc35cf14e678e3afb47389bb0
fetched_at: '2026-06-28T22:41:07.641791+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gerar registro
  na tabela SRK a partir do Documento de Entrada com Autônomo - NFA ?
type: support-article
updated_at: '2022-05-16T22:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026158432-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-registro-na-tabela-SRK-a-partir-do-Documento-de-Entrada-com-Aut%C3%B4nomo-NFA
---

**Dúvida**Como gerar registro na tabela SRK a partir do Documento de Entrada com Autônomo - NFA ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**Cadastro do Fornecedor (MATA020): **A2\_NUMRA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625672/mceclip1.png)

Cadastro de Autônomo (GPEA265): **RA\_MAT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025641511/mceclip2.png)

Verba (GPEA040): 218

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625872/mceclip3.png)

Criar Documento de Entrada com o Fornecedor com vínculo do Autônomo, com TES que gera duplicata:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025641831/mceclip5.png)

Nesse processo deve gerar registro na tabela SRK:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025626272/mceclip6.png)
