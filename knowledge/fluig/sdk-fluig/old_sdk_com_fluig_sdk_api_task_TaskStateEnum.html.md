---
content_hash: 78e5e533ab676555e111df7e4e11fd85451166d2ef7a8e67e41e29da7bebc661
fetched_at: '2026-11-03T14:35:05.029851+00:00'
page_id: com/fluig/sdk/api/task/TaskStateEnum
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.TaskStateEnum (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskStateEnum.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Enum TaskStateEnum

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[TaskStateEnum](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskStateEnum.html "enum in com.fluig.sdk.api.task")>
  + - com.fluig.sdk.api.task.TaskStateEnum

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<TaskStateEnum>`

  ---

  ```
  public enum TaskStateEnum
  extends Enum<TaskStateEnum>
  ```

  Author:
  :   vinicius.michelutti

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `DOCUMENT` |  |
    | `LEARN` |  |
    | `PROCESS` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `toString()` |  |
    | `static TaskStateEnum` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static TaskStateEnum[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### PROCESS

      ```
      public static final TaskStateEnum PROCESS
      ```
    - #### DOCUMENT

      ```
      public static final TaskStateEnum DOCUMENT
      ```
    - #### LEARN

      ```
      public static final TaskStateEnum LEARN
      ```

  + ### Method Detail

    - #### values

      ```
      public static TaskStateEnum[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (TaskStateEnum c : TaskStateEnum.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static TaskStateEnum valueOf​(String name)
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
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Enum<TaskStateEnum>`
