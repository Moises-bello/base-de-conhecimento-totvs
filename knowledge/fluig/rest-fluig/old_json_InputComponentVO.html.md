---
content_hash: 1963dbaa89a0f503127fe388e2fc9abf98228d259d8eb63ec53664a29a0e1383
fetched_at: '2026-11-03T14:34:37.204069+00:00'
page_id: json_InputComponentVO
product: fluig
source: rest-fluig
title: Fluig REST — InputComponentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_InputComponentVO.html
version: 1
---

# InputComponentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| Properties inherited from [AbstractFormComponentVO](https://api.fluig.com/old/json_AbstractFormComponentVO.html) | | |
| minsize | string |  |
| configurations | [ConfigurationVO](https://api.fluig.com/old/json_ConfigurationVO.html) |  |
| type | string |  |
| helpmessage | string |  |
| fieldid | string |  |
| label | string |  |
| configuratorId | string |  |
| size | string |  |
| children | array of [AbstractFormComponentVO](https://api.fluig.com/old/json_AbstractFormComponentVO.html) |  |
| sensitivedata | [SensitiveDataVO](https://api.fluig.com/old/json_SensitiveDataVO.html) |  |
| fieldType | string |  |
| placeholder | string |  |
| value | object |  |

Example

```
{
  "fieldType" : "INPUT",
  "minsize" : "...",
  "configurations" : {
    "analyticsText" : [ {
      "index" : 12345,
      "fieldId" : "..."
    }, {
      "index" : 12345,
      "fieldId" : "..."
    } ],
    "analyticsNumber" : [ {
      "index" : 12345,
      "fieldId" : "..."
    }, {
      "index" : 12345,
      "fieldId" : "..."
    } ],
    "fieldDescription" : "...",
    "datasetName" : "..."
  },
  "type" : "...",
  "helpmessage" : "...",
  "fieldid" : "...",
  "label" : "...",
  "configuratorId" : "...",
  "size" : "...",
  "children" : [ {
    "fieldType" : "AbstractFormComponentVO",
    "minsize" : "...",
    "configurations" : {
      "analyticsText" : [ { }, { } ],
      "analyticsNumber" : [ { }, { } ],
      "fieldDescription" : "...",
      "datasetName" : "..."
    },
    "type" : "...",
    "helpmessage" : "...",
    "fieldid" : "...",
    "label" : "...",
    "configuratorId" : "...",
    "size" : "...",
    "children" : [ { }, { } ],
    "sensitivedata" : {
      "canAnonymizeData" : true,
      "sensitiveDataType" : "...",
      "sensitiveData" : true,
      "reasons" : [ { }, { } ]
    },
    "placeholder" : "...",
    "value" : { },
    "extension1" : "...",
    "extension2" : "..."
  }, {
    "fieldType" : "AbstractFormComponentVO",
    "minsize" : "...",
    "configurations" : {
      "analyticsText" : [ { }, { } ],
      "analyticsNumber" : [ { }, { } ],
      "fieldDescription" : "...",
      "datasetName" : "..."
    },
    "type" : "...",
    "helpmessage" : "...",
    "fieldid" : "...",
    "label" : "...",
    "configuratorId" : "...",
    "size" : "...",
    "children" : [ { }, { } ],
    "sensitivedata" : {
      "canAnonymizeData" : true,
      "sensitiveDataType" : "...",
      "sensitiveData" : true,
      "reasons" : [ { }, { } ]
    },
    "placeholder" : "...",
    "value" : { },
    "extension1" : "...",
    "extension2" : "..."
  } ],
  "sensitivedata" : {
    "canAnonymizeData" : true,
    "sensitiveDataType" : "...",
    "sensitiveData" : true,
    "reasons" : [ {
      "sensitiveDataClassification" : "...",
      "sensitiveDataClassificationJustify" : "..."
    }, {
      "sensitiveDataClassification" : "...",
      "sensitiveDataClassificationJustify" : "..."
    } ]
  },
  "placeholder" : "...",
  "value" : { },
  "extension1" : "...",
  "extension2" : "..."
}
```
