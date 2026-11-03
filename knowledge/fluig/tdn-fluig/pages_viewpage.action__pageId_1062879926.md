---
content_hash: 50c5d6a449e5adfa1c3fbff2041fee72c1a87fe725019f63e963298bb816968a
fetched_at: '2026-06-28T21:35:17.425469+00:00'
page_id: '1062879926'
product: fluig
source: tdn-fluig
title: Identity | Guia de Implementação e uso do WebAuthN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062879926
version: 34
---

# Falando de WebAuthn no Identity...

---

O **WebAuthn** (Web Authentication) é um padrão global de autenticação que permite o acesso a sistemas sem a necessidade de senhas tradicionais ou códigos de MFA (Multi-Factor Authentication) manuais. Ele utiliza criptografia de chave pública para delegar a autenticação a um hardware externo confiável (como biometria ou tokens de segurança).

## Visão Geral

---

O protocolo funciona através de uma troca de dados criptografados:

1. **Registro:** O usuário (já autenticado) registra uma **chave pública** no Identity (IDP), enquanto a **chave privada** permanece protegida no hardware (dispositivo do usuário).
2. **Autenticação:** O Identity envia um "desafio" (challenge) ao hardware. O hardware assina esse desafio com a chave privada e o devolve ao Identity. Se a descriptografia com a chave pública for bem-sucedida, o acesso é concedido.

Importante

O WebAuthn no Identity herda os **ACRs (Authentication Context Class Reference)** presentes no momento da criação da chave. Se um usuário criar a chave sem MFA e, posteriormente, a empresa exigir MFA, o usuário precisará gerar uma nova chave para refletir essa mudança de segurança.

## Pré-requisitos de Navegador

---

Para utilizar o WebAuthn,  o ambiente deve suportar nativamente o WebAuthn ou possuir integração com hardwares específicos (ex: **FIDO Tokens**) ou biometria de sistema operacional (**Windows Hello/TouchID**):

* **Google Chrome:** Suporte nativo simplificado (utiliza o PIN do gerenciador de senhas ou biometria do SO).
* **Mozilla Firefox:** Requer integração externa ou hardware específico.
* **Hardwares compatíveis:** Windows Hello, Apple FaceID/TouchID, ou tokens físicos.

## Fluxo de Uso no Identity (Interface)

---

O Identity disponibiliza uma camada de APIs exclusiva para o suporte ao protocolo WebAuthn. Para que o usuário final possa utilizar essa funcionalidade, é necessário seguir os passos de provisionamento abaixo

1. **Cadastro:** O usuário logado deve acessar a URL de criação: <https://app.fluigidentity.com/ui/user-settings>
2. **Login:** Na tela de autenticação, o usuário poderá selecionar a opção **"Entrar com Certificado".**

Atenção

O token WebAuthn armazena os ACRs do momento da sua criação. Mudanças em configurações de MFA não são retroativas para chaves já cadastradas, nesses casos, é imprescindível a recriação da chave pelo usuário.

## Fluxo de Integração via APIs (Swagger)

---

Abaixo estão descritos os endpoints necessários para os processos de registro e autenticação. A documentação completa pode ser consultada no Swagger em:

#f2f2f2

