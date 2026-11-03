---
content_hash: 1e0d712e1099d9a09b79848f7a35d159c560b903b3d5eba9400ade3ebc151c4d
fetched_at: '2026-06-29T00:12:14.040901+00:00'
page_id: '963025529'
product: rm
source: tdn-rm
title: Cálculo da Rescisão considerando Eventos do Crédito Trabalhador no parametrizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963025529
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo da Rescisão considerando Eventos do Crédito Trabalhador no parametrizador.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

* PARÃMETRO DESMARCADO COM EVENTOS INFORMADOS - Serão considerados APENAS eventos informados no Anexo ou Parametrizador para Remuneração Créd.Trabalhador

Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572)

No parametrizador [Eventos do Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311837) foram inseridos os eventos que devem ser considerados para o cálculo da margem consignável do empréstimo para todos os funcionários

Dica:

Caso tenha eventos a considerar exclusivamente para um funcionário, poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando o anexo [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818).

No cadastro de empréstimo está cadastrado

Lançando o empréstimo na rescisão

A margem consignável foi calculada considerando:

01 - Eventos cadastrados no parametrizador anteriormente

02 - Valores de INSS e IRRF calculados na rescisão

IMPORTANTE:

Veja que o valor do IRRF FÉRIAS também foi considerado porque deverá considerar todos os eventos de INSS e IRRF lançados no período do cálculo onde está descontando o empréstimo

03 - Sobre o valor total da remuneração será calculado o percentual para margem consignável cadastrado no cadastro de empréstimo para verificar se desconta o valor integral do empréstimo.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
