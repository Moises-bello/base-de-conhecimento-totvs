---
content_hash: 02b84311e23dd662d5a84a6b4254cf6252dd35468e9c46c7c87c0ead957ee13a
fetched_at: '2026-11-03T14:34:36.671855+00:00'
page_id: json_DocumentSecurityVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentSecurityVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentSecurityVO.html
version: 1
---

# DocumentSecurityVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| documentPermissionVO | array of [DocumentPermissionVO](https://api.fluig.com/old/json_DocumentPermissionVO.html) |  |
| documentApproverVO | array of [DocumentApproverVO](https://api.fluig.com/old/json_DocumentApproverVO.html) |  |
| documentSecurityConfigVOs | array of [DocumentSecurityConfigVO](https://api.fluig.com/old/json_DocumentSecurityConfigVO.html) |  |

Example

```
{
  "documentPermissionVO" : [ {
    "inheritSecurity" : true,
    "securityLevel" : 12345,
    "downloadEnabled" : true,
    "securityVersion" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  }, {
    "inheritSecurity" : true,
    "securityLevel" : 12345,
    "downloadEnabled" : true,
    "securityVersion" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  } ],
  "documentApproverVO" : [ {
    "approvalStatus" : "...",
    "digitalSignature" : true,
    "levelId" : 12345,
    "email" : "...",
    "levelDescription" : "...",
    "fullName" : "...",
    "companyId" : 12345,
    "colleagueId" : "...",
    "approverType" : 12345,
    "alias" : "...",
    "approvalObservation" : "...",
    "approvalMode" : 12345
  }, {
    "approvalStatus" : "...",
    "digitalSignature" : true,
    "levelId" : 12345,
    "email" : "...",
    "levelDescription" : "...",
    "fullName" : "...",
    "companyId" : 12345,
    "colleagueId" : "...",
    "approverType" : 12345,
    "alias" : "...",
    "approvalObservation" : "...",
    "approvalMode" : 12345
  } ],
  "documentSecurityConfigVOs" : [ {
    "securityVersion" : true,
    "permission" : true,
    "companyId" : 12345,
    "showContent" : true,
    "attributionType" : 12345,
    "downloadEnabled" : true,
    "securityLevel" : 12345,
    "attributionValue" : "...",
    "version" : 12345,
    "sequence" : 12345,
    "documentId" : 12345
  }, {
    "securityVersion" : true,
    "permission" : true,
    "companyId" : 12345,
    "showContent" : true,
    "attributionType" : 12345,
    "downloadEnabled" : true,
    "securityLevel" : 12345,
    "attributionValue" : "...",
    "version" : 12345,
    "sequence" : 12345,
    "documentId" : 12345
  } ]
}
```
