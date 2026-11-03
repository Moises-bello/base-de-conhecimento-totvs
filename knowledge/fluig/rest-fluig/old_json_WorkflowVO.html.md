---
content_hash: 6f2a2ed127a7ea3221791b06f398e47ee024763d393d38acbe07462452be8ad0
fetched_at: '2026-11-03T14:34:39.160691+00:00'
page_id: json_WorkflowVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowVO.html
version: 1
---

# WorkflowVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processId | string |  |  |
| deadlineDate | number |  |  |
| rowId | number | required |  |
| processDescription | string |  |  |
| movementHour | string |  |  |
| mainAttachmentDocumentVersion | number | required |  |
| mainAttachmentDocumentId | number |  |  |
| colleagueName | string |  |  |
| movementSequence | number | required |  |
| active | boolean |  |  |
| documentDescription | string |  |  |
| sourceThreadSequence | number |  |  |
| deadlineText | string |  |  |
| version | number |  |  |
| canCancel | boolean |  |  |
| code | string |  |  |
| sourceProcess | number |  |  |
| mobileReady | boolean |  |  |
| canTake | boolean |  |  |
| processInstanceId | number | required |  |
| attachmentSeqId | number |  |  |
| url | string |  |  |
| requesterId | string |  |  |
| stateDescription | string |  |  |
| stateId | number |  |  |
| companyId | number | required |  |
| requesterName | string |  |  |

Example

```
{
  "processId" : "...",
  "deadlineDate" : 12345,
  "rowId" : 12345,
  "processDescription" : "...",
  "movementHour" : "...",
  "mainAttachmentDocumentVersion" : 12345,
  "mainAttachmentDocumentId" : 12345,
  "colleagueName" : "...",
  "movementSequence" : 12345,
  "active" : true,
  "documentDescription" : "...",
  "sourceThreadSequence" : 12345,
  "deadlineText" : "...",
  "version" : 12345,
  "canCancel" : true,
  "code" : "...",
  "sourceProcess" : 12345,
  "mobileReady" : true,
  "canTake" : true,
  "processInstanceId" : 12345,
  "attachmentSeqId" : 12345,
  "url" : "...",
  "requesterId" : "...",
  "stateDescription" : "...",
  "stateId" : 12345,
  "companyId" : 12345,
  "requesterName" : "..."
}
```
