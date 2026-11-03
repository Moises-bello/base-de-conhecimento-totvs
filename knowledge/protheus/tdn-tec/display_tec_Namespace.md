---
content_hash: d3b1278e44b5063e612ece8d3c3233140f3a0ffa6db82ed06ed9087f01cf3b8b
fetched_at: '2026-07-02T19:24:21.268908+00:00'
page_id: '265783950'
product: protheus
source: tdn-tec
title: Namespace
type: documentation
url: https://tdn.totvs.com/display/tec/Namespace
version: 17
---

### trueGreentlpp - language

O recurso de *namespace* foi liberado na versão 17.3.0.0 para a linguagem true e tem como benefício a melhor organização do código.

Observações

* O nome do *namespace* pode ser um nome simples ou um nome que contenha "." como separador
* Importante ressaltar que todo nome de *namespace* iniciado com "tlpp." está reservado ao tlppCore. Desse modo, qualquer tentativa de uso fora desse domínio, será bloqueada em tempo de compilação.
* Uma vez utilizado o recurso *namespace* no 'main' da sua aplicação,  é necessário que o explicite utilizando o separador "."

Exemplo: -p  em vez de -p 

Os namespaces iniciados por: "**tlpp**" e ou "**core**", são reservados para funções específicas da linguagem, sendo vetados para uso fora do ambiente da **TOTVS** ou para funções de usuário !

Classes em true que herdam de classe com *namespace* precisam utilizar o *namespace* na declaração da classe ou utilizar o *namespace* no programa que executa a chamada da classe.

## Funções dentro de namespace:

### Exemplo:

exemplo1.tlpptrue

Para chamar uma função que está declarada dentro de um namespace de um outro fonte é necessário que o explicite, o separador utilizado para isso é o "." conforme exemplo a seguir:

exemplo2.tlpptrue

Outra opção para chamar uma função que está declarada dentro de um namespace é utilizar a instrução "using namespace" conforme o exemplo a seguir:

exemplo3.tlpptrue

## Classes dentro de namespace:

### Exemplo:

exemplo4.tlpptrue

Para utilizar uma classe que está declarada dentro de um namespace de um outro fonte é necessário que o explicite, o separador utilizado para isso é o "." conforme exemplo a seguir:

exemplo5.tlpptrue

Outra opção para utilizar uma classe que está declarada dentro de um namespace de um outro fonte  é utilizar a instrução "using namespace" conforme o exemplo a seguir:

exemplo6.tlpptrue
