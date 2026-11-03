---
content_hash: 710052cfc6271bc69d66f37d0a78029bebac4960d145e3f089cfca8f94a4fc06
fetched_at: '2026-11-03T14:34:36.375580+00:00'
page_id: json_CardIndexVO
product: fluig
source: rest-fluig
title: Fluig REST — CardIndexVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardIndexVO.html
version: 1
---

# CardIndexVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| publisherId | string |  |
| cardDescription | string |  |
| tenantId | number |  |
| parentDocumentId | number |  |
| attachments | array of [CardIndexAttachmentVO](https://api.fluig.com/old/json_CardIndexAttachmentVO.html) |  |
| datasetName | string |  |
| documentId | number |  |
| documentDescription | string |  |
| persistenceType | number |  |

Example

```
{
  "publisherId" : "...",
  "cardDescription" : "...",
  "tenantId" : 12345,
  "parentDocumentId" : 12345,
  "attachments" : [ {
    "fileName" : "...",
    "principal" : true,
    "attach" : true
  }, {
    "fileName" : "...",
    "principal" : true,
    "attach" : true
  } ],
  "datasetName" : "...",
  "documentId" : 12345,
  "documentDescription" : "...",
  "persistenceType" : 12345
}
```
