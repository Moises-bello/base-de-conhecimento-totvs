---
content_hash: 5fc327edc01e2f99f308fedcb0f3ab8de6ce32287fc514786d0bbde445fdcc72
fetched_at: '2026-06-28T21:35:17.332161+00:00'
page_id: '1045013610'
product: fluig
source: tdn-fluig
title: Identity | API de validação de MFA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1045013610
version: 14
---

75%

5.\*ndice

50%

trueIdioma

Para validar o MFA de um usuário no TOTVS Identity, via API, basta realizar uma chamada para o endpoint **post /auth/v1/mfa/totp/validate**, passando o token do usuário logado e o código TOTP a ser validado no campo totp\_token.

A API irá retornar **204** quando o **código TOTP for válido.**

Em caso de **código TOTP inválido**, será retornado o **Response Code 400.**

YellowATENÇÃO Para prevenir incidentes, implementamos um limite de taxa (rate limit) de 5 requisições por minuto por endereço IP neste endpoint.

## Documentações relacionadas

---

* [Configuração de Políticas de Segurança](https://tdn.totvs.com/display/fluig/Identity)
* [Guia do Aplicativo My Safe ID](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Identity | Multi-Factor Authentication](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Fazer login com autenticação multifator (MFA)](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity|Login-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA))
* [Identity | Configuração e Uso do MFA por e-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=1048505459)
* [Identity | Validação do MFA desvinculado do Login](https://tdn.totvs.com/pages/viewpage.action?pageId=1048504602)
* [Identity | API de validação de MFA por E-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=1060219992)
