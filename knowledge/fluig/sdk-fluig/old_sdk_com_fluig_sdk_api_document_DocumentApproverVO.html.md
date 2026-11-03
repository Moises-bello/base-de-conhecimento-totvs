---
content_hash: 4fe693209ae9cc10b026510524e999cc1a06a70983fa6281443f813edec9ca7a
fetched_at: '2026-11-03T14:35:03.953827+00:00'
page_id: com/fluig/sdk/api/document/DocumentApproverVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.DocumentApproverVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/DocumentApproverVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class DocumentApproverVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.DocumentApproverVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DocumentApproverVO
  extends Object
  implements Serializable
  ```

  Value Object para DocumentApprover

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.DocumentApproverVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DocumentApproverVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAlias()` |  |
    | `Integer` | `getApprovalMode()` | Recupera valor do approvalMode |
    | `String` | `getApprovalObservation()` |  |
    | `String` | `getApprovalStatus()` |  |
    | `Integer` | `getApproverType()` | Recupera valor do approverType |
    | `String` | `getColleagueId()` | Recupera valor do colleagueId |
    | `Long` | `getCompanyId()` |  |
    | `Boolean` | `getDigitalSignature()` | Recupera valor do digitalSignature |
    | `String` | `getEmail()` |  |
    | `String` | `getFullName()` |  |
    | `String` | `getLevelDescription()` | Recupera valor do levelDescription |
    | `Integer` | `getLevelId()` | Recupera valor do levelId |
    | `void` | `setAlias​(String alias)` |  |
    | `void` | `setApprovalMode​(Integer approvalMode)` | Atribui valor para approvalMode |
    | `void` | `setApprovalObservation​(String approvalObservation)` |  |
    | `void` | `setApprovalStatus​(String approvalStatus)` |  |
    | `void` | `setApproverType​(Integer approverType)` | Atribui valor para approverType |
    | `void` | `setColleagueId​(String colleagueId)` | Atribui valor para colleagueId |
    | `void` | `setCompanyId​(Long companyId)` |  |
    | `void` | `setDigitalSignature​(Boolean digitalSignature)` | Atribui valor para digitalSignature |
    | `void` | `setEmail​(String email)` |  |
    | `void` | `setFullName​(String fullName)` |  |
    | `void` | `setLevelDescription​(String levelDescription)` | Atribui valor para levelDescription |
    | `void` | `setLevelId​(Integer levelId)` | Atribui valor para levelId |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DocumentApproverVO

      ```
      public DocumentApproverVO()
      ```

  + ### Method Detail

    - #### getApproverType

      ```
      public Integer getApproverType()
      ```

      Recupera valor do approverType

      Returns:
      :   the approverType
    - #### setApproverType

      ```
      public void setApproverType​(Integer approverType)
      ```

      Atribui valor para approverType

      Parameters:
      :   `approverType` - the approverType to set
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```

      Recupera valor do colleagueId

      Returns:
      :   the colleagueId
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```

      Atribui valor para colleagueId

      Parameters:
      :   `colleagueId` - the colleagueId to set
    - #### getLevelId

      ```
      public Integer getLevelId()
      ```

      Recupera valor do levelId

      Returns:
      :   the levelId
    - #### setLevelId

      ```
      public void setLevelId​(Integer levelId)
      ```

      Atribui valor para levelId

      Parameters:
      :   `levelId` - the levelId to set
    - #### getApprovalMode

      ```
      public Integer getApprovalMode()
      ```

      Recupera valor do approvalMode

      Returns:
      :   the approvalMode
    - #### setApprovalMode

      ```
      public void setApprovalMode​(Integer approvalMode)
      ```

      Atribui valor para approvalMode

      Parameters:
      :   `approvalMode` - the approvalMode to set
    - #### getDigitalSignature

      ```
      public Boolean getDigitalSignature()
      ```

      Recupera valor do digitalSignature

      Returns:
      :   the digitalSignature
    - #### setDigitalSignature

      ```
      public void setDigitalSignature​(Boolean digitalSignature)
      ```

      Atribui valor para digitalSignature

      Parameters:
      :   `digitalSignature` - the digitalSignature to set
    - #### getLevelDescription

      ```
      public String getLevelDescription()
      ```

      Recupera valor do levelDescription

      Returns:
      :   the levelDescription
    - #### setLevelDescription

      ```
      public void setLevelDescription​(String levelDescription)
      ```

      Atribui valor para levelDescription

      Parameters:
      :   `levelDescription` - the levelDescription to set
    - #### getAlias

      ```
      public String getAlias()
      ```

      Returns:
      :   the alias
    - #### setAlias

      ```
      public void setAlias​(String alias)
      ```

      Parameters:
      :   `alias` - the alias to set
    - #### getFullName

      ```
      public String getFullName()
      ```

      Returns:
      :   the fullName
    - #### setFullName

      ```
      public void setFullName​(String fullName)
      ```

      Parameters:
      :   `fullName` - the fullName to set
    - #### getEmail

      ```
      public String getEmail()
      ```

      Returns:
      :   the email
    - #### setEmail

      ```
      public void setEmail​(String email)
      ```

      Parameters:
      :   `email` - the email to set
    - #### getApprovalStatus

      ```
      public String getApprovalStatus()
      ```

      Returns:
      :   the approvalStatus
    - #### setApprovalStatus

      ```
      public void setApprovalStatus​(String approvalStatus)
      ```

      Parameters:
      :   `approvalStatus` - the approvalStatus to set
    - #### getApprovalObservation

      ```
      public String getApprovalObservation()
      ```

      Returns:
      :   the approvalObservation
    - #### setApprovalObservation

      ```
      public void setApprovalObservation​(String approvalObservation)
      ```

      Parameters:
      :   `approvalObservation` - the approvalObservation to set
    - #### getCompanyId

      ```
      public Long getCompanyId()
      ```

      Returns:
      :   companyId
    - #### setCompanyId

      ```
      public void setCompanyId​(Long companyId)
      ```

      Parameters:
      :   `companyId` -
