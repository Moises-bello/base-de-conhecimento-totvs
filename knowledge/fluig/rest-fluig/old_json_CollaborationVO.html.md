---
content_hash: 039f4a787423e6fa56078636e30deacc09fd4175313335fbc2ee1bd17b1478d7
fetched_at: '2026-11-03T14:34:36.444560+00:00'
page_id: json_CollaborationVO
product: fluig
source: rest-fluig
title: Fluig REST — CollaborationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CollaborationVO.html
version: 1
---

# CollaborationVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sourceDocumentVersion | number | required |  |
| uploaderLogin | string |  |  |
| collaborationId | number |  |  |
| endDate | number |  |  |
| documentVersion | number |  |  |
| documentId | number |  |  |
| tenantId | number |  |  |
| startDate | number |  |  |
| oauthCode | string |  |  |
| sourceDocumentId | number | required |  |
| guests | array of string |  |  |

Example

```
{
  "sourceDocumentVersion" : 12345,
  "uploaderLogin" : "...",
  "collaborationId" : 12345,
  "endDate" : 12345,
  "documentVersion" : 12345,
  "documentId" : 12345,
  "tenantId" : 12345,
  "startDate" : 12345,
  "oauthCode" : "...",
  "sourceDocumentId" : 12345,
  "guests" : [ "...", "..." ]
}
```
