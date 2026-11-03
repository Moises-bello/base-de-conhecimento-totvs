---
content_hash: 8d8536e4745759032dd06c4eabce7d4ec5cafd097d1cb96265efe4beb278ffaa
fetched_at: '2026-11-03T14:34:37.850931+00:00'
page_id: json_Module
product: fluig
source: rest-fluig
title: Fluig REST — Module Data Type
type: documentation
url: https://api.fluig.com/old/json_Module.html
version: 1
---

# Module Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| named | boolean | required |  |
| classLoader | [ClassLoader](https://api.fluig.com/old/json_ClassLoader.html) |  |  |
| packages | array of string |  |  |
| descriptor | [ModuleDescriptor](https://api.fluig.com/old/json_ModuleDescriptor.html) |  |  |
| name | string |  |  |
| layer | [ModuleLayer](https://api.fluig.com/old/json_ModuleLayer.html) |  |  |
| annotations | array of [Annotation](https://api.fluig.com/old/json_Annotation.html) |  |  |
| declaredAnnotations | array of [Annotation](https://api.fluig.com/old/json_Annotation.html) |  |  |

Example

```
{
  "named" : true,
  "classLoader" : {
    "registeredAsParallelCapable" : true,
    "platformClassLoader" : { },
    "definedPackages" : [ {
      "implementationTitle" : "...",
      "sealed" : true,
      "declaredAnnotations" : [ { }, { } ],
      "packages" : [ { }, { } ],
      "implementationVersion" : "...",
      "implementationVendor" : "...",
      "specificationVersion" : "...",
      "specificationTitle" : "...",
      "annotations" : [ { }, { } ],
      "specificationVendor" : "...",
      "name" : "..."
    }, {
      "implementationTitle" : "...",
      "sealed" : true,
      "declaredAnnotations" : [ { }, { } ],
      "packages" : [ { }, { } ],
      "implementationVersion" : "...",
      "implementationVendor" : "...",
      "specificationVersion" : "...",
      "specificationTitle" : "...",
      "annotations" : [ { }, { } ],
      "specificationVendor" : "...",
      "name" : "..."
    } ],
    "name" : "...",
    "unnamedModule" : {
      "named" : true,
      "classLoader" : { },
      "packages" : [ "...", "..." ],
      "descriptor" : { },
      "name" : "...",
      "layer" : { },
      "annotations" : [ { }, { } ],
      "declaredAnnotations" : [ { }, { } ]
    },
    "parent" : { },
    "systemClassLoader" : { }
  },
  "packages" : [ "...", "..." ],
  "descriptor" : {
    "open" : true,
    "automatic" : true
  },
  "name" : "...",
  "layer" : { },
  "annotations" : [ { }, { } ],
  "declaredAnnotations" : [ { }, { } ]
}
```
