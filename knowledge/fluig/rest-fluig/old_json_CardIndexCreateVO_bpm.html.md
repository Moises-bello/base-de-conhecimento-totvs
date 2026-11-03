---
content_hash: dcc51ffeb1c2e9b2e32c8e019459759ec0aa6a8987f797e9c2700b8dbd3cf96e
fetched_at: '2026-11-03T14:34:36.368971+00:00'
page_id: json_CardIndexCreateVO_bpm
product: fluig
source: rest-fluig
title: Fluig REST — CardIndexCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardIndexCreateVO_bpm.html
version: 1
---

# CardIndexCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| attachments | array of [CardIndexAttachmentCreateVO](https://api.fluig.com/old/json_CardIndexAttachmentCreateVO.html) |  |
| tenantId | number |  |
| parentDocumentId | number |  |
| publisherId | string |  |
| documentDescription | string |  |
| cardDescription | string |  |
| datasetName | string |  |
| persistenceType | number |  |

Example

```
{
  "attachments" : [ {
    "fileName" : "...",
    "principal" : true,
    "attach" : true
  }, {
    "fileName" : "...",
    "principal" : true,
    "attach" : true
  } ],
  "tenantId" : 12345,
  "parentDocumentId" : 12345,
  "publisherId" : "...",
  "documentDescription" : "...",
  "cardDescription" : "...",
  "datasetName" : "...",
  "persistenceType" : 12345
}
```
