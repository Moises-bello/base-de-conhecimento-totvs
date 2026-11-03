---
content_hash: 1ed602ff6c4728e16c3f7b28a3f22c9c461117970dd9f62cbd202a7ccea65f83
fetched_at: '2026-11-03T14:35:06.025565+00:00'
page_id: com/fluig/sdk/api/workflow/WorkflowVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.WorkflowVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/WorkflowVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class WorkflowVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.WorkflowVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class WorkflowVO
  extends Object
  implements Serializable
  ```

  Author:
  :   marcelo.pereira

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.WorkflowVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `WorkflowVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Boolean` | `getActive()` |  |
    | `Integer` | `getAttachmentSeqId()` |  |
    | `Boolean` | `getCanCancel()` |  |
    | `Boolean` | `getCanTake()` |  |
    | `String` | `getCode()` |  |
    | `String` | `getColleagueName()` |  |
    | `long` | `getCompanyId()` |  |
    | `Date` | `getDeadlineDate()` |  |
    | `String` | `getDeadlineText()` |  |
    | `String` | `getDocumentDescription()` |  |
    | `Integer` | `getMainAttachmentDocumentId()` |  |
    | `int` | `getMainAttachmentDocumentVersion()` |  |
    | `Boolean` | `getMobileReady()` |  |
    | `String` | `getMovementHour()` |  |
    | `int` | `getMovementSequence()` |  |
    | `String` | `getProcessDescription()` |  |
    | `String` | `getProcessId()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `String` | `getRequesterId()` |  |
    | `String` | `getRequesterName()` |  |
    | `int` | `getRowId()` |  |
    | `Integer` | `getSourceProcess()` |  |
    | `Integer` | `getSourceThreadSequence()` |  |
    | `String` | `getStateDescription()` |  |
    | `Integer` | `getStateId()` |  |
    | `String` | `getUrl()` |  |
    | `Integer` | `getVersion()` |  |
    | `void` | `setActive​(Boolean active)` |  |
    | `void` | `setAttachmentSeqId​(Integer attachmentSeqId)` |  |
    | `void` | `setCanCancel​(Boolean canCancel)` |  |
    | `void` | `setCanTake​(Boolean canTake)` |  |
    | `void` | `setCode​(String code)` |  |
    | `void` | `setColleagueName​(String colleagueName)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setDeadlineDate​(Date deadlineDate)` |  |
    | `void` | `setDeadlineText​(String deadlineText)` |  |
    | `void` | `setDocumentDescription​(String documentDescription)` |  |
    | `void` | `setMainAttachmentDocumentId​(Integer mainAttachmentDocumentId)` |  |
    | `void` | `setMainAttachmentDocumentVersion​(int mainAttachmentDocumentVersion)` |  |
    | `void` | `setMobileReady​(Boolean mobileReady)` |  |
    | `void` | `setMovementHour​(String movementHour)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setProcessDescription​(String processDescription)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setRequesterId​(String requesterId)` |  |
    | `void` | `setRequesterName​(String requesterName)` |  |
    | `void` | `setRowId​(int rowId)` |  |
    | `void` | `setSourceProcess​(Integer sourceProcess)` |  |
    | `void` | `setSourceThreadSequence​(Integer sourceThreadSequence)` |  |
    | `void` | `setStateDescription​(String stateDescription)` |  |
    | `void` | `setStateId​(Integer stateId)` |  |
    | `void` | `setUrl​(String url)` |  |
    | `void` | `setVersion​(Integer version)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### WorkflowVO

      ```
      public WorkflowVO()
      ```

  + ### Method Detail

    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```

      Returns:
      :   the processDescription
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```

      Parameters:
      :   `processDescription` - the processDescription to set
    - #### getProcessId

      ```
      public String getProcessId()
      ```

      Returns:
      :   the processId
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```

      Parameters:
      :   `processId` - the processId to set
    - #### getCompanyId

      ```
      public long getCompanyId()
      ```

      Returns:
      :   the companyId
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
      ```

      Parameters:
      :   `companyId` - the companyId to set
    - #### getProcessInstanceId

      ```
      public int getProcessInstanceId()
      ```

      Returns:
      :   the processInstanceId
    - #### setProcessInstanceId

      ```
      public void setProcessInstanceId​(int processInstanceId)
      ```

      Parameters:
      :   `processInstanceId` - the processInstanceId to set
    - #### getVersion

      ```
      public Integer getVersion()
      ```

      Returns:
      :   the version
    - #### setVersion

      ```
      public void setVersion​(Integer version)
      ```

      Parameters:
      :   `version` - the version to set
    - #### getRequesterId

      ```
      public String getRequesterId()
      ```

      Returns:
      :   the requesterId
    - #### setRequesterId

      ```
      public void setRequesterId​(String requesterId)
      ```

      Parameters:
      :   `requesterId` - the requesterId to set
    - #### getRequesterName

      ```
      public String getRequesterName()
      ```

      Returns:
      :   the requesterName
    - #### setRequesterName

      ```
      public void setRequesterName​(String requesterName)
      ```

      Parameters:
      :   `requesterName` - the requesterName to set
    - #### getActive

      ```
      public Boolean getActive()
      ```

      Returns:
      :   the active
    - #### setActive

      ```
      public void setActive​(Boolean active)
      ```

      Parameters:
      :   `active` - the active to set
    - #### getAttachmentSeqId

      ```
      public Integer getAttachmentSeqId()
      ```

      Returns:
      :   the attachmentSeqId
    - #### setAttachmentSeqId

      ```
      public void setAttachmentSeqId​(Integer attachmentSeqId)
      ```

      Parameters:
      :   `attachmentSeqId` - the attachmentSeqId to set
    - #### getSourceProcess

      ```
      public Integer getSourceProcess()
      ```

      Returns:
      :   the sourceProcess
    - #### setSourceProcess

      ```
      public void setSourceProcess​(Integer sourceProcess)
      ```

      Parameters:
      :   `sourceProcess` - the sourceProcess to set
    - #### getSourceThreadSequence

      ```
      public Integer getSourceThreadSequence()
      ```

      Returns:
      :   the sourceThreadSequence
    - #### setSourceThreadSequence

      ```
      public void setSourceThreadSequence​(Integer sourceThreadSequence)
      ```

      Parameters:
      :   `sourceThreadSequence` - the sourceThreadSequence to set
    - #### getStateId

      ```
      public Integer getStateId()
      ```

      Returns:
      :   the stateId
    - #### setStateId

      ```
      public void setStateId​(Integer stateId)
      ```

      Parameters:
      :   `stateId` - the stateId to set
    - #### getStateDescription

      ```
      public String getStateDescription()
      ```

      Returns:
      :   the stateDescription
    - #### setStateDescription

      ```
      public void setStateDescription​(String stateDescription)
      ```

      Parameters:
      :   `stateDescription` - the stateDescription to set
    - #### getDeadlineDate

      ```
      public Date getDeadlineDate()
      ```

      Returns:
      :   the deadlineDate
    - #### setDeadlineDate

      ```
      public void setDeadlineDate​(Date deadlineDate)
      ```

      Parameters:
      :   `deadlineDate` - the deadlineDate to set
    - #### getDeadlineText

      ```
      public String getDeadlineText()
      ```

      Returns:
      :   the deadlineText
    - #### setDeadlineText

      ```
      public void setDeadlineText​(String deadlineText)
      ```

      Parameters:
      :   `deadlineText` - the deadlineText to set
    - #### getDocumentDescription

      ```
      public String getDocumentDescription()
      ```

      Returns:
      :   the documentDescription
    - #### setDocumentDescription

      ```
      public void setDocumentDescription​(String documentDescription)
      ```

      Parameters:
      :   `documentDescription` - the documentDescription to set
    - #### getColleagueName

      ```
      public String getColleagueName()
      ```

      Returns:
      :   the colleagueName
    - #### setColleagueName

      ```
      public void setColleagueName​(String colleagueName)
      ```

      Parameters:
      :   `colleagueName` - the colleagueName to set
    - #### getMovementSequence

      ```
      public int getMovementSequence()
      ```

      Returns:
      :   the movementSequence
    - #### setMovementSequence

      ```
      public void setMovementSequence​(int movementSequence)
      ```

      Parameters:
      :   `movementSequence` - the movementSequence to set
    - #### getMainAttachmentDocumentId

      ```
      public Integer getMainAttachmentDocumentId()
      ```

      Returns:
      :   the mainAttachmentDocumentId
    - #### setMainAttachmentDocumentId

      ```
      public void setMainAttachmentDocumentId​(Integer mainAttachmentDocumentId)
      ```

      Parameters:
      :   `mainAttachmentDocumentId` - the mainAttachmentDocumentId to set
    - #### getMainAttachmentDocumentVersion

      ```
      public int getMainAttachmentDocumentVersion()
      ```

      Returns:
      :   the mainAttachmentDocumentVersion
    - #### setMainAttachmentDocumentVersion

      ```
      public void setMainAttachmentDocumentVersion​(int mainAttachmentDocumentVersion)
      ```

      Parameters:
      :   `mainAttachmentDocumentVersion` - the mainAttachmentDocumentVersion to set
    - #### getRowId

      ```
      public int getRowId()
      ```

      Returns:
      :   the rowId
    - #### setRowId

      ```
      public void setRowId​(int rowId)
      ```

      Parameters:
      :   `rowId` - the rowId to set
    - #### getMovementHour

      ```
      public String getMovementHour()
      ```

      Returns:
      :   the movementHour
    - #### setMovementHour

      ```
      public void setMovementHour​(String movementHour)
      ```

      Parameters:
      :   `movementHour` - the movementHour to set
    - #### getMobileReady

      ```
      public Boolean getMobileReady()
      ```

      Returns:
      :   the mobileReady
    - #### setMobileReady

      ```
      public void setMobileReady​(Boolean mobileReady)
      ```

      Parameters:
      :   `mobileReady` - the mobileReady to set
    - #### getCanCancel

      ```
      public Boolean getCanCancel()
      ```

      Returns:
      :   the canCancel
    - #### setCanCancel

      ```
      public void setCanCancel​(Boolean canCancel)
      ```

      Parameters:
      :   `canCancel` - the canCancel to set
    - #### getCanTake

      ```
      public Boolean getCanTake()
      ```

      Returns:
      :   the canTake
    - #### setCanTake

      ```
      public void setCanTake​(Boolean canTake)
      ```

      Parameters:
      :   `canTake` - the canTake to set
    - #### getUrl

      ```
      public String getUrl()
      ```

      Returns:
      :   the url
    - #### setUrl

      ```
      public void setUrl​(String url)
      ```

      Parameters:
      :   `url` - the url to set
    - #### getCode

      ```
      public String getCode()
      ```

      Returns:
      :   the code
    - #### setCode

      ```
      public void setCode​(String code)
      ```

      Parameters:
      :   `code` - the code to set
