---
content_hash: e5693ab6b8514e04d2af9474cf00d4ea0595c90570915f5852e31baea60d0edf
fetched_at: '2026-11-03T14:34:37.769556+00:00'
page_id: json_LiteralServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — LiteralServiceRest Data Type
type: documentation
url: https://api.fluig.com/old/json_LiteralServiceRest.html
version: 1
---

# LiteralServiceRest Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| mobileLastUpdate | [Response](https://api.fluig.com/old/json_Response.html) |  |
| mobileCustomLiteral | [Response](https://api.fluig.com/old/json_Response.html) |  |

Example

```
{
  "mobileLastUpdate" : {
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
      "family" : "REDIRECTION"
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
  },
  "mobileCustomLiteral" : {
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
      "family" : "SUCCESSFUL"
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
