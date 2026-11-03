---
content_hash: 9812ba8df57df7f8924d9d34d67f450f51df9c43c1f16d619065a7eb68c8c580
fetched_at: '2026-11-03T14:35:05.843821+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessTaskVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessTaskVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessTaskVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessTaskVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessTaskVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessTaskVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessTaskVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessTaskVO()` |  |
    | `ProcessTaskVO​(long companyId, int processInstanceId, int movementSequence, int transferredSequence, String colleagueId, String selectedColleagueId, String complement)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getColleagueId()` |  |
    | `long` | `getCompanyId()` |  |
    | `String` | `getComplement()` |  |
    | `int` | `getMovementSequence()` |  |
    | `int` | `getProcessInstanceId()` |  |
    | `String` | `getSelectedColleagueId()` |  |
    | `int` | `getTransferredSequence()` |  |
    | `void` | `setColleagueId​(String colleagueId)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setComplement​(String complement)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setProcessInstanceId​(int processInstanceId)` |  |
    | `void` | `setSelectedColleagueId​(String selectedColleagueId)` |  |
    | `void` | `setTransferredSequence​(int transferredSequence)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessTaskVO

      ```
      public ProcessTaskVO()
      ```
    - #### ProcessTaskVO

      ```
      public ProcessTaskVO​(long companyId,
                           int processInstanceId,
                           int movementSequence,
                           int transferredSequence,
                           String colleagueId,
                           String selectedColleagueId,
                           String complement)
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
    - #### getTransferredSequence

      ```
      public int getTransferredSequence()
      ```
    - #### setTransferredSequence

      ```
      public void setTransferredSequence​(int transferredSequence)
      ```
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```
    - #### getSelectedColleagueId

      ```
      public String getSelectedColleagueId()
      ```
    - #### setSelectedColleagueId

      ```
      public void setSelectedColleagueId​(String selectedColleagueId)
      ```
    - #### getComplement

      ```
      public String getComplement()
      ```
    - #### setComplement

      ```
      public void setComplement​(String complement)
      ```
