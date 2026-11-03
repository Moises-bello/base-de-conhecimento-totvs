---
content_hash: d9b36540d1f623850bbe77534e47d4f6b9ccb21f346be4a130632960318561c4
fetched_at: '2026-11-03T14:34:38.569907+00:00'
page_id: json_SolvedPermissionVO
product: fluig
source: rest-fluig
title: Fluig REST — SolvedPermissionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SolvedPermissionVO.html
version: 1
---

# SolvedPermissionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| securityLevel | number | required |  |
| document | [DocumentVO](https://api.fluig.com/old/json_DocumentVO_document.html) |  |  |
| showContent | boolean | required |  |
| downloadEnabled | boolean | required |  |

Example

```
{
  "securityLevel" : 12345,
  "document" : {
    "accessCount" : 12345,
    "watermarkId" : 12345,
    "additionalComments" : "...",
    "activeVersion" : true,
    "imutable" : true,
    "lastModifiedDate" : 12345,
    "documentType" : "...",
    "lastModifiedTime" : "...",
    "inheritSecurity" : true,
    "privateDocument" : true,
    "languageId" : "...",
    "colleagueId" : "...",
    "documentTypeId" : "...",
    "crc" : 12345,
    "internalVisualizer" : true,
    "priority" : 12345,
    "externalDocumentId" : "...",
    "parentDocumentId" : 12345,
    "restrictionType" : 12345,
    "volumeId" : "...",
    "expires" : true,
    "downloadEnabled" : true,
    "versionDescription" : "...",
    "documentId" : 12345,
    "approvalAndOr" : true,
    "userNotify" : true,
    "documentPropertyVersion" : 12345,
    "siteCode" : "...",
    "phisicalFile" : "...",
    "validationStartDate" : 12345,
    "onCheckout" : true,
    "visualization" : "...",
    "translated" : true,
    "iconPath" : "...",
    "allowMuiltiCardsPerUser" : true,
    "deleted" : true,
    "documentDescription" : "...",
    "keyWord" : "...",
    "tenantId" : 12345,
    "draft" : true,
    "documentPropertyNumber" : 12345,
    "createDate" : 12345,
    "approved" : true,
    "phisicalFileSize" : 12345.0,
    "privateColleagueId" : "...",
    "uploadId" : "...",
    "versionAction" : "...",
    "expirationDate" : 12345,
    "indexed" : true,
    "iconId" : 12345,
    "UUID" : "...",
    "updateIsoProperties" : true,
    "publisherId" : "...",
    "approvedDate" : 12345,
    "permissionType" : 12345,
    "cardDescription" : "...",
    "version" : 12345,
    "relatedFiles" : "...",
    "atualizationId" : 12345,
    "topicId" : 12345
  },
  "showContent" : true,
  "downloadEnabled" : true
}
```
