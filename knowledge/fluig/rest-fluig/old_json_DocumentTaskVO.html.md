---
content_hash: d4b3c5a7603a6fd1eb7503c333694c3cbe0f00acc9bf3ba6d60808b3ba861ff3
fetched_at: '2026-11-03T14:34:36.684398+00:00'
page_id: json_DocumentTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentTaskVO.html
version: 1
---

# DocumentTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| documentDescription | string |  |  |
| documentId | number |  |  |
| version | number | required |  |
| approved | number | required |  |
| approvedString | string |  |  |
| documentType | string |  |  |
| colleagueName | string |  |  |
| publisherName | string |  |  |
| know | boolean | required |  |
| lastModifiedDate | number |  |  |

Example

```
{
  "documentDescription" : "...",
  "documentId" : 12345,
  "version" : 12345,
  "approved" : 12345,
  "approvedString" : "...",
  "documentType" : "...",
  "colleagueName" : "...",
  "publisherName" : "...",
  "know" : true,
  "lastModifiedDate" : 12345
}
```
