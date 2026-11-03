---
content_hash: 01cce6b3a7b3746f72bb7e89406c5b807f54db60cd1ef465e4d9c79101d6521f
fetched_at: '2026-06-29T00:12:14.116767+00:00'
page_id: '965457219'
product: rm
source: tdn-rm
title: Cálculo da Folha - Quando tem mais de um empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965457219
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador quando o funcionário tem mais de um empréstimo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Existindo 6 empréstimos no cadastro de empréstimo

Foram descontados apenas 3 dos empréstimos

Gerou insuficiência de saldo que será acumulado em apenas um evento

No log de cálculo podemos ver o percentual sendo aplicado na base consignável e dessa base o desconto é aplicado até o limite, iniciando pelo empréstimo mais antigo de acordo com a data do empréstimo.

O Valor da insuficiência inicia o acumulo no terceiro empréstimo somando com os demais porque não tem saldo na margem consignável para o desconto.

Veja também que a data do empréstimo é a mesma do cálculo anterior e a ordem de cálculo considerou o cadastro que o evento 1480 (código de empréstimo = 00002) foi cadastrado primeiro que o evento 2480 (código de empréstimo = 00003).

Como não tem mais valor na margem consignável para desconto dos próximos empréstimos, estes serão somados e lançados no evento de insuficiência de saldo

Então considerando os cálculos acima o evento de insuficiência de saldo será a soma:

732,84 + 1000,00 + 1000,00 + 1745,09 = 4477,93

Dica:

Cada empréstimo cadastrado no cadastro de empréstimos recebe o respectivo valor descontado e insuficiência de saldo quando devido.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
