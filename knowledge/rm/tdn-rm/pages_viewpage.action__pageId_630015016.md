---
content_hash: c6809054b8d7885f4f6207fd406007e097fff166ef323768dddcdc3a5ca9fda0
fetched_at: '2026-06-29T00:11:05.343991+00:00'
page_id: '630015016'
product: rm
source: tdn-rm
title: Movimento - Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=630015016
version: 6
---

As férias no contrato verde amarelo são pagas ao funcionário mês a mês junto com o movimento mensal. Com o fim do contrato verde amarelo, temos duas situações à tratar:

1ª - O funcionário com o contrato verde amarelo é demitido e pago TODOS os seus direitos conforme a legislação, e este mesmo funcionário é contratado como funcionário normal e passa a seguir a CLT com todos os seus direitos trabalhistas quitados no primeiro contrato e iniciando um novo vínculo trabalhista, onde terá início de período aquisitivo de férias, 13º Salário, etc.

2ª - O funcionário com o contrato verde amarelo tem seu tipo alterado para o tipo de funcionário '**N - Normal**' e continua o vínculo trabalhista, onde o funcionário terá direito as férias, 13º salário, etc. Nesse caso, o funcionário já recebeu avos de férias e de 13º salário que deverão ser descontados do funcionário quando este for receber o 13º salário e/ou gozar as férias do período aquisitivo adquirido na vigência do contrato verde/amarelo e posteriormente do contrato normal de trabalho.

Para atender as demandas , onde o vínculo trabalhista é continuado, alterando apenas o tipo de funcionário para **'N - Normal'**, foram criados os códigos de cálculo abaixo:

* **446 - Férias Antecipadas Contrato Verde Amarelo,**Provento do tipo valor.
* **447 - Abatimento Férias Contrato Verde Amarelo,**Desconto do tipo valor.
* **448 - Abatimento Férias Contrato Verde Amarelo Primeiro Mês,**Desconto do tipo valor.
* **449 - Abatimento Férias Contrato Verde Amarelo Segundo Mês,**Desconto do tipo valor.
* **450 - Saldo Devedor Férias Contrato Verde Amarelo,**Base de Cálculo do tipo valor.

O usuário deverá informar o código do evento criado com o código de cálculo '**446 - Férias Antecipadas Contrato Verde Amarelo'**nos eventos lançados na ficha financeira mês a mês do período em que o funcionário tinha o contrato verde amarelo à título de férias, médias e 1/3 de férias.

Após informar o código do evento, o usuário deverá calcular as férias normalmente para o funcionário. Ao calcular as férias,  o sistema irá lançar os eventos com os códigos de cálculo **'38 - Férias', '40 - 1/3 Férias' e os eventos de médias de férias**e também irá lançar o evento com código de cálculo '**447 - Abatimento Férias Contrato Verde Amarelo'**abatendo as férias pagas mês a mês ao funcionário para as férias integrais no mês. Quando o valor dos abatimentos forem maiores que os proventos de férias do funcionário,  o sistema irá lançar o evento com código de cálculo '**450 - Saldo Devedor Férias Contrato Verde Amarelo'**para que seja descontado o restante do valor do funcionário desde que sejam férias referentes ao mesmo período aquisitivo de férias.

Para o cálculo das férias partidas, o usuário deverá informar o código do evento criado com o código de cálculo '**446 - Férias Antecipadas Contrato Verde Amarelo'**nos eventos lançados na ficha financeira mês a mês do período em que o funcionário tinha o contrato verde amarelo à título de férias, médias e 1/3 de férias.

Após informar o código do evento, o usuário deverá calcular as férias normalmente para o funcionário. Ao calcular as férias,  o sistema irá lançar os eventos com os códigos de cálculo **'41 - Férias no mês', '42 - Férias no próximo mês', '76 -1/3 Férias no mês', '77 - 1/3 Férias no próximo mês' e os eventos de médias de férias** e também irá lançar os eventos com código de cálculo '**448 - Abatimento Férias Contrato Verde Amarelo Primeiro Mês' e  '449 - Abatimento Férias Contrato Verde Amarelo Segundo Mês',**abatendo as férias pagas mês a mês ao funcionário para as férias partidas no mês e próximo mês. Quando o valor dos abatimentos forem maiores que os proventos de férias do funcionário,  o sistema irá lançar o evento com código de cálculo '**450 - Saldo Devedor Férias Contrato Verde Amarelo'** para que seja descontado o restante do valor do funcionário desde que sejam férias referentes ao mesmo período aquisitivo de férias.
