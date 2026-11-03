---
content_hash: bb0f8f0efb190f3b7f84e2de0a3297caecd4bd327affdb9f33a33d8429cd66fe
fetched_at: '2026-11-03T14:35:05.861685+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessVersionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessVersionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessVersionVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessVersionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessVersionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessVersionVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessVersionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessVersionVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<ProcessVersionVO>` | `getChildren()` |  |
    | `long` | `getCompanyId()` |  |
    | `Boolean` | `getFavorite()` |  |
    | `Integer` | `getFormId()` |  |
    | `String` | `getProcessId()` |  |
    | `Boolean` | `getSelected()` |  |
    | `String` | `getVersionDescription()` |  |
    | `void` | `setChildren​(List<ProcessVersionVO> children)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setFavorite​(Boolean favorite)` |  |
    | `void` | `setFormId​(Integer formId)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setSelected​(Boolean selected)` |  |
    | `void` | `setVersionDescription​(String versionDescription)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessVersionVO

      ```
      public ProcessVersionVO()
      ```

  + ### Method Detail

    - #### getSelected

      ```
      public Boolean getSelected()
      ```

      Returns:
      :   the selected
    - #### setSelected

      ```
      public void setSelected​(Boolean selected)
      ```

      Parameters:
      :   `selected` - the selected to set
    - #### getChildren

      ```
      public List<ProcessVersionVO> getChildren()
      ```

      Returns:
      :   the children
    - #### setChildren

      ```
      public void setChildren​(List<ProcessVersionVO> children)
      ```

      Parameters:
      :   `children` - the children to set
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
    - #### getFormId

      ```
      public Integer getFormId()
      ```

      Returns:
      :   the formId
    - #### setFormId

      ```
      public void setFormId​(Integer formId)
      ```

      Parameters:
      :   `formId` - the formId to set
    - #### getVersionDescription

      ```
      public String getVersionDescription()
      ```

      Returns:
      :   the versionDescription
    - #### setVersionDescription

      ```
      public void setVersionDescription​(String versionDescription)
      ```

      Parameters:
      :   `versionDescription` - the versionDescription to set
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
    - #### getFavorite

      ```
      public Boolean getFavorite()
      ```

      Returns:
      :   the favorite
    - #### setFavorite

      ```
      public void setFavorite​(Boolean favorite)
      ```

      Parameters:
      :   `favorite` - the favorite to set
