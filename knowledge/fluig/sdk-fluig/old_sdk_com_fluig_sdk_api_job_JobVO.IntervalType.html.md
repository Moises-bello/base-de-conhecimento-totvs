---
content_hash: 346b54f08a07a92a1e882da840e39639567f228c1e236fce41141218b4e9350b
fetched_at: '2026-11-03T14:35:04.453922+00:00'
page_id: com/fluig/sdk/api/job/JobVO.IntervalType
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.job.JobVO.IntervalType (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/JobVO.IntervalType.html
version: 1
---

Package [com.fluig.sdk.api.job](https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/package-summary.html)

## Enum JobVO.IntervalType

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[JobVO.IntervalType](https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/JobVO.IntervalType.html "enum in com.fluig.sdk.api.job")>
  + - com.fluig.sdk.api.job.JobVO.IntervalType

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<JobVO.IntervalType>`

  Enclosing class:
  :   [JobVO](https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/JobVO.html "class in com.fluig.sdk.api.job")

  ---

  ```
  public static enum JobVO.IntervalType
  extends Enum<JobVO.IntervalType>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `DAILY` |  |
    | `MONTHLY` |  |
    | `WEEKLY` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `static JobVO.IntervalType` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static JobVO.IntervalType[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### DAILY

      ```
      public static final JobVO.IntervalType DAILY
      ```
    - #### WEEKLY

      ```
      public static final JobVO.IntervalType WEEKLY
      ```
    - #### MONTHLY

      ```
      public static final JobVO.IntervalType MONTHLY
      ```

  + ### Method Detail

    - #### values

      ```
      public static JobVO.IntervalType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (JobVO.IntervalType c : JobVO.IntervalType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static JobVO.IntervalType valueOf​(String name)
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
