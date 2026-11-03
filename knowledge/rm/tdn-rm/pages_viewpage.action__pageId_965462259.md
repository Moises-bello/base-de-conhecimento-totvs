---
content_hash: c4193f3bdff9c0f7102f2b088764667d43851a23a892d72c9ff81a67e62bc6ee
fetched_at: '2026-06-29T00:12:14.141443+00:00'
page_id: '965462259'
product: rm
source: tdn-rm
title: Cálculo de Férias - Provisionamento nas Férias quando tem mais de um empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965462259
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo de Férias com Provisionamento nas Férias quando tem mais de um empréstimo.

Veja também dicas e observações importantes no exemplo [Cálculo de Férias - Provisionamento nas Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=963024323).

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Existindo 6 empréstimos no cadastro de empréstimo

Calculando férias partidas proporcionalizando a provisão do empréstimo

IMPORTANTE:

Veja que o líquido desse exemplo ainda ficou positivo, pode ser que o líquido fique zerado porque os empréstimos serão provisionados no total até o limite do líquido a receber no envelope de férias.

No log de cálculo aparece a soma de todos os empréstimos sendo proporcionalizado por dias de férias

1000,00 + 1000,00 + 1000,00 + 1000,00 + 1000,00 + 1745,09 = 6745,09

Lançamento das férias no mês

Lançamento das férias no envelope de pagamento e automaticamente lança a provisão do primeiro mês.

Lançamento dos descontos dos empréstimos juntamente com os dias trabalhados no mês

IMPORTANTE:

Foram descontados apenas dois dos empréstimos devido a margem consignada ser calculada 35% dos eventos que incidem em contribuição previdenciária descontando INSS e IRRF.

Log de cálculo após lançamento do desconto do empréstimo

IMPORTANTE:

No primeiro print do envelope pode ser visualizado o evento que incide em INSS e no log abaixo os eventos considerados na margem consignável. Com isso o valor que possibilita os descontos dos empréstimos fica menor que a quantidade de empréstimos que o funcionário adquiriu. Nesse cenário será descontado o empréstimo até o limite da base consignável, ficando o restante do valor para insuficiência de saldo.

No log de cálculo podemos ver o percentual sendo aplicado na base consignável e dessa base o desconto é aplicado até o limite, iniciando pelo empréstimo mais antigo de acordo com a data do empréstimo.

Então considerando os cálculos acima o evento de insuficiência de saldo será a soma:

501,97 + 1000,00 + 1000,00 + 1000,00 + 1745,09 = 5247,06

 

Lançamento das férias no próximo mês

Finalizando as férias para o próximo mês

Lançamento dos descontos dos empréstimos juntamente com os dias trabalhados no mês pelo processo Lançamento Multi-coligadas

IMPORTANTE:

Foram descontados apenas três dos empréstimos devido a margem consignada ser calculada 35% dos eventos que incidem em contribuição previdenciária descontando INSS e IRRF.

Log de cálculo após lançamento do desconto do empréstimo

IMPORTANTE:

No print do envelope pode ser visualizado o evento que incide em INSS e no log abaixo os eventos considerados na margem consignável. Com isso o valor que possibilita os descontos dos empréstimos fica menor que a quantidade de empréstimos que o funcionário adquiriu. Nesse cenário será descontado o empréstimo até o limite da base consignável, ficando o restante do valor para insuficiência de saldo.

No log de cálculo podemos ver o percentual sendo aplicado na base consignável e dessa base o desconto é aplicado até o limite, iniciando pelo empréstimo mais antigo de acordo com a data do empréstimo.

Então considerando os cálculos acima o evento de insuficiência de saldo será a soma:

22,58 + 1000,00 + 1000,00 + 1745,09 = 3767,67

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
