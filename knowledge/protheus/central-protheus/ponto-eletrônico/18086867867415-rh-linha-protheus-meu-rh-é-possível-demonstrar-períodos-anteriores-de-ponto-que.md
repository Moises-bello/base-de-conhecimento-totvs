---
article_id: 18086867867415
category: PONTO ELETRÔNICO
content_hash: b049b540c959c5b4087dc0c34e25a31c72e9eaff90ce80796318110264c05f2c
fetched_at: '2026-06-28T22:44:36.572354+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível demonstrar períodos anteriores de
  ponto, que não estão fechados, no App Meu RH
type: support-article
updated_at: '2026-06-19T14:11:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18086867867415-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-demonstrar-per%C3%ADodos-anteriores-de-ponto-que-n%C3%A3o-est%C3%A3o-fechados-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18086875072535) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possível demonstrar períodos anteriores de ponto, que não estão fechados, no App Meu RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O App Meu RH sempre demonstrará **o período de Ponto aberto pelo parâmetro MV\_PONMES** e, os **demais que já foram fechados** pelo módulo do SIGAPON - Ponto Eletrônico.  
  
Demonstraremos abaixo, na prática qual o funcionamento do Meu RH.  
  
Mês aberto pelo **MV\_PONMES - Outubro 2023**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18085933478807)  
  
Meses fechados pelo Ponto Eletrônico **(Junho e Julho)**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18085692898967)  
  
Quando logar no Meu RH, irá demonstrar:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18085987227031)  
  
Sempre o Meu RH, **demonstrará o período aberto, junto aos fechados**, se houver períodos anteriores aberto, como é o caso de **Agosto e Setembro nesse exemplo**, e **o parâmetro MV\_PONMES estando em Outubro**, eles **não serão demonstrados**.  
  
Será demonstrado somente quando, **efetivamente, o mês de Agosto e Setembro, pelo módulo SIGAPON - Ponto Eletrônico, forem fechados**, ou então, o parâmetro **MV\_PONMES estiver cadastrado com o período aberto**.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
