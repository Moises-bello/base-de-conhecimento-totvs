---
content_hash: 028a722d925129ecbc5665c5df83406bbfcfe7383f09c629698cadb38d06f56c
fetched_at: '2026-11-03T14:34:37.965400+00:00'
page_id: json_PingServlet
product: fluig
source: rest-fluig
title: Fluig REST — PingServlet Data Type
type: documentation
url: https://api.fluig.com/old/json_PingServlet.html
version: 1
---

# PingServlet Data Type

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
    "defaultSessionTrackingModes" : [ "COOKIE", "COOKIE" ],
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
      "defaultSessionTrackingModes" : [ "URL", "COOKIE" ],
      "minorVersion" : 12345,
      "effectiveSessionTrackingModes" : [ "SSL", "URL" ],
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
