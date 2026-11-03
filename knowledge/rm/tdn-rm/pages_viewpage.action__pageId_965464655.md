---
content_hash: 5a976b781b11e42b3044c524b07563fa735df1f72f106c7f697b341a54b9ae2e
fetched_at: '2026-06-29T00:12:14.145319+00:00'
page_id: '965464655'
product: rm
source: tdn-rm
title: Cálculo da Rescisão quando tem mais de um empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965464655
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Rescisão quando tem mais de um empréstimo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Existindo 6 empréstimos no cadastro de empréstimo

Cadastrada e calculada a rescisão do funcionário 

Dica:

Lembrar de marcar para descontar os empréstimos. No exemplo foi marcado para lançar todos, mas fica a critério do usuário selecionar como será lançado na rescisão, ou seja, se será por tipo ou manual.

No envelope de pagamento foram lançados conforme abaixo 

Log de cálculo do desconto do empréstimo

IMPORTANTE:

No primeiro print do envelope pode ser visualizado o evento que incide em INSS e no log abaixo os eventos considerados na margem consignável. Com isso o valor que possibilita os descontos dos empréstimos fica menor que a quantidade de empréstimos que o funcionário adquiriu. Nesse cenário será descontado o empréstimo até o limite da base consignável, ficando o restante do valor para insuficiência de saldo.

No log de cálculo podemos ver o percentual sendo aplicado na base consignável e dessa base o desconto é aplicado até o limite, iniciando pelo empréstimo mais antigo de acordo com a data do empréstimo.

Então considerando os cálculos acima o evento de insuficiência de saldo será a soma:

292,52 + 1000,00 + 1000,00 + 1000,00 + 1745,09 = 5037,61

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
