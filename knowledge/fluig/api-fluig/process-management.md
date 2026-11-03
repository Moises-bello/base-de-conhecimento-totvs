---
category: process-management
content_hash: 9d32568fd816b54606b1ca65e0c3b6a1dcad30afc5dc9b4f27bae6514ab59d82
endpoints: 58
fetched_at: '2026-11-03T17:04:19.791494+00:00'
module: process-management
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Process Management
type: api-reference
url: https://api.fluig.com/latest/process-management/swagger-ui/
---

# Process Management

This API manages information related to processes, activities, requests and tasks.

**Spec:** https://api.fluig.com/latest/process-management/swagger-ui/swagger.json

## GET `/v2/activities`

**Searches activities**

- **operationId:** `findActivities`
- **tags:** Activities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | query | array | não | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivities`
- **tags:** Activities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | query | array | não | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/date-calculator/duration`

**Duration between two dates**

- **operationId:** `duration`
- **tags:** Date calculation

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `startDate` | query | string | sim | Start from |
| `endDate` | query | string | sim | End date |
| `localId` | query | integer | não | Location identifier |
| `periodId` | query | string | não | Identifier of the period used to calculate deadlines |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/date-calculator/end-date`

**Calculate end date**

- **operationId:** `endDate`
- **tags:** Date calculation

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `startDate` | query | string | sim | Start from |
| `seconds` | query | integer | sim | Number of seconds to calculate deadline. |
| `localId` | query | integer | não | Location identifier |
| `periodId` | query | string | não | Identifier of the period used to calculate deadlines |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/date-calculator/start-date`

**Calculate start date**

- **operationId:** `startDate`
- **tags:** Date calculation

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `endDate` | query | string | sim | End date |
| `seconds` | query | integer | sim | Number of seconds to calculate deadline. |
| `localId` | query | integer | não | Location identifier |
| `periodId` | query | string | não | Identifier of the period used to calculate deadlines |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** respofindWorkflowTasksOnDemand_v2nse.status.server.error

## GET `/v2/processes`

**Searches processes**

- **operationId:** `findProcesses`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `order` | query | array | não | Ordered fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `processId` | query | array | não | Process Id |
| `active` | query | string | não | Search for active processes |
| `public` | query | string | não | Search for public processes |
| `categoryId` | query | string | não | Search based on literal category id |
| `likeCategories` | query | string | não | Turns category search to a like search, allowing sub category queries |
| `uniqueFormRecord` | query | string | não | Search for processes that don't keep version track of their form records |
| `released` | query | string | não | Search for processes that have at least one active and published version |
| `deadlinePresent` | query | string | não | If the search is for processes with deadline |
| `warningPresent` | query | string | não | If the search is for processes with warning timeout |
| `processDescription` | query | string | não | Search for processes based on description (like search) |
| `volumeId` | query | string | não | Search for processes within certain volume |
| `periodId` | query | string | não | Search for processes with certain period |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## POST `/v2/processes`

**Create simple process with few parameters**

- **operationId:** `createSimpleProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processSimpleCreate` | body | ProcessSimpleCreate | não | Simple process creation template |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Corpo da requisição

`ProcessSimpleCreate`

### Respostas

- **201:** Created
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/import/xml`

**Import process XML**

- **operationId:** `importNewProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | string | não |  |
| `processId` | query | string | não | Process identifier |
| `formId` | query | integer | não | Form identifier |
| `release` | query | boolean | não | Release |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Corpo da requisição

`string`

### Respostas

- **200:** Created
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## DELETE `/v2/processes/{processId}`

**Remove a process**

- **operationId:** `removeProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}`

**Searches processes**

- **operationId:** `findProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/activities`

**Searches activities**

- **operationId:** `findActivitiesByProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivitiesByProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/export/xml`

**Export configuration xml from the latest version of the process**

- **operationId:** `exportProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |

### Respostas

- **200:** Created
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/import/xml`

**Import process XML**

