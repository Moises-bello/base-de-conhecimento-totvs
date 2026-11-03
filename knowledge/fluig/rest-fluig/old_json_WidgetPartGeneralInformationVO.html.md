---
content_hash: b5389eb5c020f0f240ff2d704b70c984125ddc7b66a7c884ded6928b380f4aab
fetched_at: '2026-11-03T14:34:39.029340+00:00'
page_id: json_WidgetPartGeneralInformationVO
product: fluig
source: rest-fluig
title: Fluig REST — WidgetPartGeneralInformationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WidgetPartGeneralInformationVO.html
version: 1
---

# WidgetPartGeneralInformationVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| enableInternalVisualizer | boolean |  |  |
| languageId | string |  |  |
| onlyActiveRows | boolean |  |  |
| icondescUtilization | string |  |  |
| listDocumentTypeVO | array of [WidgetPartGeneralInformationDocumentTypeVO](https://api.fluig.com/old/json_WidgetPartGeneralInformationDocumentTypeVO.html) |  |  |
| persistenceType | number |  |  |
| colleagueName | string |  |  |
| downloadEnabled | boolean |  |  |
| documentLanguageVO | array of [DocumentLanguageVO](https://api.fluig.com/old/json_DocumentLanguageVO.html) |  |  |
| validationStartDate | string |  |  |
| versionOption | string |  |  |
| publisherName | string |  |  |
| quota | number |  |  |
| watermarkId | number |  |  |
| documentId | number |  |  |
| listcustomFieldsVO | array of [WidgetPartGeneralInformationCustomFieldsVO](https://api.fluig.com/old/json_WidgetPartGeneralInformationCustomFieldsVO.html) |  |  |
| listApplication | array of [ApplicationPublisherVO](https://api.fluig.com/old/json_ApplicationPublisherVO.html) |  |  |
| applicationId | string |  |  |
| internalVisualizer | boolean |  |  |
| topicId | number |  |  |
| iconPathFile | string |  |  |
| keyWord | string |  |  |
| volumeId | string |  |  |
| url | string |  |  |
| fieldQuotaDisabled | boolean | required |  |
| expirationDate | string |  |  |
| userNotify | boolean |  |  |
| updateIsoProperties | boolean | required |  |
| pdfRenderEngine | string |  |  |
| quotaEnabled | boolean | required |  |
| listIconVO | array of [WidgetPartGeneralInformationIconVO](https://api.fluig.com/old/json_WidgetPartGeneralInformationIconVO.html) |  |  |
| datasetName | string |  |  |
| convertDocumentType | number |  |  |
| iconId | number |  |  |
| showQuota | boolean | required |  |
| topicMandatory | boolean |  |  |
| messageQuotaField | string |  |  |
| notificationDays | number |  |  |
| versionDescription | string |  |  |
| expires | boolean |  |  |
| companyId | number |  |  |
| documentTypeId | string |  |  |
| listTopicVO | array of [WidgetPartGeneralInformationTopicVO](https://api.fluig.com/old/json_WidgetPartGeneralInformationTopicVO.html) |  |  |
| imutable | boolean |  |  |
| allowMuiltiCardsPerUser | boolean |  |  |
| version | string |  |  |
| additionalComments | string |  |  |
| oldViewer | boolean |  |  |
| colleagueId | string |  |  |

Example

```
{
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
}
```
