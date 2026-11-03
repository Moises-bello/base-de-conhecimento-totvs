---
content_hash: 92492a9dd34ca1ed619239b9b8d4b15ead93a3047e0c1beec9030691dbe14044
fetched_at: '2026-11-03T14:35:07.477593+00:00'
page_id: com/fluig/sdk/web/FluigRestConvertDateZone
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.web.FluigRestConvertDateZone (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/web/FluigRestConvertDateZone.html
version: 1
---

Package [com.fluig.sdk.web](https://api.fluig.com/old/sdk/com/fluig/sdk/web/package-summary.html)

## Class FluigRestConvertDateZone

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.web.FluigRestConvertDateZone

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class FluigRestConvertDateZone
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.web.FluigRestConvertDateZone)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FluigRestConvertDateZone()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `protected Object` | `convertDateTimeToTimeZone​(Object obj, boolean isDate)` |  |
    | `protected Object` | `getDateTimeZone​(Object obj, com.fasterxml.jackson.databind.ser.PropertyWriter writer)` |  |
    | `protected com.fasterxml.jackson.databind.ser.impl.SimpleFilterProvider` | `getFilterTimeZone​(com.fasterxml.jackson.databind.ObjectMapper mapper)` |  |
    | `protected boolean` | `isRegexDateTime​(Object obj)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### FluigRestConvertDateZone

      ```
      public FluigRestConvertDateZone()
      ```

  + ### Method Detail

    - #### getFilterTimeZone

      ```
      protected com.fasterxml.jackson.databind.ser.impl.SimpleFilterProvider getFilterTimeZone​(com.fasterxml.jackson.databind.ObjectMapper mapper)
      ```
    - #### isRegexDateTime

      ```
      protected boolean isRegexDateTime​(Object obj)
      ```
    - #### getDateTimeZone

      ```
      protected Object getDateTimeZone​(Object obj,
                                       com.fasterxml.jackson.databind.ser.PropertyWriter writer)
                                throws ParseException,
                                       SecurityException,
                                       IllegalArgumentException,
                                       IllegalAccessException
      ```

      Throws:
      :   `ParseException`
      :   `SecurityException`
      :   `IllegalArgumentException`
      :   `IllegalAccessException`
    - #### convertDateTimeToTimeZone

      ```
      protected Object convertDateTimeToTimeZone​(Object obj,
                                                 boolean isDate)
                                          throws ParseException
      ```

      Throws:
      :   `ParseException`
