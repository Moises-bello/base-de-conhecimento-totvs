---
content_hash: a57b57e448bc7d8228aa7f7844f265ecc2e2d1eba5def3d742050f2e7f271f51
fetched_at: '2026-11-03T14:34:38.279472+00:00'
page_id: json_ResumeVO
product: fluig
source: rest-fluig
title: Fluig REST — ResumeVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ResumeVO.html
version: 1
---

# ResumeVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| description | string |  |  |
| expired | number | required |  |
| total | number | required |  |
| warning | number | required |  |
| process | string |  |  |
| date | string |  |  |
| onTime | number | required |  |

Example

```
{
  "description" : "...",
  "expired" : 12345,
  "total" : 12345,
  "warning" : 12345,
  "process" : "...",
  "date" : "...",
  "onTime" : 12345
}
```
