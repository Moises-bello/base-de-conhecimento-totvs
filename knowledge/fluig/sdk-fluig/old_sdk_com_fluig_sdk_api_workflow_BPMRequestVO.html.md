---
content_hash: 2d4d86e1acf23ec4d17a5e6e71f914ffb1bea53c1d775be4b38bf769d52dc4b9
fetched_at: '2026-11-03T14:35:05.399825+00:00'
page_id: com/fluig/sdk/api/workflow/BPMRequestVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.BPMRequestVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/BPMRequestVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class BPMRequestVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.BPMRequestVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class BPMRequestVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.BPMRequestVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `BPMRequestVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Boolean` | `getActive()` |  |
    | `List<BPMProcessActivityVO>` | `getActivities()` |  |
    | `ZonedDateTime` | `getDeadlineDate()` |  |
    | `BPMDeadlineSpecificationVO` | `getDeadlineSpecification()` |  |
    | `ZonedDateTime` | `getEndDate()` |  |
    | `List<BPMFormFieldVO>` | `getFormFields()` |  |
    | `Integer` | `getFormId()` |  |
    | `BPMFormRecordVO` | `getFormRecord()` |  |
    | `Integer` | `getFormRecordId()` |  |
    | `Integer` | `getParentRequestId()` |  |
    | `String` | `getPeriodId()` |  |
    | `String` | `getProcessDescription()` |  |
    | `String` | `getProcessId()` |  |
    | `Integer` | `getProcessInstanceId()` |  |
    | `Integer` | `getProcessVersion()` |  |
    | `BPMUserVO` | `getRequester()` |  |
    | `String` | `getSlaStatus()` |  |
    | `ZonedDateTime` | `getStartDate()` |  |
    | `String` | `getStatus()` |  |
    | `ZonedDateTime` | `getWarningDate()` |  |
    | `void` | `setActive​(Boolean active)` |  |
    | `void` | `setActivities​(List<BPMProcessActivityVO> activities)` |  |
    | `void` | `setDeadlineDate​(ZonedDateTime deadlineDate)` |  |
    | `void` | `setDeadlineSpecification​(BPMDeadlineSpecificationVO deadlineSpecification)` |  |
    | `void` | `setEndDate​(ZonedDateTime endDate)` |  |
    | `void` | `setFormFields​(List<BPMFormFieldVO> formFields)` |  |
    | `void` | `setFormId​(Integer formId)` |  |
    | `void` | `setFormRecord​(BPMFormRecordVO formRecord)` |  |
    | `void` | `setFormRecordId​(Integer formRecordId)` |  |
    | `void` | `setParentRequestId​(Integer parentRequestId)` |  |
    | `void` | `setPeriodId​(String periodId)` |  |
    | `void` | `setProcessDescription​(String processDescription)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(Integer processInstanceId)` |  |
    | `void` | `setProcessVersion​(Integer processVersion)` |  |
    | `void` | `setRequester​(BPMUserVO requester)` |  |
    | `void` | `setSlaStatus​(String slaStatus)` |  |
    | `void` | `setStartDate​(ZonedDateTime startDate)` |  |
    | `void` | `setStatus​(String status)` |  |
    | `void` | `setWarningDate​(ZonedDateTime warningDate)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### BPMRequestVO

      ```
      public BPMRequestVO()
      ```

  + ### Method Detail

    - #### getProcessInstanceId

      ```
      public Integer getProcessInstanceId()
      ```
    - #### setProcessInstanceId

      ```
      public void setProcessInstanceId​(Integer processInstanceId)
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
      public Integer getProcessVersion()
      ```
    - #### setProcessVersion

      ```
      public void setProcessVersion​(Integer processVersion)
      ```
    - #### getActive

      ```
      public Boolean getActive()
      ```
    - #### setActive

      ```
      public void setActive​(Boolean active)
      ```
    - #### getRequester

      ```
      public BPMUserVO getRequester()
      ```
    - #### setRequester

      ```
      public void setRequester​(BPMUserVO requester)
      ```
    - #### getFormRecordId

      ```
      public Integer getFormRecordId()
      ```
    - #### setFormRecordId

      ```
      public void setFormRecordId​(Integer formRecordId)
      ```
    - #### getFormId

      ```
      public Integer getFormId()
      ```
    - #### setFormId

      ```
      public void setFormId​(Integer formId)
      ```
    - #### getParentRequestId

      ```
      public Integer getParentRequestId()
      ```
    - #### setParentRequestId

      ```
      public void setParentRequestId​(Integer parentRequestId)
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
    - #### getWarningDate

      ```
      public ZonedDateTime getWarningDate()
      ```
    - #### setWarningDate

      ```
      public void setWarningDate​(ZonedDateTime warningDate)
      ```
    - #### getDeadlineDate

      ```
      public ZonedDateTime getDeadlineDate()
      ```
    - #### setDeadlineDate

      ```
      public void setDeadlineDate​(ZonedDateTime deadlineDate)
      ```
    - #### getPeriodId

      ```
      public String getPeriodId()
      ```
    - #### setPeriodId

      ```
      public void setPeriodId​(String periodId)
      ```
    - #### getActivities

      ```
      public List<BPMProcessActivityVO> getActivities()
      ```
    - #### setActivities

      ```
      public void setActivities​(List<BPMProcessActivityVO> activities)
      ```
    - #### getFormRecord

      ```
      public BPMFormRecordVO getFormRecord()
      ```
    - #### setFormRecord

      ```
      public void setFormRecord​(BPMFormRecordVO formRecord)
      ```
    - #### getFormFields

      ```
      public List<BPMFormFieldVO> getFormFields()
      ```
    - #### setFormFields

      ```
      public void setFormFields​(List<BPMFormFieldVO> formFields)
      ```
    - #### getSlaStatus

      ```
      public String getSlaStatus()
      ```
    - #### setSlaStatus

      ```
      public void setSlaStatus​(String slaStatus)
      ```
    - #### getStatus

      ```
      public String getStatus()
      ```
    - #### setStatus

      ```
      public void setStatus​(String status)
      ```
    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```
    - #### getDeadlineSpecification

      ```
      public BPMDeadlineSpecificationVO getDeadlineSpecification()
      ```
    - #### setDeadlineSpecification

      ```
      public void setDeadlineSpecification​(BPMDeadlineSpecificationVO deadlineSpecification)
      ```
