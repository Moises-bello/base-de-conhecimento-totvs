---
content_hash: 2a698c353b332ed28f9711e9bb6d6824cffe4b70ac98af2ed347fd1ac4e7ae68
fetched_at: '2026-11-03T14:34:38.271003+00:00'
page_id: json_RestorePermissionsVO
product: fluig
source: rest-fluig
title: Fluig REST — RestorePermissionsVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RestorePermissionsVO.html
version: 1
---

# RestorePermissionsVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| permissions | array of [RestorePermissionObjectVO](https://api.fluig.com/old/json_RestorePermissionObjectVO.html) |  |

Example

```
{
  "permissions" : [ {
    "role" : "...",
    "code" : "...",
    "user" : "...",
    "description" : "..."
  }, {
    "role" : "...",
    "code" : "...",
    "user" : "...",
    "description" : "..."
  } ]
}
```
