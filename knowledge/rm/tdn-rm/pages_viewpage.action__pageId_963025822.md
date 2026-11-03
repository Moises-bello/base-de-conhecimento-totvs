---
content_hash: 1bd46c008b70f05a08e50ca8ddd059ef79a141f109ad1bb98d1bdc184fe1d824
fetched_at: '2026-06-29T00:12:14.049742+00:00'
page_id: '963025822'
product: rm
source: tdn-rm
title: Lançamento Financeiro do empréstimo Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963025822
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Lançamento Financeiro.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para geração de Títulos de Lançamentos Financeiros, o mesmo pode ser customizado por fórmula, onde a mesma irá retornar o valor do evento.

Conforme o exemplo abaixo, foi utilizado a função de fórmula MVRUBRICA que utiliza como parâmetro (MES, ANO, '9253') onde **9253 é correspondente a natureza da rubrica do eSocial.**

Cadastrar o Lançamento financeiro do tipo 7 - Fórmula e associar a fórmula criada a ele:

E o título será gerado conforme as configurações:

**Observação:**

Embora o FGTS e o Crédito do Trabalhador estejam reunidos em uma mesma guia de recolhimento, eles são tratados como lançamentos financeiros distintos no sistema.  
Do ponto de vista financeiro, cada um deve ser registrado separadamente para garantir a correta identificação dos pagamentos.

Um exemplo é a guia DCFTWEB: trata-se de um único documento, porém composto por dois lançamentos financeiros — o valor da empresa (eSocial) e o valor referente ao REINF, originado do fiscal.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
