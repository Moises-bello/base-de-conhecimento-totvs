---
content_hash: a8994c8a5afccb94f857f47bf2ddebbc02fca21dadbda64d95ec250d08796ce5
fetched_at: '2026-11-03T14:34:40.391232+00:00'
page_id: resource_UserRest
product: fluig
source: rest-fluig
title: Fluig REST — UserRest Resource
type: documentation
url: https://api.fluig.com/old/resource_UserRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# UserRest Resource

User - V2

Available Since
:   1.5.9

### POST /2.0/users/changeUserPassword

Change User password.   
The Administrator can change other user's password passing the target login in the JSON.  
Otherwise, the current user's password will be change.

Available Since
:   1.5.9

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserPasswordVO](https://api.fluig.com/old/json_UserPasswordVO.html) (JSON) | REQUIRED Request JSON (example):`{ "login": "john.lennon", "currentPassword": "beatles@123", "newPassword": "YokoMyLove", "confirmNewPassword": "YokoMyLove", }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: null message: { message: "Senha alterada com sucesso!" detail: "Senha alterada com sucesso!" type: "INFO" }- }` |

Available Since
:   1.5

### POST /2.0/users/create

Create a new user  
  
Create a new user: fill object UserCreateVO

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserCreateVO](https://api.fluig.com/old/json_UserCreateVO.html) (JSON) | REQUIRED Request JSON (example):`{ "login": "login.fluig", "email": "login.fluig@fluig.com", "code": "123456", "firstName": "Login", "lastName": "Fluig", "fullName": "Login Fluig", "password": "Teste@123", "extData" :{"consumerKey":"12454544"} }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: { id: 60, login: "maria", email: "maria@teste.teste", code: "1579232", firstName: "Maria", lastName: "Sila", fullName: "Maria Silva", password: "******", tokenAccess: "d7531bfb-921d-4f77-9367-f094a965e6ce", // oAuth access token tokenSecret: "e08e5928-41ba-431c-98fc-86dfb0532e35de33dc54-9b94-4e0a-880a-d1abbb82ab54", // oAuth secret token extData: {}, }, message: { message: "Usuário criado com sucesso!", detail: "Usuário criado com sucesso!", type: "INFO" } }` |

Available Since
:   1.4.8

### GET /2.0/users/getCurrent

Get current user

Available Since
:   1.4.8

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { content: { id: 3 login: "login.login" email: "login.login@fluig.com" code: "login.login" firstName: "Login" lastName: "Login" fullName: "Login Login" password: "******" extData: { locationId: 1 tenantId: 1 tenantCode: "1" }- }- message: { message: "OK" detail: "OK" type: "INFO" }- }` |

Available Since
:   1.5.12

### GET /2.0/users/listAll

Retrieve all user list

Available Since
:   1.5.12

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records returned | 20 | required |
| offset | query | the offset | 0 | required |
| pattern | query | Pattern to filter results |  |  |
| sortField | query | sort field | fullName |  |
| sortType | query | Options ASC e DESC | ASC |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: [{ id: 3, login: "login.login", email: "login.login@fluig.com", code: "login.login", firstName: "Login", lastName: "Login", fullName: "Login Login", password: "******", isActive: true, extData: { locationId: 1, tenantId: 1, tenantCode: "1", }], message: { message: "OK" detail: "OK" type: "INFO" } }` |

Available Since
:   1.5.9

### POST /2.0/users/updateUser

Update Basic User Informations

Available Since
:   1.5.9

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserCreateVO](https://api.fluig.com/old/json_UserCreateVO.html) (JSON) | REQUIRED Request JSON (example):`{ "login": "john.lennon", "email": "john.lennon@fluig.com", "firstName": "John", "lastName": "Lennon", "fullName": "John Lennon", "timezone": "Europe/London" }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: { id: 60, login: "john.lennon", email: "john.lennon@fluig.com", firstName: "John", lastName: "Lennon", fullName: "John Lennon", password: "******", tokenAccess: "d7531bfb-921d-4f77-9367-f094a965e6ce", // oAuth access token tokenSecret: "e08e5928-41ba-431c-98fc-86dfb0532e35de33dc54-9b94-4e0a-880a-d1abbb82ab54", // oAuth secret token extData: { firstAccess: false, tenantId: 1, userType: NORMAL } } message: { message: "OK", detail: "OK", type: "INFO" } }` |

Available Since
:   1.5.9

### POST /2.0/users/updateUserData

Update User Metadata

Available Since
:   1.5.9

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | map of string (JSON) | REQUIRED Request JSON (example):`{ "WCMUserLang": "pt_BR", // language "UserRamal": "+1 42 4242424242", // phone "UserProjects": "RH" // area }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: true, message: { message: "OK", detail: "OK", type: "INFO" } }` |

Available Since
:   1.5.12

### POST /2.0/users/updateUserEvenDisabled

Update Basic User Informations even one that is disabled

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserCreateVO](https://api.fluig.com/old/json_UserCreateVO.html) (JSON) | REQUIRED Request JSON (example):`{ "login": "john.lennon", "email": "john.lennon@fluig.com", "firstName": "John", "lastName": "Lennon", "fullName": "John Lennon", "timezone": "Europe/London" }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: { id: 60, login: "john.lennon", email: "john.lennon@fluig.com", firstName: "John", lastName: "Lennon", fullName: "John Lennon", password: "******", tokenAccess: "d7531bfb-921d-4f77-9367-f094a965e6ce", // oAuth access token tokenSecret: "e08e5928-41ba-431c-98fc-86dfb0532e35de33dc54-9b94-4e0a-880a-d1abbb82ab54", // oAuth secret token extData: { firstAccess: false, tenantId: 1, userType: NORMAL } } message: { message: "OK", detail: "OK", type: "INFO" } }` |

Available Since
:   1.5.12

### POST /2.0/users/activateByCode/{genericId}

This method has been deprecated. User returned is undetermined in some scenarios.

Activate an user  
  
Activate an user by his login, idpId or userCode

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | :User's generic indentifier, can be (login, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: null message: { message: "Usuário ativado com sucesso!" detail: "Usuário ativado com sucesso!" type: "INFO" }- }` |

Available Since
:   1.5

### POST /2.0/users/deactivateByLogin/{genericId}

This method has been deprecated. User returned is undetermined in some scenarios.

Deactivate an user  
  
Deactivate an user by his login, idpId or userCode

Available Since
:   1.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | :User's generic indentifier, can be (login, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: null message: { message: "Usuário removido com sucesso!" detail: "Usuário removido com sucesso!" type: "INFO" }- }` |

Available Since
:   1.6.0

### GET /2.0/users/findById/{id}

Get user by id

Available Since
:   1.6.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { content: { id: 3 login: "login.login" email: "login.login@fluig.com" code: "login.login" firstName: "Login" lastName: "Login" fullName: "Login Login" password: "******" extData: { locationId: 1 tenantId: 1 tenantCode: "1" }- }- message: { message: "OK" detail: "OK" type: "INFO" }- }` |

Available Since
:   1.5.12

### GET /2.0/users/getUser/{genericId}

This method has been deprecated. User returned is undetermined in some scenarios.

Retrieve a specific user

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | User generic id |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { content: { id: 3 login: "login.login" email: "login.login@fluig.com" code: "login.login" firstName: "Login" lastName: "Login" fullName: "Login Login" password: "******" extData: { locationId: 1 tenantId: 1 tenantCode: "1" }- }- message: { message: "OK" detail: "OK" type: "INFO" }- }` |

Available Since
:   1.5

### GET /2.0/users/list/{state}

Retrieve User list

Available Since
:   1.5

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| state | path | The user state [UNCONFIRMED, ACTIVE, BLOCKED, REMOVED] |  | "ACTIVE" or "BLOCKED" or "REMOVED" or "UNCONFIRMED" |
| limit | query | limit of records returned | 20 | required |
| offset | query | the offset | 0 | required |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content[1]: { id: 3 login: "login.login" email: "login.login@fluig.com" code: "login.login" firstName: "Login" lastName: "Login" fullName: "Login Login" password: "******" extData: { locationId: 1 tenantId: 1 tenantCode: "1" }- }- message: { message: "OK" detail: "OK" type: "INFO" }- }` |

Available Since
:   1.5.12

### GET /2.0/users/listData/{login}

Retrieve user data

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| login | path | login of the user |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: { groups: "[MEMBER]", idpId: "", roles: "[user]", tenantCode: "01", tenantId: "1", UserEmailHTML: "true", UserProjects: "", UserQuotaDocument: "0", UserSpecialization: "", userType: "NORMAL", UserWorkflowGroup: "" }, message: { message: "OK", detail: "OK", type: "INFO", errorCode: null } }` |

Available Since
:   1.5.12

### GET /2.0/users/listGroups/{login}

Retrieve user groups

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| login | path | login of the user |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { content: [ "DefaultGroup-1", "MEMBER" ], message: { message: "OK" detail: "OK" type: "INFO" } }` |

Available Since
:   1.6.2

### GET /2.0/users/{userCode}/locals

Query user location.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| userCode | path | User Code. |  |
| expand | query | Can be passed as localUsers, to expand localUsers collection inside. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |
