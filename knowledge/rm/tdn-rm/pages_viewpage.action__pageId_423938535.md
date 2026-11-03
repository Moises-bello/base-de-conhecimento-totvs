---
content_hash: 8c694429a441dcab95e80bcaa210595b20ac2bdcb16833a2bed90ceb38549f55
fetched_at: '2026-06-29T00:09:27.531229+00:00'
page_id: '423938535'
product: rm
source: tdn-rm
title: Recálculo do Segundo Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938535
version: 3
---

Nos Parâmetros do Sistema|Lançamentos define-se  a moeda nacional ou moeda corrente a ser utilizada pelo Totvs Gestão Contábil e, a partir desta configuração, todos os valores informados para os lançamentos são sempre feitos em moeda corrente, entretanto, no momento da inclusão dos lançamentos, o sistema pode calcular automaticamente estes valores em outra moeda, basta que isto também seja definido nos Parâmetros do Sistema. Assim, os valores dos lançamentos continuam sendo informados em moeda corrente, mas o sistema apresenta também o 2º Valor para os lançamentos, tomando como base outra moeda.

Sabemos, porém, que o valor de determinadas moedas precisam ser reajustados constantemente e, consequentemente, o 2º Valor que havia sido calculado automaticamente na inclusão do lançamento.

Este processo possibilita a qualquer momento fazer o **Recálculo do 2º Valor** tomando como base a Moeda indicada para o recálculo. Esta moeda não precisa ser necessariamente a mesma moeda indicada nos Parâmetros como moeda para o 2º Valor.

O recálculo do 2º Valor será aplicado somente nos lançamentos filtrados para o processo, conforme os dados indicados nos filtros de seleção para o recálculo.

**Regras para o recálculo:**

* O 2º Valor é calculado, pegando-se o Valor do lançamento e dividindo-o pelo valor da cotação da Moeda no dia informado conforme regras repassadas nos filtros.
* Se a opção 'Usa cotação da data do lançamento' estiver marcada o sistema utiliza para o cálculo a cotação da moeda cadastrada na data do lançamento, caso não esteja marcada, utiliza a cotação da moeda cadastrada na Data da 2ª Moeda, que é informada na tela da partida do lançamento e, caso esta Data da 2ª Moeda esteja em branco, utiliza a data do lançamento.
* Se o 2º Valor dentro da tela da partida do lançamento estiver em branco, o sistema somente fará o cálculo se a opção 'Recalcula inclusive quando Segundo Valor = 0' estiver marcada.
* O sistema verifica se existe cotação na data informada para execução do processo (data do lançamento ou data da 2ª moeda), caso não exista busca a primeira cotação cadastrada com data menor que a data informada para o processo, se ainda assim não existir cotação cadastrada, busca a primeira cotação cadastrada com data superior à data informada para o processo. Se para nenhuma das opções tiver cotação cadastrada o sistema não fará o recálculo.

Veja também

* **.**
