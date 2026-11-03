---
content_hash: 265f725f4c67fded263fa4ec1f587e7d2a5fdf1382dc57d796af8738db150a32
fetched_at: '2026-11-03T14:34:38.756540+00:00'
page_id: json_UserServiceRest_user
product: fluig
source: rest-fluig
title: Fluig REST — UserServiceRest Data Type
type: documentation
url: https://api.fluig.com/old/json_UserServiceRest_user.html
version: 1
---

# UserServiceRest Data Type

Users

Properties

| name | data type | description |
| --- | --- | --- |
| ~~loggedUser~~ | ~~[SocialVO](https://api.fluig.com/old/json_SocialVO.html)~~ | ~~Return the logged user details.~~ |
| loggedUserV2 | [Response](https://api.fluig.com/old/json_Response.html) | Return the logged user details. |
| Properties inherited from [GenericBean](https://api.fluig.com/old/json_GenericBean.html) | | |
| errorHandler | [ErrorHandler](https://api.fluig.com/old/json_ErrorHandler.html) |  |

Example

```
{
  "loggedUserV2" : {
    "mediaType" : {
      "subtype" : "...",
      "type" : "...",
      "parameters" : {
        "property1" : "...",
        "property2" : "..."
      },
      "wildcardType" : true,
      "wildcardSubtype" : true
    },
    "status" : 12345,
    "metadata" : {
      "property1" : [ { }, { } ],
      "property2" : [ { }, { } ]
    },
    "lastModified" : 12345,
    "links" : [ {
      "uri" : "...",
      "uriBuilder" : { },
      "rels" : [ "...", "..." ],
      "type" : "...",
      "rel" : "...",
      "title" : "...",
      "params" : {
        "property1" : "...",
        "property2" : "..."
      }
    }, {
      "uri" : "...",
      "uriBuilder" : { },
      "rels" : [ "...", "..." ],
      "type" : "...",
      "rel" : "...",
      "title" : "...",
      "params" : {
        "property1" : "...",
        "property2" : "..."
      }
    } ],
    "date" : 12345,
    "statusInfo" : {
      "reasonPhrase" : "...",
      "statusCode" : 12345,
      "family" : "OTHER"
    },
    "entityTag" : {
      "weak" : true,
      "value" : "..."
    },
    "entity" : { },
    "stringHeaders" : {
      "property1" : [ "...", "..." ],
      "property2" : [ "...", "..." ]
    },
    "headers" : {
      "property1" : [ { }, { } ],
      "property2" : [ { }, { } ]
    },
    "cookies" : {
      "property1" : {
        "secure" : true,
        "comment" : "...",
        "maxAge" : 12345,
        "httpOnly" : true,
        "expiry" : 12345,
        "name" : "...",
        "domain" : "...",
        "version" : 12345,
        "path" : "...",
        "value" : "..."
      },
      "property2" : {
        "secure" : true,
        "comment" : "...",
        "maxAge" : 12345,
        "httpOnly" : true,
        "expiry" : 12345,
        "name" : "...",
        "domain" : "...",
        "version" : 12345,
        "path" : "...",
        "value" : "..."
      }
    },
    "location" : "...",
    "allowedMethods" : [ "...", "..." ],
    "length" : 12345,
    "language" : "..."
  }
}
```
