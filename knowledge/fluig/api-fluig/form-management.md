---
category: form-management
content_hash: f6084b163f641f88a39b770bb57f01e45903b25e684527e389620bc3e45526a5
endpoints: 12
fetched_at: '2026-11-03T17:04:22.420434+00:00'
module: form-management
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Form Management
type: api-reference
url: https://api.fluig.com/latest/form-management/swagger-ui/
---

# Form Management

This API manages the forms of the new form editor and their records.

**Spec:** https://api.fluig.com/latest/form-management/swagger-ui/swagger.json

## GET `/v2/forms`

**List all forms**

- **operationId:** `getForms`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `formCategory` | query | string | não | Form Category |
| `versionStatus` | query | string | não | Form Version Status |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/forms`

**Create a new form in a draft version**

- **operationId:** `createFormInDraftWithInitialVersion`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | FormCreate | sim | Object to create a new form in a draft version |

### Corpo da requisição

`FormCreate`

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/image/{filename}`

**Search the image by file name**

- **operationId:** `getImage`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `filename` | path | string | sim | Image |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/forms/upload/image`

**Uploads the image to be used by the Image field**

- **operationId:** `uploadImage`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `file` | formData | file | sim | Image |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}`

**Search the latest version of the form**

- **operationId:** `getFormByCode`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `activityId` | query | string | não | Code of a process activity linked to the form |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## PUT `/v2/forms/{code}`

**Save the draft version of the form**

- **operationId:** `saveDraftVersion`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `body` | body | FormDraft | sim | Object to update the draft version of the form |

### Corpo da requisição

`FormDraft`

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}/activity/{activityId}`

**Search the published form by code and process activity code**

- **operationId:** `getFormByCodeAndActivity`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `activityId` | path | string | sim | Code of a process activity linked to the form |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}/activity/{activityId}/process-instance/{processInstanceId}`

**Search the published form by code, process activity code, and request number**

- **operationId:** `getFormByActivityAndProcessInstance`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `activityId` | path | string | sim | Code of a process activity linked to the form |
| `processInstanceId` | path | integer | sim | Number of a request from the process linked to the form |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}/components`

**Search all form fields**

- **operationId:** `getFormFields`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `name` | query | string | não | Filtro por identificador ou rótulo do campo |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/forms/{code}/publish`

**Publish the draft version of the form**

- **operationId:** `publish`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}/versions`

**Search all versions of the form**

- **operationId:** `getFormVersions`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/forms/{code}/{version}`

**Search the form version**

- **operationId:** `getFormByCodeAndVersion`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | integer | sim | Form code |
| `version` | path | integer | sim | Form Version |
| `activityId` | query | string | não | Code of a process activity linked to the form |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details
