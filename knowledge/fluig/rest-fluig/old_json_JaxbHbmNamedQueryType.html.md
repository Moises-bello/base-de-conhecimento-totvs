---
content_hash: 0732516aaffa543c726743edd54440587081331257ac62b4e0dc565a01e2f14d
fetched_at: '2026-11-03T14:34:37.546468+00:00'
page_id: json_JaxbHbmNamedQueryType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNamedQueryType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html
version: 1
---

# JaxbHbmNamedQueryType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| content | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| cacheable | boolean | required |  |
| name | string |  |  |
| comment | string |  |  |
| flushMode | [FlushMode](https://api.fluig.com/old/json_FlushMode.html) |  |  |
| cacheRegion | string |  |  |
| timeout | number |  |  |
| fetchSize | number |  |  |
| cacheMode | [CacheMode](https://api.fluig.com/old/json_CacheMode.html) |  |  |
| readOnly | boolean | required |  |

Example

```
{
  "content" : [ { }, { } ],
  "cacheable" : true,
  "name" : "...",
  "comment" : "...",
  "flushMode" : "COMMIT",
  "cacheRegion" : "...",
  "timeout" : 12345,
  "fetchSize" : 12345,
  "cacheMode" : "NORMAL",
  "readOnly" : true
}
```
