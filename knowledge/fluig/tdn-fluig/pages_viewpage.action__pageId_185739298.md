---
content_hash: 857d814d8da7ce3ad2887e219ea5b0e76b22fc2234db0e0bbeb1de2748f6d3bb
fetched_at: '2026-06-28T21:35:18.811693+00:00'
page_id: '185739298'
product: fluig
source: tdn-fluig
title: Chamada de métodos síncrona vs. assíncrona
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739298
version: 10
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desse guia é apresentar as características das chamadas de métodos síncrona e assíncrona.

# Chamada de métodos síncrona vs. assíncrona

Sempre que se efetua uma integração por chamada REST/Ajax é possível configurá-la para que o *widget* aguarde ou não o término do processamento no servidor. Salvo quando existe a real necessidade de se esperar pelo retorno da chamada, é recomendado que sempre se faça a integração de forma assíncrona. Abaixo são apresentados dois exemplos de chamada remota - uma para Ajax e outra para REST:

## Ajax

js

Onde:

| Elemento | Descrição |
| --- | --- |
| **async:** | Determina que a chamada seja feita de forma assíncrona *(true)* ou síncrona *(false).* |
| **success:** | Código a ser executado quando a função retorna com sucesso. |
| **error:** | Código que tratará eventuais erros no processamento remoto. |

## REST

js

Onde:

| Elemento | Descrição |
| --- | --- |
| **async:** | Determina que a chamada seja feita de forma assíncrona *(true)* ou síncrona *(false).* |
| **success:** | Código a ser executado quando a função retorna com sucesso. |
| **fail:** | Código que tratará eventuais erros no processamento remoto. |

## Componente visual para chamadas assíncronas

Muitas vezes a execução remota de um código demora muito tempo, deixando o usuário com dúvidas sobre o sucesso ou falha do comando enviado ao servidor. Pensando nisso, a plataforma Fluig disponibilizou uma forma para que haja um elemento que visualmente indique que algo está sendo processado. A documentação completa a respeito de sua utilização pode ser encontrada [aqui](http://style.fluig.com/javascript.html#fluig-loading).
