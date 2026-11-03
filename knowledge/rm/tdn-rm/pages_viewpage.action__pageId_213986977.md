---
content_hash: 6b04eb1ecf4e6ca2ffab6e073a75fde9718f6d354f8ac0feca7cefe196aff541
fetched_at: '2026-06-29T00:06:17.936030+00:00'
page_id: '213986977'
product: rm
source: tdn-rm
title: Informações Técnicas da Action
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=213986977
version: 27
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Para utilizar essa funcionalidade, basta abrir uma visão do sistema e pressionar as teclas **Ctrl + Alt + F9**.

       Veja o exemplo abaixo onde utilizamos a visão de Funcionários:

## **02. EXEMPLO DE UTILIZAÇÃO**

Nesta tela é possível encontrar o detalhamento dos dados da visão:

* Localize **a action** utilizada pela visão:

* Localize **a tag** de segurança da action:

* Localize **o DataServer** utilizado:

* **As informações** do carregamento da visão serão exibidas no sumário:

* **ServerDatabaseOperations**: Quantidade de queries executadas no banco para concluir a operação;
* **FormShown**: Tempo total gasto desde a criação do form até a sua exibição na tela. Normalmente é o mais longo de todos [hh:mm:ss];
* **FopFuncionarioFormView**.**ctor():** Tempo gasto pelo construtor do form;
* **InternalReadViewClient**: Tempo total gasto no CLIENT para a operação ReadView (trazer os registros para a grid);
* **InternalReadViewSchemaClient**: Tempo gasto no CLIENT para se ler o Schema do DataSet e criar as colunas tipadas da grid;
* **ReadViewDataClient**: Tempo gasto na chamada wcf a partir do cliente para receber os dados do server que serão mostrados na grid;
* **NetworkDelayReadView**: Diferença de tempo entre o InternalreadviewClient e InternalReadViewServer;
* **InternalReadViewServer**: Tempo gasto no server para se criar o dataset a ser enviado para o cliente com os dados da grid;
* **Registros**: Quantidade de registros exibidos na visão;
* **Tamanho** **Dados**:Tamanho do dataset em bytes.

* Na **aba Dados** é possível visualizar os registros da visão:

* Na aba Dados é possível visualizar **o detalhe dos campos** da visão:

false

**Versão:** 11.82.XX ou 12.01.XX
