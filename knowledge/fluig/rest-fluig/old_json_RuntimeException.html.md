---
content_hash: 08d3c2dd37a89f3c5aa874462387dabe85fcbaa5473ad4d8fb156d26f9e59d65
fetched_at: '2026-11-03T14:34:38.311520+00:00'
page_id: json_RuntimeException
product: fluig
source: rest-fluig
title: Fluig REST — RuntimeException Data Type
type: documentation
url: https://api.fluig.com/old/json_RuntimeException.html
version: 1
---

# RuntimeException Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| Properties inherited from [Throwable](https://api.fluig.com/old/json_Throwable.html) | | |
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
