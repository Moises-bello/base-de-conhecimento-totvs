---
content_hash: 5c4be96e1860a0287524794d19ab24e3e89d765b99a4dbd12cb2079e2424bd49
fetched_at: '2026-11-03T14:34:37.740059+00:00'
page_id: json_JspConfigDescriptor
product: fluig
source: rest-fluig
title: Fluig REST — JspConfigDescriptor Data Type
type: documentation
url: https://api.fluig.com/old/json_JspConfigDescriptor.html
version: 1
---

# JspConfigDescriptor Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| jspPropertyGroups | array of [JspPropertyGroupDescriptor](https://api.fluig.com/old/json_JspPropertyGroupDescriptor.html) |  |
| taglibs | array of [TaglibDescriptor](https://api.fluig.com/old/json_TaglibDescriptor.html) |  |

Example

```
{
  "jspPropertyGroups" : [ {
    "includePreludes" : [ "...", "..." ],
    "urlPatterns" : [ "...", "..." ],
    "buffer" : "...",
    "isXml" : "...",
    "errorOnUndeclaredNamespace" : "...",
    "defaultContentType" : "...",
    "deferredSyntaxAllowedAsLiteral" : "...",
    "elIgnored" : "...",
    "pageEncoding" : "...",
    "includeCodas" : [ "...", "..." ],
    "scriptingInvalid" : "...",
    "trimDirectiveWhitespaces" : "..."
  }, {
    "includePreludes" : [ "...", "..." ],
    "urlPatterns" : [ "...", "..." ],
    "buffer" : "...",
    "isXml" : "...",
    "errorOnUndeclaredNamespace" : "...",
    "defaultContentType" : "...",
    "deferredSyntaxAllowedAsLiteral" : "...",
    "elIgnored" : "...",
    "pageEncoding" : "...",
    "includeCodas" : [ "...", "..." ],
    "scriptingInvalid" : "...",
    "trimDirectiveWhitespaces" : "..."
  } ],
  "taglibs" : [ {
    "taglibLocation" : "...",
    "taglibURI" : "..."
  }, {
    "taglibLocation" : "...",
    "taglibURI" : "..."
  } ]
}
```
