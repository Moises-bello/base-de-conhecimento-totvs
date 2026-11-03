---
content_hash: 69d683e37da607e3fcc2ce74e302dd313dc981d41a428fd6e9abbce43e7fd567
fetched_at: '2026-11-03T14:35:05.827544+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessTaskInfoVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessTaskInfoVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessTaskInfoVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessTaskInfoVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessTaskInfoVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessTaskInfoVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessTaskInfoVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessTaskInfoVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getColleagueName()` |  |
    | `int` | `getMovementSequence()` |  |
    | `Date` | `getStartDateTask()` |  |
    | `ProcessStateVO` | `getState()` |  |
    | `int` | `getStateSequence()` |  |
    | `int` | `getStatus()` |  |
    | `Date` | `getTaskDeadline()` |  |
    | `int` | `getTransferredSequence()` |  |
    | `boolean` | `isActive()` |  |
    | `boolean` | `isExpired()` |  |
    | `void` | `setActive​(boolean active)` |  |
    | `void` | `setColleagueName​(String colleagueName)` |  |
    | `void` | `setExpired​(boolean expired)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setStartDateTask​(Date startDateTask)` |  |
    | `void` | `setState​(ProcessStateVO state)` |  |
    | `void` | `setStateSequence​(int stateSequence)` |  |
    | `void` | `setStatus​(int status)` |  |
    | `void` | `setTaskDeadline​(Date taskDeadline)` |  |
    | `void` | `setTransferredSequence​(int transferredSequence)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessTaskInfoVO

      ```
      public ProcessTaskInfoVO()
      ```

  + ### Method Detail

    - #### getMovementSequence

      ```
      public int getMovementSequence()
      ```
    - #### setMovementSequence

      ```
      public void setMovementSequence​(int movementSequence)
      ```
    - #### getTransferredSequence

      ```
      public int getTransferredSequence()
      ```
    - #### setTransferredSequence

      ```
      public void setTransferredSequence​(int transferredSequence)
      ```
    - #### getStateSequence

      ```
      public int getStateSequence()
      ```
    - #### setStateSequence

      ```
      public void setStateSequence​(int stateSequence)
      ```
    - #### getColleagueName

      ```
      public String getColleagueName()
      ```
    - #### setColleagueName

      ```
      public void setColleagueName​(String colleagueName)
      ```
    - #### getState

      ```
      public ProcessStateVO getState()
      ```
    - #### setState

      ```
      public void setState​(ProcessStateVO state)
      ```
    - #### getTaskDeadline

      ```
      public Date getTaskDeadline()
      ```
    - #### setTaskDeadline

      ```
      public void setTaskDeadline​(Date taskDeadline)
      ```
    - #### isExpired

      ```
      public boolean isExpired()
      ```
    - #### setExpired

      ```
      public void setExpired​(boolean expired)
      ```
    - #### getStartDateTask

      ```
      public Date getStartDateTask()
      ```
    - #### setStartDateTask

      ```
      public void setStartDateTask​(Date startDateTask)
      ```
    - #### getStatus

      ```
      public int getStatus()
      ```
    - #### setStatus

      ```
      public void setStatus​(int status)
      ```
    - #### isActive

      ```
      public boolean isActive()
      ```
    - #### setActive

      ```
      public void setActive​(boolean active)
      ```
