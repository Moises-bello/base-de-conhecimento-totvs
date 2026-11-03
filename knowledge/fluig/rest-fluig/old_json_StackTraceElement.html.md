---
content_hash: 8b71ef5588343ef79a135b3a9fe74d80a5a080da76e64d78d802171273c28b66
fetched_at: '2026-11-03T14:34:38.578388+00:00'
page_id: json_StackTraceElement
product: fluig
source: rest-fluig
title: Fluig REST — StackTraceElement Data Type
type: documentation
url: https://api.fluig.com/old/json_StackTraceElement.html
version: 1
---

# StackTraceElement Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| methodName | string |  |  |
| fileName | string |  |  |
| classLoaderName | string |  |  |
| moduleName | string |  |  |
| lineNumber | number | required |  |
| nativeMethod | boolean | required |  |
| className | string |  |  |
| moduleVersion | string |  |  |

Example

```
{
  "methodName" : "...",
  "fileName" : "...",
  "classLoaderName" : "...",
  "moduleName" : "...",
  "lineNumber" : 12345,
  "nativeMethod" : true,
  "className" : "...",
  "moduleVersion" : "..."
}
```