- **operationId:** `importProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | string | não |  |
| `processId` | path | string | sim | Process identifier |
| `formId` | query | integer | não | Form identifier |
| `release` | query | boolean | não | Release |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Corpo da requisição

`string`

### Respostas

- **200:** Created
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions`

**Searches process versions**

- **operationId:** `findProcessVersions`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `order` | query | array | não | Ordered fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `version` | query | array | não | Version number |
| `formId` | query | string | não | Form Id |
| `formExistent` | query | string | não | If there is a form attached to the version |
| `editing` | query | string | não | Search for versions in editing mode |
| `active` | query | string | não | Search for active versions |
| `blocked` | query | string | não | Search for blocked versions |
| `requiresPassword` | query | string | não | Search for versions that requires password for moving |
| `bpmnVersion` | query | string | não | Search for versions by bpmn version number |
| `inheritFormSecurity` | query | string | não | Search for versions in which forms inherit security from documents |
| `mobileReady` | query | string | não | Search for versions that are able to be handled in mobile |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## DELETE `/v2/processes/{processId}/process-versions/latest`

**Remove the latest version of the process**

- **operationId:** `removeLatestVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |

### Respostas

- **204:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/process-versions/latest/release`

**Release the latest version of the process for use**

- **operationId:** `releaseLatestVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |

### Respostas

- **204:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/process-versions/latest/withdraw`

**Remove release of the latest version of the process**

- **operationId:** `withdrawLatestVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |

### Respostas

- **204:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## DELETE `/v2/processes/{processId}/process-versions/{processVersion}`

**Remove a version of the process**

- **operationId:** `removeVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}`

**Searches processes**

- **operationId:** `findProcessVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/activities`

**Searches activities**

- **operationId:** `findActivitiesByProcessIdAndVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivitiesByProcessIdAndVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/diagram`

**Retrieve process diagram in SVG**

- **operationId:** `findProcessVersionSVG`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## PUT `/v2/processes/{processId}/process-versions/{processVersion}/diagram`

**Retrieve process diagram in SVG**

- **operationId:** `updateProcessVersionSVG`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | string | não |  |
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Corpo da requisição

`string`

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/export/xml`

**Export configuration xml from a version of the process**

- **operationId:** `exportProcessVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/process-versions/{processVersion}/release`

**Release a version of the process for use**

- **operationId:** `releaseVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/requests`

**Searches requests**

- **operationId:** `findRequestsByProcessVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `initialProcessInstanceId` | query | integer | não | Range initial of request id |
| `finalProcessInstanceId` | query | integer | não | Range final of request id |
| `participants` | query | array | não | Task participants |
| `completeColleagueIds` | query | array | não | Completed task with manager or substitute |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Request status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requester |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/requests/tasks`

**Searches tasks**

- **operationId:** `findTasksByProcessIdAndProcessVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `appDecisionSearch` | query | string | não | Searches by title, description and highlight, only if the 'appDecisionInfo' attribute is expanded |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/requests/tasks/resume`

**Shows the query result of tasks grouped by status**

- **operationId:** `resumeTasksByProcessAndVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/states`

**Searches by process status**

- **operationId:** `findProcessStates`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `stateSequence` | query | string | não | String identifier of the process status |
| `processVersion` | path | integer | sim | Process version |
| `order` | query | array | não | Ordered fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `stateType` | query | string | não | State Type |
| `bpmnType` | query | string | não | Bpmn Type (bpmnType is used only in processes created by Fluig Studio) |
| `stateName` | query | string | não | State Name |
| `stateDescription` | query | string | não | State Description |
| `interactives` | query | string | não | Returns only iteractive states, those who requires user iteraction, it's the equivalent to search for bpmn types START_EVENT_NORMAL, TASK_NORMAL and TASK_USER |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/states/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivitiesByStates`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | path | integer | sim | Process version |
| `interactives` | query | string | não | Returns only interactive states, those who requires user interaction, it's the equivalent to search for bpmn types START_EVENT_NORMAL, TASK_NORMAL and TASK_USER |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/states/{stateSequence}`

