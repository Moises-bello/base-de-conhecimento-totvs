---
article_id: 360047817794
category: Call Center - Televendas
content_hash: fc46e1fe65de0367f3d3185fdf53ed2b6a89a884dddc87a23fc3e48a56387723
fetched_at: '2026-06-28T22:41:30.279409+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - SIGATMK- HELP - DESCMAIOR2
type: support-article
updated_at: '2024-04-29T13:08:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047817794-Cross-Segmentos-Backoffice-Protheus-SIGATMK-SIGATMK-HELP-DESCMAIOR2
---

**Dúvida**

Orientação sobre o **Help DESCMAIOR**2 no Televendas.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

Caso o valor do campo **UB\_VALDESC** (Valor de Desconto) seja maior que o campo **UB\_VRUNIT** (Valor Unitário) em uma operação que a quantidade vendida for 1, o sistema vai gerar este Help **DESCMAIOR2**.

Esta mensagem ocorre, porque o sistema não aceita valor maior que 100% de desconto no valor unitário quando a quantidade for igual a 1.

O desconto maior que 100% vai gerar o valor unitário como negativo (uma vez que o campo **UB\_VALDESC** deduz o valor do desconto no preço unitário).  
  
Abaixo a imagem mostra outro meio de gerar Desconto o Atendimento Call Center, por meio do Total do Atendimento.

![](https://totvssuporte.zendesk.com/attachments/token/NYRnZ872zZj8JoEymkaZBOYg4/?name=inline356444615.png)  
  
Para habilitar o desconto no total do Atendimento é necessário dar permissão no Grupo de Atendimento.

![](https://totvssuporte.zendesk.com/attachments/token/TlfWHyfeQkxhwNFAbcfE9dp0N/?name=inline2053211084.png)
