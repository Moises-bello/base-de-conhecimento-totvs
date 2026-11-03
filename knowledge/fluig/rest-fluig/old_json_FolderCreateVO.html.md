---
content_hash: 2dbcb21cfaef481e9892dc435a418bda2678df180e3fb8e63bab2480c20d4979
fetched_at: '2026-11-03T14:34:37.025987+00:00'
page_id: json_FolderCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — FolderCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FolderCreateVO.html
version: 1
---

# FolderCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| publisherId | string |  |
| documentDescription | string |  |
| additionalComments | string |  |
| parentFolderId | number |  |
| iconId | number |  |
| volumeId | string |  |
| keyWord | string |  |
| inheritSecurity | boolean |  |
| permissionType | number |  |
| restrictionType | number |  |
| permissions | array of [DocumentPermissionVO](https://api.fluig.com/old/json_DocumentPermissionVO.html) |  |
| restrictions | array of [DocumentRestrictionVO](https://api.fluig.com/old/json_DocumentRestrictionVO.html) |  |
| publisherApprovers | array of [DocumentApproverVO](https://api.fluig.com/old/json_DocumentApproverVO.html) |  |
| versionDescription | string |  |
| expires | boolean |  |
| topicId | number |  |
| approvalAndOr | boolean |  |
| downloadEnabled | boolean |  |
| updateIsoProperties | boolean |  |
| documentTypeId | string |  |
| notifyUser | boolean |  |
| imutable | boolean |  |
| internalVisualizer | boolean |  |

Example

```
{
  "publisherId" : "...",
  "documentDescription" : "...",
  "additionalComments" : "...",
  "parentFolderId" : 12345,
  "iconId" : 12345,
  "volumeId" : "...",
  "keyWord" : "...",
  "inheritSecurity" : true,
  "permissionType" : 12345,
  "restrictionType" : 12345,
  "permissions" : [ {
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
  "restrictions" : [ {
    "showContent" : true,
    "inheritSecurity" : true,
    "attributionValue" : "...",
    "attributionDescription" : "...",
    "downloadEnabled" : true,
    "securityLevel" : 12345,
    "attributionType" : 12345,
    "securityVersion" : true
  }, {
    "showContent" : true,
    "inheritSecurity" : true,
    "attributionValue" : "...",
    "attributionDescription" : "...",
    "downloadEnabled" : true,
    "securityLevel" : 12345,
    "attributionType" : 12345,
    "securityVersion" : true
  } ],
  "publisherApprovers" : [ {
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
  "versionDescription" : "...",
  "expires" : true,
  "topicId" : 12345,
  "approvalAndOr" : true,
  "downloadEnabled" : true,
  "updateIsoProperties" : true,
  "documentTypeId" : "...",
  "notifyUser" : true,
  "imutable" : true,
  "internalVisualizer" : true
}
```