**Searches by process status**

- **operationId:** `findProcessState`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `stateSequence` | path | string | sim | String identifier of the process status |
| `processVersion` | path | integer | sim | Process version |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/process-versions/{processVersion}/states/{stateSequence}/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivitiesByState`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `stateSequence` | path | integer | sim | String identifier of the process status |
| `processVersion` | path | integer | sim | Process version |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/process-versions/{processVersion}/withdraw`

**Remove release of a version of the process**

- **operationId:** `withdrawVersion`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `processVersion` | path | integer | sim | Process version |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/requests`

**Searches requests**

- **operationId:** `findRequestsByProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `initialProcessInstanceId` | query | integer | não | Range initial of request id |
| `finalProcessInstanceId` | query | integer | não | Range final of request id |
| `participants` | query | array | não | Task participants |
| `completeColleagueIds` | query | array | não | Completed task with manager or substitute |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Request status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requester |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/requests/tasks`

**Searches tasks by request**

- **operationId:** `findTasksByProcessIdAndProcessInstanceId`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `appDecisionSearch` | query | string | não | Searches by title, description and highlight, only if the 'appDecisionInfo' attribute is expanded |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/processes/{processId}/requests/tasks/resume`

**Shows the query result of tasks grouped by status**

- **operationId:** `resumeSlaTasksByProcess`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | path | string | sim | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## POST `/v2/processes/{processId}/start`

**Start request**

- **operationId:** `start`
- **tags:** Processes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processId` | path | string | sim | Process identifier |
| `startRequest` | body | StartRequest | não | Request start information |
| `device` | header | string | não | Device used if mobile |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `expand` | query | array | não | Expandable fields |

### Corpo da requisição

`StartRequest`

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **412:** Failed to move due to the need of an assignee to be appointed for the next task
- **500:** Internal server error, see reply for more details

## GET `/v2/requests`

**Searches requests**

- **operationId:** `findRequests`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `initialProcessInstanceId` | query | integer | não | Range initial of request id |
| `finalProcessInstanceId` | query | integer | não | Range final of request id |
| `participants` | query | array | não | Task participants |
| `completeColleagueIds` | query | array | não | Completed task with manager or substitute |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Request status |
| `slaStatus` | query | array | não | Deadline status |
| `processId` | query | array | não | Process identifier |
| `requester` | query | string | não | Requester |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}`

**Searches requests**

- **operationId:** `findRequest`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/activities`

**Searches activities**

- **operationId:** `findActivitiesByRequest`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/activities/resume`

**Shows the query result of activities grouped by status**

- **operationId:** `resumeActivitiesByRequest`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `active` | query | string | não | Active activities |
| `slaStatus` | query | array | não | Deadline status |
| `requester` | query | string | não | Requisitioner’s registration |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/attachments`

**Searches request attachments**

- **operationId:** `findAttachments`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `user` | query | string | não | Registration of the user who did the attachment |
| `userName` | query | string | não | Name of the user who did the attachment |
| `published` | query | string | não | If the attachment was posted |
| `mainForm` | query | string | não | If the attachment is the main form for the request |
| `documentId` | query | string | não | Document identifier |
| `documentName` | query | string | não | Name of the main physical document, if any |
| `documentDescription` | query | string | não | Main document description |
| `documentVersion` | query | string | não | Document version |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `attachmentSequence` | query | string | não | String identifier of the attachment in the request |
| `initialAttachmentDate` | query | string | não | Attached from |
| `finalAttachmentDate` | query | string | não | Attached to |
| `latestVersionsOnly` | query | string | não | Filters only by the latest attachment version |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/attachments/download`

**Download filtered attachments**

