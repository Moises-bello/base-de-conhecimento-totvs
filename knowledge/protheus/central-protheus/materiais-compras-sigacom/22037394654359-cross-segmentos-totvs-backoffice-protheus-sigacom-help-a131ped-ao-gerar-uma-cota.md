---
article_id: 22037394654359
category: Materiais - Compras (SIGACOM)
content_hash: 6413ec9283b3505120b1113ea1fba2bd2757d74b80e4171c12f60848e426bcbe
fetched_at: '2026-06-28T22:41:18.877625+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A131PED ao Gerar
  uma Cotação.
type: support-article
updated_at: '2024-03-13T14:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22037394654359-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A131PED-ao-Gerar-uma-Cota%C3%A7%C3%A3o
---

**Dúvida**

Ocorre o HELP A131PED ao Gerar uma Cotação.   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM -  Todas as Versões

**Solução**

O HELP ocorre quando a Solicitação de Compra para qual está tentando gerar a cotação já possui um Pedido de Compras vinculado a mesma. Ou seja, quando o campo C1\_PEDIDO já encontra-se preenchido com o número do Pedido de Compras que foi criado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22037394615703)

Para que esse HELP não ocorra, o Pedido de Compra vinculado a Solicitação de Compra deve ser excluído na rotina MATA121.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
