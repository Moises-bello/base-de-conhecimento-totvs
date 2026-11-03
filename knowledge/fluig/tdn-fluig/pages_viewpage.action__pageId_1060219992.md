---
content_hash: de0dc498aa263f857f287a6e87b6106d3d2b1e6299486dc56ff4683afa7dba45
fetched_at: '2026-06-28T21:35:17.413201+00:00'
page_id: '1060219992'
product: fluig
source: tdn-fluig
title: Identity | API de validação de MFA por E-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060219992
version: 19
---

# Falando de API de validação de MFA por E-mail...

---

Esta documentação descreve os procedimentos para o envio e a validação do código de Autenticação Multifator (MFA) via e-mail utilizando as APIs do TOTVS Identity.

ProcedimentosEnvio do Código MFA por E-mail

Para iniciar o processo, é necessário solicitar o envio do código de autenticação para o e-mail cadastrado do usuário.

* **Endpoint:**

  js
* **Descrição:** Realiza o envio de um código TOTP (Time-based One-Time Password) de **6 dígitos** para o e-mail do usuário.
* **Regras de Negócio:**

  + O código enviado possui validade de **10 minutos**.
  + **HTTP Status 202:** Indica que a solicitação de envio foi aceita com sucesso.

**Request no endpoint de /sendTOTPKeyToEmail**

**Código enviado para o e-mail após o request**

Validação do Código MFA

Após o recebimento do código pelo usuário, a aplicação deve realizar a validação para concluir a autenticação.

* **Endpoint:** `POST /auth/v1/mfa/totp/validate`
* **Parâmetros de Cabeçalho (Header):**

  + `Authorization: Bearer {token}`: Token do usuário logado.
* **Parâmetros de Corpo (form-data):**

  + `totp_token`: O código de 6 dígitos recebido por e-mail.
* **Respostas da API:**

  + **HTTP Status 204/200:** O código TOTP é válido e a autenticação foi concluída.
  + **HTTP Status 401:** Acesso não autorizado ou token inválido.
  + **Erro (Exemplo IDM\_MFA\_0004):** O código TOTP já foi utilizado ou é inválido. Cada código pode ser utilizado apenas uma vez.

Segurança e Rate LimitAtenção

Como medida de prevenção contra incidentes e ataques de força bruta, foi implementada uma política de limite de requisições:

* **Rate Limit:** Máximo de **5 requisições por minuto** por endereço IP para este endpoint.

## Documentações relacionadas

---

* [Identity | Segurança](https://tdn.totvs.com/pages/viewpage.action?pageId=273980166)
* [Guia do Aplicativo My Safe ID](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Identity | Multi-Factor Authentication](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Fazer login com autenticação multifator (MFA)](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity|Login-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA))
* [Identity | Configuração e Uso do MFA por e-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=1048505459)
* [Identity | Validação do MFA desvinculado do Login](https://tdn.totvs.com/pages/viewpage.action?pageId=1048504602)
* Identity | API de validação de MFA
