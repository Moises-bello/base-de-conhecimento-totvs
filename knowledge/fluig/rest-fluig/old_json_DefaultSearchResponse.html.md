---
content_hash: 02314961558300a16461d97a54c10fee046a47cec754c5feb38e4f110b50a45c
fetched_at: '2026-11-03T14:34:36.583719+00:00'
page_id: json_DefaultSearchResponse
product: fluig
source: rest-fluig
title: Fluig REST — DefaultSearchResponse Data Type
type: documentation
url: https://api.fluig.com/old/json_DefaultSearchResponse.html
version: 1
---

# DefaultSearchResponse Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| offset | number | required |  |
| items | array of map of object |  |  |
| solrAvailable | boolean | required |  |
| totalHits | number |  |  |
| timeElapsed | number |  |  |

Example

```
{
  "offset" : 12345,
  "items" : [ {
    "property1" : { },
    "property2" : { }
  }, {
    "property1" : { },
    "property2" : { }
  } ],
  "solrAvailable" : true,
  "totalHits" : 12345,
  "timeElapsed" : 12345
}
```
