---
content_hash: cdf7b3095728e377b9122a99aebd336be94959c823c42216e6bc2480fe6c248c
fetched_at: '2026-11-03T14:34:38.526724+00:00'
page_id: json_SocialInviteVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialInviteVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialInviteVO.html
version: 1
---

# SocialInviteVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| expiration | number |  |
| tenantId | number |  |
| token | string |  |
| alias | string |  |
| qttSubmission | number |  |
| userCreated | number |  |
| id | number |  |
| email | string |  |
| status | [SocialInviteStatus](https://api.fluig.com/old/json_SocialInviteStatus.html) |  |
| fileName | string |  |
| lastSubmission | number |  |

Example

```
{
  "expiration" : 12345,
  "tenantId" : 12345,
  "token" : "...",
  "alias" : "...",
  "qttSubmission" : 12345,
  "userCreated" : 12345,
  "id" : 12345,
  "email" : "...",
  "status" : "DUPLICATED_INVITE",
  "fileName" : "...",
  "lastSubmission" : 12345
}
```
