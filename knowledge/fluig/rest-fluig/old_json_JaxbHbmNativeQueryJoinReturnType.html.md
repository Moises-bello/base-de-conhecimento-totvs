---
content_hash: 2f21721e4d4274f551120ce863842f515eba8e37832db2f68d76b0fb23b4defa
fetched_at: '2026-11-03T14:34:37.552433+00:00'
page_id: json_JaxbHbmNativeQueryJoinReturnType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNativeQueryJoinReturnType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNativeQueryJoinReturnType.html
version: 1
---

# JaxbHbmNativeQueryJoinReturnType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| alias | string |  |
| lockMode | [LockMode](https://api.fluig.com/old/json_LockMode.html) |  |
| returnProperty | array of [JaxbHbmNativeQueryPropertyReturnType](https://api.fluig.com/old/json_JaxbHbmNativeQueryPropertyReturnType.html) |  |
| property | string |  |

Example

```
{
  "alias" : "...",
  "lockMode" : "PESSIMISTIC_FORCE_INCREMENT",
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
  "property" : "..."
}
```
