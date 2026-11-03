---
category: use-policy
content_hash: cafbc10247612d9447a3ad26e2a538febea020956d225b6fb74052155a6ef00f
endpoints: 3
fetched_at: '2026-11-03T17:04:22.194853+00:00'
module: use-policy
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Use Policy
type: api-reference
url: https://api.fluig.com/latest/use-policy/swagger-ui/
---

# Use Policy

The Use Policy API allows you to check and accept the use policy document

**Spec:** https://api.fluig.com/latest/use-policy/swagger-ui/swagger.json

## GET `/v1/use-policies`

**Checks if the logged user has already accepted the use policy document for the respective company and language.**

- **operationId:** `checkAcceptance`
- **tags:** Use policies

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v1/use-policies/accept`

**Accepts the use policy document according to the company and language of the logged user.**

- **operationId:** `accept`
- **tags:** Use policies

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v1/use-policies/document/{id}/accept`

**Accepts the use policy document informed by the logger used.**

- **operationId:** `acceptByDocumentId`
- **tags:** Use policies

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Use policy document ID informed by logged user. |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further
