---
content_hash: 1ad73ea42c83b38c0f065a0da8095e2aec7a08fd3890cddecc35d354882f7e0e
fetched_at: '2026-11-03T14:34:38.953349+00:00'
page_id: json_WCMTenantApplication
product: fluig
source: rest-fluig
title: Fluig REST — WCMTenantApplication Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMTenantApplication.html
version: 1
---

# WCMTenantApplication Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| appCodeExt | string |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| enabled | boolean |  |
| id | number |  |
| application | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |

Example

```
{
  "appCodeExt" : "...",
  "tenant" : {
    "federalId" : "...",
    "idpId" : "...",
    "resourceType" : "...",
    "useWizard" : true,
    "code" : "...",
    "organizationUrl" : "...",
    "tenantActive" : true,
    "products" : [ {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    }, {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    } ],
    "idpLogOff" : true,
    "id" : 12345,
    "resourceDescription" : "...",
    "data" : [ {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    }, {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    } ],
    "securityCode" : "...",
    "thumbnailEnabled" : true,
    "UUID" : "...",
    "description" : "...",
    "removeVolume" : true
  },
  "enabled" : true,
  "id" : 12345,
  "application" : {
    "earFileName" : "...",
    "title" : "...",
    "maxHeight" : 12345,
    "locales" : [ {
      "application" : { },
      "code" : "...",
      "id" : 12345
    }, {
      "application" : { },
      "code" : "...",
      "id" : 12345
    } ],
    "minHeight" : 12345,
    "product" : "...",
    "internal" : true,
    "fileName" : "...",
    "originCode" : "...",
    "description" : "...",
    "icon" : "...",
    "developerUrl" : "...",
    "id" : 12345,
    "extendedData" : "...",
    "localeFileBaseName" : "...",
    "appTenantCode" : "...",
    "developerName" : "...",
    "applicationExtensible" : true,
    "categories" : [ {
      "category" : "...",
      "application" : { },
      "id" : 12345
    }, {
      "category" : "...",
      "application" : { },
      "id" : 12345
    } ],
    "maxWidth" : 12345,
    "services" : [ {
      "varName" : "...",
      "jndiName" : "...",
      "application" : { },
      "id" : 12345
    }, {
      "varName" : "...",
      "jndiName" : "...",
      "application" : { },
      "id" : 12345
    } ],
    "renderer" : "...",
    "developerCode" : "...",
    "resources" : [ {
      "order" : 12345,
      "type" : "...",
      "id" : 12345,
      "application" : { },
      "resource" : "..."
    }, {
      "order" : 12345,
      "type" : "...",
      "id" : 12345,
      "application" : { },
      "resource" : "..."
    } ],
    "context" : "...",
    "applicationVersion" : "...",
    "applicationPublic" : true,
    "isExtension" : true,
    "minWidth" : 12345,
    "code" : "...",
    "activationClass" : "..."
  }
}
```
