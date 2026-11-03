---
content_hash: 651a133ce01741eb950d3291d9a6d7bf603ccabc5d078e7df90ebdaac02a1ab8
fetched_at: '2026-11-03T14:34:37.057266+00:00'
page_id: json_FormDatasetVO
product: fluig
source: rest-fluig
title: Fluig REST — FormDatasetVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FormDatasetVO.html
version: 1
---

# FormDatasetVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| mobileCache | boolean | required |  |
| version | number | required |  |
| documentId | number |  |  |
| type | string |  |  |
| datasetId | string |  |  |
| serverOffline | boolean | required |  |
| id | number |  |  |
| companyId | number | required |  |

Example

```
{
  "mobileCache" : true,
  "version" : 12345,
  "documentId" : 12345,
  "type" : "...",
  "datasetId" : "...",
  "serverOffline" : true,
  "id" : 12345,
  "companyId" : 12345
}
```
