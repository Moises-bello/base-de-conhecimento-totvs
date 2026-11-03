---
content_hash: 9b665d9144357f510195fdaf64b513c72d7044dc7882e8c35c552c834adcd9c5
fetched_at: '2026-11-03T14:34:37.078802+00:00'
page_id: json_GenericServlet
product: fluig
source: rest-fluig
title: Fluig REST — GenericServlet Data Type
type: documentation
url: https://api.fluig.com/old/json_GenericServlet.html
version: 1
---

# GenericServlet Data Type

Properties

| name | data type | description |
| --- | --- | --- |
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
      "defaultSessionTrackingModes" : [ "SSL", "SSL" ],
      "minorVersion" : 12345,
      "effectiveSessionTrackingModes" : [ "URL", "SSL" ],
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
