---
content_hash: 76b2c1c79a48caec690bdf43bb0babcbd1f5073aadc9d3a8c19c46b4602c6e57
fetched_at: '2026-06-28T21:35:24.672866+00:00'
page_id: '271180031'
product: fluig
source: tdn-fluig
title: Integrando widget com serviços JSON externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271180031
version: 7
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desse guia é apresentar a integração de *widgets* com serviços JSON de outras fontes de dados, que estão fora do domínio do servidor Fluig. Utilizaremos a técnica de *Json Padding* - JSONP - para obtermos dados de terceiros com uma função de *callback*.

# Problema

Se você chegou aqui é porque provavelmente estava desenvolvendo um *widget* e se deparou com uma mensagem similar a apresentada abaixo:

Páginas *web* comuns podem utilizar o objeto [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) para enviar e receber dados de servidores remotos, porém as ações que essas páginas poderão realizar são limitadas pela [política de mesma origem](https://en.wikipedia.org/wiki/Same-origin_policy) (*same-origin policy*).

Este é um conceito muito importante no modelo de segurança dos navegadores atuais, pois define que *scripts* de uma página "A" somente podem acessar dados de uma página "B" **se ambas possuírem a mesma origem**. A origem de uma página é definida pelo seu protocolo, endereço e porta.

Felizmente, nem tudo é afetado pela *same-origin policy*. Por exemplo, é possível carregar uma imagem externa ou um *script* de um domínio diferente da página atual. Entretanto, isso ainda não é o suficiente quando precisa-se obter dados JSON e exibi-los em um *widget* na plataforma Fluig.

# JSONP pode ser a solução

 [JSONP](https://en.wikipedia.org/wiki/JSONP) (*JSON with Padding*) é uma técnica que disponibiliza uma forma de acessar os dados JSON que precisamos. Isto é feito através do empacotamento dos dados em uma função de *callback* (o "*padding*") que será interpretada pelo navegador em JavaScript. Esta função precisa ser definida no *widget* que receberá o retorno JSONP.

# Exemplo

Veja abaixo um exemplo de uma chamada JSONP a um serviço fictício de terceiros:

js
