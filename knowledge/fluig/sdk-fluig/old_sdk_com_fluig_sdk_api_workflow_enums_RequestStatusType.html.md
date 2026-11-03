---
content_hash: b3e7be13831499f4d367557437bf9e47dce751aa11238c99c44bde91f7efab09
fetched_at: '2026-11-03T14:35:06.042773+00:00'
page_id: com/fluig/sdk/api/workflow/enums/RequestStatusType
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.enums.RequestStatusType (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/RequestStatusType.html
version: 1
---

Package [com.fluig.sdk.api.workflow.enums](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/package-summary.html)

## Enum RequestStatusType

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[RequestStatusType](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/RequestStatusType.html "enum in com.fluig.sdk.api.workflow.enums")>
  + - com.fluig.sdk.api.workflow.enums.RequestStatusType

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<RequestStatusType>`

  ---

  ```
  public enum RequestStatusType
  extends Enum<RequestStatusType>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `CANCELED_EXPIRED_REQUESTS` |  |
    | `CANCELED_ON_TIME_REQUESTS` |  |
    | `CANCELED_REQUESTS` |  |
    | `CANCELED_WARNING_REQUESTS` |  |
    | `FINISHED_EXPIRED_REQUESTS` |  |
    | `FINISHED_ON_TIME_REQUESTS` |  |
    | `FINISHED_REQUESTS` |  |
    | `FINISHED_WARNING_REQUESTS` |  |
    | `OPEN_EXPIRED_REQUESTS` |  |
    | `OPEN_ON_TIME_REQUESTS` |  |
    | `OPEN_REQUESTS` |  |
    | `OPEN_WARNING_REQUESTS` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getValue()` |  |
    | `static RequestStatusType` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static RequestStatusType[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### FINISHED\_REQUESTS

      ```
      public static final RequestStatusType FINISHED_REQUESTS
      ```
    - #### FINISHED\_EXPIRED\_REQUESTS

      ```
      public static final RequestStatusType FINISHED_EXPIRED_REQUESTS
      ```
    - #### FINISHED\_ON\_TIME\_REQUESTS

      ```
      public static final RequestStatusType FINISHED_ON_TIME_REQUESTS
      ```
    - #### FINISHED\_WARNING\_REQUESTS

      ```
      public static final RequestStatusType FINISHED_WARNING_REQUESTS
      ```
    - #### CANCELED\_REQUESTS

      ```
      public static final RequestStatusType CANCELED_REQUESTS
      ```
    - #### CANCELED\_EXPIRED\_REQUESTS

      ```
      public static final RequestStatusType CANCELED_EXPIRED_REQUESTS
      ```
    - #### CANCELED\_ON\_TIME\_REQUESTS

      ```
      public static final RequestStatusType CANCELED_ON_TIME_REQUESTS
      ```
    - #### CANCELED\_WARNING\_REQUESTS

      ```
      public static final RequestStatusType CANCELED_WARNING_REQUESTS
      ```
    - #### OPEN\_REQUESTS

      ```
      public static final RequestStatusType OPEN_REQUESTS
      ```
    - #### OPEN\_EXPIRED\_REQUESTS

      ```
      public static final RequestStatusType OPEN_EXPIRED_REQUESTS
      ```
    - #### OPEN\_ON\_TIME\_REQUESTS

      ```
      public static final RequestStatusType OPEN_ON_TIME_REQUESTS
      ```
    - #### OPEN\_WARNING\_REQUESTS

      ```
      public static final RequestStatusType OPEN_WARNING_REQUESTS
      ```

  + ### Method Detail

    - #### values

      ```
      public static RequestStatusType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (RequestStatusType c : RequestStatusType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static RequestStatusType valueOf​(String name)
      ```

      Returns the enum constant of this type with the specified name.
      The string must match *exactly* an identifier used to declare an
      enum constant in this type. (Extraneous whitespace characters are
      not permitted.)

      Parameters:
      :   `name` - the name of the enum constant to be returned.

      Returns:
      :   the enum constant with the specified name

      Throws:
      :   `IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `NullPointerException` - if the argument is null
    - #### getValue

      ```
      public String getValue()
      ```
