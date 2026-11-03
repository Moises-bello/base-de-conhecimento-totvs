---
content_hash: 3cf2c9d18cdfb56fd9ba4a4213dd0751f7191c1947bce3667eec52eda97de522
fetched_at: '2026-11-03T14:34:36.351195+00:00'
page_id: json_CardCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — CardCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardCreateVO.html
version: 1
---

# CardCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| attachments | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO_workflow.html) |  |
| formData | array of map of string |  |
| permissions | array of [CardPermissionVO](https://api.fluig.com/old/json_CardPermissionVO.html) |  |
| documentDescription | string |  |
| parentDocumentId | number |  |
| version | number |  |
| attachments | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO_workflow.html) |  |
| topicId | number |  |
| inheritSecurity | boolean |  |

Example

```
{
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
  "formData" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ],
  "permissions" : [ {
    "serialVersionUID" : 12345,
    "securityLevel" : 12345,
    "securityVersion" : true,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  }, {
    "serialVersionUID" : 12345,
    "securityLevel" : 12345,
    "securityVersion" : true,
    "inheritSecurity" : true,
    "downloadEnabled" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  } ],
  "documentDescription" : "...",
  "parentDocumentId" : 12345,
  "version" : 12345,
  "topicId" : 12345,
  "inheritSecurity" : true
}
```
