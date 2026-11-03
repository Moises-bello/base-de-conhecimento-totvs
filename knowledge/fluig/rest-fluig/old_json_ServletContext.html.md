---
content_hash: 610d7c0771325851f062e7e107223dc506e4ed8ebe33e963d47ecc1728bbe4c8
fetched_at: '2026-11-03T14:34:38.376511+00:00'
page_id: json_ServletContext
product: fluig
source: rest-fluig
title: Fluig REST — ServletContext Data Type
type: documentation
url: https://api.fluig.com/old/json_ServletContext.html
version: 1
---

# ServletContext Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| attributeNames | [EnumerationOfString](https://api.fluig.com/old/json_EnumerationOfString.html) |  |  |
| defaultSessionTrackingModes | array of [SessionTrackingMode](https://api.fluig.com/old/json_SessionTrackingMode.html) |  |  |
| minorVersion | number | required |  |
| effectiveSessionTrackingModes | array of [SessionTrackingMode](https://api.fluig.com/old/json_SessionTrackingMode.html) |  |  |
| jspConfigDescriptor | [JspConfigDescriptor](https://api.fluig.com/old/json_JspConfigDescriptor.html) |  |  |
| majorVersion | number | required |  |
| classLoader | [ClassLoader](https://api.fluig.com/old/json_ClassLoader.html) |  |  |
| filterRegistrations | map of object |  |  |
| servletContextName | string |  |  |
| virtualServerName | string |  |  |
| initParameterNames | [EnumerationOfString](https://api.fluig.com/old/json_EnumerationOfString.html) |  |  |
| serverInfo | string |  |  |
| effectiveMinorVersion | number | required |  |
| sessionTimeout | number | required |  |
| ~~servlets~~ | ~~[EnumerationOfServlet](https://api.fluig.com/old/json_EnumerationOfServlet.html)~~ |  |  |
| responseCharacterEncoding | string |  |  |
| effectiveMajorVersion | number | required |  |
| sessionCookieConfig | [SessionCookieConfig](https://api.fluig.com/old/json_SessionCookieConfig.html) |  |  |
| contextPath | string |  |  |
| servletRegistrations | map of object |  |  |
| requestCharacterEncoding | string |  |  |
| ~~servletNames~~ | ~~[EnumerationOfString](https://api.fluig.com/old/json_EnumerationOfString.html)~~ |  |  |

Example

```
{
  "attributeNames" : { },
  "defaultSessionTrackingModes" : [ "COOKIE", "SSL" ],
  "minorVersion" : 12345,
  "effectiveSessionTrackingModes" : [ "URL", "URL" ],
  "jspConfigDescriptor" : {
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
  },
  "majorVersion" : 12345,
  "classLoader" : {
    "registeredAsParallelCapable" : true,
    "platformClassLoader" : { },
    "definedPackages" : [ {
      "implementationTitle" : "...",
      "sealed" : true,
      "declaredAnnotations" : [ { }, { } ],
      "packages" : [ { }, { } ],
      "implementationVersion" : "...",
      "implementationVendor" : "...",
      "specificationVersion" : "...",
      "specificationTitle" : "...",
      "annotations" : [ { }, { } ],
      "specificationVendor" : "...",
      "name" : "..."
    }, {
      "implementationTitle" : "...",
      "sealed" : true,
      "declaredAnnotations" : [ { }, { } ],
      "packages" : [ { }, { } ],
      "implementationVersion" : "...",
      "implementationVendor" : "...",
      "specificationVersion" : "...",
      "specificationTitle" : "...",
      "annotations" : [ { }, { } ],
      "specificationVendor" : "...",
      "name" : "..."
    } ],
    "name" : "...",
    "unnamedModule" : {
      "named" : true,
      "classLoader" : { },
      "packages" : [ "...", "..." ],
      "descriptor" : { },
      "name" : "...",
      "layer" : { },
      "annotations" : [ { }, { } ],
      "declaredAnnotations" : [ { }, { } ]
    },
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
}
```
