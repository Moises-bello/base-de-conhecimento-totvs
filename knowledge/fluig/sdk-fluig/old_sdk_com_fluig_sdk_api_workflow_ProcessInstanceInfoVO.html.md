---
content_hash: b1b0d9061abbcb3cadf771a39b7172a08ae4df33b5d6e483dfcd1ad2a04ceb81
fetched_at: '2026-11-03T14:35:05.761031+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessInstanceInfoVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessInstanceInfoVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessInstanceInfoVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessInstanceInfoVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessInstanceInfoVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessInstanceInfoVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessInstanceInfoVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessInstanceInfoVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<ProcessAttachmentVO>` | `getAttachments()` |  |
    | `long` | `getCompanyId()` |  |
    | `int` | `getFormId()` |  |
    | `Map<String,​String>` | `getFormValues()` |  |
    | `int` | `getFormVersion()` |  |
    | `String` | `getProcessId()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `int` | `getProcessVersion()` |  |
    | `Date` | `getStartDateProcess()` |  |
    | `List<ProcessObservationVO>` | `getTaskObservations()` |  |
    | `List<ProcessTaskInfoVO>` | `getTasksInfo()` |  |
    | `void` | `setAttachments​(List<ProcessAttachmentVO> attachments)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setFormId​(int formId)` |  |
    | `void` | `setFormValues​(Map<String,​String> formValues)` |  |
    | `void` | `setFormVersion​(int formVersion)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setProcessVersion​(int processVersion)` |  |
    | `void` | `setStartDateProcess​(Date startDateProcess)` |  |
    | `void` | `setTaskObservations​(List<ProcessObservationVO> taskObservations)` |  |
    | `void` | `setTasksInfo​(List<ProcessTaskInfoVO> tasksInfo)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessInstanceInfoVO

      ```
      public ProcessInstanceInfoVO()
      ```

  + ### Method Detail

    - #### getCompanyId

      ```
      public long getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
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
    - #### getProcessInstanceId

      ```
      public int getProcessInstanceId()
      ```
    - #### setProcessInstanceId

      ```
      public void setProcessInstanceId​(int processInstanceId)
      ```
    - #### getFormId

      ```
      public int getFormId()
      ```
    - #### setFormId

      ```
      public void setFormId​(int formId)
      ```
    - #### getFormVersion

      ```
      public int getFormVersion()
      ```
    - #### setFormVersion

      ```
      public void setFormVersion​(int formVersion)
      ```
    - #### getFormValues

      ```
      public Map<String,​String> getFormValues()
      ```
    - #### setFormValues

      ```
      public void setFormValues​(Map<String,​String> formValues)
      ```
    - #### getTaskObservations

      ```
      public List<ProcessObservationVO> getTaskObservations()
      ```
    - #### getAttachments

      ```
      public List<ProcessAttachmentVO> getAttachments()
      ```
    - #### setAttachments

      ```
      public void setAttachments​(List<ProcessAttachmentVO> attachments)
      ```
    - #### setTaskObservations

      ```
      public void setTaskObservations​(List<ProcessObservationVO> taskObservations)
      ```
    - #### getTasksInfo

      ```
      public List<ProcessTaskInfoVO> getTasksInfo()
      ```
    - #### setTasksInfo

      ```
      public void setTasksInfo​(List<ProcessTaskInfoVO> tasksInfo)
      ```
    - #### getStartDateProcess

      ```
      public Date getStartDateProcess()
      ```
    - #### setStartDateProcess

      ```
      public void setStartDateProcess​(Date startDateProcess)
      ```
