---
content_hash: 924f5e2d7a16b5e3fd90296616819501daa85f0436a097949f38f4902d80ee7d
fetched_at: '2026-11-03T14:35:05.927985+00:00'
page_id: com/fluig/sdk/api/workflow/RequestSLAVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.RequestSLAVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/RequestSLAVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class RequestSLAVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.RequestSLAVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class RequestSLAVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.RequestSLAVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `RequestSLAVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object o)` |  |
    | `List<RequestTaskSLAVO>` | `getActualTasks()` |  |
    | `Map<String,​String>` | `getCardFields()` |  |
    | `Date` | `getDeadlineDate()` |  |
    | `Date` | `getEndDate()` |  |
    | `List<String>` | `getExpandables()` |  |
    | `Long` | `getFullTime()` |  |
    | `Long` | `getPercentageConcluded()` |  |
    | `String` | `getProcessDescription()` |  |
    | `String` | `getProcessId()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `int` | `getProcessVersion()` |  |
    | `Long` | `getRemainingTime()` |  |
    | `String` | `getRequesterCode()` |  |
    | `LocalVO` | `getRequesterLocal()` |  |
    | `String` | `getRequesterName()` |  |
    | `Long` | `getSpentTime()` |  |
    | `Date` | `getStartDate()` |  |
    | `String` | `getStatusRequest()` |  |
    | `String` | `getStatusSla()` |  |
    | `Date` | `getWarningDate()` |  |
    | `int` | `hashCode()` |  |
    | `void` | `setActualTasks​(List<RequestTaskSLAVO> actualTasks)` |  |
    | `void` | `setCardFields​(Map<String,​String> cardFields)` |  |
    | `void` | `setDeadlineDate​(Date deadlineDate)` |  |
    | `void` | `setEndDate​(Date endDate)` |  |
    | `void` | `setExpandables​(List<String> expandables)` |  |
    | `void` | `setFullTime​(Long fullTime)` |  |
    | `void` | `setPercentageConcluded​(Long percentageConcluded)` |  |
    | `void` | `setProcessDescription​(String processDescription)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setProcessVersion​(int processVersion)` |  |
    | `void` | `setRemainingTime​(Long remainingTime)` |  |
    | `void` | `setRequesterCode​(String requesterCode)` |  |
    | `void` | `setRequesterLocal​(LocalVO requesterLocal)` |  |
    | `void` | `setRequesterName​(String requesterName)` |  |
    | `void` | `setSpentTime​(Long spentTime)` |  |
    | `void` | `setStartDate​(Date startDate)` |  |
    | `void` | `setStatusRequest​(String statusRequest)` |  |
    | `void` | `setStatusSla​(String statusSla)` |  |
    | `void` | `setWarningDate​(Date warningDate)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### RequestSLAVO

      ```
      public RequestSLAVO()
      ```

  + ### Method Detail

    - #### getPercentageConcluded

      ```
      public Long getPercentageConcluded()
      ```
    - #### setPercentageConcluded

      ```
      public void setPercentageConcluded​(Long percentageConcluded)
      ```
    - #### getDeadlineDate

      ```
      public Date getDeadlineDate()
      ```
    - #### setDeadlineDate

      ```
      public void setDeadlineDate​(Date deadlineDate)
      ```
    - #### getProcessInstanceId

      ```
      public int getProcessInstanceId()
      ```
    - #### setProcessInstanceId

      ```
      public void setProcessInstanceId​(int processInstanceId)
      ```
    - #### getRequesterCode

      ```
      public String getRequesterCode()
      ```
    - #### setRequesterCode

      ```
      public void setRequesterCode​(String requesterCode)
      ```
    - #### getRequesterName

      ```
      public String getRequesterName()
      ```
    - #### setRequesterName

      ```
      public void setRequesterName​(String requesterName)
      ```
    - #### getRemainingTime

      ```
      public Long getRemainingTime()
      ```
    - #### setRemainingTime

      ```
      public void setRemainingTime​(Long remainingTime)
      ```
    - #### getStatusSla

      ```
      public String getStatusSla()
      ```
    - #### setStatusSla

      ```
      public void setStatusSla​(String statusSla)
      ```
    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```
    - #### getProcessId

      ```
      public String getProcessId()
      ```
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```
    - #### getStartDate

      ```
      public Date getStartDate()
      ```
    - #### setStartDate

      ```
      public void setStartDate​(Date startDate)
      ```
    - #### getFullTime

      ```
      public Long getFullTime()
      ```
    - #### setFullTime

      ```
      public void setFullTime​(Long fullTime)
      ```
    - #### getRequesterLocal

      ```
      public LocalVO getRequesterLocal()
      ```
    - #### setRequesterLocal

      ```
      public void setRequesterLocal​(LocalVO requesterLocal)
      ```
    - #### getActualTasks

      ```
      public List<RequestTaskSLAVO> getActualTasks()
      ```
    - #### setActualTasks

      ```
      public void setActualTasks​(List<RequestTaskSLAVO> actualTasks)
      ```
    - #### getEndDate

      ```
      public Date getEndDate()
      ```
    - #### setEndDate

      ```
      public void setEndDate​(Date endDate)
      ```
    - #### getProcessVersion

      ```
      public int getProcessVersion()
      ```
    - #### setProcessVersion

      ```
      public void setProcessVersion​(int processVersion)
      ```
    - #### getStatusRequest

      ```
      public String getStatusRequest()
      ```
    - #### setStatusRequest

      ```
      public void setStatusRequest​(String statusRequest)
      ```
    - #### setWarningDate

      ```
      public void setWarningDate​(Date warningDate)
      ```
    - #### getWarningDate

      ```
      public Date getWarningDate()
      ```
    - #### equals

      ```
      public boolean equals​(Object o)
      ```

      Overrides:
      :   `equals` in class `Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `Object`
    - #### getExpandables

      ```
      public List<String> getExpandables()
      ```
    - #### setExpandables

      ```
      public void setExpandables​(List<String> expandables)
      ```
    - #### getCardFields

      ```
      public Map<String,​String> getCardFields()
      ```
    - #### setCardFields

      ```
      public void setCardFields​(Map<String,​String> cardFields)
      ```
    - #### getSpentTime

      ```
      public Long getSpentTime()
      ```
    - #### setSpentTime

      ```
      public void setSpentTime​(Long spentTime)
      ```
