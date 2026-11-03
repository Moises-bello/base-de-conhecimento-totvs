---
content_hash: 1b5e3e7bfc909066a3da54671eae0a87d59d8021a031788812da0d287ac7ce88
fetched_at: '2026-11-03T14:35:05.739409+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessDefinitionVersionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessDefinitionVersionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessDefinitionVersionVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessDefinitionVersionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessDefinitionVersionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessDefinitionVersionVO
  extends Object
  implements Serializable
  ```

  Value Object para ProcessDefinitionVersion

  Version:
  :   1.5.3

  Author:
  :   marcelo.pereira

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessDefinitionVersionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessDefinitionVersionVO()` |  |
    | `ProcessDefinitionVersionVO​(long tenantId, String processId, int version, String versionDescription, String categoryStructure, String fullCategoryStructure, String processDescription)` | Cria uma instância do ProcessDefinitionVersionVO |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getCategoryStructure()` | Recupera valor do categoryStructure |
    | `Integer` | `getFormId()` | Recupera valor do formId |
    | `Integer` | `getFormVersion()` | Recupera valor do formVersion |
    | `String` | `getFullCategoryStructure()` | Recupera valor do fullCategoryStructure |
    | `ProcessStateVO` | `getInitialProcessState()` | Recupera valor do initialProcessState |
    | `String` | `getProcessDescription()` | Recupera valor do processDescription |
    | `String` | `getProcessId()` | Recupera valor do processId |
    | `int` | `getRowId()` | Recupera valor do rowId |
    | `long` | `getTenantId()` | Recupera valor do tenantId |
    | `int` | `getVersion()` | Recupera valor do version |
    | `String` | `getVersionDescription()` | Recupera valor do versionDescription |
    | `boolean` | `isFavorite()` | Favorito? |
    | `boolean` | `isMobileReady()` | Mobile? |
    | `void` | `setCategoryStructure​(String categoryStructure)` | Atribui valor para categoryStructure |
    | `void` | `setFavorite​(boolean favorite)` | Atribui valor para favorite |
    | `void` | `setFormId​(Integer formId)` | Atribui valor para formId |
    | `void` | `setFormVersion​(Integer formVersion)` | Atribui valor para formVersion |
    | `void` | `setFullCategoryStructure​(String fullCategoryStructure)` | Atribui valor para fullCategoryStructure |
    | `void` | `setInitialProcessState​(ProcessStateVO initialProcessState)` | Atribui valor para initialProcessState |
    | `void` | `setMobileReady​(boolean mobileReady)` | Atribui valor para mobileReady |
    | `void` | `setProcessDescription​(String processDescription)` | Atribui valor para processDescription |
    | `void` | `setProcessId​(String processId)` | Atribui valor para processId |
    | `void` | `setRowId​(int rowId)` | Atribui valor para rowId |
    | `void` | `setTenantId​(long tenantId)` | Atribui valor para tenantId |
    | `void` | `setVersion​(int version)` | Atribui valor para version |
    | `void` | `setVersionDescription​(String versionDescription)` | Atribui valor para versionDescription |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessDefinitionVersionVO

      ```
      public ProcessDefinitionVersionVO()
      ```
    - #### ProcessDefinitionVersionVO

      ```
      public ProcessDefinitionVersionVO​(long tenantId,
                                        String processId,
                                        int version,
                                        String versionDescription,
                                        String categoryStructure,
                                        String fullCategoryStructure,
                                        String processDescription)
      ```

      Cria uma instância do ProcessDefinitionVersionVO

      Parameters:
      :   `tenantId` - the tenantId to set
      :   `processId` - the processId to set
      :   `version` - the version to set
      :   `versionDescription` - the versionDescription to set
      :   `categoryStructure` - the categoryStructure to set
      :   `fullCategoryStructure` - the fullCategoryStructure to set
      :   `processDescription` - the processDescription to set

  + ### Method Detail

    - #### getTenantId

      ```
      public long getTenantId()
      ```

      Recupera valor do tenantId

      Returns:
      :   the tenantId
    - #### setTenantId

      ```
      public void setTenantId​(long tenantId)
      ```

      Atribui valor para tenantId

      Parameters:
      :   `tenantId` - the tenantId to set
    - #### getProcessId

      ```
      public String getProcessId()
      ```

      Recupera valor do processId

      Returns:
      :   the processId
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```

      Atribui valor para processId

      Parameters:
      :   `processId` - the processId to set
    - #### getVersion

      ```
      public int getVersion()
      ```

      Recupera valor do version

      Returns:
      :   the version
    - #### setVersion

      ```
      public void setVersion​(int version)
      ```

      Atribui valor para version

      Parameters:
      :   `version` - the version to set
    - #### getVersionDescription

      ```
      public String getVersionDescription()
      ```

      Recupera valor do versionDescription

      Returns:
      :   the versionDescription
    - #### setVersionDescription

      ```
      public void setVersionDescription​(String versionDescription)
      ```

      Atribui valor para versionDescription

      Parameters:
      :   `versionDescription` - the versionDescription to set
    - #### getCategoryStructure

      ```
      public String getCategoryStructure()
      ```

      Recupera valor do categoryStructure

      Returns:
      :   the categoryStructure
    - #### setCategoryStructure

      ```
      public void setCategoryStructure​(String categoryStructure)
      ```

      Atribui valor para categoryStructure

      Parameters:
      :   `categoryStructure` - the categoryStructure to set
    - #### setFullCategoryStructure

      ```
      public void setFullCategoryStructure​(String fullCategoryStructure)
      ```

      Atribui valor para fullCategoryStructure

      Parameters:
      :   `fullCategoryStructure` - the fullCategoryStructure to set
    - #### getFullCategoryStructure

      ```
      public String getFullCategoryStructure()
      ```

      Recupera valor do fullCategoryStructure

      Returns:
      :   the fullCategoryStructure
    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```

      Recupera valor do processDescription

      Returns:
      :   the processDescription
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```

      Atribui valor para processDescription

      Parameters:
      :   `processDescription` - the processDescription to set
    - #### getRowId

      ```
      public int getRowId()
      ```

      Recupera valor do rowId

      Returns:
      :   the rowId
    - #### setRowId

      ```
      public void setRowId​(int rowId)
      ```

      Atribui valor para rowId

      Parameters:
      :   `rowId` - the rowId to set
    - #### isFavorite

      ```
      public boolean isFavorite()
      ```

      Favorito?

      Returns:
      :   the favorite
    - #### setFavorite

      ```
      public void setFavorite​(boolean favorite)
      ```

      Atribui valor para favorite

      Parameters:
      :   `favorite` - the favorite to set
    - #### isMobileReady

      ```
      public boolean isMobileReady()
      ```

      Mobile?

      Returns:
      :   the mobileReady
    - #### setMobileReady

      ```
      public void setMobileReady​(boolean mobileReady)
      ```

      Atribui valor para mobileReady

      Parameters:
      :   `mobileReady` - the mobileReady to set
    - #### getFormId

      ```
      public Integer getFormId()
      ```

      Recupera valor do formId

      Returns:
      :   the formId
    - #### setFormId

      ```
      public void setFormId​(Integer formId)
      ```

      Atribui valor para formId

      Parameters:
      :   `formId` - the formId to set
    - #### getInitialProcessState

      ```
      public ProcessStateVO getInitialProcessState()
      ```

      Recupera valor do initialProcessState

      Returns:
      :   the initialProcessState
    - #### setInitialProcessState

      ```
      public void setInitialProcessState​(ProcessStateVO initialProcessState)
      ```

      Atribui valor para initialProcessState

      Parameters:
      :   `initialProcessState` - the initialProcessState to set
    - #### getFormVersion

      ```
      public Integer getFormVersion()
      ```

      Recupera valor do formVersion

      Returns:
      :   the formVersion
    - #### setFormVersion

      ```
      public void setFormVersion​(Integer formVersion)
      ```

      Atribui valor para formVersion

      Parameters:
      :   `formVersion` - the formVersion to set
