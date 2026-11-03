---
content_hash: f876ef12bfa4d5c01925d2f8cb3b772721b6db1f5a9ec21bd690c697a974dbef
fetched_at: '2026-11-03T14:34:37.558639+00:00'
page_id: json_JaxbHbmNativeQueryReturnType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNativeQueryReturnType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNativeQueryReturnType.html
version: 1
---

# JaxbHbmNativeQueryReturnType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| alias | string |  |
| returnProperty | array of [JaxbHbmNativeQueryPropertyReturnType](https://api.fluig.com/old/json_JaxbHbmNativeQueryPropertyReturnType.html) |  |
| clazz | string |  |
| entityName | string |  |
| returnDiscriminator | [JaxbHbmReturnDiscriminator](https://api.fluig.com/old/json_JaxbHbmReturnDiscriminator.html) |  |
| lockMode | [LockMode](https://api.fluig.com/old/json_LockMode.html) |  |

Example

```
{
  "alias" : "...",
  "returnProperty" : [ {
    "name" : "...",
    "returnColumn" : [ {
      "name" : "..."
    }, {
      "name" : "..."
    } ],
    "column" : "..."
  }, {
    "name" : "...",
    "returnColumn" : [ {
      "name" : "..."
    }, {
      "name" : "..."
    } ],
    "column" : "..."
  } ],
  "clazz" : "...",
  "entityName" : "...",
  "returnDiscriminator" : {
    "column" : "..."
  },
  "lockMode" : "FORCE"
}
```
