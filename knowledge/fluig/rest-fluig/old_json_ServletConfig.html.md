---
content_hash: 2e0ae67bbb420536890eeffa37587ae7193e55f94b430a1655527bbbf3e44440
fetched_at: '2026-11-03T14:34:38.368952+00:00'
page_id: json_ServletConfig
product: fluig
source: rest-fluig
title: Fluig REST — ServletConfig Data Type
type: documentation
url: https://api.fluig.com/old/json_ServletConfig.html
version: 1
---

# ServletConfig Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| servletContext | [ServletContext](https://api.fluig.com/old/json_ServletContext.html) |  |
| initParameterNames | [EnumerationOfString](https://api.fluig.com/old/json_EnumerationOfString.html) |  |
| servletName | string |  |

Example

```
{
  "servletContext" : {
    "attributeNames" : { },
    "defaultSessionTrackingModes" : [ "COOKIE", "SSL" ],
    "minorVersion" : 12345,
    "effectiveSessionTrackingModes" : [ "URL", "URL" ],
    "jspConfigDescriptor" : {
      "jspPropertyGroups" : [ { }, { } ],
      "taglibs" : [ { }, { } ]
    },
    "majorVersion" : 12345,
    "classLoader" : {
      "registeredAsParallelCapable" : true,
      "platformClassLoader" : { },
      "definedPackages" : [ { }, { } ],
      "name" : "...",
      "unnamedModule" : { },
      "parent" : { },
      "systemClassLoader" : { }
    },
    "filterRegistrations" : {
      "property1" : { },
      "property2" : { }
    },
    "servletContextName" : "...",
    "virtualServerName" : "...",
    "initParameterNames" : { },
    "serverInfo" : "...",
    "effectiveMinorVersion" : 12345,
    "sessionTimeout" : 12345,
    "responseCharacterEncoding" : "...",
    "effectiveMajorVersion" : 12345,
    "sessionCookieConfig" : {
      "maxAge" : 12345,
      "comment" : "...",
      "name" : "...",
      "path" : "...",
      "httpOnly" : true,
      "domain" : "...",
      "secure" : true
    },
    "contextPath" : "...",
    "servletRegistrations" : {
      "property1" : { },
      "property2" : { }
    },
    "requestCharacterEncoding" : "..."
  },
  "initParameterNames" : { },
  "servletName" : "..."
}
```