[https://app.fluigidentity.net/api/webauthn/doc/#](https://app.fluigidentity.net/api/webauthn/doc/)

Referência de APIs (Desenvolvedor)Fluxo de Registro (Criação de Chave)

Este fluxo deve ser executado com o usuário já autenticado no Identity.

1. **Iniciar Registro:** `GET /api/webauthn/options`

   Gera as opções de criação e o desafio (*challenge*) necessário para o hardware.
2. **Realizar o Cadastro:** `POST /api/webauthn/register/creation`

   Envia a resposta assinada pelo hardware para persistir a chave pública no Identity.
Fluxo de Autenticação (Login)

Este fluxo permite a obtenção de um token de acesso sem o uso de senhas.

**01. Iniciar Login:** `GET /api/webauthn/challenge`

#f2f2f2

Solicita um desafio de autenticação para o hardware do usuário.

**02. Validar Desafio:** `POST /api/webauthn/verify`

#f2f2f2

Valida a assinatura do hardware e, em caso de sucesso, retorna o `pre_auth_token`.

**03. Efetuar Login:** `POST /api/auth/v1/token`

#f2f2f2

Utiliza o `pre_auth_token` para gerar o `access_token` final.

**Parâmetros (Form Params):**

* + `grant_type`: `http://fluigidentity.com/api/login/webauthn`
  + `pre_auth_token`: [Valor obtido no passo anterior]
  + `domain`: [Domínio da empresa ou "app"]

Atenção

O **`pre_auth_token` é de uso único** (one-time use). A API realiza a invalidação automática do token imediatamente após o consumo, impedindo sua reutilização em qualquer etapa subsequente do processo de autenticação.

Gerenciamento

* **Busca:** `GET /api/webauthn/doc/#!/Creation_Options/search` (Retorna chaves apenas do usuário logado por segurança).
* **Exclusão:** `DELETE /api/webauthn/doc/#!/Creation_Options/delete`.
* **Atualização:** `PATCH /api/webauthn/doc/#!/Creation_Options/patch` (Permite alterar apenas o `nickname`).

## WebAuthn no Android

---

A implementação em Android possui restrições rigorosas de segurança do Sistema Operacional.

WebAuthn no AndroidPré-requisitos do Dispositivo:

* PIN de tela bloqueada cadastrado.
* Biometria cadastrada.
* Sistema autenticado com uma **Google Account** ativa.
Configuração de AssetLinks (Well-Known):

Para que o Android confie no aplicativo, a assinatura do app deve estar registrada no Identity:

* **Consulta:** `GET /.well-known/assetlinks.json` (ou via API `/api/webauthn/doc/#!/Well_Known_API/android`).

Estas APIs são expostas por meio de um **Behavior no AWS CloudFront**. Por questões de governança, o provisionamento de novos registros é restrito ao perfil de **SysAdmin**, devendo ser realizado através do endpoint:

* **Cadastro (SysAdmin):** Através da API `updateAndroidAssetLinks`.

Atenção

* O preenchimento deste registro deve ser realizado com extrema precisão. A propriedade **`applicationId` deve ser obrigatoriamente única,** a duplicidade deste identificador causará a sobrescrita de dados de outros aplicativos, resultando na interrupção do serviço de login (indisponibilidade).
* Os parâmetros técnicos devem ser validados previamente com o desenvolvedor do aplicativo.

## Fluxo Headless (Mobile/Accounts)

---

Destinado à comunicação do componente *Accounts* com o Identity para apps Mobile.

1. **Autorização:** Inicie o `/authorize` informando `acr_values=headless`.
2. **Request Code:** O sistema não redirecionará para o login, mas retornará um `request_code`.
3. **Token:** Após obter o `pre_auth_token` via fluxo WebAuthn normal, execute a chamada:

   * **Endpoint:** `/accounts/api/v2/token`
   * **Parâmetros:** \* `grant_type=urn:ietf:params:oauth:grant-type:webauthn`

     + `client_id=[ID_DO_CLIENT]`
     + `code=[request_code]`
     + `pre_auth_token=[preAuthToken]`

Sucesso

* Após o processamento bem-sucedido da requisição, o Identity retornará o objeto de autenticação padronizado pelo **OIDC (OpenID Connect)**, contendo os atributos `access_token`, `refresh_token` e `id_token`.
* Para fins de referência e estudo da implementação, o diretório `tools` disponibiliza um projeto Android exemplo com este fluxo completo.

## Ferramentas de Suporte

---

Para desenvolvedores, o Identity disponibiliza um projeto exemplo na pasta **"tools"** do código-fonte. Este projeto simula um app configurado em ambiente de QA, demonstrando tanto o fluxo padrão quanto o Headless.

## Modo de Uso

---

Para utilizar o WebauthN no seu dia a dia utilize a seguinte Documentação:
