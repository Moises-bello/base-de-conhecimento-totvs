---
content_hash: e8d879c0ff61da852e8b48dc73c81065db0e38a43f33edb8e6c22c47b48a92c7
fetched_at: '2026-06-28T21:35:31.251264+00:00'
page_id: '910677890'
product: fluig
source: tdn-fluig
title: Identity | Aplicativos RM Empresa e Papeis - API Identity
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Aplicativos+RM+Empresa+e+Papeis+-+API+Identity
version: 4
---

## Autenticação

---

Para autenticação e obtenção do token de acesso, siga o procedimento descrito abaixo:

1. **Obtenção do OAuth Client Assertion:**

* Acesse o seguinte endpoint:  
  <https://app.customerfi.com/rest/swagger-ui/index.html#!/oauth2/getOAuthClientAssertion_get_6>`GET   
  /rest/v2/oauth2/clients/{clientId}/assertion`
* Informe o `clientID`correspondente à empresa. Pode ser obtido no painel de Configurações > Segurança > Token REST API
* Utilize o resultado para obtenção do `assertion`.

2. **Geração do Access Token:**

* Utilize o seguinte endpoint:  
  <https://app.customerfi.com/rest/swagger-ui/index.html#!/oauth2/getToken_post_0>`POST  
  /rest/v2/oauth2/auth`
* Com o `assertion`obtido no passo anterior, gere o `access_token`.

O `access_token`deverá ser informado no campo `app_key`antes de realizar as consultas seguintes:

## APIs Úteis

---

O `companyId`utilizado na maioria das APIs pode ser obtido através de consulta no painel do Identity Configurações > Segurança > Token REST API 

### **Lista todos os Usuários**

`GET   
/rest/v2/companies/{companyId}/users`

* Podendo ser informado o PageSize ou offset para necessidade de paginação.

### Lista todos os Aplicativos

`GET   
/rest/v2/companies/{companyId}/apps`

### Listar todas as Roles ou Empresas associadas a um Aplicativo de ERP

`GET   
/rest/v2/scim/v2/extensions/Resources/Companies/{companyId}/Applications/{appId}`

* Podendo ser informado o `resourceTypes`como `Role`ou `Company`se precisar retornar todos os registros de Papeis e Empresa, respectivamente.

## Gerenciamento de Recursos dos Aplicativos

---

As APIs responsáveis pela manipulação de recursos dos aplicativos estão documentadas no seguinte endpoint:

<https://app.customerfi.com/rest/swagger-ui/index.html#!/scim>

### Consulta de Papeis e Empresas de um Aplicativo (RM ou Protheus)

Para listar os papeis atribuídos a um determinado aplicativo, utilize o seguinte endpoint:

`GET   
/rest/v2/scim/v2/extensions/Resources/Companies/{companyId}/Applications/{appId}`

* Filtrando apenas os Papeis informando o `resourceTypes`como `Role`ou Empresa passando `resourceTypes`como `Company`

### Consulta de Papeis ou Empresas Atribuídos a um Usuário

Para consultar os papeis vinculados a um usuário específico, utilize:

`GET   
/rest/v2/scim/v2/extensions/Entitlements/Companies/{companyId}/Users/{userId}`

* Filtrando apenas os Papeis informando o `resourceTypes`como `Role`ou Empresa passando `resourceTypes`como `Company`

Para identificar a qual Empresa uma determinada Role está vinculada é possível consultar o `ext.restrictions` informado. Exemplo:

**Papel:** Acesso\_H  
`id`: “”  
  
**Empresa:**  
`ext.restrictions`: “”

Retorno do JSON:

### Estrutura Hierárquica das Empresas no RM

No contexto do RM:

* Os papeis são organizados hierarquicamente abaixo de uma empresa, definido o type como “Role”.
* Cada empresa possui um identificador **resourceID** e um **type** definido como "Company".

No exemplo, a empresa abaixo possui o seguinte `resourceID= 01010101010101__PR`

### Atribuição de Aplicativo a um Usuário

Para atribuir um aplicativo a um usuário, utilize o seguinte endpoint:  
  
`POST   
/rest/v2/companies/{companyId}/users/{userId}/applications`

Ao efetuar a atribuição, é necessário informar:

* O ID da empresa do usuário
* O ID do usuário
* O ID do aplicativo a ser adicionado ao usuário
* Informe o send-events como true quando desejar que este usuário seja enviado para a fila de provisionamento do ERP. Caso o usuário já esteja ativo  no ERP, não é necessário enviá-lo novamente, então mantenha o send-events como false.

### Atribuição de Papeis a um Usuário

Para atribuir um papel a um usuário, restringindo por empresa, utilize o seguinte endpoint:  
  
`POST   
/rest/v2/scim/v2/extensions/Entitlements/Companies/{companyId}/Applications/{appId}/Users/{userId}`

Ao efetuar a atribuição, é necessário informar:

* O papel que será vinculado ao usuário
* Se necessário uma empresa a qual o vínculo será restrito
* Informe o send-events como true quando desejar que este evento seja enviado para a fila de provisionamento do ERP.

Com isso será configurado apenas o Papel Acesso\_H para empresa exemplo.

Se não for informado um `modelRestriction`será ativo o papel para todas as empresas presentes.

Caso seja necessário remover a Role a API é semelhante, pode ser passado o mesm

`POST  
/rest/v2/scim/v2/extensions/Entitlements/Companies/{companyId}/Applications/{appId}/Users/{userId}/remove`

### **Explicação sobre a Estrutura de Papeis no Identity**

Os papeis dentro do Identity não são entidades independentes. A estrutura segue o modelo:

* O Identity possui **usuários, grupos e aplicativos**.
* Quando há integração com um ERP (como Protheus ou RM), é criado um **aplicativo correspondente**.
* No RM, um **grupo de permissão** determina quais itens de menu um usuário pode visualizar.
* Durante a sincronização do RM com o Identity, os **grupos de permissão do RM** são enviados para o aplicativo RM criado na integração.
* Para evitar confusão com os grupos do Identity, esses grupos de permissão são referenciados com o nome de **papeis**.
* Um papel **só existe dentro de um aplicativo** e **não pode ser consultado sem referência ao aplicativo**.
* Caso um aplicativo seja removido, todos os papeis associados também são excluídos.

Portanto, **não é possível obter uma lista global de papeis** sem especificar um aplicativo ou vínculo com o aplicativo. A listagem de papeis deve ser feita por aplicativo, utilizando os endpoints descritos anteriormente.

É possível consultar os Papeis vinculados a um usuário através do endpoint abaixo, filtrando o `resourceTypes=”Role”`, porém note que todo `Role`está vinculado a um `applicationId`:  
  
`GET   
/rest/v2/scim/v2/extensions/Entitlements/Companies/{companyId}/Users/{userId}`

## Documentações relacionadas

---
