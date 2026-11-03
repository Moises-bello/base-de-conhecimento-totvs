---
category: environment
content_hash: a88ba9acf5e3ddc5f49c31150ec23f7ee61ea63e06f7478bb5ad281f6b91afe4
endpoints: 4
fetched_at: '2026-11-03T17:04:21.987517+00:00'
module: environment
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Environment
type: api-reference
url: https://api.fluig.com/latest/environment/swagger-ui/
---

# Environment

The Environment API allows you to monitor and manage your company

**Spec:** https://api.fluig.com/latest/environment/swagger-ui/swagger.json

## GET `/v2/monitors`

**Returns the status list for all available monitors**

- **operationId:** `getAllMonitors`
- **tags:** Monitor status

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting by monitor key |

### Respostas

- **200:** Success!
- **400:** Failure, see the response for more details
- **401:** Access denied!
- **403:** Forbidden
- **500:** Internal error, see the response for more details

## GET `/v2/monitors/{monitorName}`

**Returns the status of the selected monitor**

- **operationId:** `getMonitor`
- **tags:** Monitor status

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `monitorName` | path | string | sim | Monitoring type |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Success!
- **400:** Failure, see the response for more details
- **401:** Access denied!
- **403:** Forbidden
- **404:** Not found
- **500:** Internal error, see the response for more details

## GET `/v2/statistics`

**Returns the list of all available statistics and recorded information**

- **operationId:** `getAllStatistics`
- **tags:** Statistics

### Respostas

- **200:** Success!
- **400:** Failure, see the response for more details
- **401:** Access denied!
- **403:** Forbidden
- **500:** Internal error, see the response for more details

## GET `/v2/statistics/{statisticName}`

**Returns the status of the selected statistic**

- **operationId:** `getStatistics`
- **tags:** Statistics

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `statisticName` | path | string | sim |  |

### Respostas

- **200:** Success!
- **400:** Failure, see the response for more details
- **401:** Access denied!
- **403:** Forbidden
- **404:** Not found
- **500:** Internal error, see the response for more details
