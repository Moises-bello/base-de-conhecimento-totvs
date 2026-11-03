---
content_hash: bf9b83e3ce0a4c0447c9160feffeeeca33bf75c1376d8df8e15a01111e581a17
fetched_at: '2026-11-03T14:34:38.788181+00:00'
page_id: json_UserWorkflowProcessVO
product: fluig
source: rest-fluig
title: Fluig REST — UserWorkflowProcessVO Data Type
type: documentation
url: https://api.fluig.com/old/json_UserWorkflowProcessVO.html
version: 1
---

# UserWorkflowProcessVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| formId | number |  |  |
| processDescription | string |  |  |
| processInstruction | string |  |  |
| fullCategoryStructure | string |  |  |
| favorite | boolean | required |  |
| companyId | number |  |  |
| inheritFormSecurity | boolean |  |  |
| version | number | required |  |
| publicProcess | boolean |  |  |
| processId | string |  |  |
| mobileReady | boolean |  |  |
| categoryStructure | string |  |  |
| formIdV2 | number |  |  |
| processDiagram | string |  |  |
| active | boolean |  |  |

Example

```
{
  "formId" : 12345,
  "processDescription" : "...",
  "processInstruction" : "...",
  "fullCategoryStructure" : "...",
  "favorite" : true,
  "companyId" : 12345,
  "inheritFormSecurity" : true,
  "version" : 12345,
  "publicProcess" : true,
  "processId" : "...",
  "mobileReady" : true,
  "categoryStructure" : "...",
  "formIdV2" : 12345,
  "processDiagram" : "...",
  "active" : true
}
```
