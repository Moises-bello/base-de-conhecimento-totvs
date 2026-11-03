---
content_hash: 36b89ea765dcdb59ba4c6559f449ccf7dd2c449ada70c8cdf70e8844b5bf1da4
fetched_at: '2026-06-28T21:35:29.949910+00:00'
page_id: '778541252'
product: fluig
source: tdn-fluig
title: Lidando com Objetos (Object) no Rhino
type: documentation
url: https://tdn.totvs.com/display/fluig/Lidando+com+Objetos+%28Object%29+no+Rhino
version: 8
---

false

Esta página não tem como objetivo ser um guia de como programar com Rhino ou mesmo como um "aprenda a programar", mas sim para listar algumas características interessantes que serão referenciadas em outros pontos da documentação. Se você ainda não tem experiência com o desenvolvimento no Rhino, recomendamos que deixe essa documentação para o futuro.

Nas personalizações é normal que uma função retorne um objeto com dados de retorno. Cada função tem um retorno diferente, podendo ser número, uma string, uma lista, um mapa ou um objeto.

No caso dos objetos, é feito uma conversão do objeto Java para javascript, o que permite que seus atributos possam ser acessados tanto diretamente quanto pelas funções get como é feito no java.  Recomendamos usar sempre da forma nativa de acesso direto ao atributo por deixar o código mais legível, exceto quando a documentação explicitamente recomendar o uso no formato java.

Como exemplo, supomos que o retorno de uma função seja o objeto Example, que tenha os atributos id e name:

javaEstrutura do objeto java de exemplotrue

## Exemplo da flexibilidade do objeto:

Este é apenas um exemplo, não deve ser usado dessa forma por questões de legibilidade de código

jstrue

## Utilização na forma nativa:

jstrue

## Utilização na forma Java:

jstrue
