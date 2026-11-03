---
content_hash: 0730c09467ead57b3698604242288e7293604180d28c95cf21b8e3a0175c366f
fetched_at: '2026-11-03T14:34:37.929433+00:00'
page_id: json_Package
product: fluig
source: rest-fluig
title: Fluig REST — Package Data Type
type: documentation
url: https://api.fluig.com/old/json_Package.html
version: 1
---

# Package Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| implementationTitle | string |  |  |
| sealed | boolean | required |  |
| declaredAnnotations | array of [Annotation](https://api.fluig.com/old/json_Annotation.html) |  |  |
| packages | array of [Package](https://api.fluig.com/old/json_Package.html) |  |  |
| implementationVersion | string |  |  |
| implementationVendor | string |  |  |
| specificationVersion | string |  |  |
| specificationTitle | string |  |  |
| annotations | array of [Annotation](https://api.fluig.com/old/json_Annotation.html) |  |  |
| specificationVendor | string |  |  |
| name | string |  |  |

Example

```
{
  "implementationTitle" : "...",
  "sealed" : true,
  "declaredAnnotations" : [ { }, { } ],
  "packages" : [ {
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
  "implementationVersion" : "...",
  "implementationVendor" : "...",
  "specificationVersion" : "...",
  "specificationTitle" : "...",
  "annotations" : [ { }, { } ],
  "specificationVendor" : "...",
  "name" : "..."
}
```
