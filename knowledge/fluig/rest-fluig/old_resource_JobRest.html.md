---
content_hash: ff9555897c0109ced93c778f82d9d797501e0d7b3505895301e32c71d10ba021
fetched_at: '2026-11-03T14:34:39.901359+00:00'
page_id: resource_JobRest
product: fluig
source: rest-fluig
title: Fluig REST — JobRest Resource
type: documentation
url: https://api.fluig.com/old/resource_JobRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# JobRest Resource

Job Scheduler - V2

Available Since
:   1.5.8

### POST /2.0/job/createDaily

Create a job to execute daily.  
  
Return the job that was created.

#### Examples of use:

Execute the job every 5 days, after 10:35 am
`{
"jobType": 20, // selected job type
"interval": 5, // Execute every 5 days MAX VALUE 30
"executionHour": 10, // execute after 10:35 am
"executionMinute": 35 // execute after 10:35 am
"description": "Job name" // name of the given job
"data": { 'extraDataKey': 'extraDataValue' } // generic field to store any extra key/value data about the job
}`

Available Since
:   1.5.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [JobRestVO](https://api.fluig.com/old/json_JobRestVO.html) (JSON) | Request JSON (example):`{ "jobId": "Processar_mensagens_do_EAI", // the job ID "description": "Job para Processar mensagens do EAI", // Description of the job "interval": 1, // Use this property to create a job that will be executed at each X day(s), where X is the value o this property MAX VALUE = 30. "executionHour": 10, // Use this property to configure that this job should be executed after HH hour (where HH range is 00 to 23) "executionMinute": 30, // Use this property to configure that this job should be executed after mm minute (where mm range is 00 to 60) "data": { // A string key-value map, to pass extra data to Job executor "datasetId" : "97" }, "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) // 0 - Expiração de Documentos // 1 - Tarefas Atrasadas // 2 - Fluxo Automático // 3 - Indexação de Documentos // 4 - Recalcular Volumes // 6 - Timer de início de Processo // 7 - Início condicional de Processo // 8 - Compactar Solicitações Finalizadas // 9 - Expiração de Tarefas // 10 - Início multiplo de Processo // 11 - Conversão de documentos para visualizador interno // 12 - Limpeza de arquivos Temporarios de documentos // 13 - Processar mensagens do EAI // 14 - Cancelar matrículas expiradas em turmas // 15 - Cancelar matrículas expiradas em treinamentos // 16 - Notificar aprovação de requisição de matrícula pendente // 17 - Notificar expiração de contas // 18 - Finalizar tópicos expirados // 19 - Processar requisições de matrícula // 20 - Limpeza de notificações // 22 - Monitoramento de métricas // 23 - Sincronização de Dataset }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message "content": { "jobId": "Processar_mensagens_do_EAI", // the job ID "companyId": 123, // The Tenant Id of the job "interval": 5 // Job is executed every 5 days "executionHour": 10, // hour which the job will start to execute "executionMinute": 30, // minute which the job will start to execute "description": "Job para Processar mensagens do EAI", // Description of the job "recurrenceExpression": "0 00 00 1/1 * ? *", // The cron expression used to schedule the job "lastExecution": "2016-03-23 21:00:00", // The date of job's last execution "nextExecution": "2016-03-24 21:00:00", // The date of job's next execution "started": "true", // A boolean value to show if the jobs is started "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.8

### POST /2.0/job/createMonthly

Create a job to be executed monthly.  
  
Return the job that was created.

#### Examples of use:

Execute the job at day 10 monthly after 23:30 am
`{
"jobType": 20, // selected job type
"interval": 1, // Execute every month
"target": 10 // every day 10
"executionHour": 23, // execute after 23:30 am
"executionMinute": 30 // execute after 23:30 am
"description": "Job name" // name of the given job
"data": { 'extraDataKey': 'extraDataValue' } // generic field to store any extra key/value data about the job
}`

Available Since
:   1.5.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [JobRestVO](https://api.fluig.com/old/json_JobRestVO.html) (JSON) | Request JSON (example):`{ "jobId": "Processar_mensagens_do_EAI", // the job ID "description": "Job para Processar mensagens do EAI", // Description of the job "interval": 3, // Use this property to create a job that will be executed every X months(s), where X is the value o this property "target": 10 // specififc day of the month when the job should be executed MAX VALUE 30 "executionHour": 10, // Use this property to configure that this job should be executed after HH hour (where HH range is 00 to 23) "executionMinute": 30, // Use this property to configure that this job should be executed after mm minute (where mm range is 00 to 60) "data": { // A string key-value map, to pass extra data to Job executor "datasetId" : "97" }, "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) // 0 - Expiração de Documentos // 1 - Tarefas Atrasadas // 2 - Fluxo Automático // 3 - Indexação de Documentos // 4 - Recalcular Volumes // 6 - Timer de início de Processo // 7 - Início condicional de Processo // 8 - Compactar Solicitações Finalizadas // 9 - Expiração de Tarefas // 10 - Início multiplo de Processo // 11 - Conversão de documentos para visualizador interno // 12 - Limpeza de arquivos Temporarios de documentos // 13 - Processar mensagens do EAI // 14 - Cancelar matrículas expiradas em turmas // 15 - Cancelar matrículas expiradas em treinamentos // 16 - Notificar aprovação de requisição de matrícula pendente // 17 - Notificar expiração de contas // 18 - Finalizar tópicos expirados // 19 - Processar requisições de matrícula // 20 - Limpeza de notificações // 22 - Monitoramento de métricas // 23 - Sincronização de Dataset }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message "content": { "jobId": "Processar_mensagens_do_EAI", // the job ID "companyId": 123, // The Tenant Id of the job "interval": 2 // Job is executed every 2 months "target": 10 // Job is executed at day 10 "executionHour": 10, // hour which the job will start to execute "executionMinute": 30, // minute which the job will start to execute "description": "Job para Processar mensagens do EAI", // Description of the job "recurrenceExpression": "0 00 00 1/1 * ? *", // The cron expression used to schedule the job "lastExecution": "2016-03-23 21:00:00", // The date of job's last execution "nextExecution": "2016-03-24 21:00:00", // The date of job's next execution "started": "true", // A boolean value to show if the jobs is started "data": { 'extraDataKey': 'extraDataValue' } // extra key/value data about the job "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.8

### POST /2.0/job/createWeekly

Create a job to be executed weekly.  
  
Return the job that was created.

#### Examples of use:

Execute the job on saturday every 2 weeks after 10:35 am
`{
"jobType": 20, // selected job type
"interval": 2, // Execute every 2 weeks
"target": 7 // every saturday
"executionHour": 10, // execute after 10:35 am
"executionMinute": 35 // execute after 10:35 am
"description": "Job name" // name of the given job
"data": { 'extraDataKey': 'extraDataValue' } // generic field to store any extra key/value data about the job
}`

Available Since
:   1.5.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [JobRestVO](https://api.fluig.com/old/json_JobRestVO.html) (JSON) | Request JSON (example):`{ "jobId": "Processar_mensagens_do_EAI", // the job ID "description": "Job para Processar mensagens do EAI", // Description of the job "interval": 3, // Use this property to create a job that will be executed every X week(s), where X is the value o this property "target": 7 // specififc day of the week when the job should be executed // 1 - Sunday // 2 - Monday // 3 - Tuesday // 4 - Wednesday // 5 - Thursday // 6 - Friday // 7 - Saturday "executionHour": 10, // Use this property to configure that this job should be executed after HH hour (where HH range is 00 to 23) "executionMinute": 30, // Use this property to configure that this job should be executed after mm minute (where mm range is 00 to 60) "data": { // A string key-value map, to pass extra data to Job executor "datasetId" : "97" }, "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) // 0 - Expiração de Documentos // 1 - Tarefas Atrasadas // 2 - Fluxo Automático // 3 - Indexação de Documentos // 4 - Recalcular Volumes // 6 - Timer de início de Processo // 7 - Início condicional de Processo // 8 - Compactar Solicitações Finalizadas // 9 - Expiração de Tarefas // 10 - Início multiplo de Processo // 11 - Conversão de documentos para visualizador interno // 12 - Limpeza de arquivos Temporarios de documentos // 13 - Processar mensagens do EAI // 14 - Cancelar matrículas expiradas em turmas // 15 - Cancelar matrículas expiradas em treinamentos // 16 - Notificar aprovação de requisição de matrícula pendente // 17 - Notificar expiração de contas // 18 - Finalizar tópicos expirados // 19 - Processar requisições de matrícula // 20 - Limpeza de notificações // 22 - Monitoramento de métricas // 23 - Sincronização de Dataset }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message "content": { "jobId": "Processar_mensagens_do_EAI", // the job ID "companyId": 123, // The Tenant Id of the job "interval": 5 // Job is executed every 5 weeks "target": 7 // Job is executed only at saturdays "executionHour": 10, // hour which the job will start to execute "executionMinute": 30, // minute which the job will start to execute "description": "Job para Processar mensagens do EAI", // Description of the job "recurrenceExpression": "0 00 00 1/1 * ? *", // The cron expression used to schedule the job "lastExecution": "2016-03-23 21:00:00", // The date of job's last execution "nextExecution": "2016-03-24 21:00:00", // The date of job's next execution "started": "true", // A boolean value to show if the jobs is started "data": { 'extraDataKey': 'extraDataValue' } // extra key/value data about the job "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.8

### POST /2.0/job/delete

Delete a job by company ID an job ID.

Available Since
:   1.5.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [JobRestVO](https://api.fluig.com/old/json_JobRestVO.html) (JSON) | Request JSON (example):`{ "jobId": "Processar_mensagens_do_EAI", // the job ID }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message "content": null, "message": { "message": "Job successfully removed", "detail": "Job successfully removed", "type": "INFO" } }` |

Available Since
:   1.5.8

### GET /2.0/job/list

List the jobs based on filter and pagination parameters

Available Since
:   1.5.8

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| filter | query | the pattern used to filter the results (Optional - default = "") |  |  |
| limit | query | limit of records returned (Optional - Default: 30) | 30 | int |
| offset | query | the offset (Optional - default = "0") | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message "content": [{ "jobId": "Processar_mensagens_do_EAI", // the job ID "companyId": 123, // The Tenant Id of the job "description": "Job para Processar mensagens do EAI", // Description of the job "recurrenceExpression": "0 00 00 1/1 * ? *", // The cron expression used to schedule the job "lastExecution": "2016-03-23 21:00:00", // The date of job's last execution "nextExecution": "2016-03-24 21:00:00", // The date of job's next execution "interval": 3, // Execution interval of the job "target": 10 // target execution day ( 1-7 for intervalType = 'WEEKLY' or 1-30 for intervalType = 'MONTHLY') "started": "true", // A boolean value to show if the jobs is started "data": { // A string key-value map, to get extra data to Job executor "datasetId" : "97" }, "jobType": 13 // Current valid values existing in JobTypes enum (com.fluig.foundation.scheduler.entity.JobTypes) // 0 - Expiração de Documentos // 1 - Tarefas Atrasadas // 2 - Fluxo Automático // 3 - Indexação de Documentos // 4 - Recalcular Volumes // 6 - Timer de início de Processo // 7 - Início condicional de Processo // 8 - Compactar Solicitações Finalizadas // 9 - Expiração de Tarefas // 10 - Início multiplo de Processo // 11 - Conversão de documentos para visualizador interno // 12 - Limpeza de arquivos Temporarios de documentos // 13 - Processar mensagens do EAI // 14 - Cancelar matrículas expiradas em turmas // 15 - Cancelar matrículas expiradas em treinamentos // 16 - Notificar aprovação de requisição de matrícula pendente // 17 - Notificar expiração de contas // 18 - Finalizar tópicos expirados // 19 - Processar requisições de matrícula // 20 - Limpeza de notificações // 22 - Monitoramento de métricas // 23 - Sincronização de Dataset }], "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |
