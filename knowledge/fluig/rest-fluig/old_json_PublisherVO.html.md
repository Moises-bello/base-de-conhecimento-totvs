---
content_hash: a37a7ac55eb7eaddd722a8274c1d8616a3a2d4131ccb263adfd698c3d1b82496
fetched_at: '2026-11-03T14:34:38.168786+00:00'
page_id: json_PublisherVO
product: fluig
source: rest-fluig
title: Fluig REST — PublisherVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PublisherVO.html
version: 1
---

# PublisherVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| inheritApprovers | boolean | required |  |
| allocatedPK | [PublisherAllocatedPKVO](https://api.fluig.com/old/json_PublisherAllocatedPKVO.html) |  |  |
| changeAllActiveCards | boolean | required |  |
| attachments | array of string |  |  |
| uploadUrl | string |  |  |
| approved | boolean | required |  |
| relatedDocumentVO | array of [WidgetPartRelatedDocumentVO](https://api.fluig.com/old/json_WidgetPartRelatedDocumentVO.html) |  |  |
| tabActivated | boolean | required |  |
| privateDocument | boolean | required |  |
| additionalComments | string |  |  |
| manualVersion | boolean | required |  |
| securityPermissionVOs | array of [WidgetPartSecurityConfigVO](https://api.fluig.com/old/json_WidgetPartSecurityConfigVO.html) |  |  |
| companyId | number |  |  |
| message | string |  |  |
| deleteUploadFiles | boolean | required |  |
| version | number |  |  |
| formDatasetVOs | array of [FormDatasetVO](https://api.fluig.com/old/json_FormDatasetVO.html) |  |  |
| hasParentApprover | boolean | required |  |
| defaultPropertyVO | [WidgetPartDefaultPropertyVO](https://api.fluig.com/old/json_WidgetPartDefaultPropertyVO.html) |  |  |
| activeApproverTab | boolean | required |  |
| parentDocumentId | number |  |  |
| metaListId | number |  |  |
| attachmentsList | array of [PublisherFileVO](https://api.fluig.com/old/json_PublisherFileVO.html) |  |  |
| permissionType | number |  |  |
| uploadId | string |  |  |
| documentType | string |  |  |
| documentTypeId | string |  |  |
| hasPendentApprovals | boolean |  |  |
| watermarkId | number |  |  |
| rootPrivateFolder | boolean | required |  |
| saveDraft | boolean | required |  |
| openBy | string |  |  |
| publisherId | string |  |  |
| ckbDefaultPropertyVO | [FolderPublisherCheckboxDefaultPropertyVO](https://api.fluig.com/old/json_FolderPublisherCheckboxDefaultPropertyVO.html) |  |  |
| documentId | number |  |  |
| relatedFiles | string |  |  |
| principalFileName | string |  |  |
| phisicalFile | string |  |  |
| securityRestrictionVOs | array of [WidgetPartSecurityConfigVO](https://api.fluig.com/old/json_WidgetPartSecurityConfigVO.html) |  |  |
| editableDocumentData | string |  |  |
| cardFormData | array of map of string |  |  |
| versionDescription | string |  |  |
| folderList | array of string |  |  |
| hashAnnotations | string |  |  |
| inheritSecurity | boolean | required |  |
| formData | map of string |  |  |
| imutable | boolean |  |  |
| infGeralVO | [WidgetPartGeneralInformationVO](https://api.fluig.com/old/json_WidgetPartGeneralInformationVO.html) |  |  |
| markupProcessId | string |  |  |
| cardDescription | string |  |  |
| publicDocument | boolean | required |  |
| restrictionType | number |  |  |
| viewingSessionId | string |  |  |
| internalFields | array of string |  |  |
| attach | array of [CardPublisherAttachmentVO](https://api.fluig.com/old/json_CardPublisherAttachmentVO.html) |  |  |
| userSecurityLevel | number |  |  |
| publisherApproverVOs | array of [WidgetPartApproverConfigVO](https://api.fluig.com/old/json_WidgetPartApproverConfigVO.html) |  |  |
| adminUser | boolean | required |  |
| oldViewer | boolean | required |  |
| documentDescription | string |  |  |
| uploadFolder | string |  |  |

Example

```
{
  "inheritApprovers" : true,
  "allocatedPK" : {
    "destinationDocument" : 12345,
    "sourceDocument" : 12345,
    "sourceVersion" : 12345
  },
  "changeAllActiveCards" : true,
  "attachments" : [ "...", "..." ],
  "uploadUrl" : "...",
  "approved" : true,
  "relatedDocumentVO" : [ {
    "documentId" : 12345,
    "documentDescription" : "...",
    "documentVersion" : 12345
  }, {
    "documentId" : 12345,
    "documentDescription" : "...",
    "documentVersion" : 12345
  } ],
  "tabActivated" : true,
  "privateDocument" : true,
  "additionalComments" : "...",
  "manualVersion" : true,
  "securityPermissionVOs" : [ {
    "securityVersion" : true,
    "attributionDescription" : "...",
    "attributionValue" : "...",
    "inheritOriginSecurity" : true,
    "tableId" : "...",
    "attributionType" : 12345,
    "permission" : true,
    "securityLevel" : 12345,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true
  }, {
    "securityVersion" : true,
    "attributionDescription" : "...",
    "attributionValue" : "...",
    "inheritOriginSecurity" : true,
    "tableId" : "...",
    "attributionType" : 12345,
    "permission" : true,
    "securityLevel" : 12345,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true
  } ],
  "companyId" : 12345,
  "message" : "...",
  "deleteUploadFiles" : true,
  "version" : 12345,
  "formDatasetVOs" : [ {
    "mobileCache" : true,
    "version" : 12345,
    "documentId" : 12345,
    "type" : "...",
    "datasetId" : "...",
    "serverOffline" : true,
    "id" : 12345,
    "companyId" : 12345
  }, {
    "mobileCache" : true,
    "version" : 12345,
    "documentId" : 12345,
    "type" : "...",
    "datasetId" : "...",
    "serverOffline" : true,
    "id" : 12345,
    "companyId" : 12345
  } ],
  "hasParentApprover" : true,
  "defaultPropertyVO" : {
    "pdfrenderengine" : "...",
    "updateISOProperties" : true,
    "versionOption" : 12345,
    "mapNrDocument" : {
      "property1" : { },
      "property2" : { }
    },
    "customFields" : true,
    "listCustomFieldsVO" : [ {
      "customFieldDescription" : "...",
      "alwaysShow" : true,
      "valueId" : "...",
      "customFieldId" : "..."
    }, {
      "customFieldDescription" : "...",
      "alwaysShow" : true,
      "valueId" : "...",
      "customFieldId" : "..."
    } ],
    "imutable" : true,
    "notifyUser" : true,
    "type" : "...",
    "listPublisherTopicVO" : [ {
      "topicId" : 12345,
      "mandatory" : true,
      "description" : "..."
    }, {
      "topicId" : 12345,
      "mandatory" : true,
      "description" : "..."
    } ],
    "listInheritCustomFieldsVO" : [ {
      "customFieldDescription" : "...",
      "alwaysShow" : true,
      "valueId" : "...",
      "customFieldId" : "..."
    }, {
      "customFieldDescription" : "...",
      "alwaysShow" : true,
      "valueId" : "...",
      "customFieldId" : "..."
    } ],
    "internalVisualizer" : true,
    "downloadble" : true,
    "subject" : 12345,
    "listPublisherDocumentTypeVO" : [ {
      "description" : "...",
      "companyId" : 12345,
      "typeId" : "..."
    }, {
      "description" : "...",
      "companyId" : 12345,
      "typeId" : "..."
    } ]
  },
  "activeApproverTab" : true,
  "parentDocumentId" : 12345,
  "metaListId" : 12345,
  "attachmentsList" : [ {
    "attachmentSource" : "REMOTE",
    "main" : true,
    "source" : "...",
    "filename" : "..."
  }, {
    "attachmentSource" : "REMOTE",
    "main" : true,
    "source" : "...",
    "filename" : "..."
  } ],
  "permissionType" : 12345,
  "uploadId" : "...",
  "documentType" : "...",
  "documentTypeId" : "...",
  "hasPendentApprovals" : true,
  "watermarkId" : 12345,
  "rootPrivateFolder" : true,
  "saveDraft" : true,
  "openBy" : "...",
  "publisherId" : "...",
  "ckbDefaultPropertyVO" : {
    "ckbVersionOption" : true,
    "ckbNotifyUser" : true,
    "ckbType" : true,
    "ckbSubject" : true,
    "ckbCustomFields" : true,
    "ckbInternalVisualizer" : true,
    "ckbImutable" : true,
    "ckbUpdateISOProperties" : true,
    "ckbDownloadble" : true
  },
  "documentId" : 12345,
  "relatedFiles" : "...",
  "principalFileName" : "...",
  "phisicalFile" : "...",
  "securityRestrictionVOs" : [ {
    "securityVersion" : true,
    "attributionDescription" : "...",
    "attributionValue" : "...",
    "inheritOriginSecurity" : true,
    "tableId" : "...",
    "attributionType" : 12345,
    "permission" : true,
    "securityLevel" : 12345,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true
  }, {
    "securityVersion" : true,
    "attributionDescription" : "...",
    "attributionValue" : "...",
    "inheritOriginSecurity" : true,
    "tableId" : "...",
    "attributionType" : 12345,
    "permission" : true,
    "securityLevel" : 12345,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true
  } ],
  "editableDocumentData" : "...",
  "cardFormData" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ],
  "versionDescription" : "...",
  "folderList" : [ "...", "..." ],
  "hashAnnotations" : "...",
  "inheritSecurity" : true,
  "formData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "imutable" : true,
  "infGeralVO" : {
    "enableInternalVisualizer" : true,
    "languageId" : "...",
    "onlyActiveRows" : true,
    "icondescUtilization" : "...",
    "listDocumentTypeVO" : [ {
      "typeId" : "...",
      "description" : "...",
      "companyId" : 12345
    }, {
      "typeId" : "...",
      "description" : "...",
      "companyId" : 12345
    } ],
    "persistenceType" : 12345,
    "colleagueName" : "...",
    "downloadEnabled" : true,
    "documentLanguageVO" : [ {
      "languageCode" : "...",
      "description" : "..."
    }, {
      "languageCode" : "...",
      "description" : "..."
    } ],
    "validationStartDate" : "...",
    "versionOption" : "...",
    "publisherName" : "...",
    "quota" : 12345,
    "watermarkId" : 12345,
    "documentId" : 12345,
    "listcustomFieldsVO" : [ {
      "customFieldId" : "...",
      "valueId" : "...",
      "customFieldDescription" : "...",
      "alwaysShow" : true
    }, {
      "customFieldId" : "...",
      "valueId" : "...",
      "customFieldDescription" : "...",
      "alwaysShow" : true
    } ],
    "listApplication" : [ {
      "description" : "...",
      "applicationId" : "..."
    }, {
      "description" : "...",
      "applicationId" : "..."
    } ],
    "applicationId" : "...",
    "internalVisualizer" : true,
    "topicId" : 12345,
    "iconPathFile" : "...",
    "keyWord" : "...",
    "volumeId" : "...",
    "url" : "...",
    "fieldQuotaDisabled" : true,
    "expirationDate" : "...",
    "userNotify" : true,
    "updateIsoProperties" : true,
    "pdfRenderEngine" : "...",
    "quotaEnabled" : true,
    "listIconVO" : [ {
      "companyId" : 12345,
      "descUtilization" : "...",
      "iconPathFile" : "...",
      "iconFile" : "...",
      "iconId" : 12345
    }, {
      "companyId" : 12345,
      "descUtilization" : "...",
      "iconPathFile" : "...",
      "iconFile" : "...",
      "iconId" : 12345
    } ],
    "datasetName" : "...",
    "convertDocumentType" : 12345,
    "iconId" : 12345,
    "showQuota" : true,
    "topicMandatory" : true,
    "messageQuotaField" : "...",
    "notificationDays" : 12345,
    "versionDescription" : "...",
    "expires" : true,
    "companyId" : 12345,
    "documentTypeId" : "...",
    "listTopicVO" : [ {
      "description" : "...",
      "mandatory" : true,
      "topicId" : 12345
    }, {
      "description" : "...",
      "mandatory" : true,
      "topicId" : 12345
    } ],
    "imutable" : true,
    "allowMuiltiCardsPerUser" : true,
    "version" : "...",
    "additionalComments" : "...",
    "oldViewer" : true,
    "colleagueId" : "..."
  },
  "markupProcessId" : "...",
  "cardDescription" : "...",
  "publicDocument" : true,
  "restrictionType" : 12345,
  "viewingSessionId" : "...",
  "internalFields" : [ "...", "..." ],
  "attach" : [ {
    "newFileName" : "...",
    "source" : "...",
    "attach" : true,
    "principal" : true,
    "initFileName" : "..."
  }, {
    "newFileName" : "...",
    "source" : "...",
    "attach" : true,
    "principal" : true,
    "initFileName" : "..."
  } ],
  "userSecurityLevel" : 12345,
  "publisherApproverVOs" : [ {
    "approvalMode" : 12345,
    "levelDescription" : "...",
    "digitalSignature" : true,
    "colleagueLogin" : "...",
    "levelId" : 12345,
    "tableId" : 12345,
    "colleagueName" : "...",
    "colleagueId" : "...",
    "approverType" : 12345
  }, {
    "approvalMode" : 12345,
    "levelDescription" : "...",
    "digitalSignature" : true,
    "colleagueLogin" : "...",
    "levelId" : 12345,
    "tableId" : 12345,
    "colleagueName" : "...",
    "colleagueId" : "...",
    "approverType" : 12345
  } ],
  "adminUser" : true,
  "oldViewer" : true,
  "documentDescription" : "...",
  "uploadFolder" : "..."
}
```