- **operationId:** `downloadAttachments`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `user` | query | string | não | Registration of the user who did the attachment |
| `replacedUser` | query | string | não | Registration of the substituted user for permission use |
| `published` | query | string | não | If the attachment was posted |
| `documentId` | query | string | não | Document identifier |
| `documentName` | query | string | não | Name of the main physical document, if any |
| `documentDescription` | query | string | não | Main document description |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `attachmentSequence` | query | string | não | String identifier of the attachment in the request |
| `initialAttachmentDate` | query | string | não | Attached from |
| `finalAttachmentDate` | query | string | não | Attached to |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/attachments/{attachmentSequence}/download`

**Download filtered attachments**

- **operationId:** `downloadAttachment`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `replacedUser` | query | string | não | Registration of the substituted user for permission use |
| `attachmentSequence` | path | integer | sim | String identifier of the attachment in the request |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/histories`

**Fetch history from requests, DO NOT USE THIS, it is on beta test and will change completely**

- **operationId:** `findHistoriesByProcessInstanceId`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request Id |
| `movementSequence` | query | string | não | Movement id where those tasks are identified |
| `types` | query | string | não | Movement id where those tasks are identified |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `order` | query | array | não | Ordered fields |
| `fields` | query | array | não | Fields that will be returned with the response JSON, if not sent, the whole resource will be returned |

### Respostas

- **200:** OK
- **400:** Failed to proceed the operation due to a business problem, see response for more details
- **401:** Access denied
- **404:** Failed to find a resource needed for operation, see response for more details
- **500:** Internal error, see response for more details

## POST `/v2/requests/{processInstanceId}/move`

**Moves a request**

- **operationId:** `move`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `moveRequest` | body | MoveRequest | não | Information to move the request |
| `device` | header | string | não | Device used if mobile |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `expand` | query | array | não | Expandable fields |

### Corpo da requisição

`MoveRequest`

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **412:** Failed to move due to the need of an assignee to be appointed for the next task
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/possible-assignees`

**Find possible assignees for the next activity, the results may change by events between the activities.**

- **operationId:** `findPossibleAssignees`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request Id |
| `movementSequence` | query | string | não | Movement Sequence |
| `assignee` | query | string | não | Actual assignee |
| `targetState` | query | string | não | Target state |
| `subProcessTargetState` | query | string | não | Sub process target state |
| `pattern` | query | string | não | User pattern used to search, filters by code and name |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `order` | query | array | não | Ordered fields |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields that will be returned with the response JSON, if not sent, the whole resource will be returned |

### Respostas

- **200:** OK
- **400:** Failed to proceed the operation due to a business problem, see response for more details
- **401:** Access denied
- **403:** User without permission to proceed the operation
- **404:** Failed to find a resource needed for operation, see response for more details
- **500:** Internal error, see response for more details

## GET `/v2/requests/{processInstanceId}/tasks`

**Searches tasks**

- **operationId:** `findTasksByProcessInstanceId`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `stateSequence` | query | string | não | String identifier of the process status |
| `appDecisionSearch` | query | string | não | Searches by title, description and highlight, only if the 'appDecisionInfo' attribute is expanded |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/requests/{processInstanceId}/tasks/resume`

**Shows the query result of tasks grouped by status**

- **operationId:** `resumeSlaTasksByRequest`
- **tags:** Requests

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `slaStatus` | query | array | não | Deadline status |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `stateSequence` | query | string | não | String identifier of the process status |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/tasks`

**Searches tasks**

- **operationId:** `findTasks`
- **tags:** Tasks

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `processId` | query | string | não | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `slaStatus` | query | array | não | Deadline status |
| `appDecisionSearch` | query | string | não | Searches by title, description and highlight, only if the 'appDecisionInfo' attribute is expanded |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `viewJustProcessWithApproval` | query | boolean | não | Only view processes with approval |
| `viewJustApproachingExpiration` | query | boolean | não | View only activities close to expiration |
| `replacedUserCode` | query | string | não | Use user replaced as logged in |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Ordered fields |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/tasks/count`

**Total activity counter by expiration date**

