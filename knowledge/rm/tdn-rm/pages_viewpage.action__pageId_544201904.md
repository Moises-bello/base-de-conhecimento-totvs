---
content_hash: 285dd9c1f19a86e7aed64f0bba82530e3aaae3d59408718be8264555f3e869f4
fetched_at: '2026-06-29T00:10:38.215395+00:00'
page_id: '544201904'
product: rm
source: tdn-rm
title: Autenticação usando um aplicativo Provedor Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544201904
version: 3
---

## **Autenticação com Provedor Externo**

---

**REQUISITO:**

* Para autenticar utilizando um provedor externo é necessário primeiro fazer o cadastro do mesmo em . Disponibilizado a partir da versão 12.1.28.

**COMO FUNCIONA:**

* Pelo endpoint **http(s)://{dominio}:{porta}/api/connect/external-token?providerId=<identificador do provedor>** será enviado o access token gerado pelo provedor do aplicativo externo, como por exemplo o facebook, e retornará um access token válido para autenticação no RM.

**COMO UTILIZAR**

**Exemplo de utilização - Sucesso:**

Realize uma requisição http ao endpoint **http(s)://{dominio}:{porta}/api/connect/external-token?providerId=<identificador do provedor>.**

Na requisição deve-se utilizar o método **POST**.

O **identificador do provedor**é o campo 'ID' presente na tela de cadastro de Provedores Externos.

No corpo da requisição utilize no body o access\_token gerado pelo provedor externo:

• access\_token

Informações de login e senha no corpo da requisição:

O token de segurança será gerado e já poderá ser utilizado no cabeçalho das requisições subsequentes às APIs disponibilizadas pela Totvs.

A resposta da requisição tem o padrão Outh contendo o token, tipo e espiração do token gerado. O token é um JWT no padrão RM.

Token de Segurança gerado com sucesso e pronto para ser utilizado:

Utilize o token gerado incluindo-o no cabeçalho da requisição através da diretiva:

**• Authorization: Bearer {token}**

Inclusão do token no cabeçalho da requisição:
