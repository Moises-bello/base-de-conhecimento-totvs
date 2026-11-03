---
article_id: 360049737753
category: RH - Rescisão
content_hash: cc560dc2180aedc75dbfd14e0a6fe922d6b106144675a37844b42c128b08cf47
fetched_at: '2026-06-28T22:43:52.049333+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como descontar taxa negocial em rescisão complementar
  por PLR?
type: support-article
updated_at: '2022-07-20T14:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049737753-RH-Linha-Protheus-GPE-Como-descontar-taxa-negocial-em-rescis%C3%A3o-complementar-por-PLR
---

**Dúvida**Como descontar taxa negocial em rescisão complementar por PLR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

1. Para calcular rescisão complementar por PLR com desconto da taxa negocial, aplique a patch abaixo e crie o campo RV\_REFPLR no cadastro de verbas.

12.1.33:  <https://suporte.totvs.com/portal/p/10098/download#detail/1039093>

Aplique-o primeiro em base teste e faça um Backup do RPO antes da aplicação  
  
2. Efetue a configuração do campo conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074324433/mceclip0.png)

3. Após a criação do campo, crie uma verba sem ID para Taxa Negocial a verba deve ser de Desconto.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074346073/mceclip1.png)

Na aba Outros será demonstrado o campo criado Ref.PLR deixe = SIM.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073158114/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073159094/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074348713/mceclip4.png)
