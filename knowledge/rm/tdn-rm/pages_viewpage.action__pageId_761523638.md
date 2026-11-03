---
content_hash: 177e16032a1317b250aa114572b055fdd59baa53f4bffadeaa99a583b4efa5eb
fetched_at: '2026-06-29T00:11:33.904404+00:00'
page_id: '761523638'
product: rm
source: tdn-rm
title: Reajuste - Price - Deságio dentro/fora período reajustado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=761523638
version: 16
---

Este documento tem o objetivo de explicitar o funcionamento do cálculo para planos do tipo price, utilizando o reajuste online com o intuito de trazer as parcelas a valor presente, efetuando o deságio dos juros prefixados, calculados no momento da geração do plano de financiamento. 

Clique aqui para entender o **[cálculo realizado no Deságio](https://tdn.totvs.com/pages/releaseview.action?pageId=435105138)**.

## **Cenário 1: Deságio será calculado conforme configuração do tipo de correção do seu componente (antes, após ou ambos)**

* Sistema se encontra com o parâmetro de reajuste online marcado.
* Sendo gerado uma venda com data base do reajuste em 01/01/2023.
* Data entrega empreendimento 01/12/2023.
* Considerando que estamos em 01/06/2023 e a venda já se encontra reajustada.
* Será solicitado o cálculo do valor liquido em (01/06/2023) para uma parcela com vencimento no futuro (25/02/2028)
* **Comportamento esperado com o componente de juros configurado para tipo correção antes:**
  + O sistema **irá calcular o deságio**, pois o empreendimento não está entregue e o componente de juros é do tipo **antes entrega**;

* **Comportamento esperado com o componente de juros configurado para tipo correção após:**
  + O sistema **não** **irá calcular o deságio**, pois o empreendimento não está entregue e o componente de juros é do tipo **após entrega**.
  + Somente irá calcular deságio para a data do valor líquido 01/12/2023, que é a data de entrega do empreendimento

* **Comportamento esperado com o componente de juros configurado para tipo correção ambos:**
  + O sistema **irá calcular o deságio**, pois o empreendimento não está entregue e o componente de juros é do tipo **ambos**;

**Cenário 2: Deságio calculado e Correção Monetária já calculada**

* Sistema se encontra com o parâmetro de reajuste online marcado, parâmetro  proporcionalizar juros/correção monetária quando período maior que 1 desmarcado.
* Sendo gerado uma venda com data base do reajuste em 01/10/2020 e com periodicidade de recálculo da correção monetária em 12 meses.
* Considerando que estamos em 01/04/2023 e a venda já se encontra reajustada até 01/10/2023.
* Será solicitado o cálculo do valor liquido em (30/08/2023) para uma parcela com vencimento no futuro (25/02/2028), fora do período considerado como o último já reajustado (10/2023).

**Comportamento esperado:**

* + A Parcela deverá ter o seu valor de juros prefixado calculado para a data de (30/08/2023) e a correção monetária deverá se manter com o valor já calculado até a data de (01/10/2023). Ou seja, irá ocorrer o valor do deságio para juros, mas a correção monetária não será calculada proporcionalmente, porque o parâmetro proporcionalizar juros/correção monetária quando período maior que 1 esta desmarcado.   
    Assim não será exigido índice de cotação para a moeda utilizada como referência para o reajuste da correção monetária.

## **Cenário 3: Deságio calculado e Correção monetária calculada**

* Sistema se encontra com o parâmetro de reajuste online marcado, parâmetro  proporcionalizar juros/correção monetária quando período maior que 1 marcado.
* Sendo gerado uma venda com data base do reajuste em 01/10/2020 e com periodicidade de recálculo da correção monetária em 12 meses.
* Considerando que estamos em 01/04/2023 e a venda já se encontra reajustada até 01/10/2023.
* Será solicitado o cálculo do valor liquido em (30/08/2023) para uma parcela com vencimento no futuro (25/02/2028), fora do período considerado como o último já reajustado (10/2023).

**Comportamento esperado:**

* + A Parcela deverá ter o seu valor de juros prefixado calculado para a data de (30/08/2023) e a correção monetária deverá ter o valor calculado até a data de (30/08/2023). Ou seja, irá ocorrer o cálculo para o valor do deságio no juros e na correção monetária proporcionalmente utilizando os índices cadastrados, porque o parâmetro proporcionalizar juros/correção monetária quando período maior que 1 esta marcado.   
    Assim será exigido índice de cotação para a moeda utilizada como referência para o reajuste da correção monetária.

## **Cenário 4: Deságio e correção monetária solicitado para a data do próximo reajuste ou acima.**

* Sistema se encontra com o parâmetro de reajuste online marcado, parâmetro proporcionalizar juros/correção monetária quando período maior que 1 desmarcado.
* Sendo gerado uma venda com data base do reajuste em 01/10/2020 e com periodicidade de recálculo da correção monetária em 12 meses.
* Considerando que estamos em 01/04/2023 e a venda já se encontra reajustada até 01/10/2023.
* Será solicitado o cálculo do valor liquido em (01/10/2023) para uma parcela com vencimento no futuro (25/02/2028), fora do período considerado como o último já reajustado (10/2023).

**Comportamento esperado:**

* + - A Parcela deverá calcular o seu valor de juros prefixado para a data de (30/10/2023) e a correção monetária deverá ter o valor calculado até a data de (30/10/2024).   
      Ou seja, irá ocorrer o cálculo para o valor do deságio no juros e o cálculo da correção monetária utilizando os índices cadastrados para todo o próximo período, porque a data de solicitação do deságio é a data de cálculo para o reajuste da correção monetária do próximo período, com isso, não podemos calcular o deságio se não conseguirmos efetuar o reajuste do próximo período que se encontra com o reajuste ainda pendente. Mesmo que se tenha os índices já cadastrados não poderemos calcular a correção monetária para o próximo período, pois o parâmetro proporcionalizar juros/correção monetária quando período maior que 1 esta desmarcado.  
      Assim será exigido índice de cotação para a moeda utilizada como referência para o reajuste da correção monetária.
