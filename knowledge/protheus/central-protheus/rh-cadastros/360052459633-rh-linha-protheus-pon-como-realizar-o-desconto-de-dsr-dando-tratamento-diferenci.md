---
article_id: 360052459633
category: RH - Cadastros
content_hash: a03da5dfdd9f53a25821f058320d133991a5f2084c48a04ee0fab0ab4fc92867
fetched_at: '2026-06-28T22:44:52.918445+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como realizar o desconto de DSR dando tratamento
  diferenciado para turnos com diferentes cargas horárias
type: support-article
updated_at: '2025-06-16T18:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052459633-RH-Linha-Protheus-PON-Como-realizar-o-desconto-de-DSR-dando-tratamento-diferenciado-para-turnos-com-diferentes-cargas-hor%C3%A1rias
---

**Dúvida**Como realizar o desconto de DSR de forma diferente para funcionários com carga horária de 06h e 08h?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para realizar o desconto de DSR de forma diferente por conta da carga horária dos turnos, o cadastro do Arredondamento de DSR deve ser feito por turno. Por exemplo, se na empresa existir apenas um turno com carga horária de 06h, deverá ser criado um arredondamento de DSR atrelado a este turno e depois deverá ser criado um outro arredondamento de DSR com campo de turno em branco para que o desconto seja processado para os demais turnos existentes na empresa.  
  
No exemplo abaixo, apenas o turno 01 tem carga horária de 06h, portanto, preciso realizar desconto de 06h de DSR. Os demais turnos da empresa, tem carga horária de 08h, portanto, o desconto deve ser de 07h20, neste caso, o cadastro de Arredondamento ficará desta forma:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082012494/mceclip3.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083154213/mceclip0.png)
