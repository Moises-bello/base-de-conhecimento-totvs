---
content_hash: 5aea4d34d329d1a1901b4055d54bc251cb8687a7e0a35439f225c740f6bbcb01
fetched_at: '2026-06-29T00:12:14.053948+00:00'
page_id: '963025862'
product: rm
source: tdn-rm
title: eSocial do empréstimo Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963025862
version: 14
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a eSocial.

## **02. EXEMPLO DE UTILIZAÇÃO**

Na geração do XML dos eventos **S-1200, S-2299 ou S-2399**, o sistema validará a existência da Modalidade de Empréstimo "**Crédito do Trabalhador eSocial**" para a correta geração da tag **`<descFolha>`**.

### 

Aviso

Caso exista um evento com a natureza de rubrica **"9253 - Empréstimos eConsignado - Desconto"** no envelope do funcionário, para à competência em que está sendo gerado um dos seguintes eventos: **S-1200, S-2299 ou S-2399**, e não exista um empréstimo cadastrado para esse evento ou o campo "Comp final Desc" esteja preenchido com zero (0), o sistema apresentará a seguinte mensagem de erro:

O usuário deverá acessar o menu Funcionários | Anexos | Folha de Pagamento | Empréstimo e preencher as informações do empréstimo **"Crédito do Trabalhador eSocial"**, conforme demonstrado na tela abaixo:

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT

## **04.** **DOCUMENTAÇÃO**
