---
content_hash: 7d377dc7bbd643d425b781455c4e1838a6bf44d37c3395a2801cfe3ba26e9f8d
fetched_at: '2026-11-03T14:35:05.343470+00:00'
page_id: com/fluig/sdk/api/workflow/BPMProcessTaskVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.BPMProcessTaskVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/BPMProcessTaskVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class BPMProcessTaskVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.BPMProcessTaskVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class BPMProcessTaskVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.BPMProcessTaskVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `BPMProcessTaskVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `BPMUserVO` | `getAssignee()` |  |
    | `ZonedDateTime` | `getAssignEndDate()` |  |
    | `ZonedDateTime` | `getAssignStartDate()` |  |
    | `ZonedDateTime` | `getDeadlineDate()` |  |
    | `ZonedDateTime` | `getEndDate()` |  |
    | `int` | `getMovementSequence()` |  |
    | `String` | `getProcessDescription()` |  |
    | `String` | `getProcessId()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `int` | `getProcessVersion()` |  |
    | `ZonedDateTime` | `getStartDate()` |  |
    | `String` | `getStatus()` |  |
    | `int` | `getThreadSequence()` |  |
    | `int` | `getTransferSequence()` |  |
    | `ZonedDateTime` | `getWarningDate()` |  |
    | `void` | `setAssignee​(BPMUserVO assignee)` |  |
    | `void` | `setAssignEndDate​(ZonedDateTime assignEndDate)` |  |
    | `void` | `setAssignStartDate​(ZonedDateTime assignStartDate)` |  |
    | `void` | `setDeadlineDate​(ZonedDateTime deadlineDate)` |  |
    | `void` | `setEndDate​(ZonedDateTime endDate)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setProcessDescription​(String processDescription)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setProcessVersion​(int processVersion)` |  |
    | `void` | `setStartDate​(ZonedDateTime startDate)` |  |
    | `void` | `setStatus​(String status)` |  |
    | `void` | `setThreadSequence​(int threadSequence)` |  |
    | `void` | `setTransferSequence​(int transferSequence)` |  |
    | `void` | `setWarningDate​(ZonedDateTime warningDate)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### BPMProcessTaskVO

      ```
      public BPMProcessTaskVO()
      ```

  + ### Method Detail

    - #### getProcessInstanceId

      ```
      public int getProcessInstanceId()
      ```
    - #### setProcessInstanceId

      ```
      public void setProcessInstanceId​(int processInstanceId)
      ```
    - #### getMovementSequence

      ```
      public int getMovementSequence()
      ```
    - #### setMovementSequence

      ```
      public void setMovementSequence​(int movementSequence)
      ```
    - #### getTransferSequence

      ```
      public int getTransferSequence()
      ```
    - #### setTransferSequence

      ```
      public void setTransferSequence​(int transferSequence)
      ```
    - #### getAssignee

      ```
      public BPMUserVO getAssignee()
      ```
    - #### setAssignee

      ```
      public void setAssignee​(BPMUserVO assignee)
      ```
    - #### getDeadlineDate

      ```
      public ZonedDateTime getDeadlineDate()
      ```
    - #### setDeadlineDate

      ```
      public void setDeadlineDate​(ZonedDateTime deadlineDate)
      ```
    - #### getStatus

      ```
      public String getStatus()
      ```
    - #### setStatus

      ```
      public void setStatus​(String status)
      ```
    - #### getStartDate

      ```
      public ZonedDateTime getStartDate()
      ```
    - #### setStartDate

      ```
      public void setStartDate​(ZonedDateTime startDate)
      ```
    - #### getEndDate

      ```
      public ZonedDateTime getEndDate()
      ```
    - #### setEndDate

      ```
      public void setEndDate​(ZonedDateTime endDate)
      ```
    - #### getAssignStartDate

      ```
      public ZonedDateTime getAssignStartDate()
      ```
    - #### setAssignStartDate

      ```
      public void setAssignStartDate​(ZonedDateTime assignStartDate)
      ```
    - #### getAssignEndDate

      ```
      public ZonedDateTime getAssignEndDate()
      ```
    - #### setAssignEndDate

      ```
      public void setAssignEndDate​(ZonedDateTime assignEndDate)
      ```
    - #### getWarningDate

      ```
      public ZonedDateTime getWarningDate()
      ```
    - #### setWarningDate

      ```
      public void setWarningDate​(ZonedDateTime warningDate)
      ```
    - #### getProcessId

      ```
      public String getProcessId()
      ```
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```
    - #### getProcessVersion

      ```
      public int getProcessVersion()
      ```
    - #### setProcessVersion

      ```
      public void setProcessVersion​(int processVersion)
      ```
    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```
    - #### getThreadSequence

      ```
      public int getThreadSequence()
      ```
    - #### setThreadSequence

      ```
      public void setThreadSequence​(int threadSequence)
      ```
