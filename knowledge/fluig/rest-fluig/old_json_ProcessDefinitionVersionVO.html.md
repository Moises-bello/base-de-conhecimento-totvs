---
content_hash: 8b01b8f52de3cea264cabee4100704ec37a2b1a30709966d4eacc68fe69ed80e
fetched_at: '2026-11-03T14:34:38.041548+00:00'
page_id: json_ProcessDefinitionVersionVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessDefinitionVersionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessDefinitionVersionVO.html
version: 1
---

# ProcessDefinitionVersionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| formIdV2 | number |  |  |
| rowId | number | required |  |
| categoryStructure | string |  |  |
| companyId | number | required |  |
| formId | number |  |  |
| favorite | boolean |  |  |
| selected | boolean |  |  |
| relatedDatasets | array of string |  |  |
| fullCategoryStructure | string |  |  |
| mobileReady | boolean | required |  |
| processId | string |  |  |
| initialProcessState | [ProcessStateDto](https://api.fluig.com/old/json_ProcessStateDto.html) |  |  |
| children | array of [ProcessDefinitionVersionVO](https://api.fluig.com/old/json_ProcessDefinitionVersionVO.html) |  |  |
| childrenBackup | array of [ProcessDefinitionVersionVO](https://api.fluig.com/old/json_ProcessDefinitionVersionVO.html) |  |  |
| counterSign | boolean |  |  |
| version | number | required |  |
| icon | string |  |  |
| processDescription | string |  |  |
| formVersion | number |  |  |
| versionDescription | string |  |  |

Example

```
{
  "formIdV2" : 12345,
  "rowId" : 12345,
  "categoryStructure" : "...",
  "companyId" : 12345,
  "formId" : 12345,
  "favorite" : true,
  "selected" : true,
  "relatedDatasets" : [ "...", "..." ],
  "fullCategoryStructure" : "...",
  "mobileReady" : true,
  "processId" : "...",
  "initialProcessState" : {
    "stateDescription" : "...",
    "sequence" : 12345,
    "companyId" : 12345,
    "stateName" : "...",
    "counterSign" : true
  },
  "children" : [ {
    "formIdV2" : 12345,
    "rowId" : 12345,
    "categoryStructure" : "...",
    "companyId" : 12345,
    "formId" : 12345,
    "favorite" : true,
    "selected" : true,
    "relatedDatasets" : [ "...", "..." ],
    "fullCategoryStructure" : "...",
    "mobileReady" : true,
    "processId" : "...",
    "initialProcessState" : {
      "stateDescription" : "...",
      "sequence" : 12345,
      "companyId" : 12345,
      "stateName" : "...",
      "counterSign" : true
    },
    "children" : [ { }, { } ],
    "childrenBackup" : [ { }, { } ],
    "counterSign" : true,
    "version" : 12345,
    "icon" : "...",
    "processDescription" : "...",
    "formVersion" : 12345,
    "versionDescription" : "..."
  }, {
    "formIdV2" : 12345,
    "rowId" : 12345,
    "categoryStructure" : "...",
    "companyId" : 12345,
    "formId" : 12345,
    "favorite" : true,
    "selected" : true,
    "relatedDatasets" : [ "...", "..." ],
    "fullCategoryStructure" : "...",
    "mobileReady" : true,
    "processId" : "...",
    "initialProcessState" : {
      "stateDescription" : "...",
      "sequence" : 12345,
      "companyId" : 12345,
      "stateName" : "...",
      "counterSign" : true
    },
    "children" : [ { }, { } ],
    "childrenBackup" : [ { }, { } ],
    "counterSign" : true,
    "version" : 12345,
    "icon" : "...",
    "processDescription" : "...",
    "formVersion" : 12345,
    "versionDescription" : "..."
  } ],
  "childrenBackup" : [ {
    "formIdV2" : 12345,
    "rowId" : 12345,
    "categoryStructure" : "...",
    "companyId" : 12345,
    "formId" : 12345,
    "favorite" : true,
    "selected" : true,
    "relatedDatasets" : [ "...", "..." ],
    "fullCategoryStructure" : "...",
    "mobileReady" : true,
    "processId" : "...",
    "initialProcessState" : {
      "stateDescription" : "...",
      "sequence" : 12345,
      "companyId" : 12345,
      "stateName" : "...",
      "counterSign" : true
    },
    "children" : [ { }, { } ],
    "childrenBackup" : [ { }, { } ],
    "counterSign" : true,
    "version" : 12345,
    "icon" : "...",
    "processDescription" : "...",
    "formVersion" : 12345,
    "versionDescription" : "..."
  }, {
    "formIdV2" : 12345,
    "rowId" : 12345,
    "categoryStructure" : "...",
    "companyId" : 12345,
    "formId" : 12345,
    "favorite" : true,
    "selected" : true,
    "relatedDatasets" : [ "...", "..." ],
    "fullCategoryStructure" : "...",
    "mobileReady" : true,
    "processId" : "...",
    "initialProcessState" : {
      "stateDescription" : "...",
      "sequence" : 12345,
      "companyId" : 12345,
      "stateName" : "...",
      "counterSign" : true
    },
    "children" : [ { }, { } ],
    "childrenBackup" : [ { }, { } ],
    "counterSign" : true,
    "version" : 12345,
    "icon" : "...",
    "processDescription" : "...",
    "formVersion" : 12345,
    "versionDescription" : "..."
  } ],
  "counterSign" : true,
  "version" : 12345,
  "icon" : "...",
  "processDescription" : "...",
  "formVersion" : 12345,
  "versionDescription" : "..."
}
```
