---
content_hash: 940f30709193806491127aa6531cd0e1b4570ddc9d3b76b241b09804a30dd5d4
fetched_at: '2026-06-29T00:11:13.370237+00:00'
page_id: '659909935'
product: rm
source: tdn-rm
title: Preencher Lote e Número de Série automaticamente por Código de barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=659909935
version: 4
---

Importante

Recurso disponível na release 12.1.2205 ou superior.

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastro de Código de Barras**
3. **Parametrização do Tipo de Movimento**
4. **Movimento**

## **01. VISÃO GERAL**

No TOTVS Gestão de Estoque, Compras e Faturamento é possível realizar a inclusão automática de um lote ou Número de Série vinculado a um Código de Barras de produto.  Para realizar essa opção, siga os passos abaixo.

## **02. CADASTRO DE CÓDIGO DE BARRAS**

Para utilizar esse recurso, o cadastro de Código de Barras deve estar com as informações de Lote e/ou Número de Série preenchidas.

Importante

Para mais informações sobre o cadastro de Código de Barras verifique o Documento de Referência de 

## **03. PARAMETRIZAÇÃO DO TIPO DE MOVIMENTO**

São necessárias a seguintes parametrizações no Tipo de Movimento para realizar corretamente a operação:

* Na etapa **Item - Identificação** informar o **Código do Produto** como **Código EAN**

* Na etapa **Item - Lote / Grade Numerada / Número de Série**:
  + Caso se queira utilizar Número de Série é necessário marcar a opção **Aceita Número de Série**
  + Caso se queira utilizar Lote é necessário marcar a opção **Consiste Lote** ou **Carrega Lotes Mais Antigos**

## **04. MOVIMENTO**

Após parametrizado, é possível realizar essa inclusão automática de duas maneiras:

* **Visão de Itens de Movimento:**

Na visão de itens de movimento, basta informar o código de barras pelo botão **Insere Itens pelo Código EAN**

* **Edição de item de Movimento**

Na tela de edição basta buscar o produto pelo Código de Barras no campo de Produto. Para a busca automática do Lote também é necessário informar o campo Quantidade já que o cadastro de lote precisa dessa informação para ser preenchido corretamente. 

Após utilizar um desses dois métodos, o sistema irá buscar o Lote e/ou Número de Série inseridos no cadastro do Código de Barras informado. 

Documentos Relacionados
