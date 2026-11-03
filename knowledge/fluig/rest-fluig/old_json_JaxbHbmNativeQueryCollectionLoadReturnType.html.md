---
content_hash: ac8f811fe9f0afcef413dca9b5234fb5fa217faca260479883477a7d6aea68c8
fetched_at: '2026-11-03T14:34:37.549384+00:00'
page_id: json_JaxbHbmNativeQueryCollectionLoadReturnType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNativeQueryCollectionLoadReturnType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNativeQueryCollectionLoadReturnType.html
version: 1
---

# JaxbHbmNativeQueryCollectionLoadReturnType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| alias | string |  |
| lockMode | [LockMode](https://api.fluig.com/old/json_LockMode.html) |  |
| returnProperty | array of [JaxbHbmNativeQueryPropertyReturnType](https://api.fluig.com/old/json_JaxbHbmNativeQueryPropertyReturnType.html) |  |
| role | string |  |

Example

```
{
  "alias" : "...",
  "lockMode" : "PESSIMISTIC_WRITE",
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
  "role" : "..."
}
```
