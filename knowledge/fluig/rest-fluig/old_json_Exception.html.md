---
content_hash: 8e63e87bab2a60caf830375350eb61c16b5e1bd98f9d1db82a7b2bf7741ae706
fetched_at: '2026-11-03T14:34:36.779842+00:00'
page_id: json_Exception
product: fluig
source: rest-fluig
title: Fluig REST — Exception Data Type
type: documentation
url: https://api.fluig.com/old/json_Exception.html
version: 1
---

# Exception Data Type

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
