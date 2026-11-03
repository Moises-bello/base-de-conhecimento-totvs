---
content_hash: 6d038eb665121cfd200dc8e0bddf33aa7c65238ceab80f5d3715f22e901bddeb
fetched_at: '2026-11-03T14:34:37.542006+00:00'
page_id: json_JaxbHbmNamedNativeQueryType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNamedNativeQueryType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html
version: 1
---

# JaxbHbmNamedNativeQueryType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| cacheRegion | string |  |  |
| readOnly | boolean | required |  |
| timeout | number |  |  |
| comment | string |  |  |
| cacheable | boolean | required |  |
| callable | boolean | required |  |
| cacheMode | [CacheMode](https://api.fluig.com/old/json_CacheMode.html) |  |  |
| fetchSize | number |  |  |
| resultsetRef | string |  |  |
| content | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| name | string |  |  |
| flushMode | [FlushMode](https://api.fluig.com/old/json_FlushMode.html) |  |  |

Example

```
{
  "cacheRegion" : "...",
  "readOnly" : true,
  "timeout" : 12345,
  "comment" : "...",
  "cacheable" : true,
  "callable" : true,
  "cacheMode" : "NORMAL",
  "fetchSize" : 12345,
  "resultsetRef" : "...",
  "content" : [ { }, { } ],
  "name" : "...",
  "flushMode" : "ALWAYS"
}
```
