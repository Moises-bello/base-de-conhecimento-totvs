---
content_hash: bade3d0f72e47a366ead66a81430667336d0884c48ed600850d2891642da3255
fetched_at: '2026-11-03T14:34:38.699437+00:00'
page_id: json_Throwable
product: fluig
source: rest-fluig
title: Fluig REST — Throwable Data Type
type: documentation
url: https://api.fluig.com/old/json_Throwable.html
version: 1
---

# Throwable Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| message | string |  |
| stackTrace | array of [StackTraceElement](https://api.fluig.com/old/json_StackTraceElement.html) |  |
| localizedMessage | string |  |
| cause | [Throwable](https://api.fluig.com/old/json_Throwable.html) |  |
| suppressed | array of [Throwable](https://api.fluig.com/old/json_Throwable.html) |  |

Example

```
{
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
