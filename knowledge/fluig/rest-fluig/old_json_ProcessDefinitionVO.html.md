---
content_hash: 3147862e39f605db0cc151e5626df22e2a4a3288934006a7c285d342bb97b916
fetched_at: '2026-11-03T14:34:38.025110+00:00'
page_id: json_ProcessDefinitionVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessDefinitionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessDefinitionVO.html
version: 1
---

# ProcessDefinitionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| complementsLevel | number |  |  |
| processTemplateId | string |  |  |
| bpmnVersion | number | required |  |
| editionMode | string |  |  |
| active | string |  |  |
| processDescription | string |  |  |
| notifyManagerComplements | boolean |  |  |
| notifyRequisitionerComplements | boolean |  |  |
| version | number | required |  |
| webEditable | boolean | required |  |
| formId | number | required |  |
| notifyAuthorityComplements | boolean |  |  |
| mobileReady | boolean | required |  |
| icon | string |  |  |
| processId | string |  |  |
| formIdV2 | number | required |  |

Example

```
{
  "complementsLevel" : 12345,
  "processTemplateId" : "...",
  "bpmnVersion" : 12345,
  "editionMode" : "...",
  "active" : "...",
  "processDescription" : "...",
  "notifyManagerComplements" : true,
  "notifyRequisitionerComplements" : true,
  "version" : 12345,
  "webEditable" : true,
  "formId" : 12345,
  "notifyAuthorityComplements" : true,
  "mobileReady" : true,
  "icon" : "...",
  "processId" : "...",
  "formIdV2" : 12345
}
```
