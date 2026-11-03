---
content_hash: cd0167b8cb5ea7d0b73cd7d6fa5daa6e051c4d110a6353ce18f4c5b753e3577f
fetched_at: '2026-11-03T14:34:37.845510+00:00'
page_id: json_MobileDocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — MobileDocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_MobileDocumentVO.html
version: 1
---

# MobileDocumentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| versionDescription | string |  |  |
| colleagueId | string |  |  |
| accessCount | number |  |  |
| additionalComments | string |  |  |
| phisicalFile | string |  |  |
| onCheckout | boolean |  |  |
| parentId | number |  |  |
| forApproval | boolean |  |  |
| version | number |  |  |
| children | array of [MobileDocumentVO](https://api.fluig.com/old/json_MobileDocumentVO.html) |  |  |
| idSource | number |  |  |
| createDate | number |  |  |
| approvedDate | number |  |  |
| securityLevel | number | required |  |
| type | string |  |  |
| immutable | boolean | required |  |
| versionSource | number |  |  |
| removed | boolean |  |  |
| phisicalFileSize | number |  |  |
| crc | number |  |  |
| versionOption | string |  |  |
| articleContent | string |  |  |
| publisherId | string |  |  |
| publisherName | string |  |  |
| allowMuiltiCardsPerUser | boolean |  |  |
| documentPropertyNumber | number |  |  |
| fileURL | string |  |  |
| activeUserApprover | boolean |  |  |
| documentPropertyVersion | number |  |  |
| favorite | boolean |  |  |
| expirationDate | number |  |  |
| activeVersion | boolean |  |  |
| expiredForm | boolean |  |  |
| validationStartDate | number |  |  |
| iconPath | string |  |  |
| id | number |  |  |
| userAnswerForm | boolean |  |  |
| companyId | number |  |  |
| description | string |  |  |
| userPermission | number |  |  |
| lastModifiedDate | number |  |  |
| isPrivate | boolean |  |  |
| colleagueName | string |  |  |
| attachments | array of [MobileAttachmentVO](https://api.fluig.com/old/json_MobileAttachmentVO.html) |  |  |

Example

```
{
  "versionDescription" : "...",
  "colleagueId" : "...",
  "accessCount" : 12345,
  "additionalComments" : "...",
  "phisicalFile" : "...",
  "onCheckout" : true,
  "parentId" : 12345,
  "forApproval" : true,
  "version" : 12345,
  "children" : [ {
    "versionDescription" : "...",
    "colleagueId" : "...",
    "accessCount" : 12345,
    "additionalComments" : "...",
    "phisicalFile" : "...",
    "onCheckout" : true,
    "parentId" : 12345,
    "forApproval" : true,
    "version" : 12345,
    "children" : [ { }, { } ],
    "idSource" : 12345,
    "createDate" : 12345,
    "approvedDate" : 12345,
    "securityLevel" : 12345,
    "type" : "...",
    "immutable" : true,
    "versionSource" : 12345,
    "removed" : true,
    "phisicalFileSize" : 12345.0,
    "crc" : 12345,
    "versionOption" : "...",
    "articleContent" : "...",
    "publisherId" : "...",
    "publisherName" : "...",
    "allowMuiltiCardsPerUser" : true,
    "documentPropertyNumber" : 12345,
    "fileURL" : "...",
    "activeUserApprover" : true,
    "documentPropertyVersion" : 12345,
    "favorite" : true,
    "expirationDate" : 12345,
    "activeVersion" : true,
    "expiredForm" : true,
    "validationStartDate" : 12345,
    "iconPath" : "...",
    "id" : 12345,
    "userAnswerForm" : true,
    "companyId" : 12345,
    "description" : "...",
    "userPermission" : 12345,
    "lastModifiedDate" : 12345,
    "isPrivate" : true,
    "colleagueName" : "...",
    "attachments" : [ {
      "attachment" : true,
      "downloadURL" : "...",
      "principal" : true,
      "fileName" : "..."
    }, {
      "attachment" : true,
      "downloadURL" : "...",
      "principal" : true,
      "fileName" : "..."
    } ]
  }, {
    "versionDescription" : "...",
    "colleagueId" : "...",
    "accessCount" : 12345,
    "additionalComments" : "...",
    "phisicalFile" : "...",
    "onCheckout" : true,
    "parentId" : 12345,
    "forApproval" : true,
    "version" : 12345,
    "children" : [ { }, { } ],
    "idSource" : 12345,
    "createDate" : 12345,
    "approvedDate" : 12345,
    "securityLevel" : 12345,
    "type" : "...",
    "immutable" : true,
    "versionSource" : 12345,
    "removed" : true,
    "phisicalFileSize" : 12345.0,
    "crc" : 12345,
    "versionOption" : "...",
    "articleContent" : "...",
    "publisherId" : "...",
    "publisherName" : "...",
    "allowMuiltiCardsPerUser" : true,
    "documentPropertyNumber" : 12345,
    "fileURL" : "...",
    "activeUserApprover" : true,
    "documentPropertyVersion" : 12345,
    "favorite" : true,
    "expirationDate" : 12345,
    "activeVersion" : true,
    "expiredForm" : true,
    "validationStartDate" : 12345,
    "iconPath" : "...",
    "id" : 12345,
    "userAnswerForm" : true,
    "companyId" : 12345,
    "description" : "...",
    "userPermission" : 12345,
    "lastModifiedDate" : 12345,
    "isPrivate" : true,
    "colleagueName" : "...",
    "attachments" : [ {
      "attachment" : true,
      "downloadURL" : "...",
      "principal" : true,
      "fileName" : "..."
    }, {
      "attachment" : true,
      "downloadURL" : "...",
      "principal" : true,
      "fileName" : "..."
    } ]
  } ],
  "idSource" : 12345,
  "createDate" : 12345,
  "approvedDate" : 12345,
  "securityLevel" : 12345,
  "type" : "...",
  "immutable" : true,
  "versionSource" : 12345,
  "removed" : true,
  "phisicalFileSize" : 12345.0,
  "crc" : 12345,
  "versionOption" : "...",
  "articleContent" : "...",
  "publisherId" : "...",
  "publisherName" : "...",
  "allowMuiltiCardsPerUser" : true,
  "documentPropertyNumber" : 12345,
  "fileURL" : "...",
  "activeUserApprover" : true,
  "documentPropertyVersion" : 12345,
  "favorite" : true,
  "expirationDate" : 12345,
  "activeVersion" : true,
  "expiredForm" : true,
  "validationStartDate" : 12345,
  "iconPath" : "...",
  "id" : 12345,
  "userAnswerForm" : true,
  "companyId" : 12345,
  "description" : "...",
  "userPermission" : 12345,
  "lastModifiedDate" : 12345,
  "isPrivate" : true,
  "colleagueName" : "...",
  "attachments" : [ {
    "attachment" : true,
    "downloadURL" : "...",
    "principal" : true,
    "fileName" : "..."
  }, {
    "attachment" : true,
    "downloadURL" : "...",
    "principal" : true,
    "fileName" : "..."
  } ]
}
```
