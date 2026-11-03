---
content_hash: 43316cfdaf3adeeba6e9b7643c415a23c02c1ad59d98cf33f098b34cb58b6516
fetched_at: '2026-11-03T14:34:36.710159+00:00'
page_id: json_DocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentVO.html
version: 1
---

# DocumentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| isPrivate | boolean |  |  |
| versionOption | string |  |  |
| removed | boolean |  |  |
| onCheckout | boolean |  |  |
| forApproval | boolean |  |  |
| securityLevel | number | required |  |
| id | number |  |  |
| version | number |  |  |
| companyId | number |  |  |
| type | string |  |  |
| description | string |  |  |
| colleagueId | string |  |  |
| publisherId | string |  |  |
| createDate | number |  |  |
| approvedDate | number |  |  |
| expirationDate | number |  |  |
| expires | boolean |  |  |
| lastModifiedDate | number |  |  |
| parentId | number |  |  |
| activeVersion | boolean |  |  |
| phisicalFile | string |  |  |
| validationStartDate | number |  |  |
| children | array of [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) |  |  |
| attachments | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO_vo.html) |  |  |
| userPermission | number |  |  |
| iconPath | string |  |  |
| publisherName | string |  |  |
| immutable | boolean | required |  |
| crc | number |  |  |
| idSource | number |  |  |
| versionSource | number |  |  |
| additionalComments | string |  |  |
| documentPropertyNumber | number |  |  |
| documentPropertyVersion | number |  |  |
| accessCount | number |  |  |
| versionDescription | string |  |  |
| colleagueName | string |  |  |
| phisicalFileSize | number |  |  |
| favorite | boolean |  |  |
| articleContent | string |  |  |
| userAnswerForm | boolean |  |  |
| allowMuiltiCardsPerUser | boolean |  |  |
| expiredForm | boolean |  |  |
| sociableDocumentDto | [SociableDocumentDto](https://api.fluig.com/old/json_SociableDocumentDto.html) |  |  |
| activeUserApprover | boolean |  |  |
| fileURL | string |  |  |
| downloadEnabled | boolean |  |  |
| watermarkId | number |  |  |
| hashAnnotations | string |  |  |

Example

```
{
  "isPrivate" : true,
  "versionOption" : "...",
  "removed" : true,
  "onCheckout" : true,
  "forApproval" : true,
  "securityLevel" : 12345,
  "id" : 12345,
  "version" : 12345,
  "companyId" : 12345,
  "type" : "...",
  "description" : "...",
  "colleagueId" : "...",
  "publisherId" : "...",
  "createDate" : 12345,
  "approvedDate" : 12345,
  "expirationDate" : 12345,
  "expires" : true,
  "lastModifiedDate" : 12345,
  "parentId" : 12345,
  "activeVersion" : true,
  "phisicalFile" : "...",
  "validationStartDate" : 12345,
  "children" : [ {
    "isPrivate" : true,
    "versionOption" : "...",
    "removed" : true,
    "onCheckout" : true,
    "forApproval" : true,
    "securityLevel" : 12345,
    "id" : 12345,
    "version" : 12345,
    "companyId" : 12345,
    "type" : "...",
    "description" : "...",
    "colleagueId" : "...",
    "publisherId" : "...",
    "createDate" : 12345,
    "approvedDate" : 12345,
    "expirationDate" : 12345,
    "expires" : true,
    "lastModifiedDate" : 12345,
    "parentId" : 12345,
    "activeVersion" : true,
    "phisicalFile" : "...",
    "validationStartDate" : 12345,
    "children" : [ { }, { } ],
    "attachments" : [ {
      "downloadURL" : "...",
      "fileName" : "...",
      "principal" : true,
      "attachment" : true
    }, {
      "downloadURL" : "...",
      "fileName" : "...",
      "principal" : true,
      "attachment" : true
    } ],
    "userPermission" : 12345,
    "iconPath" : "...",
    "publisherName" : "...",
    "immutable" : true,
    "crc" : 12345,
    "idSource" : 12345,
    "versionSource" : 12345,
    "additionalComments" : "...",
    "documentPropertyNumber" : 12345,
    "documentPropertyVersion" : 12345,
    "accessCount" : 12345,
    "versionDescription" : "...",
    "colleagueName" : "...",
    "phisicalFileSize" : 12345.0,
    "favorite" : true,
    "articleContent" : "...",
    "userAnswerForm" : true,
    "allowMuiltiCardsPerUser" : true,
    "expiredForm" : true,
    "sociableDocumentDto" : {
      "denounced" : true,
      "version" : 12345,
      "commented" : true,
      "following" : true,
      "numberShares" : 12345,
      "documentId" : 12345,
      "numberFollows" : 12345,
      "shared" : true,
      "liked" : true,
      "sociableId" : 12345,
      "numberLikes" : 12345,
      "numberComments" : 12345,
      "numberDenouncements" : 12345
    },
    "activeUserApprover" : true,
    "fileURL" : "...",
    "downloadEnabled" : true,
    "watermarkId" : 12345,
    "hashAnnotations" : "..."
  }, {
    "isPrivate" : true,
    "versionOption" : "...",
    "removed" : true,
    "onCheckout" : true,
    "forApproval" : true,
    "securityLevel" : 12345,
    "id" : 12345,
    "version" : 12345,
    "companyId" : 12345,
    "type" : "...",
    "description" : "...",
    "colleagueId" : "...",
    "publisherId" : "...",
    "createDate" : 12345,
    "approvedDate" : 12345,
    "expirationDate" : 12345,
    "expires" : true,
    "lastModifiedDate" : 12345,
    "parentId" : 12345,
    "activeVersion" : true,
    "phisicalFile" : "...",
    "validationStartDate" : 12345,
    "children" : [ { }, { } ],
    "attachments" : [ {
      "downloadURL" : "...",
      "fileName" : "...",
      "principal" : true,
      "attachment" : true
    }, {
      "downloadURL" : "...",
      "fileName" : "...",
      "principal" : true,
      "attachment" : true
    } ],
    "userPermission" : 12345,
    "iconPath" : "...",
    "publisherName" : "...",
    "immutable" : true,
    "crc" : 12345,
    "idSource" : 12345,
    "versionSource" : 12345,
    "additionalComments" : "...",
    "documentPropertyNumber" : 12345,
    "documentPropertyVersion" : 12345,
    "accessCount" : 12345,
    "versionDescription" : "...",
    "colleagueName" : "...",
    "phisicalFileSize" : 12345.0,
    "favorite" : true,
    "articleContent" : "...",
    "userAnswerForm" : true,
    "allowMuiltiCardsPerUser" : true,
    "expiredForm" : true,
    "sociableDocumentDto" : {
      "denounced" : true,
      "version" : 12345,
      "commented" : true,
      "following" : true,
      "numberShares" : 12345,
      "documentId" : 12345,
      "numberFollows" : 12345,
      "shared" : true,
      "liked" : true,
      "sociableId" : 12345,
      "numberLikes" : 12345,
      "numberComments" : 12345,
      "numberDenouncements" : 12345
    },
    "activeUserApprover" : true,
    "fileURL" : "...",
    "downloadEnabled" : true,
    "watermarkId" : 12345,
    "hashAnnotations" : "..."
  } ],
  "attachments" : [ {
    "downloadURL" : "...",
    "fileName" : "...",
    "principal" : true,
    "attachment" : true
  }, {
    "downloadURL" : "...",
    "fileName" : "...",
    "principal" : true,
    "attachment" : true
  } ],
  "userPermission" : 12345,
  "iconPath" : "...",
  "publisherName" : "...",
  "immutable" : true,
  "crc" : 12345,
  "idSource" : 12345,
  "versionSource" : 12345,
  "additionalComments" : "...",
  "documentPropertyNumber" : 12345,
  "documentPropertyVersion" : 12345,
  "accessCount" : 12345,
  "versionDescription" : "...",
  "colleagueName" : "...",
  "phisicalFileSize" : 12345.0,
  "favorite" : true,
  "articleContent" : "...",
  "userAnswerForm" : true,
  "allowMuiltiCardsPerUser" : true,
  "expiredForm" : true,
  "sociableDocumentDto" : {
    "denounced" : true,
    "version" : 12345,
    "commented" : true,
    "following" : true,
    "numberShares" : 12345,
    "documentId" : 12345,
    "numberFollows" : 12345,
    "shared" : true,
    "liked" : true,
    "sociableId" : 12345,
    "numberLikes" : 12345,
    "numberComments" : 12345,
    "numberDenouncements" : 12345
  },
  "activeUserApprover" : true,
  "fileURL" : "...",
  "downloadEnabled" : true,
  "watermarkId" : 12345,
  "hashAnnotations" : "..."
}
```
