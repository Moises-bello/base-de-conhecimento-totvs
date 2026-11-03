---
article_id: 360028965051
category: Materiais - Compras (SIGACOM)
content_hash: 31bd6b42823ae5aadcb281c2664c4518116e9e9d70662bff0c2818c0a7ff6349
fetched_at: '2026-06-28T22:41:22.048933+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetro MV_RESTSCC
  - Por que ocorre o Help SOLEC na inclusão da Solicitação de Compras ?
type: support-article
updated_at: '2025-09-24T20:40:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028965051-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-MV-RESTSCC-Por-que-ocorre-o-Help-SOLEC-na-inclus%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**Parâmetro MV\_RESTSCC - Por que ocorre o Help SOLEC na inclusão da Solicitação de Compras ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
**Solução**O Help Solec ocorre devido o sistema estar validando o cadastro de solicitante, produto e centro de custo, ou seja, quando a empresa possui uma regra de negócio onde possui um solicitante que poderá incluir as solicitações para este determinado centro de custo.

Caso outro solicitante inclua as solicitações para este centro de custo o sistema emite o ***Help SOLEC***

No cadastro de solicitantes informe no campo ***AI\_PRODUTO*** algum produto especifico juntamente com o campo ***DBK\_CC*** com o centro de custo, pois com ambos preenchidos na inclusão da solicitação de compras deverá também ser informado o que está no cadastro do solicitante.

![tela_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029910232/tela_2.PNG)

Caso na inclusão informar um centro de custo diferente ou produto diferente o sistema emite a mensagem de Help: Solec - *Es**ta Entidade Contábil não pode ser informada para este Produto x Solicitantes”*. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030705932/mceclip0.png)

**Parâmetros Envolvidos:**

* MV\_RESTSCC
* MV\_APRSCEC

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
