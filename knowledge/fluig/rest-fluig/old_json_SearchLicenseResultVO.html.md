---
content_hash: 8f10d90b43786661aec8f4709cb630de12834dbbadf0543f4e55be0df8522af3
fetched_at: '2026-11-03T14:34:38.327265+00:00'
page_id: json_SearchLicenseResultVO
product: fluig
source: rest-fluig
title: Fluig REST — SearchLicenseResultVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchLicenseResultVO.html
version: 1
---

# SearchLicenseResultVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| hasNext | boolean |  |
| licenses | array of [LicenseDataVO](https://api.fluig.com/old/json_LicenseDataVO.html) |  |

Example

```
{
  "hasNext" : true,
  "licenses" : [ {
    "remainingLicenses" : 12345,
    "tenantId" : 12345,
    "activeUsers" : 12345,
    "totalLicenses" : 12345
  }, {
    "remainingLicenses" : 12345,
    "tenantId" : 12345,
    "activeUsers" : 12345,
    "totalLicenses" : 12345
  } ]
}
```
