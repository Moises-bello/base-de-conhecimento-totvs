---
article_id: 360061762394
category: Rescisão
content_hash: 57e09aea2cbd8f962bc7edd9ecb140609100fdd35215d7c45e66e1c6aec77bcb
fetched_at: '2026-06-28T22:46:55.256395+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Como calcular o Aviso Prévio Indenizado quando o número de
  dias não for divisível por dois
type: support-article
updated_at: '2021-06-18T17:02:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061762394-RH-RM-FOP-Como-calcular-o-Aviso-Pr%C3%A9vio-Indenizado-quando-o-n%C3%BAmero-de-dias-n%C3%A3o-for-divis%C3%ADvel-por-dois
---

**Dúvida**

Como realizar o cálculo do aviso prévio indenizado quando o número de dias não for divisível por dois?  
  
**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões  
  
**Solução**

Para rescisões de comum acordo (Tipo V), no campo Dias de Aviso Indenizado, deve ser informado com a metade da quantidade de dias total a ser indenizado. Quando a metade destes dias resultar em decimal, por exemplo 33 dias de aviso prévio indenizado que deveria ser 16,5 dias, o valor a ser informado no campo será o valor arredondado para cima, no caso deste exemplo, 17 dias de aviso prévio indenizado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104367733/mceclip0.png)  
  
 No momento do cálculo, ou seja, quando clicar em "Calcular Rescisão", deverá ser marcado ou não o parâmetro "Aviso Prévio Indenizado abate 0,5 dia", de acordo com o entendimento do usuário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102201334/mceclip1.png)  
  
Caso o parâmetro seja marcado, o sistema calculará 16,5 dias de avivo prévio, ou seja, ele abate 0,5 que foi arredondado no cadastro do aviso indenizado, corrigindo o cálculo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104368513/mceclip2.png)  
  
Para mais informações sobre o tema, [Clique AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=452719173#:~:text=Caso%20o%20usu%C3%A1rio%20queira%20que,metade%20dos%20dias%20de%20aviso.)
