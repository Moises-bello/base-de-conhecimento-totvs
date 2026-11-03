---
content_hash: 12bcb7f780a6b4c7de456022c20209fdb235f32bbd0ff8e343cc4df560b08ab5
fetched_at: '2026-11-03T14:35:04.992845+00:00'
page_id: com/fluig/sdk/api/task/ResumedTasksVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.ResumedTasksVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/ResumedTasksVO.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Class ResumedTasksVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.task.ResumedTasksVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ResumedTasksVO
  extends Object
  implements Serializable
  ```

  Simple VO for all menu items in central tasks

  Since:
  :   1.5.4

  Author:
  :   vinicius.michelutti

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.task.ResumedTasksVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ResumedTasksVO​(String type, String state, int totalTask)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<ResumedTasksVO>` | `getChildren()` |  |
    | `String` | `getCustomURL()` |  |
    | `String` | `getName()` |  |
    | `String` | `getState()` |  |
    | `String` | `getTaskId()` |  |
    | `int` | `getTotalTask()` |  |
    | `String` | `getType()` |  |
    | `void` | `setChildren​(List<ResumedTasksVO> children)` |  |
    | `void` | `setCustomURL​(String customURL)` |  |
    | `void` | `setName​(String name)` |  |
    | `void` | `setState​(String state)` |  |
    | `void` | `setTaskId​(String taskId)` |  |
    | `void` | `setTotalTask​(int totalTask)` |  |
    | `void` | `setType​(String type)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ResumedTasksVO

      ```
      public ResumedTasksVO​(String type,
                            String state,
                            int totalTask)
      ```

  + ### Method Detail

    - #### getType

      ```
      public String getType()
      ```
    - #### setType

      ```
      public void setType​(String type)
      ```
    - #### getName

      ```
      public String getName()
      ```
    - #### setName

      ```
      public void setName​(String name)
      ```
    - #### getTaskId

      ```
      public String getTaskId()
      ```
    - #### setTaskId

      ```
      public void setTaskId​(String taskId)
      ```
    - #### getState

      ```
      public String getState()
      ```
    - #### setState

      ```
      public void setState​(String state)
      ```
    - #### getCustomURL

      ```
      public String getCustomURL()
      ```
    - #### setCustomURL

      ```
      public void setCustomURL​(String customURL)
      ```
    - #### getTotalTask

      ```
      public int getTotalTask()
      ```
    - #### setTotalTask

      ```
      public void setTotalTask​(int totalTask)
      ```
    - #### getChildren

      ```
      public List<ResumedTasksVO> getChildren()
      ```
    - #### setChildren

      ```
      public void setChildren​(List<ResumedTasksVO> children)
      ```
