---
content_hash: f52ae88280d0719afd55a95e15cb3a98aed61227ffc4a6a0a372b43ea68425a3
fetched_at: '2026-06-29T00:11:33.997719+00:00'
page_id: '764339294'
product: rm
source: tdn-rm
title: Reajuste Pró-Rata
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=764339294
version: 6
---

Atenção!

Recomendamos o uso do [Reajuste Online](https://tdn.totvs.com/pages/viewpage.action?pageId=633072776) para evitar divergência de valores entre o valor que deveria ser cobrado e o valor reajustado (que pode variar de acordo com as configurações abaixo).

Ao utilizar o Reajuste Pró-Rata, seja de Periodicidade anual ou mensal, o parâmetro da Data do Reajuste, poderá ser configurado de quatro formas:

* Reajustar até o **último** dia do mês (destaque em verde) e o parâmetro reajustar até o dia de vencimento **desmarcado** (destaque em azul):
  + Com esta configuração o sistema irá reajustar desde o início da Data Base do componente da Regra até o último dia do mês do reajuste solicitado. Exemplo: se a parcela vence no dia 17, a mesma será reajustada até data do reajuste parametrizada, ao invés de somente até o dia do seu vencimento;
* Reajustar até o **último** dia do mês (destaque em verde) e o parâmetro reajustar até o dia de vencimento **marcado** (destaque em azul):
  + Com esta configuração o sistema irá reajustar desde o início da Data Base do componente da Regra até o dia do vencimento da parcela do contrato. Exemplo: se a parcela vence no dia 17, a mesma só será reajustada até o seu vencimento;
* Reajustar até o **primeiro** dia do mês (destaque em verde) e o parâmetro reajustar até o dia de vencimento **desmarcado** (destaque em azul):
  + **Não recomendamos este tipo de configuração** porque o sistema irá reajustar desde o início da Data Base do componente da Regra **até o primeiro dia do mês** do reajuste solicitado e desta forma o reajuste aplicado será inferior à sua periodicidade, cobrando-se um valor inferior ao esperado. Exemplo: se a parcela vence no dia 17, a mesma só será reajustada até o primeiro dia do mês, deixando o seu reajuste incompleto, inferior à sua periodicidade, ao invés reajustar até o dia do seu vencimento;
* Reajustar até o **primeiro** dia do mês (destaque em verde) e o parâmetro reajustar até o dia de vencimento **marcado** (destaque em azul):
  + Com esta configuração o sistema irá reajustar desde o início da Data Base do componente da Regra até o dia do vencimento da parcela do contrato. Ou seja apesar de solicitar o reajuste para o primeiro dia do mês, o sistema irá reajustar todas as parcelas até a data do seu vencimento. Exemplo: se a parcela vence no dia 17, a mesma só será reajustada até o seu vencimento;
