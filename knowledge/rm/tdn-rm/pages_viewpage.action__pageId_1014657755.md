---
content_hash: a0326c225a427b5a1dbc2a0302ecc907371e1197fdc238cebe0abfa36bacb328
fetched_at: '2026-06-29T00:05:47.449225+00:00'
page_id: '1014657755'
product: rm
source: tdn-rm
title: Cálculo dos eventos com código de cálculo 329 / 330 / 331 quando tem fórmula
  nos eventos de média
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1014657755
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Quando os eventos de média no cadastro de sindicato tem fórmula são proporcionalizados ao final do cálculo da fórmula para cada um dos códigos de cálculo 329/330/331 e nesse caso são acumulados para lançamento no envelope de pagamento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios:

No inicio dos cálculos esses eventos não consideram os valores das médias:

Médias calculadas por fórmulas:

**SOMA DO CC329**

**993,94 + 71,90 + 14,38 + 95,87 = 1176,09**

**SOMA DO CC330**

**4969,72 + 359,49 + 539,24 + 71,90 + 107,85 + 479,33 + 718,99 = 7246,52**

**SOMA DO CC 331**

**11927,32 + 862,79 + 172,56 + 1150,37 = 14113,04**

No log será demonstrado essa soma:

IMPORTANTE:

Caso haja um evento que não tenha fórmula e o cálculo da média seja feito pelo sistema, esse evento será somado ao valor original, por exemplo:

CÁLCULO FINAL CONSIDERANDO EVENTOS CALCULADOS POR FÓRMULA

CC329 - 993,94 + **112,95** = 1106,89

CC330 - 4969,72 + **564,74** = 5534,46

CC331 - 11927,32 + 969,55 = 12896,87

LOG DE MÉDIA - ANALISANDO O VALOR DO CC329

Calculando Média de Férias Proporcionais para o funcionário 00024

RESULTADO FINAL APÓS COMPARAÇÃO DAS MÉDIAS

Será considerada a média do período aquisitivo.

Média do Grupo 1: 1.355,38

Valor total da média: 1.355,38

Proporcionaliza valor da média do grupo 1 para 15,0 dias: 1.355,38 / 30 \* 15,0 = 677,690000

**1355,38 / 30 \* 12,5 = 564,74 - proporcional**

**1355,38 / 30 \* 2,5 = 112,95 - indenizada**

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
