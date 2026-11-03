---
category: dataservice
content_hash: 47d2a88670f722e39c66ff630f27fd5fe054b47855cd707cbeaf8fa7ba917e85
endpoints: 3
fetched_at: '2026-11-03T17:04:20.260219+00:00'
module: dataservice
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Integration
type: api-reference
url: https://api.fluig.com/latest/dataservice/swagger-ui/
---

# Integration

Manage integration operations

**Spec:** https://api.fluig.com/latest/dataservice/swagger-ui/swagger.json

## GET `/v2/operations`

**Returns the list of available operations**

- **operationId:** `findOperations`
- **tags:** Operations

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting by field(s) |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/operations/{operationId}`

**Returns an operation**

- **operationId:** `findByOperationCode`
- **tags:** Operations

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `operationId` | path | integer | sim | Operation Id |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **404:** Operation not found.
- **500:** Internal server error, see reply for more details

## POST `/v2/operations/{operationId}/execute`

**Perform an operation.**

- **operationId:** `executeOperation`
- **tags:** Operations

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `operationId` | path | integer | sim | Operation Id |
| `params` | body | Operation Execution Input Params | não | Parameters to perform the operation |

### Corpo da requisição

`Operation Execution Input Params`

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **404:** Operation not found.
- **500:** Internal server error, see reply for more details
