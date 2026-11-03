---
content_hash: bc8ed1553a8fd55fe6f1226c10034cda0465b9b8f4452252e4b2087cfbc263c4
fetched_at: '2026-11-03T14:34:36.816022+00:00'
page_id: json_FDNException
product: fluig
source: rest-fluig
title: Fluig REST — FDNException Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNException.html
version: 1
---

# FDNException Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| parameters | array of object |  |
| status | [Status](https://api.fluig.com/old/json_Status.html) |  |
| code | string |  |
| Properties inherited from [Throwable](https://api.fluig.com/old/json_Throwable.html) | | |
| message | string |  |
| stackTrace | array of [StackTraceElement](https://api.fluig.com/old/json_StackTraceElement.html) |  |
| localizedMessage | string |  |
| cause | [Throwable](https://api.fluig.com/old/json_Throwable.html) |  |
| suppressed | array of [Throwable](https://api.fluig.com/old/json_Throwable.html) |  |

Example

```
{
  "parameters" : [ { }, { } ],
  "status" : "BAD_REQUEST",
  "code" : "...",
  "message" : "...",
  "stackTrace" : [ {
    "methodName" : "...",
    "fileName" : "...",
    "classLoaderName" : "...",
    "moduleName" : "...",
    "lineNumber" : 12345,
    "nativeMethod" : true,
    "className" : "...",
    "moduleVersion" : "..."
  }, {
    "methodName" : "...",
    "fileName" : "...",
    "classLoaderName" : "...",
    "moduleName" : "...",
    "lineNumber" : 12345,
    "nativeMethod" : true,
    "className" : "...",
    "moduleVersion" : "..."
  } ],
  "localizedMessage" : "...",
  "cause" : {
    "message" : "...",
    "stackTrace" : [ {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    }, {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    } ],
    "localizedMessage" : "...",
    "cause" : { },
    "suppressed" : [ { }, { } ]
  },
  "suppressed" : [ {
    "message" : "...",
    "stackTrace" : [ {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    }, {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    } ],
    "localizedMessage" : "...",
    "cause" : { },
    "suppressed" : [ { }, { } ]
  }, {
    "message" : "...",
    "stackTrace" : [ {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    }, {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    } ],
    "localizedMessage" : "...",
    "cause" : { },
    "suppressed" : [ { }, { } ]
  } ]
}
```
