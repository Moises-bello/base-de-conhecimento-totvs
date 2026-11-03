---
content_hash: d441898c78c1f71cae9b3755a238c2a4a3e4916a0781ddd733c00875f0fa9166
fetched_at: '2026-11-03T14:35:04.346952+00:00'
page_id: com/fluig/sdk/api/enums/AssumeProcessTaskStatus
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.enums.AssumeProcessTaskStatus (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/enums/AssumeProcessTaskStatus.html
version: 1
---

Package [com.fluig.sdk.api.enums](https://api.fluig.com/old/sdk/com/fluig/sdk/api/enums/package-summary.html)

## Enum AssumeProcessTaskStatus

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[AssumeProcessTaskStatus](https://api.fluig.com/old/sdk/com/fluig/sdk/api/enums/AssumeProcessTaskStatus.html "enum in com.fluig.sdk.api.enums")>
  + - com.fluig.sdk.api.enums.AssumeProcessTaskStatus

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<AssumeProcessTaskStatus>`

  ---

  ```
  public enum AssumeProcessTaskStatus
  extends Enum<AssumeProcessTaskStatus>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `ERROR` |  |
    | `SUCCESS` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `static AssumeProcessTaskStatus` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static AssumeProcessTaskStatus[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### SUCCESS

      ```
      public static final AssumeProcessTaskStatus SUCCESS
      ```
    - #### ERROR

      ```
      public static final AssumeProcessTaskStatus ERROR
      ```

  + ### Method Detail

    - #### values

      ```
      public static AssumeProcessTaskStatus[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (AssumeProcessTaskStatus c : AssumeProcessTaskStatus.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static AssumeProcessTaskStatus valueOf​(String name)
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
