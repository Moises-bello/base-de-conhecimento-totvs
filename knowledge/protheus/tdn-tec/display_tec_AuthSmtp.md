---
content_hash: ae283322f58c181ca80b46ad6ccba352da0b2be76a9e19d614c0c3b0210856f5
fetched_at: '2026-07-02T19:24:28.791627+00:00'
page_id: '856947869'
product: protheus
source: tdn-tec
title: AuthSmtp
type: documentation
url: https://tdn.totvs.com/display/tec/AuthSmtp
version: 4
---

AuthSmtp

Permite indicar que a autenticação dos usuários de e-mail será realizado por um servidor POP. Essa configuração pode ser necessária conforme necessidades definidas pelo servidor de e-mail utilizado.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| POP3 | Ativa a autenticação dos usuários de e-mail através de servidor POP |

## Observações

* Quando do uso desta configuração é necessário realizar a configuração do servidor POP através da chaves  e .
* Quando essa configuração **não** está configurada a autenticação dos usuários de e-mail é realizada através do servidor **SMTP** através das chaves ,  e .
* Essa configuração também pode ser ativada através do método  da classe .

## Exemplos

Eclipsefalse

## Abrangência

A partir da build **20.3.1.0**
