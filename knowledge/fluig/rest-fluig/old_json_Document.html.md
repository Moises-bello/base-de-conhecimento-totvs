---
content_hash: 6b88e572c3f096e2b29546590e8c737dedcf699d6f8fd7f62caf6125d8aa62c8
fetched_at: '2026-11-03T14:34:36.619373+00:00'
page_id: json_Document
product: fluig
source: rest-fluig
title: Fluig REST — Document Data Type
type: documentation
url: https://api.fluig.com/old/json_Document.html
version: 1
---

# Document Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| phisicalFile | string |  |  |
| socialDocument | string |  |  |
| formCommunity | boolean |  |  |
| convertDocumentType | number |  |  |
| pdfConversionStatus | number |  |  |
| inheritApprovers | boolean |  |  |
| validationStartDate | number |  |  |
| iconPath | string |  |  |
| lastModifiedDate | number |  |  |
| languageId | string |  |  |
| metaListRecordId | number |  |  |
| datasetName | string |  |  |
| documentPropertyVersion | number |  |  |
| metadataFormVersionStatus | string |  |  |
| inheritSecurity | boolean | required |  |
| visualization | string |  |  |
| allowMuiltiCardsPerUser | boolean |  |  |
| userNotify | boolean | required |  |
| downloadEnabled | boolean | required |  |
| iconId | number | required |  |
| expirationDate | number |  |  |
| previousVersion | number |  |  |
| hashAnnotations | string |  |  |
| metaListId | number |  |  |
| topicId | number | required |  |
| versionDescription | string |  |  |
| pdfRenderEngine | string |  |  |
| notificationDays | number |  |  |
| viewedDocument | boolean |  |  |
| translated | boolean | required |  |
| restrictionType | number |  |  |
| documentTypeId | string |  |  |
| publicDocument | boolean |  |  |
| isEncrypted | boolean |  |  |
| linkDocument | boolean | required |  |
| permissionType | number | required |  |
| publisherName | string |  |  |
| crc | number |  |  |
| colleagueId | string |  |  |
| parentDocument | [Document](https://api.fluig.com/old/json_Document.html) |  |  |
| ~~siteCode~~ | ~~string~~ |  |  |
| processingBatch | boolean | required |  |
| indexed | boolean |  |  |
| onlyActiveRows | boolean |  |  |
| createDate | number |  |  |
| cardDescription | string |  |  |
| rowId | number | required |  |
| keyWord | string |  |  |
| additionalComments | string |  |  |
| size | number |  |  |
| internalVisualizer | boolean | required |  |
| encrypted | boolean | required |  |
| approvedDate | number |  |  |
| relatedDocument | boolean |  |  |
| documentPropertyNumber | number |  |  |
| quota | number |  |  |
| priority | number |  |  |
| documentDescription | string |  |  |
| publisherId | string |  |  |
| UUID | string |  |  |
| watermarkId | number |  |  |
| externalDocumentId | string |  |  |
| deleted | boolean | required |  |
| persistenceType | [CardPersistenceType](https://api.fluig.com/old/json_CardPersistenceType.html) |  |  |
| fileSize | number | required |  |
| parentDocumentId | number |  |  |
| accessCount | number |  |  |
| volumeId | string |  |  |
| privateColleagueId | string |  |  |
| documentPK | [DocumentPK](https://api.fluig.com/old/json_DocumentPK.html) |  |  |
| activeVersion | boolean | required |  |
| usedQuota | number |  |  |
| updateIsoProperties | boolean | required |  |
| phisicalFilePath | string |  |  |
| checkoutFolder | boolean |  |  |
| metaList | boolean | required |  |
| documentType | string |  |  |
| atualizationId | number |  |  |
| imutable | boolean | required |  |
| isLinkDocument | boolean |  |  |
| privateDocument | boolean | required |  |
| mimetype | string |  |  |
| draft | boolean | required |  |
| expires | boolean |  |  |
| versionOption | string |  |  |
| statusArmazLongoPrazo | number |  |  |
| relatedFiles | string |  |  |
| canBeCheckout | boolean |  |  |
| colleagueName | string |  |  |
| lastModifiedTime | string |  |  |
| tenantId | number |  |  |
| approvalAndOr | boolean |  |  |
| checkOutFolder | boolean | required |  |
| linkRootFolder | number |  |  |
| approved | boolean | required |  |

Example

```
{
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
  "parentDocument" : {
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
    "documentPK" : {
      "companyId" : 12345,
      "version" : 12345,
      "documentId" : 12345
    },
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
  "documentPK" : {
    "companyId" : 12345,
    "version" : 12345,
    "documentId" : 12345
  },
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
}
```
