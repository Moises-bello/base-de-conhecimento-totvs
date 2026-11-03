---
content_hash: bc28263dde7b5451ee5edd4bb3d99a70bbee3ec2847dbff3624ef0977b1e8e2a
fetched_at: '2026-11-03T14:34:37.246479+00:00'
page_id: json_JaxbCfgSecurity
product: fluig
source: rest-fluig
title: Fluig REST — JaxbCfgSecurity Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbCfgSecurity.html
version: 1
---

# JaxbCfgSecurity Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| context | string |  |
| grant | array of [JaxbCfgGrant](https://api.fluig.com/old/json_JaxbCfgGrant.html) |  |

Example

```
{
  "context" : "...",
  "grant" : [ {
    "entityName" : "...",
    "actions" : "...",
    "role" : "..."
  }, {
    "entityName" : "...",
    "actions" : "...",
    "role" : "..."
  } ]
}
```
