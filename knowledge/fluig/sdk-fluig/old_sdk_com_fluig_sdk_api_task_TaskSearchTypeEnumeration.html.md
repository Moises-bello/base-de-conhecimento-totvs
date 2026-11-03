---
content_hash: 7c1633d199f49e612440bc0d619db803ae7d4b0dec377dd6a537dd153807f6ed
fetched_at: '2026-11-03T14:35:05.017857+00:00'
page_id: com/fluig/sdk/api/task/TaskSearchTypeEnumeration
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.TaskSearchTypeEnumeration (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskSearchTypeEnumeration.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Enum TaskSearchTypeEnumeration

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[TaskSearchTypeEnumeration](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskSearchTypeEnumeration.html "enum in com.fluig.sdk.api.task")>
  + - com.fluig.sdk.api.task.TaskSearchTypeEnumeration

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<TaskSearchTypeEnumeration>`

  ---

  ```
  public enum TaskSearchTypeEnumeration
  extends Enum<TaskSearchTypeEnumeration>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `ALL` |  |
    | `MANAGER_OR_SUBSTITUTE` |  |
    | `OPENED` |  |
    | `PARTICIPATED` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `int` | `getType()` |  |
    | `static TaskSearchTypeEnumeration` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static TaskSearchTypeEnumeration[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### OPENED

      ```
      public static final TaskSearchTypeEnumeration OPENED
      ```
    - #### PARTICIPATED

      ```
      public static final TaskSearchTypeEnumeration PARTICIPATED
      ```
    - #### MANAGER\_OR\_SUBSTITUTE

      ```
      public static final TaskSearchTypeEnumeration MANAGER_OR_SUBSTITUTE
      ```
    - #### ALL

      ```
      public static final TaskSearchTypeEnumeration ALL
      ```

  + ### Method Detail

    - #### values

      ```
      public static TaskSearchTypeEnumeration[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (TaskSearchTypeEnumeration c : TaskSearchTypeEnumeration.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static TaskSearchTypeEnumeration valueOf​(String name)
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
    - #### getType

      ```
      public int getType()
      ```
