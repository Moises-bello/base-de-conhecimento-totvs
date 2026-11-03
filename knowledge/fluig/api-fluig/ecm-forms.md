---
category: ecm-forms
content_hash: 103d4ea4fb9855f7905043058098e67871e85d13f2f1d965e47b4a43bf770c37
endpoints: 16
fetched_at: '2026-11-03T17:04:20.024065+00:00'
module: ecm-forms
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — ECM Form Management
type: api-reference
url: https://api.fluig.com/latest/ecm-forms/swagger-ui/
---

# ECM Form Management

This API manages information related to cards, card indexes and their records.

**Spec:** https://api.fluig.com/latest/ecm-forms/swagger-ui/swagger.json

## GET `/v2/cardindex`

**Searches company forms**

- **operationId:** `findCardIndex`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | query | integer | não | Document number |
| `version` | query | integer | não | Document version |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PATCH `/v2/cardindex`

**Updates the form based on an html or compressed (ZIP) file. Images, css and javascript elements used in the form can be sent in ZIP files. Form events stored in a folder named “events” can also be sent in ZIP files.**

- **operationId:** `updateCardIndexUsingPATCH`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | formData | string | sim | Document ID |
| `updateMode` | formData | string | não | Update type 0 = Keep current version and 2 = New version |
| `mainFile` | formData | string | não | Name of the main file (in case of compressed files with multiple html files) |
| `formName` | formData | string | não | Document description |
| `descriptorField` | formData | string | não | Card description |
| `datasetName` | formData | string | não | Dataset name |
| `onlyActiveRows` | formData | boolean | não | List only active form records |
| `file` | formData | file | não | Form content download |

### Respostas

- **201:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/cardindex`

**Creates forms based on html or compressed (ZIP) files. Images, css and javascript elements used in the form can be sent in ZIP files. Form events stored in a folder named “events” can also be sent in ZIP files. **

- **operationId:** `createCardIndex`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `mainFile` | formData | string | não | Name of the main file (in case of compressed files with multiple html files) |
| `formName` | formData | string | sim | Document description |
| `descriptorField` | formData | string | não | Card description |
| `datasetName` | formData | string | não | Dataset name |
| `persistenceType` | formData | int | não | Form record storage type (1 = multiple tables, 0 = single table) |
| `onlyActiveRows` | formData | boolean | não | List only active form records |
| `parentId` | formData | string | sim | Parent document number |
| `file` | formData | file | sim | Form content download |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/cardindex`

**Updates the form based on an html or compressed (ZIP) file. Images, css and javascript elements used in the form can be sent in ZIP files. Form events stored in a folder named “events” can also be sent in ZIP files.**

- **operationId:** `updateCardIndexUsingPUT`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | formData | string | sim | Document ID |
| `updateMode` | formData | string | não | Update type 0 = Keep current version and 2 = New version |
| `mainFile` | formData | string | não | Name of the main file (in case of compressed files with multiple html files) |
| `formName` | formData | string | sim | Document description |
| `descriptorField` | formData | string | não | Card description |
| `datasetName` | formData | string | não | Dataset name |
| `onlyActiveRows` | formData | boolean | não | List only active form records |
| `file` | formData | file | sim | Form content download |

### Respostas

- **201:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/cardindex/html`

**Returns the form stream URL based either on the associated request identifier or the document version code**

- **operationId:** `getHtml`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | query | string | não | Process name |
| `processInstanceId` | query | integer | não | Process number |
| `documentId` | query | integer | não | Document identifier |
| `documentVersionId` | query | integer | não | Document version identifier |
| `currentMovto` | query | integer | não | Current movement |
| `editable` | query | boolean | não | Editing mode |
| `taskUserId` | query | string | não | User registration in the task |
| `managerMode` | query | boolean | não | Process manager |
| `mobile` | query | boolean | não | mobile form |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/cardindex/{documentId}`

**Deletes form (Bin)**

- **operationId:** `removeCardIndex`
- **tags:** Forms

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/cardindex/{documentId}/cards`

**Search form records**

- **operationId:** `findRecordCardIndex`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `$filter` | query | string | não | Filters by ODATA, implemented queries eq ne and or, use [] to identify optionFields, examples:  For field equals to value: field eq 'value' For field not equals to value: field ne 'value' For two filters: field1 eq 'value1' and field2 eq 'value2' For or operator: field1 eq 'value1' or field1 eq 'value2' For between operator: field1 ge 'value1' and field1 le 'value2' For option fields: field[optionField] eq 'value' For like search: field eq '%value%'  Rules for this beta version:  You cannot use double quotes, only use single quotes: 'value'  You cannot search with ONLY ge or le operator, it MUST be used on between You cannot search using ne operator on or operations You cannot use not operation, only ne operator referencing the field |
| `listInactive` | query | boolean | não |  |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/cardindex/{documentId}/cards`

**Creates a form record**

- **operationId:** `create`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardCreateDTO` | body | CardCreate | não | cardindex.cardCreateDTO |

### Corpo da requisição

`CardCreate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/cardindex/{documentId}/cards/{cardId}`

**Deletes a form record**

- **operationId:** `delete`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/cardindex/{documentId}/cards/{cardId}`

**Searches form records by Id**

- **operationId:** `findCardIndexById`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | expandable.fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/cardindex/{documentId}/cards/{cardId}`

**Updates a form record**

- **operationId:** `update`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `cardCreateDTO` | body | CardCreate | não | cardindex.cardCreateDTO |

### Corpo da requisição

`CardCreate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/cardindex/{documentId}/cards/{cardId}/children`

**Creates child record**

- **operationId:** `createChild`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `cardChildrenDTO` | body | CardChildren | não | card.cardChildrenDTO |

### Corpo da requisição

`CardChildren`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/cardindex/{documentId}/cards/{cardId}/children/{row}`

**Deletes a child record**

- **operationId:** `deleteChild`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `row` | path | integer | sim | Child record line |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/cardindex/{documentId}/cards/{cardId}/children/{row}`

**Searches child records by line**

- **operationId:** `findCardChildByRow`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `row` | path | integer | sim | Child record line |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/cardindex/{documentId}/cards/{cardId}/children/{row}`

**Updates child record**

- **operationId:** `updateChild`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `row` | path | integer | sim | Child record line |
| `cardChildrenDTO` | body | CardChildren | não | card.cardChildrenDTO |

### Corpo da requisição

`CardChildren`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/cardindex/{documentId}/cards/{cardId}/childrens`

**Searches child records of a form record**

- **operationId:** `findCardChildren`
- **tags:** Form records

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Document number |
| `cardId` | path | integer | sim | Record number |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further
