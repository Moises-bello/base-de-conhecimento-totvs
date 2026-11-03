---
content_hash: cb056507f11e13d83f0b33e2ae51e88c9975d2447403ba7c511cf687b349fce3
fetched_at: '2026-11-03T14:34:39.098099+00:00'
page_id: json_WorkflowProcessDto
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessDto Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessDto.html
version: 1
---

# WorkflowProcessDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sourceProcess | number |  |  |
| colleagueName | string |  |  |
| mainAttachmentDocumentId | number |  |  |
| code | string |  |  |
| processId | string |  |  |
| processDescription | string |  |  |
| movementHour | string |  |  |
| startupHour | string |  |  |
| companyId | number | required |  |
| documentDescription | string |  |  |
| processInstanceId | number | required |  |
| formRecordId | number |  |  |
| mobileReady | boolean |  |  |
| mainAttachmentDocumentVersion | number | required |  |
| formCode | number | required |  |
| canTake | boolean |  |  |
| stateId | number |  |  |
| requesterId | string |  |  |
| deadlineText | string |  |  |
| stateDescription | string |  |  |
| version | number |  |  |
| deadlineDate | number |  |  |
| attachmentSeqId | number |  |  |
| sourceThreadSequence | number |  |  |
| movementSequence | number | required |  |
| relatedDatasets | array of string |  |  |
| active | boolean |  |  |
| canCancel | boolean |  |  |
| requesterName | string |  |  |
| url | string |  |  |
| rowId | number | required |  |
| counterSign | boolean |  |  |

Example

```
{
  "sourceProcess" : 12345,
  "colleagueName" : "...",
  "mainAttachmentDocumentId" : 12345,
  "code" : "...",
  "processId" : "...",
  "processDescription" : "...",
  "movementHour" : "...",
  "startupHour" : "...",
  "companyId" : 12345,
  "documentDescription" : "...",
  "processInstanceId" : 12345,
  "formRecordId" : 12345,
  "mobileReady" : true,
  "mainAttachmentDocumentVersion" : 12345,
  "formCode" : 12345,
  "canTake" : true,
  "stateId" : 12345,
  "requesterId" : "...",
  "deadlineText" : "...",
  "stateDescription" : "...",
  "version" : 12345,
  "deadlineDate" : 12345,
  "attachmentSeqId" : 12345,
  "sourceThreadSequence" : 12345,
  "movementSequence" : 12345,
  "relatedDatasets" : [ "...", "..." ],
  "active" : true,
  "canCancel" : true,
  "requesterName" : "...",
  "url" : "...",
  "rowId" : 12345,
  "counterSign" : true
}
```
