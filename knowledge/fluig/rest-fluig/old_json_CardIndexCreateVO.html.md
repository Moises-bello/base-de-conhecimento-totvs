---
content_hash: 68038501d4bdb72da5b716b7bec707e106910a96c53e7783d58eff528ed42343
fetched_at: '2026-11-03T14:34:36.365331+00:00'
page_id: json_CardIndexCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — CardIndexCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardIndexCreateVO.html
version: 1
---

# CardIndexCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| tenantId | number |  |
| attachments | array of [CardIndexAttachmentCreateVO](https://api.fluig.com/old/json_CardIndexAttachmentCreateVO_workflow.html) |  |
| documentDescription | string |  |
| cardDescription | string |  |
| persistenceType | number |  |
| parentDocumentId | number |  |
| datasetName | string |  |
| publisherId | string |  |

Example

```
{
  "tenantId" : 12345,
  "attachments" : [ {
    "principal" : true,
    "attach" : true,
    "fileName" : "..."
  }, {
    "principal" : true,
    "attach" : true,
    "fileName" : "..."
  } ],
  "documentDescription" : "...",
  "cardDescription" : "...",
  "persistenceType" : 12345,
  "parentDocumentId" : 12345,
  "datasetName" : "...",
  "publisherId" : "..."
}
```
