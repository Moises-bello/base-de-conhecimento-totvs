---
content_hash: 3b97fa1b7f8f0f044896450f155074cc05c0087738a72bac2840c1f2c94ceb47
fetched_at: '2026-06-28T21:35:24.962274+00:00'
page_id: '273295605'
product: fluig
source: tdn-fluig
title: IDE - Configuração de autenticação com o Identity via API
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273295605
version: 12
---

# Índice

trueÍndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5.11 ou superior

**Tipo de API:** WCMAdminTenantRest

# Ocorrência

Como realizar a configuração de autenticação do TOTVS Fluig Plataforma com o TOTVS Identity através da API Pública?

# Solução

É possível realizar a integração do Identity com a plataforma através da API Pública.

**1.** O primeiro passo, é autenticar-se na plataforma com um usuário administrador (pode ser wcmadmin).

**2.** Em seguida, deve-se chamar o *endpoint* [[URL fluig]/api/public/admin/tenant/identityConfig/v2](https://api.fluig.com/resource_WCMAdminTenantRest.html#resource_WCMAdminTenantRest_setIdentityConfigurationV2_POST)**.**

**3.** O método que deve ser utilizado é do tipo POST e os parâmetros a serem informados são:

| name | type | description | constraints |
| --- | --- | --- | --- |
| configurationToken | query | identity application configuration token (Ex: "NDI6Om4zbTQxMG52MHkyNXd5cmExNDE2OTQ1MjE0OTM3"). |  |
| enableIdentity | query | ('true' to enable / 'false' to disable). Default: false. | boolean |
| identityUrl | query | Identity Base URL |  |
| useJustInTimeProvisioning | query | to provisioning users (true / false). Default: false. | boolean |

Estes parâmetros podem ser obtidos nas configurações do aplicativo "Fluig" no Identity.

Para realizar a configuração utilizando o wcmadmin é necessário que seja informado também o código da empresa e o ID da empresa.

| name | type | description |
| --- | --- | --- |
| ``` tenantId ``` | query | Identificador da empresa |
| tenantCode | query | Código da empresa. |

Estes parâmetros podem ser obtidos nas configurações da própria empresa na plataforma Fluig.

Exemplo de requisição usando administrador de empresa:

xmlRequesttrue

Exemplo de requisição usando wcmadmin:

xmlRequesttrue

O retorno é um application/json:

jsRetorno de ativação da integraçãotrue

ou

jsRetorno de desativação da integraçãotrue

As alterações serão aplicadas imediatamente, não sendo necessário reiniciar o servidor.