- **operationId:** `countTasks`
- **tags:** Tasks

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `processId` | query | string | não | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/tasks/count/pool`

**Total activity counter in a user's pool by expiration date**

- **operationId:** `countTasksByUserPool`
- **tags:** Tasks

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `assigneeUserCode` | query | string | não | Person in charge’s registration |
| `poolType` | query | array | não | Pool activity type |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/tasks/count/pool/resume`

**Total activity counter in a user's pool for each group/role**

- **operationId:** `countTasksByUserPoolResume`
- **tags:** Tasks

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `assigneeUserCode` | query | string | não | Person in charge’s registration |
| `poolType` | query | array | não | Pool activity type |
| `pattern` | query | string | não | Group/role code |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/tasks/resume`

**Shows the query result of tasks grouped by status**

- **operationId:** `resumeSlaTasks`
- **tags:** Tasks

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | query | array | não | Request identifier |
| `movementSequence` | query | string | não | Identifier of the move associated to the task |
| `transferSequence` | query | string | não | Transfer sequence in the task itself |
| `assignee` | query | string | não | Person in charge’s registration |
| `status` | query | array | não | Task status |
| `processId` | query | string | não | Process identifier |
| `requester` | query | string | não | Requisitioner’s registration |
| `assigneeName` | query | string | não | Person In charge’s name |
| `requesterName` | query | string | não | Requisitioner’s name |
| `manager` | query | string | não | Process manager’s registration |
| `initialDeadlineDate` | query | string | não | Deadline from |
| `finalDeadlineDate` | query | string | não | Deadline until |
| `initialStartDate` | query | string | não | Start from |
| `finalStartDate` | query | string | não | Start until |
| `initialAssignStartDate` | query | string | não | Assigned from |
| `finalAssignStartDate` | query | string | não | Assigned to |
| `initialAssignEndDate` | query | string | não | Assignment end from |
| `finalAssignEndDate` | query | string | não | Assignment end until |
| `initialWarningDate` | query | string | não | Expiration notification from |
| `finalWarningDate` | query | string | não | Expiration notification until |
| `initialEndDate` | query | string | não | Conclusion from |
| `finalEndDate` | query | string | não | Conclusion until |
| `processVersion` | query | array | não | Process version |
| `stateSequence` | query | string | não | String identifier of the process status |
| `requesterLocal` | query | array | não | Requisitioner’s location identifier |
| `assigneeLocal` | query | array | não | Person in charge’s location identifier |
| `formFields` | query | array | não | Form fields for search, following the pattern Field:Value |
| `slaStatus` | query | array | não | Deadline status |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## GET `/v2/user-replacements`

**User substitution search**

- **operationId:** `findUserReplacements`
- **tags:** User substitution

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `startAt` | query | string | não | Start of substitution |
| `endAt` | query | string | não | End of substitution |
| `processIdList` | query | array | não | List of process identifiers |
| `userCode` | query | string | não | User registration |
| `userName` | query | string | não | Display user name |
| `userMail` | query | string | não | User’s e-mail address |
| `userLogin` | query | string | não | User login |
| `replacedByUserCode` | query | string | não | Substitute user registration |
| `replacedByUserName` | query | string | não | Display user name |
| `replacedByUserMail` | query | string | não | User’s e-mail address |
| `replacedByUserLogin` | query | string | não | User login |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Fields returned in JSON, to filter the response message |
| `order` | query | array | não | Sorted fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/workflow-exporter/{processInstanceId}`

**Searches process versions**

- **operationId:** `export`
- **tags:** Exportador de Workflow

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `anonymizeForms` | query | boolean | não | request.anonymizeforms |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details

## GET `/v2/workflow-exporter/{processInstanceId}/download`

**process.version.download**

- **operationId:** `exportZipFile`
- **tags:** Exportador de Workflow

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `processInstanceId` | path | integer | sim | Request identifier |
| `requestOriginalFiles` | query | boolean | não | request.original |
| `anonymizeForms` | query | boolean | não | request.anonymizeforms |

### Respostas

- **200:** Ok
- **400:** Incorrect Request
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Resource not found
- **500:** Internal server error, see reply for more details
