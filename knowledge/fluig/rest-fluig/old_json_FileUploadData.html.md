---
content_hash: 5aeafcde0df6a0809ae1069c54b33462b30182345b3b184aed489e10a5b35465
fetched_at: '2026-11-03T14:34:36.958264+00:00'
page_id: json_FileUploadData
product: fluig
source: rest-fluig
title: Fluig REST — FileUploadData Data Type
type: documentation
url: https://api.fluig.com/old/json_FileUploadData.html
version: 1
---

# FileUploadData Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| id | number | required |  |
| version | number | required |  |
| versionAction | string |  |  |
| fileName | string |  |  |
| comments | string |  |  |
| uploadId | string |  |  |
| markupProcessId | string |  |  |
| viewingSessionId | string |  |  |
| expires | boolean |  |  |
| expirationDate | number |  |  |

Example

```
{
  "id" : 12345,
  "version" : 12345,
  "versionAction" : "...",
  "fileName" : "...",
  "comments" : "...",
  "uploadId" : "...",
  "markupProcessId" : "...",
  "viewingSessionId" : "...",
  "expires" : true,
  "expirationDate" : 12345
}
```
