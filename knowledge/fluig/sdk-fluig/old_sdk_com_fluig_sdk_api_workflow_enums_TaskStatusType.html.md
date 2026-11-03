---
content_hash: 0ec2ba26500f4b4440ce3ceac86715675df5ef48c869884c786d40dd513a6e7c
fetched_at: '2026-11-03T14:35:06.057377+00:00'
page_id: com/fluig/sdk/api/workflow/enums/TaskStatusType
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.enums.TaskStatusType (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/TaskStatusType.html
version: 1
---

Package [com.fluig.sdk.api.workflow.enums](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/package-summary.html)

## Enum TaskStatusType

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[TaskStatusType](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/enums/TaskStatusType.html "enum in com.fluig.sdk.api.workflow.enums")>
  + - com.fluig.sdk.api.workflow.enums.TaskStatusType

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<TaskStatusType>`

  ---

  ```
  public enum TaskStatusType
  extends Enum<TaskStatusType>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `CANCELED_EXPIRED_TASKS` |  |
    | `CANCELED_ON_TIME_TASKS` |  |
    | `CANCELED_WARNING_TASKS` |  |
    | `FINISHED_EXPIRED_TASKS` |  |
    | `FINISHED_ON_TIME_TASKS` |  |
    | `FINISHED_WARNING_TASKS` |  |
    | `OPEN_EXPIRED_TASKS` |  |
    | `OPEN_ON_TIME_TASKS` |  |
    | `OPEN_WARNING_TASKS` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getValue()` |  |
    | `static TaskStatusType` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static TaskStatusType[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### OPEN\_EXPIRED\_TASKS

      ```
      public static final TaskStatusType OPEN_EXPIRED_TASKS
      ```
    - #### OPEN\_ON\_TIME\_TASKS

      ```
      public static final TaskStatusType OPEN_ON_TIME_TASKS
      ```
    - #### OPEN\_WARNING\_TASKS

      ```
      public static final TaskStatusType OPEN_WARNING_TASKS
      ```
    - #### CANCELED\_EXPIRED\_TASKS

      ```
      public static final TaskStatusType CANCELED_EXPIRED_TASKS
      ```
    - #### CANCELED\_ON\_TIME\_TASKS

      ```
      public static final TaskStatusType CANCELED_ON_TIME_TASKS
      ```
    - #### CANCELED\_WARNING\_TASKS

      ```
      public static final TaskStatusType CANCELED_WARNING_TASKS
      ```
    - #### FINISHED\_EXPIRED\_TASKS

      ```
      public static final TaskStatusType FINISHED_EXPIRED_TASKS
      ```
    - #### FINISHED\_ON\_TIME\_TASKS

      ```
      public static final TaskStatusType FINISHED_ON_TIME_TASKS
      ```
    - #### FINISHED\_WARNING\_TASKS

      ```
      public static final TaskStatusType FINISHED_WARNING_TASKS
      ```

  + ### Method Detail

    - #### values

      ```
      public static TaskStatusType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (TaskStatusType c : TaskStatusType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static TaskStatusType valueOf​(String name)
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
