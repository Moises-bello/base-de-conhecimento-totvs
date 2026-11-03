---
content_hash: 842333fbdde6d72c277e6e25798ed355670f9e65b6334b631fa91677b0f03367
fetched_at: '2026-11-03T14:34:36.149218+00:00'
page_id: json_AllocatedDocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — AllocatedDocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AllocatedDocumentVO.html
version: 1
---

# AllocatedDocumentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sourceVersion | number | required |  |
| checkoutDate | number |  |  |
| sourceDocument | number | required |  |
| checkinTime | string |  |  |
| checkoutAllowed | boolean |  |  |
| destinationDocument | number | required |  |
| colleagueId | string |  |  |
| active | boolean |  |  |
| comment | string |  |  |
| colleagueName | string |  |  |
| checkinDate | number |  |  |
| companyId | number | required |  |
| checkoutTime | string |  |  |

Example

```
{
  "sourceVersion" : 12345,
  "checkoutDate" : 12345,
  "sourceDocument" : 12345,
  "checkinTime" : "...",
  "checkoutAllowed" : true,
  "destinationDocument" : 12345,
  "colleagueId" : "...",
  "active" : true,
  "comment" : "...",
  "colleagueName" : "...",
  "checkinDate" : 12345,
  "companyId" : 12345,
  "checkoutTime" : "..."
}
```
