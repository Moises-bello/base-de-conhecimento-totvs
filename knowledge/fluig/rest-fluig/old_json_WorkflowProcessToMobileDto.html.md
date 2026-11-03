---
content_hash: f0ad98c88ff60c28b22829abe1ff589898b9a17317b19bd8fcee4afb606a5001
fetched_at: '2026-11-03T14:34:39.124411+00:00'
page_id: json_WorkflowProcessToMobileDto
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessToMobileDto Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessToMobileDto.html
version: 1
---

# WorkflowProcessToMobileDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| code | string |  |  |
| sourceThreadSequence | number |  |  |
| documentDescription | string |  |  |
| movementHour | string |  |  |
| startupHour | string |  |  |
| colleagueName | string |  |  |
| stateId | number |  |  |
| counterSign | boolean |  |  |
| viewed | boolean |  |  |
| requesterName | string |  |  |
| canCancel | boolean |  |  |
| mainAttachmentDocumentId | number |  |  |
| active | boolean |  |  |
| url | string |  |  |
| processDescription | string |  |  |
| formCode | number |  |  |
| requesterId | string |  |  |
| mainAttachmentDocumentVersion | number | required |  |
| version | number |  |  |
| sourceProcess | number |  |  |
| hasParallel | boolean |  |  |
| stateDescription | string |  |  |
| companyId | number | required |  |
| approachingExpiration | boolean |  |  |
| movementSequence | number | required |  |
| expired | boolean |  |  |
| processDiagram | string |  |  |
| mobileReady | boolean |  |  |
| deadlineText | string |  |  |
| canTake | boolean |  |  |
| processInstanceId | number | required |  |
| attachmentSeqId | number |  |  |
| processId | string |  |  |
| deadlineDate | number |  |  |
| relatedDatasets | array of string |  |  |
| rowId | number | required |  |

Example

```
{
  "code" : "...",
  "sourceThreadSequence" : 12345,
  "documentDescription" : "...",
  "movementHour" : "...",
  "startupHour" : "...",
  "colleagueName" : "...",
  "stateId" : 12345,
  "counterSign" : true,
  "viewed" : true,
  "requesterName" : "...",
  "canCancel" : true,
  "mainAttachmentDocumentId" : 12345,
  "active" : true,
  "url" : "...",
  "processDescription" : "...",
  "formCode" : 12345,
  "requesterId" : "...",
  "mainAttachmentDocumentVersion" : 12345,
  "version" : 12345,
  "sourceProcess" : 12345,
  "hasParallel" : true,
  "stateDescription" : "...",
  "companyId" : 12345,
  "approachingExpiration" : true,
  "movementSequence" : 12345,
  "expired" : true,
  "processDiagram" : "...",
  "mobileReady" : true,
  "deadlineText" : "...",
  "canTake" : true,
  "processInstanceId" : 12345,
  "attachmentSeqId" : 12345,
  "processId" : "...",
  "deadlineDate" : 12345,
  "relatedDatasets" : [ "...", "..." ],
  "rowId" : 12345
}
```
