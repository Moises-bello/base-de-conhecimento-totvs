---
content_hash: a7c8950da36c4bc6112eb43fe4a5014fc7271a75e0680f1b74896ec1db0df88c
fetched_at: '2026-06-29T00:05:49.330135+00:00'
page_id: '1039869246'
product: rm
source: tdn-rm
title: Cálculo de Férias - Provisionamento nas Férias utilizando período específico
  para lançamento da provisão na folha de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039869246
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo de Férias com Provisionamento nas Férias utilizando período específico para lançamento da provisão na folha de pagamento. Conforme parâmetro **"Período para lançar o provisionamento do empréstimo crédito do trabalhador nas férias"**  no Parametrizador aba Férias | [Empréstimo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719223).

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Período para lançamento do evento = 5

Lançamento de dois períodos de gozo no mesmo mês:

Primeiro período de gozo de 10 dias - 01/03/2025 a 10/03/2025

valor da provisão - PROVISÃO CRÉDITO DO TRABALHADOR FÉRIAS 1º MÊS  =   905,90

Os eventos das férias foram lançados no período selecionado em parâmetros locais

O evento de provisão do crédito do trabalhador foi lançado no período informado no parametrizador

Segundo período de gozo de 15 dias - 24/03/2025 a 07/04/2025

valores das provisões:

* PROVISÃO CRÉDITO DO TRABALHADOR FÉRIAS 1º MÊS = 1018,16
* PROVISÃO CRÉDITO DO TRABALHADOR FÉRIAS 2º MÊS = 334,06

Os eventos das férias foram lançados no período selecionado em parâmetros locais

No envelope de pagamento foi lançado no período 5 a soma dos eventos da provisão do primeiro mês

905,90 + 1018,16 = 1924,06

**Seguindo nesse mesmo teste finalizando as férias no próximo mês selecionando o período 1 para lançamento das verbas de férias**

Eventos de férias lançados no período 1

Evento da provisão segundo mês lançado no período 5 = 334,06

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
