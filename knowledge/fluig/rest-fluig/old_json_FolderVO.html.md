---
content_hash: 7e4a8355b4721d706290193d70049f9186c47809f34bdab222fb385f2eda2a9e
fetched_at: '2026-11-03T14:34:37.039842+00:00'
page_id: json_FolderVO
product: fluig
source: rest-fluig
title: Fluig REST — FolderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FolderVO.html
version: 1
---

# FolderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| createDate | number |  |
| imutable | boolean |  |
| documentDescription | string |  |
| downloadEnabled | boolean |  |
| notifyUser | boolean |  |
| volumeId | string |  |
| publisherApprovers | array of [DocumentApproverVO](https://api.fluig.com/old/json_DocumentApproverVO.html) |  |
| permissionType | number |  |
| privateDocument | boolean |  |
| approvalAndOr | boolean |  |
| expires | boolean |  |
| colleagueId | string |  |
| internalVisualizer | boolean |  |
| inheritSecurity | boolean |  |
| permissions | array of [DocumentPermissionVO](https://api.fluig.com/old/json_DocumentPermissionVO.html) |  |
| topicId | number |  |
| tenantId | number |  |
| filters | map of object |  |
| restrictions | array of [DocumentRestrictionVO](https://api.fluig.com/old/json_DocumentRestrictionVO.html) |  |
| iconId | number |  |
| parentFolderId | number |  |
| documentTypes | array of string |  |
| additionalComments | string |  |
| versionDescription | string |  |
| restrictionType | number |  |
| publisherId | string |  |
| updateIsoProperties | boolean |  |
| documentTypeId | string |  |
| keyWord | string |  |
| version | number |  |
| documentId | number |  |

Example

```
{
  "createDate" : 12345,
  "imutable" : true,
  "documentDescription" : "...",
  "downloadEnabled" : true,
  "notifyUser" : true,
  "volumeId" : "...",
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
  "permissionType" : 12345,
  "privateDocument" : true,
  "approvalAndOr" : true,
  "expires" : true,
  "colleagueId" : "...",
  "internalVisualizer" : true,
  "inheritSecurity" : true,
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
  "topicId" : 12345,
  "tenantId" : 12345,
  "filters" : {
    "property1" : { },
    "property2" : { }
  },
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
  "iconId" : 12345,
  "parentFolderId" : 12345,
  "documentTypes" : [ "...", "..." ],
  "additionalComments" : "...",
  "versionDescription" : "...",
  "restrictionType" : 12345,
  "publisherId" : "...",
  "updateIsoProperties" : true,
  "documentTypeId" : "...",
  "keyWord" : "...",
  "version" : 12345,
  "documentId" : 12345
}
```
