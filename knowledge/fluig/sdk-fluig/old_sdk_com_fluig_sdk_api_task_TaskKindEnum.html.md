---
content_hash: 4579bb1636574003ec8b1e4e162fd917d1aa5062147908d3e68ccfa9d91d3945
fetched_at: '2026-11-03T14:35:05.005941+00:00'
page_id: com/fluig/sdk/api/task/TaskKindEnum
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.TaskKindEnum (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskKindEnum.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Enum TaskKindEnum

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[TaskKindEnum](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskKindEnum.html "enum in com.fluig.sdk.api.task")>
  + - com.fluig.sdk.api.task.TaskKindEnum

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<TaskKindEnum>`

  ---

  ```
  public enum TaskKindEnum
  extends Enum<TaskKindEnum>
  ```

  Since:
  :   1.5.4

  Author:
  :   vinicius.michelutti

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `DOCUMENT_EDIT` |  |
    | `DOCUMENT_REVISION` |  |
    | `TODO` |  |
    | `WORKFLOW` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `static TaskKindEnum` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static TaskKindEnum[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### TODO

      ```
      public static final TaskKindEnum TODO
      ```
    - #### DOCUMENT\_EDIT

      ```
      public static final TaskKindEnum DOCUMENT_EDIT
      ```
    - #### WORKFLOW

      ```
      public static final TaskKindEnum WORKFLOW
      ```
    - #### DOCUMENT\_REVISION

      ```
      public static final TaskKindEnum DOCUMENT_REVISION
      ```

  + ### Method Detail

    - #### values

      ```
      public static TaskKindEnum[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (TaskKindEnum c : TaskKindEnum.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static TaskKindEnum valueOf​(String name)
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
