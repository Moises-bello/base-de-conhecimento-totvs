---
content_hash: 972dda2d332c40cef636b1b2e74605f5288cd085cda19bbb16ae0355c7aae2cc
fetched_at: '2026-11-03T14:34:39.219052+00:00'
page_id: json_WorkflowViewSendVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewSendVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewSendVO.html
version: 1
---

# WorkflowViewSendVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| subProcessSequence | number |  |
| processInstanceId | number |  |
| versionDoc | number |  |
| newObservations | array of [WorkflowViewObservationVO](https://api.fluig.com/old/json_WorkflowViewObservationVO.html) |  |
| transferTaskAfterSelection | boolean |  |
| subProcessId | string |  |
| completeTask | boolean |  |
| selectedDestinyAfterAutomatic | number |  |
| appointments | array of [WorkflowViewAppointmentVO](https://api.fluig.com/old/json_WorkflowViewAppointmentVO.html) |  |
| isDigitalSigned | boolean |  |
| managerMode | boolean |  |
| version | number |  |
| deleteUploadFiles | boolean |  |
| pass | string |  |
| internalFields | array of string |  |
| isLinkReturn | boolean |  |
| comments | string |  |
| processId | string |  |
| selectedState | number |  |
| digitalSignature | boolean |  |
| currentState | number |  |
| taskUserId | string |  |
| conditionAfterAutomatic | number |  |
| attachments | array of [WorkflowViewAttachmentVO](https://api.fluig.com/old/json_WorkflowViewAttachmentVO.html) |  |
| currentMovto | number |  |
| selectedColleague | array of string |  |
| formData | array of map of string |  |

Example

```
{
  "subProcessSequence" : 12345,
  "processInstanceId" : 12345,
  "versionDoc" : 12345,
  "newObservations" : [ {
    "stateSequence" : 12345,
    "movementSequence" : 12345,
    "processInstanceId" : 12345,
    "threadSequence" : 12345,
    "observation" : "...",
    "managerMode" : true
  }, {
    "stateSequence" : 12345,
    "movementSequence" : 12345,
    "processInstanceId" : 12345,
    "threadSequence" : 12345,
    "observation" : "...",
    "managerMode" : true
  } ],
  "transferTaskAfterSelection" : true,
  "subProcessId" : "...",
  "completeTask" : true,
  "selectedDestinyAfterAutomatic" : 12345,
  "appointments" : [ {
    "appointmentTime" : "...",
    "appointmentDate" : 12345
  }, {
    "appointmentTime" : "...",
    "appointmentDate" : 12345
  } ],
  "isDigitalSigned" : true,
  "managerMode" : true,
  "version" : 12345,
  "deleteUploadFiles" : true,
  "pass" : "...",
  "internalFields" : [ "...", "..." ],
  "isLinkReturn" : true,
  "comments" : "...",
  "processId" : "...",
  "selectedState" : 12345,
  "digitalSignature" : true,
  "currentState" : 12345,
  "taskUserId" : "...",
  "conditionAfterAutomatic" : 12345,
  "attachments" : [ {
    "id" : 12345,
    "version" : 12345,
    "fileName" : "...",
    "colleagueId" : "...",
    "deleted" : true,
    "iconUrl" : true,
    "enableEditContent" : true,
    "attachments" : [ {
      "principal" : true,
      "fileName" : "...",
      "attach" : true
    }, {
      "principal" : true,
      "fileName" : "...",
      "attach" : true
    } ],
    "fromFormField" : true,
    "physicalFileName" : "...",
    "name" : "...",
    "uploadId" : "...",
    "documentId" : 12345,
    "iconPath" : "...",
    "enableEdit" : true,
    "documentType" : "...",
    "iconClass" : "...",
    "fullPath" : "...",
    "description" : "...",
    "enablePublish" : true,
    "newAttach" : true,
    "hasOwnSubMenu" : true,
    "droppedZipZone" : true
  }, {
    "id" : 12345,
    "version" : 12345,
    "fileName" : "...",
    "colleagueId" : "...",
    "deleted" : true,
    "iconUrl" : true,
    "enableEditContent" : true,
    "attachments" : [ {
      "principal" : true,
      "fileName" : "...",
      "attach" : true
    }, {
      "principal" : true,
      "fileName" : "...",
      "attach" : true
    } ],
    "fromFormField" : true,
    "physicalFileName" : "...",
    "name" : "...",
    "uploadId" : "...",
    "documentId" : 12345,
    "iconPath" : "...",
    "enableEdit" : true,
    "documentType" : "...",
    "iconClass" : "...",
    "fullPath" : "...",
    "description" : "...",
    "enablePublish" : true,
    "newAttach" : true,
    "hasOwnSubMenu" : true,
    "droppedZipZone" : true
  } ],
  "currentMovto" : 12345,
  "selectedColleague" : [ "...", "..." ],
  "formData" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ]
}
```
