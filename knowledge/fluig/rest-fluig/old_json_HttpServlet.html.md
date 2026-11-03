---
content_hash: 3a856cbf286c2852c0f6df06f78c321513bc9461398e85c85580b338a7a7d8a7
fetched_at: '2026-11-03T14:34:37.131951+00:00'
page_id: json_HttpServlet
product: fluig
source: rest-fluig
title: Fluig REST — HttpServlet Data Type
type: documentation
url: https://api.fluig.com/old/json_HttpServlet.html
version: 1
---

# HttpServlet Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| Properties inherited from [GenericServlet](https://api.fluig.com/old/json_GenericServlet.html) | | |
| servletName | string |  |
| servletContext | [ServletContext](https://api.fluig.com/old/json_ServletContext.html) |  |
| initParameterNames | [EnumerationOfString](https://api.fluig.com/old/json_EnumerationOfString.html) |  |
| servletInfo | string |  |
| servletConfig | [ServletConfig](https://api.fluig.com/old/json_ServletConfig.html) |  |

Example

```
{
  "servletName" : "...",
  "servletContext" : {
    "attributeNames" : { },
    "defaultSessionTrackingModes" : [ "SSL", "COOKIE" ],
    "minorVersion" : 12345,
    "effectiveSessionTrackingModes" : [ "SSL", "COOKIE" ],
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
  "servletInfo" : "...",
  "servletConfig" : {
    "servletContext" : {
      "attributeNames" : { },
      "defaultSessionTrackingModes" : [ "URL", "SSL" ],
      "minorVersion" : 12345,
      "effectiveSessionTrackingModes" : [ "SSL", "SSL" ],
      "jspConfigDescriptor" : { },
      "majorVersion" : 12345,
      "classLoader" : { },
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
      "sessionCookieConfig" : { },
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
}
```
