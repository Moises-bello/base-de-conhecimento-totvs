---
content_hash: 66877c9684bcad3b6633179a9cf1b5ad2f12a62810ff8e3f16f70255f321ed03
fetched_at: '2026-11-03T14:34:38.685907+00:00'
page_id: json_TenantVO
product: fluig
source: rest-fluig
title: Fluig REST — TenantVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TenantVO.html
version: 1
---

# TenantVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| id | number | required |  |
| code | string |  |  |
| federalId | string |  |  |
| idpId | string |  |  |
| description | string |  |  |
| organizationUrl | string |  |  |
| defaultDir | string |  |  |
| idpLogOff | boolean | required |  |
| thumbnailEnabled | boolean | required |  |
| adminUser | [AdminUserVO](https://api.fluig.com/old/json_AdminUserVO_vo.html) |  |  |
| tenantData | map of string |  |  |
| keys | array of string |  |  |
| tenantActive | boolean |  |  |
| EMailConfigVO | [EMailConfigVO](https://api.fluig.com/old/json_EMailConfigVO.html) |  |  |

Example

```
{
  "id" : 12345,
  "code" : "...",
  "federalId" : "...",
  "idpId" : "...",
  "description" : "...",
  "organizationUrl" : "...",
  "defaultDir" : "...",
  "idpLogOff" : true,
  "thumbnailEnabled" : true,
  "adminUser" : {
    "id" : 12345,
    "email" : "...",
    "login" : "...",
    "password" : "...",
    "firstName" : "...",
    "lastName" : "..."
  },
  "tenantData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "keys" : [ "...", "..." ],
  "tenantActive" : true,
  "EMailConfigVO" : {
    "tenantId" : 12345,
    "smtpServer" : "...",
    "smtpPort" : 12345,
    "emailFrom" : "...",
    "emailSecurity" : "...",
    "user" : "...",
    "password" : "...",
    "connectionTimeout" : 12345
  }
}
```
