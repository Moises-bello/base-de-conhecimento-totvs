---
article_id: 1500010997741
category: Férias
content_hash: f9be87dfa3ae32d1df6fb16f40c6fd5433c46388f616e9fb0813ad268596c3b7
fetched_at: '2026-06-28T22:46:56.413160+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Qual o processo para antecipação de férias individuais conforme
  a MP 1.046/2021?
type: support-article
updated_at: '2025-03-07T14:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010997741-RH-RM-FOP-Qual-o-processo-para-antecipa%C3%A7%C3%A3o-de-f%C3%A9rias-individuais-conforme-a-MP-1-046-2021
---

**Dúvida**

Qual o processo para antecipação de férias individuais conforme MP 1.046? Ocorreram mudanças no produto?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.290
* 12.1.29.250
* 12.1.31.154 e superiores.

**Solução**

O processo de antecipação de férias não sofreu alteração nesta nova MP 1.046, sendo assim continua sendo o mesmo processo adotado anteriormente para atender à MP 927, podendo os dias antecipados serem descontados de períodos futuros conforme a parametrização abaixo:

**1)** Cadastro de antecipação com o parâmetro **‘Permite antecipação de dias de férias do próximo período aquisitivo’** no cadastro do sindicato **desmarcado:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017750882/mceclip0.png)

* ***Cenário 1**:*  Funcionário com saldo de férias menor que 30 dias: Ao marcar as férias para 30 dias, o sistema irá calcular como férias a marcar com negativo. Clicando em salvar, retorna a mensagem abaixo, porém não impede de fazer a marcação de férias:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058161/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017750902/mceclip2.png)  
  
Ao finalizar as férias o sistema abre um novo período aquisitivo. Porém o mesmo não computa com o saldo devedor que foi ‘antecipado’ no período acima, começando a contagem de dias de direito do zero para este novo período aberto. Isto ocorre porque dentro deste período o funcionário ainda teria como direito estes dias até o final do período aquisitivo.

* ***Cenário 2:*** Funcionário teve 10 dias de férias dentro do período aquisitivo vencido e ainda tem um saldo de 20 dias:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058181/mceclip3.png)  
  
Ao marcar as férias para 30 dias, o sistema retorna a mensagem abaixo. O saldo a marcar fica negativo mesmo o funcionário possuindo saldo de períodos futuros. O sistema retorna as mensagens abaixo informando que o mesmo não tem os 30 dias de direito.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017750922/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058201/mceclip5.png)  
  
Após finalizar as férias, foi aberto um novo período com 20 dias de saldo, não abatendo os 10 dias que foram concedidos para o funcionário no período anterior:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017750982/mceclip6.png)  
  
2) Cadastro de antecipação com parâmetro **‘Permite antecipação de dias de férias do próximo período aquisitivo’** do sindicato **marcado:**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058381/mceclip7.png)**

* ***Cenário 1*:** Marcando 30 dias de férias para um funcionário que tem somente 20 dias de saldo e o período aquisitivo ainda não está vencido, o saldo de férias a marcar fica negativo. O processo emite a mensagem abaixo alertando o saldo inferior aos dias de marcação de férias, mas não impede que as mesmas sejam marcadas. Repare que é exibido a aba ‘Antecipação de Férias’ após marcar o parâmetro acima:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017751102/mceclip8.png)  
  
Neste caso não é uma antecipação do próximo período, pois o funcionário ainda tem um saldo de 10 dias de férias dentro deste período.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058421/mceclip9.png)

* ***Cenário 2:*** Funcionário tem o período vencido, mas já gozou de 10 dias em Janeiro e tem um saldo de 20 deste período:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018058461/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017751122/mceclip11.png)  
  
O funcionário irá gozar de 30 dias de férias, antecipando 10 dias que é referente ao próximo período aquisitivo. O saldo do período é 20 dias e o saldo total que o funcionário tem direito é 40 dias. O sistema retorna as mensagens abaixo, informando que irá antecipar 10 dias do próximo período:  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017751162/mceclip12.png)

Mais informações: [MP927/1046 - Antecipação de Férias Individuais](https://tdn.totvs.com/pages/releaseview.action?pageId=544711400)
