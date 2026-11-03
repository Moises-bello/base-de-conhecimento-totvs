---
content_hash: 9c7bb94142b07db01f6e675c598837b5584597a437fe78e5e92055e5464fd119
fetched_at: '2026-11-03T14:35:05.448106+00:00'
page_id: com/fluig/sdk/api/workflow/CancelInstancesResultVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.CancelInstancesResultVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/CancelInstancesResultVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class CancelInstancesResultVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.CancelInstancesResultVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CancelInstancesResultVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.CancelInstancesResultVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CancelInstancesResultVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<CancelInstanceResultVO>` | `getCancelInstanceResults()` |  |
    | `long` | `getFailCount()` |  |
    | `long` | `getSuccessCount()` |  |
    | `void` | `setCancelInstanceResults​(List<CancelInstanceResultVO> cancelInstanceResults)` |  |
    | `void` | `setFailCount​(long failCount)` |  |
    | `void` | `setSuccessCount​(long successCount)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### CancelInstancesResultVO

      ```
      public CancelInstancesResultVO()
      ```

  + ### Method Detail

    - #### getSuccessCount

      ```
      public long getSuccessCount()
      ```
    - #### setSuccessCount

      ```
      public void setSuccessCount​(long successCount)
      ```
    - #### getFailCount

      ```
      public long getFailCount()
      ```
    - #### setFailCount

      ```
      public void setFailCount​(long failCount)
      ```
    - #### getCancelInstanceResults

      ```
      public List<CancelInstanceResultVO> getCancelInstanceResults()
      ```
    - #### setCancelInstanceResults

      ```
      public void setCancelInstanceResults​(List<CancelInstanceResultVO> cancelInstanceResults)
      ```
