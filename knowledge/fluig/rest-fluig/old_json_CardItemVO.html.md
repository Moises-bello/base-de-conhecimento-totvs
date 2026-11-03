---
content_hash: 116699491af2a375c879069f64116d5e1ad0751a2f13d5ce31f8019803c140af
fetched_at: '2026-11-03T14:34:36.384466+00:00'
page_id: json_CardItemVO
product: fluig
source: rest-fluig
title: Fluig REST — CardItemVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardItemVO.html
version: 1
---

# CardItemVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| additionalComments | string |  |
| permissionType | number |  |
| notificationDays | number |  |
| restrictionType | number |  |
| keyWord | string |  |
| tenantId | number |  |
| attachments | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO_workflow.html) |  |
| restrictions | array of [DocumentRestrictionVO](https://api.fluig.com/old/json_DocumentRestrictionVO.html) |  |
| documentType | string |  |
| documentTypeId | string |  |
| versionOption | string |  |
| expirationDate | number |  |
| internalVisualizer | boolean |  |
| publisherApprovers | array of [DocumentApproverVO](https://api.fluig.com/old/json_DocumentApproverVO.html) |  |
| privateDocument | boolean |  |
| versionDescription | string |  |
| metaListId | number |  |
| inheritSecurity | boolean |  |
| updateIsoProperties | boolean |  |
| topicId | number |  |
| imutable | boolean |  |
| downloadEnabled | boolean |  |
| documentDescription | string |  |
| iconId | number |  |
| parentDocumentId | number |  |
| formData | array of map of string |  |
| colleagueId | string |  |
| version | number |  |
| userNotify | boolean |  |
| languageId | string |  |
| documentId | number |  |
| validationStartDate | number |  |
| relatedDocuments | array of [RelatedDocumentVO](https://api.fluig.com/old/json_RelatedDocumentVO.html) |  |
| expires | boolean |  |
| permissions | array of [DocumentPermissionVO](https://api.fluig.com/old/json_DocumentPermissionVO.html) |  |

Example

```
{
  "additionalComments" : "...",
  "permissionType" : 12345,
  "notificationDays" : 12345,
  "restrictionType" : 12345,
  "keyWord" : "...",
  "tenantId" : 12345,
  "attachments" : [ {
    "principal" : true,
    "fileName" : "...",
    "absoluteFileName" : "...",
    "attach" : true
  }, {
    "principal" : true,
    "fileName" : "...",
    "absoluteFileName" : "...",
    "attach" : true
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
  "documentType" : "...",
  "documentTypeId" : "...",
  "versionOption" : "...",
  "expirationDate" : 12345,
  "internalVisualizer" : true,
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
  "privateDocument" : true,
  "versionDescription" : "...",
  "metaListId" : 12345,
  "inheritSecurity" : true,
  "updateIsoProperties" : true,
  "topicId" : 12345,
  "imutable" : true,
  "downloadEnabled" : true,
  "documentDescription" : "...",
  "iconId" : 12345,
  "parentDocumentId" : 12345,
  "formData" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ],
  "colleagueId" : "...",
  "version" : 12345,
  "userNotify" : true,
  "languageId" : "...",
  "documentId" : 12345,
  "validationStartDate" : 12345,
  "relatedDocuments" : [ {
    "relatedDocumentId" : 12345,
    "version" : 12345,
    "tenantId" : 12345,
    "documentId" : 12345
  }, {
    "relatedDocumentId" : 12345,
    "version" : 12345,
    "tenantId" : 12345,
    "documentId" : 12345
  } ],
  "expires" : true,
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
  } ]
}
```
