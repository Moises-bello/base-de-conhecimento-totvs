---
article_id: 360019724112
category: RH - Rescisão
content_hash: a4700acabafcd81685d07f3df0052caf374f4d2dd47e1d2a2fc5ee05f16a9671
fetched_at: '2026-06-28T22:43:48.480521+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Ao lançar manualmente o valor da diferença na rescisão
  complementar o sistema não acata o valor informado,
type: support-article
updated_at: '2026-06-25T12:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019724112-RH-Linha-Protheus-GPE-Ao-lan%C3%A7ar-manualmente-o-valor-da-diferen%C3%A7a-na-rescis%C3%A3o-complementar-o-sistema-n%C3%A3o-acata-o-valor-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33774559948823) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**GPEM040: Rescisão Complementar por Dissídio - Ao lançar manualmente o valor da diferença na rescisão complementar o sistema não acata o valor informado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 11  
  
**Solução**Exemplo com a verba 031 - SALARIO RESCISÃO ID (0048):

**![](http://tdn.totvs.com/download/attachments/285647860/image2017-7-25%2011%3A53%3A21.png?version=1&modificationDate=1500994578000&api=v2)**

Se esta verba, foi informada na Rescisão Original, ao calcular a Rescisão Complementar para ajustar o valor da mesma, deverá lançar (informar) o valor cheio, ou seja, soma-se o valor já pago + o valor a pagar, e internamente o sistema irá descontar o valor já pago e pagará somente a diferença.  
  
**1 - Rescisão Original:**Verba 031 = R$ 1.586,36

**![](http://tdn.totvs.com/download/attachments/285647860/image2017-7-25%2011%3A55%3A22.png?version=1&modificationDate=1500994578000&api=v2)**

**-**Diferença a pagar na rescisão complementar: R$1.586,36 (Verba 031 - rescisão original) x 4,57% (índice de reajuste) = **R$72,50**Valor Total Devido: 1586,36 (Verba 031 - rescisão original) + R$ 72,49 = **R$1658,86****2 - Rescisão Complementar:**Lançar manualmente na Verba 031 = 1658,86

**![](http://tdn.totvs.com/download/attachments/285647860/image2017-7-25%2013%3A26%3A1.png?version=1&modificationDate=1500999962000&api=v2)**

**3 -** O sistema irá descontar R$1586,36 dos R$1658,86, pagando apenas **R$72,50**:

**![](http://tdn.totvs.com/download/attachments/285647860/image2017-7-25%2013%3A26%3A33.png?version=1&modificationDate=1500999994000&api=v2)**

**Saiba Mais**Para adquirir mais informações acesse o *link*: [MP - GPE0204 - Rescisão Complementar por Dissídio - Ao lançar manualmente o valor da diferença na rescisão complementar o sistema não acata o valor informado.](http://tdn.totvs.com/pages/viewpage.action?pageId=285647860)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
