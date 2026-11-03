---
content_hash: 5a827614156779a16a5e1b6e49b6cf0e05a443e9d2aae3ee039b5c8056bc4362
fetched_at: '2026-11-03T14:34:36.860206+00:00'
page_id: json_FDNResource
product: fluig
source: rest-fluig
title: Fluig REST — FDNResource Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNResource.html
version: 1
---

# FDNResource Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| description | string |  |
| categoryResources | array of [FDNCategoryResource](https://api.fluig.com/old/json_FDNCategoryResource.html) |  |
| longDescription | string |  |
| tenantId | number |  |
| method | string |  |
| code | string |  |
| type | [FDNResourceType](https://api.fluig.com/old/json_FDNResourceType.html) |  |
| isInternal | boolean |  |
| id | number |  |
| parent | [FDNResource](https://api.fluig.com/old/json_FDNResource.html) |  |
| typeCode | string |  |

Example

```
{
  "description" : "...",
  "categoryResources" : [ {
    "tenantId" : 12345,
    "id" : 12345,
    "category" : {
      "parentId" : 12345,
      "iconUrl" : "...",
      "id" : 12345,
      "internal" : true,
      "description" : "...",
      "hidden" : true,
      "name" : "...",
      "tenantId" : 12345,
      "code" : "..."
    },
    "resource" : {
      "description" : "...",
      "categoryResources" : [ { }, { } ],
      "longDescription" : "...",
      "tenantId" : 12345,
      "method" : "...",
      "code" : "...",
      "type" : { },
      "isInternal" : true,
      "id" : 12345,
      "parent" : { },
      "typeCode" : "..."
    }
  }, {
    "tenantId" : 12345,
    "id" : 12345,
    "category" : {
      "parentId" : 12345,
      "iconUrl" : "...",
      "id" : 12345,
      "internal" : true,
      "description" : "...",
      "hidden" : true,
      "name" : "...",
      "tenantId" : 12345,
      "code" : "..."
    },
    "resource" : {
      "description" : "...",
      "categoryResources" : [ { }, { } ],
      "longDescription" : "...",
      "tenantId" : 12345,
      "method" : "...",
      "code" : "...",
      "type" : { },
      "isInternal" : true,
      "id" : 12345,
      "parent" : { },
      "typeCode" : "..."
    }
  } ],
  "longDescription" : "...",
  "tenantId" : 12345,
  "method" : "...",
  "code" : "...",
  "type" : {
    "isInternal" : true,
    "code" : "...",
    "id" : 12345,
    "description" : "..."
  },
  "isInternal" : true,
  "id" : 12345,
  "parent" : {
    "description" : "...",
    "categoryResources" : [ {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    }, {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    } ],
    "longDescription" : "...",
    "tenantId" : 12345,
    "method" : "...",
    "code" : "...",
    "type" : {
      "isInternal" : true,
      "code" : "...",
      "id" : 12345,
      "description" : "..."
    },
    "isInternal" : true,
    "id" : 12345,
    "parent" : { },
    "typeCode" : "..."
  },
  "typeCode" : "..."
}
```
