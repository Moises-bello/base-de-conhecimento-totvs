---
article_id: 360019947491
category: RH - Rescisão
content_hash: d2bcd553b7987e78d076bebace26ce514a978504beec3cea9ba81fe9bab39ab5
fetched_at: '2026-06-28T22:43:51.019076+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE  - Como efetuar lançamentos na rescisão complementar
  para verbas que já foram calculadas na rescisão original
type: support-article
updated_at: '2025-06-24T20:00:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019947491-RH-Linha-Protheus-GPE-Como-efetuar-lan%C3%A7amentos-na-rescis%C3%A3o-complementar-para-verbas-que-j%C3%A1-foram-calculadas-na-rescis%C3%A3o-original
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26557594213399)***Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**GPEM040: Como efetuar lançamentos na rescisão complementar para verbas que já foram calculadas na rescisão original?  
  
**Ambiente**Protheus - Gestão de Pessoal - Versão 12  
  
**Solução**Exemplo com a verba 179 - Comissões (Id 0165):

![](http://tdn.totvs.com/download/attachments/286736804/image2017-9-6%2010%3A27%3A49.png?version=1&modificationDate=1504704982000&api=v2 "Linha Microsiga Protheus > GPE006RES12_Lançamentos_Rescisão_Complementar > image2017-9-6 10:27:49.png")

Na **rescisão original** foi informada a verba 179 de comissões com o valor de R$2.000,00:

![](http://tdn.totvs.com/download/attachments/286736804/image2017-9-6%2010%3A36%3A12.png?version=1&modificationDate=1504704982000&api=v2 "Linha Microsiga Protheus > GPE006RES12_Lançamentos_Rescisão_Complementar > image2017-9-6 10:36:12.png")

Mas após o pagamento da **rescisão** surgiu a necessidade de alterar o valor da verba, deveria te sido informado R$3.000,00; então o lançamento na complementar deve ser de R$1000,00, por exemplo.  
  
Então, neste caso na **Rescisão Complementar**, deve ser lançado a diferença, ou seja, o que não foi pago.  
  
- Na rotina de **lançamentos por funcionário**:

![](http://tdn.totvs.com/download/attachments/286736804/image2017-9-6%2010%3A53%3A56.png?version=1&modificationDate=1504706036000&api=v2 "Linha Microsiga Protheus > GPE006RES12_Lançamentos_Rescisão_Complementar > image2017-9-6 10:53:56.png")

- No cálculo da **rescisão complementar**:

![](http://tdn.totvs.com/download/attachments/286736804/image2017-9-6%2010%3A57%3A56.png?version=1&modificationDate=1504706276000&api=v2 "Linha Microsiga Protheus > GPE006RES12_Lançamentos_Rescisão_Complementar > image2017-9-6 10:57:56.png")

**Importante**  
A regra acima é válida para verbas com ou sem Id de Cálculo.

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
