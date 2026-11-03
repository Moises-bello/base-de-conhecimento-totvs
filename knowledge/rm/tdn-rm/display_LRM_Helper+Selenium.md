---
content_hash: 1aece485847b6cd2fe3a7fd665a799741799d2dac4f9124a94c3023b5247e76c
fetched_at: '2026-06-29T00:11:39.203013+00:00'
page_id: '788603899'
product: rm
source: tdn-rm
title: Helper Selenium
type: documentation
url: https://tdn.totvs.com/display/LRM/Helper+Selenium
version: 4
---

## O que é?

O **Helper Selenium** foi criado na engine **Selenium** do **TestFlow** para facilitar a criação de testes automatizados. Ele fornece uma série de métodos úteis para instanciar e interagir com o WebDriver, além de manipular elementos da interface de maneira eficiente.

## Para que Serve?

O **Helper Selenium** no **TestFlow** serve para simplificar e automatizar a criação de testes utilizando o **Selenium WebDriver**. Ele oferece métodos pré-configurados para instanciar WebDrivers, interagir com elementos da interface, controlar o comportamento de páginas web e gerenciar o fluxo de testes.

## Exemplo de Uso

Modo de UsoComo Funciona

## Métodos do Helper Selenium e suas Funções

1. Instanciar o WebDriver

## Instanciar o WebDriver

* **Instanciar o WebDriver do Chrome com opções**:

  c#RDark
* **Instanciar o WebDriver do Chrome de um diretório específico**:

  c#RDark
* **Instanciar um WebDriver diferente do Chrome com opções (Exemplo: Firefox)**:

  c#RDark
* **Atualizar a largura e altura da janela do WebDriver**:

  c#RDark
2. Interação com a Interface

## Espera por Elementos

* **Esperar por um elemento usando `By` e um tempo em milissegundos**:

  c#RDark
* **Esperar por um elemento pelo ID**:

  c#RDark
* **Esperar utilizando uma função de expressão e o WebDriver**:

  c#RDark drv.FindElement(By.Id("botao")), 5000);]]>
* **Esperar até que o elemento seja clicável usando `ExpectedConditions`**:

  c#RDark

#### Outras Esperas por Condição e Tempo

* **Esperar até o elemento existir usando o ID e um tempo limite**:

  c#RDark
* **Esperar até o elemento ser clicável usando o ID e um tempo limite**:

  c#RDark
* **Esperar até o elemento existir usando `By`**:

  c#RDark
* **Esperar até o elemento ser clicável usando `By`**:

  c#RDark
* **Esperar até o elemento existir utilizando seletor CSS**:

  c#RDark
* **Esperar até o elemento ser clicável utilizando seletor CSS**:

  c#RDark
3. Interação com Elementos

## Interação com Elementos

* **Clicar em um elemento**:

  c#RDarkc#RDark
* **Navegar para uma URL**:

  + **Por string**:c#RDark
  + **Utilizando um objeto `Uri`**:c#RDark
* **Maximizar a janela do navegador**:

  c#RDark
* **Preencher um campo de texto**:

  c#RDarkc#RDark
4. Finalizar e Liberar Recursos

## Finalizar e Liberar Recursos

* **Encerrar o WebDriver e liberar recursos**:c#RDark
5. Utilização do WebDriver em Múltiplas Atividades

## Utilização do WebDriver em Múltiplas Atividades

* **Adicionar o WebDriver ao contexto do TestFlow**: Para reutilizar o WebDriver em outras atividades, adicione-o ao contexto:c#RDark
