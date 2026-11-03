---
content_hash: 477ff2ed56845b39bbb50f2274a54c8c11e22e99f51f79afac4e4cf298c00a79
fetched_at: '2026-06-29T00:10:38.706000+00:00'
page_id: '544711400'
product: rm
source: tdn-rm
title: MP927/1046 - Antecipação de Férias Individuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544711400
version: 4
---

Conforme a MP927, Art. 6º e MP1046, Art. 5º:

§1º As férias:  
I - não poderão ser gozadas em períodos inferiores a cinco dias corridos; e  
II - poderão ser concedidas por ato do empregador, ainda que o período aquisitivo a elas  
relativo não tenha transcorrido.  
§ 2º Adicionalmente, empregado e empregador poderão negociar a antecipação de períodos  
futuros de férias, mediante acordo individual escrito.

O Módulo TOTVS Folha de Pagamento já está aderente para permitir a antecipação de férias, podendo os dias antecipados serem descontados de períodos futuros conforme a parametrização abaixo:

**Cadastro de antecipação com parâmetro ‘Permite antecipação de dias de férias do próximo período aquisitivo’ no cadastro do sindicato desmarcado:**

*Caso 1:*

Funcionário com saldo de férias menor que 30 dias: Ao marcar as férias para 30 dias, o sistema irá calcular como férias a marcar com negativo. Clicando em salvar retornar a mensagem abaixo, porém não impede de fazer a marcação de férias

Ao finalizar as férias o sistema abre um novo período aquisitivo. Porém o mesmo não computa com o saldo devedor que foi ‘antecipado’ no período acima, começando a contagem de dias de direito do zero para este novo período aberto. Isto ocorre porque dentro deste período o funcionário ainda teria como direito estes dias até o final do período aquisitivo.

*Caso 2:*

Funcionário teve 10 dias de férias dentro do período aquisitivo vencido e ainda tem um saldo de 20 dias:

Ao marcar as férias para 30 dias, o sistema retorna a mensagem abaixo. O saldo a marcar fica negativo mesmo o funcionário possuindo saldo de períodos futuros. O sistema retorna as mensagens abaixo informando que o mesmo não tem os 30 dias de direito.

Após finalizar as férias, foi aberto um novo período com 20 dias de saldo, não abatendo os 10 dias que foram concedidos para o funcionário no período anterior:

**Cadastro de antecipação com parâmetro ‘Permite antecipação de dias de férias do próximo período aquisitivo’ do sindicato marcado:**

*Caso 1:*

Marcando 30 dias de férias para um funcionário que tem somente 20 dias de saldo e o período aquisitivo ainda não está vencido, o saldo de férias a marcar fica negativo. O processo emite a mensagem abaixo alertando o saldo inferior aos dias de marcação de férias, mas não impede que as mesmas sejam marcadas. Repare que é exibido a aba ‘Antecipação de Férias’ após marcar o parâmetro acima:

Neste caso não é uma antecipação do próximo período, pois o funcionário ainda tem um saldo de 10 dias de férias dentro deste período.

*Caso 2:*

Funcionário tem o período vencido, mas já gozou de 10 dias em Janeiro e tem um saldo de 20 deste período:

 

O funcionário irá gozar de 30 dias de férias, antecipando 10 dias que é referente ao próximo período aquisitivo. O saldo do período é 20 dias e o saldo total que o funcionário tem direito é 40 dias. O sistema retorna as mensagens abaixo, informando que irá antecipar 10 dias do próximo período:
