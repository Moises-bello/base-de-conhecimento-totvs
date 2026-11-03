---
content_hash: 71d90f4ba68301af76d625ee29075cc9b309a096534067927a2d6934bc4d7a0d
fetched_at: '2026-06-29T00:05:49.318617+00:00'
page_id: '1039514917'
product: rm
source: tdn-rm
title: 'Função de Fórmula: TR2'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039514917
version: 5
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

Disponibilizado nos patches descritos em [DT - Função de Fórmula TR2](https://tdn.totvs.com/pages/viewpage.action?pageId=1039515779)

## **02.****VISÃO GERAL**

Função de fórmula que retorna o valor de IRRF com dedutível considerando dois  valores passados como parâmetro. Nesta função é considerado os valores fixos dedutíveis quando for o caso, como dedução por dependente, dedução maior de 65 anos, dedução de IR Simplificado.

Sintaxe: TR2 (Valor, Valor)

Serão necessários informar dois parâmetros tipo decimal, um com a base de cálculo do IRRF e outro com o valor dedutível separado. Neste caso o valor dedutível não pode ser abatido da base informada no primeiro parâmetro, ou seja, no primeiro parâmetro deve ser informado o valor total da base sem qualquer abatimento de deduções.

IMPORTANTE:

No caso da Função de fórmula TR2, não leva em consideração deduções como **INSS**, **pensão alimentícia**, então é necessário informar o valor total das deduções no segundo parâmetro.

Dica:

Veja também - [Como calcular a Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual até 7.350,00 - LEI 15.270/2025](https://tdn.totvs.com/pages/viewpage.action?pageId=1021212238)

## **03.****EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Criada a fórmula usando a função de fórmula TR2

IMPORTANTE:

Essa fórmula deve ser cadastrada de acordo com a necessidade do usuário. A fórmula abaixo serve somente para demonstração do exemplo.

Fórmula inserida em um evento de base de cálculo

No envelope de pagamento temos os valores de IRRF e do evento criado para a fórmula TR2 com os mesmos valores

No log temos o cálculo do IRRF usando o código de cálculo 4 - IRRF

No log temos o cálculo do evento com a fórmula TR2

Dica:

No print do log adima onde está escrito \*\*\*\*\*\*\*DEMONSTRÇÃO DE TODO O CÁLCULO DA PENSÃO\*\*\*\*\*\*\*\* significa que foi retirada a demonstração para caber no print.

No log da fórmula além de demonstrar o cálculo das funções de fórmula que foram inseridas na fórmula mostra também os valores fixos utilizados, como:

* Valor do dependente que tem cadastrado nesse funcionário
* Valor a deduzir por funcionário aposentado maior que 65 anos

Perceba também que nesse caso o valor para cálculo do IRRF entrou na faixa para redução do IRRF e o cálculo também foi automático.

**04.** **TABELAS UTILIZADAS**

* GFORMULA
