---
content_hash: 27066cac979e78528327a70f6f2d1f206589e254e3c7980a22e9cff3b94192fb
fetched_at: '2026-07-02T19:24:27.045387+00:00'
page_id: '655864407'
product: protheus
source: tdn-tec
title: b - Modos de execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655864407
version: 3
---

O **PROBAT** possui uma Main Function exclusiva para a execução dos testes, sendo:

***TLPP.PROBAT.RUN()***

A função *RUN* retorna o código de execução de controle interno no formato [character].

Ela permite que você possa enviar através de parâmetros, instruções de modo de execução dos Testes

Abaixo seguem as opções permitidas

## **Todos testes**

Esse modo é útil para executar todos os testes e verificar se após alguma implementação a BUILD permanece 100% funcional.

c#

```
ou simplesmente:
```

c#
> Ao não passar parâmetro algum, o **PROBAT** assume automaticamente o type:all

## **Testes de determinada namespace**

Talvez seja necessário executar parcialmente os testes e para isso temos a opção de filtrar a execução através da namespace usada no fonte de teste.

Seguem alguns exemplos:

Somente uma namespace: string

c#

Mais de uma namespace: date e math

c#

```
Namespace longa:
```

c#

## **Testes de determinado código-fonte**

Poderemos também filtrar a execução através dos fontes de teste.

Esse modo é útil para ser rápida a execução quando estivermos desenvolvendo ou encontrando o erro em determinado teste.

Somente um fonte: test\_maximum.tlpp

c#

```
Mais de um código-fonte: test_maximum.tlpp e test_minimum.tlpp
```

c#

## **Testes com erro**

Após a execução de testes em modo ALL, erros podem ocorrer em um ou mais testes e com isso teremos a necessidade de corrigi-los.

Portanto, temos a opção para executar somente os testes com erro para facilitar o trabalho.

c#

```
ou
```

c#

```

```

Esse modo de execução só será possível quando existir no histórico do **PROBAT** alguma execução em modo ALL e que possua erros, caso contrário ele não encontrará testes elegíveis para execução.

## **Testes de Suítes específicas**

O **PROBAT** permite que possam ser criadas SUITES de testes e portanto temos a necessidade de executar somente os testes que pertençam a determinada SUITE.

Veja mais detalhes em como criar suítes customizadas em: ()

Somente uma suíte: sistemico

c#

```

```
