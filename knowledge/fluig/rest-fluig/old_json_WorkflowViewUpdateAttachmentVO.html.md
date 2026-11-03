---
content_hash: ee7004897ab90d0df18178fee425d16533f596fde5df049a1453b16b1a80a0c8
fetched_at: '2026-11-03T14:34:39.223766+00:00'
page_id: json_WorkflowViewUpdateAttachmentVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewUpdateAttachmentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewUpdateAttachmentVO.html
version: 1
---

# WorkflowViewUpdateAttachmentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| attachment | [ProcessAttachment](https://api.fluig.com/old/json_ProcessAttachment.html) |  |
| currentMovto | number |  |
| removeUploadFiles | boolean |  |
| taskUserId | string |  |
| processInstanceId | number |  |

Example

```
{
  "attachment" : {
    "document" : {
      "phisicalFile" : "...",
      "socialDocument" : "...",
      "formCommunity" : true,
      "convertDocumentType" : 12345,
      "pdfConversionStatus" : 12345,
      "inheritApprovers" : true,
      "validationStartDate" : 12345,
      "iconPath" : "...",
      "lastModifiedDate" : 12345,
      "languageId" : "...",
      "metaListRecordId" : 12345,
      "datasetName" : "...",
      "documentPropertyVersion" : 12345,
      "metadataFormVersionStatus" : "...",
      "inheritSecurity" : true,
      "visualization" : "...",
      "allowMuiltiCardsPerUser" : true,
      "userNotify" : true,
      "downloadEnabled" : true,
      "iconId" : 12345,
      "expirationDate" : 12345,
      "previousVersion" : 12345,
      "hashAnnotations" : "...",
      "metaListId" : 12345,
      "topicId" : 12345,
      "versionDescription" : "...",
      "pdfRenderEngine" : "...",
      "notificationDays" : 12345,
      "viewedDocument" : true,
      "translated" : true,
      "restrictionType" : 12345,
      "documentTypeId" : "...",
      "publicDocument" : true,
      "isEncrypted" : true,
      "linkDocument" : true,
      "permissionType" : 12345,
      "publisherName" : "...",
      "crc" : 12345,
      "colleagueId" : "...",
      "parentDocument" : { },
      "processingBatch" : true,
      "indexed" : true,
      "onlyActiveRows" : true,
      "createDate" : 12345,
      "cardDescription" : "...",
      "rowId" : 12345,
      "keyWord" : "...",
      "additionalComments" : "...",
      "size" : 12345.0,
      "internalVisualizer" : true,
      "encrypted" : true,
      "approvedDate" : 12345,
      "relatedDocument" : true,
      "documentPropertyNumber" : 12345,
      "quota" : 12345,
      "priority" : 12345,
      "documentDescription" : "...",
      "publisherId" : "...",
      "UUID" : "...",
      "watermarkId" : 12345,
      "externalDocumentId" : "...",
      "deleted" : true,
      "persistenceType" : "DB",
      "fileSize" : 12345,
      "parentDocumentId" : 12345,
      "accessCount" : 12345,
      "volumeId" : "...",
      "privateColleagueId" : "...",
      "documentPK" : { },
      "activeVersion" : true,
      "usedQuota" : 12345.0,
      "updateIsoProperties" : true,
      "phisicalFilePath" : "...",
      "checkoutFolder" : true,
      "metaList" : true,
      "documentType" : "...",
      "atualizationId" : 12345,
      "imutable" : true,
      "isLinkDocument" : true,
      "privateDocument" : true,
      "mimetype" : "...",
      "draft" : true,
      "expires" : true,
      "versionOption" : "...",
      "statusArmazLongoPrazo" : 12345,
      "relatedFiles" : "...",
      "canBeCheckout" : true,
      "colleagueName" : "...",
      "lastModifiedTime" : "...",
      "tenantId" : 12345,
      "approvalAndOr" : true,
      "checkOutFolder" : true,
      "linkRootFolder" : 12345,
      "approved" : true
    },
    "fieldValue1" : "...",
    "version" : 12345,
    "fieldValue8" : "...",
    "fieldValue11" : "...",
    "permission" : "...",
    "attachments" : [ {
      "filecontent" : "...",
      "pathName" : "...",
      "fileModificationDate" : 12345,
      "fileSelected" : { },
      "attach" : true,
      "displayFileName" : "...",
      "editing" : true,
      "iconPath" : "...",
      "principal" : true,
      "fullPatch" : "...",
      "mobile" : true,
      "supportedNewViewer" : true,
      "descriptor" : true,
      "fileSize" : 12345,
      "fileName" : "..."
    }, {
      "filecontent" : "...",
      "pathName" : "...",
      "fileModificationDate" : 12345,
      "fileSelected" : { },
      "attach" : true,
      "displayFileName" : "...",
      "editing" : true,
      "iconPath" : "...",
      "principal" : true,
      "fullPatch" : "...",
      "mobile" : true,
      "supportedNewViewer" : true,
      "descriptor" : true,
      "fileSize" : 12345,
      "fileName" : "..."
    } ],
    "description" : "...",
    "fieldValue10" : "...",
    "fieldValue15" : "...",
    "newAttach" : true,
    "replacementId" : "...",
    "fromAttachComponent" : true,
    "fieldValue4" : "...",
    "fieldValue13" : "...",
    "iconPath" : "...",
    "attachedDate" : 12345,
    "fieldValue7" : "...",
    "originalMovementSequence" : 12345,
    "fieldValue2" : "...",
    "fieldValue3" : "...",
    "processAttachmentPK" : {
      "attachmentSequence" : 12345,
      "processInstanceId" : 12345,
      "companyId" : 12345
    },
    "fieldValue14" : "...",
    "mainAttach" : true,
    "fieldValue5" : "...",
    "fileName" : "...",
    "fieldValue9" : "...",
    "colleagueId" : "...",
    "originalThreadSequence" : 12345,
    "fieldValue12" : "...",
    "fieldValue6" : "...",
    "documentId" : 12345,
    "deleted" : true
  },
  "currentMovto" : 12345,
  "removeUploadFiles" : true,
  "taskUserId" : "...",
  "processInstanceId" : 12345
}
```
