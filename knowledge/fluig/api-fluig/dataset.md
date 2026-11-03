---
category: dataset
content_hash: 79a664ebf12d082c6553de6cc8cc3e7448bc29a75ac16315888120527f064f4a
endpoints: 15
fetched_at: '2026-11-03T17:04:21.693556+00:00'
module: dataset
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Dataset
type: api-reference
url: https://api.fluig.com/latest/dataset/swagger-ui/
---

# Dataset

Create and search datas like users, forms, documents and more in the Dataset API

**Spec:** https://api.fluig.com/latest/dataset/swagger-ui/swagger.json

## GET `/v2/dataset-handle/search`

**Search for dataset values**

- **operationId:** `searchDatasetValues`
- **tags:** Dataset handle

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `datasetId` | query | string | sim | Dataset code to be used as a filter |
| `field` | query | array | não | Dataset fields that will be returned, if no values are given all fields will be returned |
| `offset` | query | integer | não | How many records are skipped before returning the values. This field is used together with the <b>limit</b> to perform pagination |
| `limit` | query | integer | não | Maximum number of records to be returned in the search. If no value is filled in, the default is 300 records. If you enter the value 0, it fetches all records. <b>You must set the limit to avoid a search with many records, which may lead to a slow response</b> |
| `orderby` | query | string | não | Name of the field where the sorting will be done, you can add <b>_ASC</b> or <b>_DESC</b> to search in ascending and descending order respectively. |
| `constraintsField` | query | array | não | Name of field for entering the search value. You can enter multiple fields, but you need to provide a value for each one. |
| `constraintsInitialValue` | query | array | não | Value to be used for filtering in accordance with the field provided in the <b>constraintsField</b> parameter. If more than one search field was provided, you will need to provide the values in the same order to create the filter correctly. |
| `constraintsFinalValue` | query | array | não | If the desired filter is a range of values, the parameter <b>constraintsInitialValue</b> will be the initial value and <b>constraintsFinalValue</b> will be the final value. If you passed more than one field for research, you will need to pass the values in the same order to create the filter correctly. If you pass the same value as the parameter <b>constraintsInitialValue</b>, only this value is searched, ignoring the range of values. |
| `constraintsType` | query | array | não | Constraint type - Allowable Values: MUST, MUST_NOT or SHOULD |
| `constraintsLikeSearch` | query | array | não | Boolean value that determines whether the values in the fields <b>constraintsInitialValue</b> and <b>constraintsFinalValue</b> can be only part of the total value if the boolean is true or whether the values need to be exact if the boolean is false. When the value is true, you can use the % symbol to determine that any value from that point will be accepted |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/dataset-history`

**Return dataset history**

- **operationId:** `findDatasetHistory`
- **tags:** Dataset history

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | query | integer | não | Dataset history id |
| `userId` | query | integer | não | User Id to be used as filter |
| `datasetId` | query | string | não | Dataset code to be used as a filter |
| `datasetDescription` | query | string | não | Dataset description to be used as filter |
| `status` | query | string | não | api.dataset.param.status |
| `version` | query | integer | não | api.dataset.param.version |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting field |

### Respostas

- **201:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## DELETE `/v2/dataset-history/drafts`

**Delete a dataset draft**

- **operationId:** `deleteDatasetDraft`
- **tags:** Dataset history

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `datasetId` | query | string | sim | Dataset code to be used as a filter |

### Respostas

- **204:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v2/dataset-history/drafts`

**Create the draft dataset**

- **operationId:** `createDatasetDraft`
- **tags:** Dataset history

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `DatasetDraft` | body | DatasetDraft | sim | Dataset to create a draft |
| `ignoreConflicts` | query | boolean | não | Whether or not to ignore conflicts |

### Corpo da requisição

`DatasetDraft`

### Respostas

- **202:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v2/dataset-history/restore`

**Restore dataset by version**

- **operationId:** `restoreDataset`
- **tags:** Dataset history

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `datasetId` | query | string | sim | Dataset code to be used as a filter |
| `version` | query | integer | não | Restore dataset by version |

### Respostas

- **202:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/dataset-history/restore/validation`

**Check if the dataset is a draft before restore**

- **operationId:** `validateRestore`
- **tags:** Dataset history

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `datasetId` | query | string | sim | Dataset code to be used as a filter |

### Respostas

- **202:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/datasets`

**Search by datasets**

- **operationId:** `findDatasets`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `datasetId` | query | array | não | Dataset code to be used as a filter |
| `search` | query | string | não | Text to search in code and description of datasets |
| `active` | query | boolean | não | Filter active or inactive datasets |
| `draft` | query | boolean | não | Filter datasets with or without draft |
| `type` | query | array | não | Dataset type to be used as a filter |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting field |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets`

**Register a new dataset**

- **operationId:** `createOrUpdate`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `Dataset` | body | Dataset | sim | api.dataset.param |
| `ignoreConflicts` | query | boolean | não | Whether or not to ignore conflicts |

### Corpo da requisição

`Dataset`

### Respostas

- **201:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets/convert/{id}`

**Change dataset type, from generated to customized**

- **operationId:** `convert`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | string | sim | Dataset code to be used as a filter |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets/disable/{id}`

**Mark dataset as inactive**

- **operationId:** `disableDataset`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | string | sim | Dataset code to be used as a filter |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **403:** Permission denied. Only system administrators can access this feature
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets/enable/{id}`

**Activate dataset**

- **operationId:** `activateDataset`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | string | sim | Dataset code to be used as a filter |

### Respostas

- **200:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **403:** Permission denied. Only system administrators can access this feature
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets/export`

**Export a list of datasets to another fluig server**

- **operationId:** `exportToRemoteServer`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `DatasetImportExport` | body | DatasetImportExport | não | The target server and the datasets to be exported |

### Corpo da requisição

`DatasetImportExport`

### Respostas

- **200:** Datasets successfully exported
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v2/datasets/import`

**Importing a list of datasets to local fluig server**

- **operationId:** `importToLocalServer`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `DatasetImportExport` | body | DatasetImportExport | não | The target server and the datasets to be imported |

### Corpo da requisição

`DatasetImportExport`

### Respostas

- **200:** Datasets successfully imported
- **400:** Bad request
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/datasets/servers/{serverId}`

**Return dataset object**

- **operationId:** `findDatasetsByServerId`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `serverId` | path | integer | sim | Server id |

### Respostas

- **201:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## PATCH `/v2/datasets/synchronize/{id}`

**Enable/Disable syncing with the Server**

- **operationId:** `synchronizeDataset`
- **tags:** Datasets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | string | sim | Dataset code to be used as a filter |
| `body` | body | DatasetSynchronize | não |  |

### Corpo da requisição

`DatasetSynchronize`

### Respostas

- **204:** Ok
- **400:** Bad request
- **401:** User is not authenticated
- **403:** Permission denied. Only system administrators can access this feature
- **404:** Resource not found
- **500:** Internal server error, see reply for more details
