---
content_hash: aa9f8a3fc80ff00435a7a7ab1e907ecde8dc3169ff0b17b081ed35aa3aff1dac
fetched_at: '2026-11-03T14:35:05.278188+00:00'
page_id: com/fluig/sdk/api/workflow/BPMProcessActivityVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.BPMProcessActivityVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/BPMProcessActivityVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class BPMProcessActivityVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.BPMProcessActivityVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class BPMProcessActivityVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.BPMProcessActivityVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `BPMProcessActivityVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `ZonedDateTime` | `getDeadlineDate()` |  |
    | `BPMDeadlineSpecificationVO` | `getDeadlineSpecification()` |  |
    | `ZonedDateTime` | `getEndDate()` |  |
    | `List<BPMFormFieldVO>` | `getFormFields()` |  |
    | `int` | `getMovementSequence()` |  |
    | `String` | `getProcessDescription()` |  |
    | `String` | `getProcessId()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `int` | `getProcessVersion()` |  |
    | `BPMUserVO` | `getRequester()` |  |
    | `String` | `getSlaStatus()` |  |
    | `ZonedDateTime` | `getStartDate()` |  |
    | `BPMProcessStateVO` | `getState()` |  |
    | `BPMProcessActivityTaskInfoVO` | `getTaskInfo()` |  |
    | `List<BPMProcessTaskVO>` | `getTasks()` |  |
    | `int` | `getThreadSequence()` |  |
    | `boolean` | `isActive()` |  |
    | `void` | `setActive​(boolean active)` |  |
    | `void` | `setDeadlineDate​(ZonedDateTime deadlineDate)` |  |
    | `void` | `setDeadlineSpecification​(BPMDeadlineSpecificationVO deadlineSpecification)` |  |
    | `void` | `setEndDate​(ZonedDateTime endDate)` |  |
    | `void` | `setFormFields​(List<BPMFormFieldVO> formFields)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setProcessDescription​(String processDescription)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setProcessVersion​(int processVersion)` |  |
    | `void` | `setRequester​(BPMUserVO requester)` |  |
    | `void` | `setSlaStatus​(String slaStatus)` |  |
    | `void` | `setStartDate​(ZonedDateTime startDate)` |  |
    | `void` | `setState​(BPMProcessStateVO state)` |  |
    | `void` | `setTaskInfo​(BPMProcessActivityTaskInfoVO taskInfo)` |  |
    | `void` | `setTasks​(List<BPMProcessTaskVO> tasks)` |  |
    | `void` | `setThreadSequence​(int threadSequence)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### BPMProcessActivityVO

      ```
      public BPMProcessActivityVO()
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
    - #### isActive

      ```
      public boolean isActive()
      ```
    - #### setActive

      ```
      public void setActive​(boolean active)
      ```
    - #### getSlaStatus

      ```
      public String getSlaStatus()
      ```
    - #### setSlaStatus

      ```
      public void setSlaStatus​(String slaStatus)
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
    - #### getDeadlineDate

      ```
      public ZonedDateTime getDeadlineDate()
      ```
    - #### setDeadlineDate

      ```
      public void setDeadlineDate​(ZonedDateTime deadlineDate)
      ```
    - #### getProcessId

      ```
      public String getProcessId()
      ```
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```
    - #### getRequester

      ```
      public BPMUserVO getRequester()
      ```
    - #### setRequester

      ```
      public void setRequester​(BPMUserVO requester)
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
    - #### getState

      ```
      public BPMProcessStateVO getState()
      ```
    - #### setState

      ```
      public void setState​(BPMProcessStateVO state)
      ```
    - #### getTasks

      ```
      public List<BPMProcessTaskVO> getTasks()
      ```
    - #### setTasks

      ```
      public void setTasks​(List<BPMProcessTaskVO> tasks)
      ```
    - #### getThreadSequence

      ```
      public int getThreadSequence()
      ```
    - #### setThreadSequence

      ```
      public void setThreadSequence​(int threadSequence)
      ```
    - #### getFormFields

      ```
      public List<BPMFormFieldVO> getFormFields()
      ```
    - #### setFormFields

      ```
      public void setFormFields​(List<BPMFormFieldVO> formFields)
      ```
    - #### getDeadlineSpecification

      ```
      public BPMDeadlineSpecificationVO getDeadlineSpecification()
      ```
    - #### setDeadlineSpecification

      ```
      public void setDeadlineSpecification​(BPMDeadlineSpecificationVO deadlineSpecification)
      ```
    - #### getTaskInfo

      ```
      public BPMProcessActivityTaskInfoVO getTaskInfo()
      ```
    - #### setTaskInfo

      ```
      public void setTaskInfo​(BPMProcessActivityTaskInfoVO taskInfo)
      ```
