---
content_hash: a58b2706e766b6eb202854b76890bbb638e598565c374853d5ac8fcff9257de4
fetched_at: '2026-06-29T00:12:14.012221+00:00'
page_id: '963023608'
product: rm
source: tdn-rm
title: Cálculo da Folha - Considerando Eventos Remuneração Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963023608
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Folha - Considerando Eventos Remuneração Crédito do Trabalhador.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

* PARÃMETRO DESMARCADO COM EVENTOS INFORMADOS - Serão considerados APENAS eventos informados no Anexo ou Parametrizador para Remuneração Créd.Trabalhador

Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572)

No anexo [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818) do cadastro de funcionários foram inseridos os eventos que devem ser considerados para o cálculo da margem consignável do empréstimo

Dica:

Caso tenha eventos a considerar para todos os funcionários , no menu Configurações | Parametrizador | Folha Normal | Eventos Crédito do Trabalhador, também poderá informar os eventos que irão compor a remuneração base para o cálculo da margem de desconto do empréstimo do crédito do trabalhador: [Eventos do Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311837)

Lançar o empréstimo do funcionário que foi importado o empréstimo via [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true) usando um arquivo CSV

No movimento do funcionário foi lançado o valor do empréstimo e a base usada para o cálculo

No Log será detalhado o cálculo considerando apenas os eventos do anexo Eventos Remuneração Crédito do Trabalhador do cadastro de funcionários e os descontos obrigatórios para a base consignável

## **03.****TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
