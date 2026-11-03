---
content_hash: 77154d3ad0337fb8398610898bda2f425f2ece22447903566e985196a6def438
fetched_at: '2026-11-03T14:34:36.420589+00:00'
page_id: json_ClassLoader
product: fluig
source: rest-fluig
title: Fluig REST — ClassLoader Data Type
type: documentation
url: https://api.fluig.com/old/json_ClassLoader.html
version: 1
---

# ClassLoader Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| registeredAsParallelCapable | boolean | required |  |
| platformClassLoader | [ClassLoader](https://api.fluig.com/old/json_ClassLoader.html) |  |  |
| definedPackages | array of [Package](https://api.fluig.com/old/json_Package.html) |  |  |
| name | string |  |  |
| unnamedModule | [Module](https://api.fluig.com/old/json_Module.html) |  |  |
| parent | [ClassLoader](https://api.fluig.com/old/json_ClassLoader.html) |  |  |
| systemClassLoader | [ClassLoader](https://api.fluig.com/old/json_ClassLoader.html) |  |  |

Example

```
{
  "registeredAsParallelCapable" : true,
  "platformClassLoader" : {
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
    "classLoader" : {
      "registeredAsParallelCapable" : true,
      "platformClassLoader" : { },
      "definedPackages" : [ { }, { } ],
      "name" : "...",
      "unnamedModule" : { },
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
  },
  "parent" : {
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
  "systemClassLoader" : {
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
  }
}
```
