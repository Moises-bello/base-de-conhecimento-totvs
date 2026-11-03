---
article_id: 1500000690702
category: Rescisão
content_hash: 058f6b66e5e26a0c09db782251d3349983cca382e4a1bf47a8e539a437597cbb
fetched_at: '2026-06-28T22:46:55.263195+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - 13º salário pago em dezembro sendo pago novamente na rescisão
type: support-article
updated_at: '2026-01-05T14:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000690702-RH-RM-FOP-13%C2%BA-sal%C3%A1rio-pago-em-dezembro-sendo-pago-novamente-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Estou na competência de dezembro, fiz o pagamento da segunda parcela do 13º salário e agora estou calculando a rescisão do funcionário. No entanto, a rescisão está calculando novamente o valor integral do 13º salário que já havia sido pago. Qual o procedimento a ser realizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Este é um comportamento esperado do sistema. Ocorre que quando é efetuada a rescisão, o sistema efetua o cálculo de todas as verbas que são devidas ao funcionário, tais como Férias, Aviso Prévio, 13º Salário, dentre outras. Como a segunda parcela do 13º Salário já havia sido lançada para o funcionário em período anterior, o sistema precisará calcula-lo novamente na rescisão a fim de verificar se houve alteração no valor. Neste momento, ele lança o evento de 13º Salário Rescisão - [Código de Cálculo 48](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718487) com o que seria o valor total do 13º.  
  
Em compensação, o sistema lança o desconto **Adiantamento de 13º Salário -** [Código de Cálculo 51](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719766), de forma que o valor do 13º Salário pago na segunda parcela seja descontado, não permitindo que o pagamento fique duplicado. O que pode ocorrer, no entanto, é que este evento esteja cadastrado sem estornar as bases de INSS, FGTS e IRRF de 13º Salário, causando valores inconsistentes em seus encargos. Cabe, portanto, verificar o cadastro do evento, aba **Incidências Descontos**, conforme imagem abaixo:  
  
**![](https://totvssuporte.zendesk.com/attachments/token/uq4O8kUh6hJCuRB0N9AUhBn0L/?name=inline1165249153.png)**Logo, marque as flags destacadas na imagem acima, sendo elas: **Estorna INSS 13º**, **Estorna FGTS 13º** e **Estorna IRRF 13º.**
