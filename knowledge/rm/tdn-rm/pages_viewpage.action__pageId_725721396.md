---
content_hash: 187892103ce44df964cf3bebb9fac4240ea14c519db90f066acb5750b3abf880
fetched_at: '2026-06-29T00:11:27.433815+00:00'
page_id: '725721396'
product: rm
source: tdn-rm
title: Insere Código de Barras (EAN128/DataMatrix), Lote e Número de Série do produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=725721396
version: 27
---

Atenção

Recurso disponível na release 12.1.2302 ou superior.

## **CONTEÚDO**

1. **Visão Geral**
2. **Parametrização**
3. **Premissas**
4. **Exemplo de utilização**
5. **Informativos**

## **01. VISÃO GERAL**

Neste recurso será possível inserir Código de Barras (EAN 128 e DataMatrix), Lote e Número de Série no cadastro do produto, a partir da leitura do código de barras na tela do item do movimento ou na edição do item do movimento.

## **02. PARAMETRIZAÇÃO**

São necessárias as seguintes parametrizações para realizar a operação:

Tipo de Movimento

* Na etapa **Item - Lote/Grade/Num. Série** informar que movimento **Consiste Lote** em sequência defina um **Status Default do Lote de Produto para Código de Barras.**

Parâmetros

* Na etapa **Parâmetros** **Gerais / Tabelas / Lote**
  + Desmarque a opção Gera Número de Lote Sequencial.
  + O campo **Usar Código** **EAN** tem que ser diferente de **Não Usa**.

## **03. PREMISSAS**

Caso o cadastro de Produto utilize Número de Série é necessário que a Máscara do Número de Série do produto selecionado esteja compatível com o tamanho do Número de Série.

Além disso, o campo Data de Entrada do Lote será informado baseado no campo Data de Entrada (TMOV.DATASAIDA) informado no Cabeçalho do Movimento.

## **04. EXEMPLO DE UTILIZAÇÃO**

No momento da inclusão de um movimento, oriundo de um faturamento ou pela inclusão manual, deverá ser selecionado o item do movimento que se deseja inserir o código de barras e clicar no ícone , realizar a leitura do código de barras e clicar no botão Inserir, conforme telas abaixo:

Tela item do movimento

Tela edição do item do movimento

Tela de leitura do código de barras

Neste momento será inserido o lote, número de série e o código de barras nos respectivos cadastros automaticamente. 

Dando sequência no lançamento do movimento, deverá ser selecionado na visão do lote e/ou número de série no item do movimento os registros incluídos para vincular o Lote e/ou o Número de Série do Produto.

## **05.** **INFORMATIVOS:**

Caso o alerta abaixo apareça é necessário corrigir o Número do Lote e/ou Número de Série manualmente no seus respectivos cadastros.

Importante

Para utilização desta funcionalidade o usuário deverá ter acesso para cadastrar Número de Série, Lote e Código de Barras do Produto.

Documentos Relacionados
