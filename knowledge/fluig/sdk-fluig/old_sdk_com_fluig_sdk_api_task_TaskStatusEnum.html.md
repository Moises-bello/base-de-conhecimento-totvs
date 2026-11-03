---
content_hash: 80faa8f722d38046a9cde3290f4c8fc7627531efec9409feecc0e570bdb46d94
fetched_at: '2026-11-03T14:35:05.043922+00:00'
page_id: com/fluig/sdk/api/task/TaskStatusEnum
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.TaskStatusEnum (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskStatusEnum.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Enum TaskStatusEnum

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[TaskStatusEnum](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskStatusEnum.html "enum in com.fluig.sdk.api.task")>
  + - com.fluig.sdk.api.task.TaskStatusEnum

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<TaskStatusEnum>`

  ---

  ```
  public enum TaskStatusEnum
  extends Enum<TaskStatusEnum>
  ```

  Author:
  :   vinicius.michelutti

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `CANCELLED` |  |
    | `COMPLETED` |  |
    | `CONSENSUS` |  |
    | `NEW` |  |
    | `PAUSED` |  |
    | `STARTED` |  |
    | `TRANSFERRED` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `static TaskStatusEnum` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static TaskStatusEnum[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### NEW

      ```
      public static final TaskStatusEnum NEW
      ```
    - #### CONSENSUS

      ```
      public static final TaskStatusEnum CONSENSUS
      ```
    - #### COMPLETED

      ```
      public static final TaskStatusEnum COMPLETED
      ```
    - #### TRANSFERRED

      ```
      public static final TaskStatusEnum TRANSFERRED
      ```
    - #### CANCELLED

      ```
      public static final TaskStatusEnum CANCELLED
      ```
    - #### STARTED

      ```
      public static final TaskStatusEnum STARTED
      ```
    - #### PAUSED

      ```
      public static final TaskStatusEnum PAUSED
      ```

  + ### Method Detail

    - #### values

      ```
      public static TaskStatusEnum[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (TaskStatusEnum c : TaskStatusEnum.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static TaskStatusEnum valueOf​(String name)
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
