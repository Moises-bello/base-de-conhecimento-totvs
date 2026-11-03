---
content_hash: 21410c4eae0f8106fa18cbf56549337d76dedbe9bd1c6f063d355d68bf0b94a7
fetched_at: '2026-06-28T21:35:17.373811+00:00'
page_id: '1050883278'
product: fluig
source: tdn-fluig
title: Identity | Especificação Técnica de ACRs e AMRs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050883278
version: 6
---

## **Falando de ACRs e AMRs...**

---

Esta documentação detalha a implementação e o uso de **Contextos de Autenticação** no Identity, abrangendo os protocolos OIDC e SAML.

Os **ACRs (Authentication Context Class Reference)** são um conjunto de identificadores (URNs) emitidos pelo Provedor de Identidade para indicar quais processos e níveis de segurança foram aplicados durante a autenticação de um usuário.

### Diferença entre ACR e AMR

* **ACR (Solicitação e Contexto):** Definidos pelo Provedor de Identidade. São utilizados pela aplicação cliente para **solicitar** um nível de segurança específico.
* **AMR (Informativo):** Baseados na [RFC 8176](https://datatracker.ietf.org/doc/html/rfc8176). São valores **informativos** que detalham os métodos exatos utilizados (ex: senha, otp). Servem para validação pós-autenticação pelo provedor de serviço.

## **Origem e Evolução (SAML vs OIDC)**

---

Embora amplamente usados no OIDC, os ACRs originaram-se no protocolo SAML através das tags `AuthnContextClassRef`.

* **AuthnContextClassRef (REF):** Uma URN com um valor chave (ex: `iam:mfa`). É o padrão utilizado para manter compatibilidade entre OIDC e SAML no Identity.
* **AuthnContextClassDecl (DECL):** Um link navegável com a documentação completa do processo. **Nota:** O modelo DECL não é utilizado atualmente pelo Identity para garantir simplicidade na migração entre protocolos.

## **Catálogo de ACRs disponíveis no Identity**

---

O Identity emite ACRs específicos baseados no fluxo de login realizado:

### Autenticação e MFA

* `iam:mfa`: Usuário passou por qualquer processo de MFA em backend (exceto Captcha).
* `iam:mfa:totp`: Uso específico de MFA via aplicativo (TOTP).
* `iam:login:password`: Validação de senha orquestrada diretamente pelo Identity.

### Provedores Externos e Integrações

* `iam:login:ad`: Autenticação via Active Directory (qualquer versão).
* `iam:login:ad:v{versao}`: Versão específica do SmartSync (ex: `iam:login:ad:v5.0.0`). Versões anteriores a 5 são reportadas como `4.0.0`.
* `iam:login:social`: Login social. Se for Google, Facebook ou LinkedIn, o valor é concatenado (ex: `iam:login:social:google`).
* `iam:login:azure`: Integração com Microsoft Entra ID.
* `iam:login:desktopsso`: Autenticação via Desktop SSO.
* `iam:login:cas`: Autenticação via protocolo CAS.
* `iam:login:client`: Autenticação via ClientCredential (versões legadas/SDKs/API rest).

### Políticas e Termos

* `iam:policy:pwd:{nível}`: Força da política de senha da empresa (`verylow`, `low`, `medium`, `strong`, `verystrong`). Se for a padrão, adiciona-se `:default`.
* `iam:policy:acceptance`: O usuário aceitou os termos de uso.

## **Catálogo de AMRs disponíveis**

---

Atualmente, o Identity emite três valores de AMR:

1. `pwd`: Uso de senha do provedor.
2. `mfa`: Processo de Multi-Fator de Autenticação concluído.
3. `wia`: Uso de Windows Integrated Authentication (DesktopSSO).

> **Onde consultar:** Os valores aparecem nos arrays `acr_values` e `amr_values` através da API de consulta `/me`.

## **Integração com Produtos**

---

### Accounts (OIDC v2)

* **Configuração:** Pode-se definir um ACR padrão no Client (`default_acr_values`) ou solicitar via API `/authorize` no parâmetro `acr_values`.
* **Comportamento:** Se `iam:mfa:totp` for solicitado e o usuário não tiver MFA, o sistema exigirá o cadastro no ato. Se o ACR solicitado faltar no token final, um erro de autenticação será gerado.
* **Leitura:** Disponível no `IDToken` ou no endpoint `/userinfo`.

### SAML

* **Resposta:** Enviada na tag `AuthnStatement`. Inclui por padrão `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport` para retrocompatibilidade.
* **Solicitação:** Via tag `RequestedAuthnContext` no `SAMLRequest`.
* **Importante:** O Identity trata todas as comparações SAML como do tipo **minimum**, ignorando as hierarquias *exact*, *maximum* ou *better*.
