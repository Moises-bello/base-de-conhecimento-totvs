---
article_id: 360048485414
category: Call Center - Televendas
content_hash: 5262e81d0ada8ed0745e15c519744512b9f9dfafd5d6f16a375e052aeb2bcba6
fetched_at: '2026-06-28T22:41:30.237021+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Como é aplicado o desconto
  no Televendas
type: support-article
updated_at: '2024-04-25T13:09:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048485414-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Como-%C3%A9-aplicado-o-desconto-no-Televendas
---

**Dúvida**Como é aplicado o desconto no Televendas?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

O desconto é aplicado da seguinte maneira:

O valor calculado está relacionado ao desconto proporcional por quantidade  ou seja , o valor do desconto é dividido pela quantidade do produto conforme abaixo:

Valor total : R$ 464,00 (UB\_VLRITEM)

Desconto : R$ 23,20 (UB\_VALDESC)  
  
Preço Bruto : 23,20 (UB\_PRCTAB)

Quantidade : 20 (UB\_QUANT)

R$ 23,20 / 20 = R$ 1,16 (Valor do Desconto)

**Recalculo efetuado**

Valor original do produto : 23,20 (UB\_PRCTAB)

Desconto: R$ 1,16

R$ 23,20- R$ 1,16 = R$ 14,15 (UB\_VRUNIT)

Valor do produto já calculado com o desconto por item  =  R$ 22,04

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071807034)  
  
\* Importante : É a mesma maneira que é calculado o Desconto do Pedido de Vendas   
  
Veja também o link abaixo sobre o Help DESCMAIOR2 (para casos onde a quantidade é 1)  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047817794-MP-TMK-HELP-DESCMAIOR2?source=search>
