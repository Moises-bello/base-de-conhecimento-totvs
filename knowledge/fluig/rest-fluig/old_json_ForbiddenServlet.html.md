---
content_hash: f083c47e685c0a577105ba1249a5f883711b52026f8ee232a7b2eccabf4da5db
fetched_at: '2026-11-03T14:34:37.043512+00:00'
page_id: json_ForbiddenServlet
product: fluig
source: rest-fluig
title: Fluig REST — ForbiddenServlet Data Type
type: documentation
url: https://api.fluig.com/old/json_ForbiddenServlet.html
version: 1
---

# ForbiddenServlet Data Type

Servlet to return correct [http forbidden](https://api.fluig.com/old/http forbidden) status to unauthenticated users.

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
    "defaultSessionTrackingModes" : [ "COOKIE", "SSL" ],
    "minorVersion" : 12345,
    "effectiveSessionTrackingModes" : [ "URL", "SSL" ],
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
      "defaultSessionTrackingModes" : [ "URL", "URL" ],
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
