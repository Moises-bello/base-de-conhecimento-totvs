---
content_hash: 714017823a8c4d7a5bfa319cc366a1276f001d3a8144e4de226b23656e667c0e
fetched_at: '2026-11-03T14:34:38.178730+00:00'
page_id: json_PushConfigurationException
product: fluig
source: rest-fluig
title: Fluig REST — PushConfigurationException Data Type
type: documentation
url: https://api.fluig.com/old/json_PushConfigurationException.html
version: 1
---

# PushConfigurationException Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| Properties inherited from [FDNException](https://api.fluig.com/old/json_FDNException.html) | | |
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
  "status" : "NOT_ACCEPTABLE",
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
