---
content_hash: 09023769744fd6be55f39a7b109923c2a10f2865d7839198528d8545b15a8c64
fetched_at: '2026-11-03T14:34:36.865961+00:00'
page_id: json_FDNResourceTypePermission
product: fluig
source: rest-fluig
title: Fluig REST — FDNResourceTypePermission Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNResourceTypePermission.html
version: 1
---

# FDNResourceTypePermission Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| resourceType | [FDNResourceType](https://api.fluig.com/old/json_FDNResourceType.html) |  |
| description | string |  |
| permission | string |  |
| selected | boolean |  |

Example

```
{
  "id" : 12345,
  "resourceType" : {
    "isInternal" : true,
    "code" : "...",
    "id" : 12345,
    "description" : "..."
  },
  "description" : "...",
  "permission" : "...",
  "selected" : true
}
```
