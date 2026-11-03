---
content_hash: 67c100d588e599872f1c31453932711aa455df33e7119300fe671ca3f59cbea1
fetched_at: '2026-11-03T14:34:36.507717+00:00'
page_id: json_ConfigurationVO
product: fluig
source: rest-fluig
title: Fluig REST — ConfigurationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ConfigurationVO.html
version: 1
---

# ConfigurationVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| analyticsText | array of [AnalyticsOrderVO](https://api.fluig.com/old/json_AnalyticsOrderVO.html) |  |
| analyticsNumber | array of [AnalyticsOrderVO](https://api.fluig.com/old/json_AnalyticsOrderVO.html) |  |
| fieldDescription | string |  |
| datasetName | string |  |

Example

```
{
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
}
```
