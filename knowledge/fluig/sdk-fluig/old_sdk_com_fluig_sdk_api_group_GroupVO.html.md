---
content_hash: e11203baf7e33c696c9fbf1f9f4bf8d10d2b3f002da1c5e648102afb06dc2a7d
fetched_at: '2026-11-03T14:35:04.382894+00:00'
page_id: com/fluig/sdk/api/group/GroupVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.group.GroupVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/group/GroupVO.html
version: 1
---

Package [com.fluig.sdk.api.group](https://api.fluig.com/old/sdk/com/fluig/sdk/api/group/package-summary.html)

## Class GroupVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.group.GroupVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class GroupVO
  extends Object
  implements Serializable
  ```

  Value Object para Group

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.group.GroupVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `GroupVO()` | Nova instância para GroupVO.java |
    | `GroupVO​(Long id, String code, String description)` | Nova instância para GroupVO.java com id, code e description |
    | `GroupVO​(String code, String description)` | Nova instância para GroupVO.java com code e description |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getCode()` | Recupera valor do code |
    | `String` | `getDescription()` | Recupera valor do description |
    | `HashMap<String,​String>` | `getExtData()` | Recupera valor do extData |
    | `String` | `getGroupType()` | Recupera valor do groupType |
    | `Long` | `getId()` | Recupera valor do id |
    | `Boolean` | `getIsInternal()` | Recupera valor do isInternal |
    | `void` | `setCode​(String code)` | Atribui valor para code |
    | `void` | `setDescription​(String description)` | Atribui valor para description |
    | `void` | `setExtData​(HashMap<String,​String> extData)` | Atribui valor para extData |
    | `void` | `setGroupType​(String groupType)` | Atribui valor para groupType |
    | `void` | `setId​(Long id)` | Atribui valor para id |
    | `void` | `setIsInternal​(Boolean isInternal)` | Atribui valor para isInternal |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### GroupVO

      ```
      public GroupVO()
      ```

      Nova instância para GroupVO.java
    - #### GroupVO

      ```
      public GroupVO​(String code,
                     String description)
      ```

      Nova instância para GroupVO.java com code e description

      Parameters:
      :   `code` -
      :   `description` -
    - #### GroupVO

      ```
      public GroupVO​(Long id,
                     String code,
                     String description)
      ```

      Nova instância para GroupVO.java com id, code e description

      Parameters:
      :   `id` -
      :   `code` -
      :   `description` -

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```

      Recupera valor do id

      Returns:
      :   the id
    - #### setId

      ```
      public void setId​(Long id)
      ```

      Atribui valor para id

      Parameters:
      :   `id` - the id to set
    - #### getCode

      ```
      public String getCode()
      ```

      Recupera valor do code

      Returns:
      :   the code
    - #### setCode

      ```
      public void setCode​(String code)
      ```

      Atribui valor para code

      Parameters:
      :   `code` - the code to set
    - #### getDescription

      ```
      public String getDescription()
      ```

      Recupera valor do description

      Returns:
      :   the description
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```

      Atribui valor para description

      Parameters:
      :   `description` - the description to set
    - #### getIsInternal

      ```
      public Boolean getIsInternal()
      ```

      Recupera valor do isInternal

      Returns:
      :   the isInternal
    - #### setIsInternal

      ```
      public void setIsInternal​(Boolean isInternal)
      ```

      Atribui valor para isInternal

      Parameters:
      :   `isInternal` - the isInternal to set
    - #### getGroupType

      ```
      public String getGroupType()
      ```

      Recupera valor do groupType

      Returns:
      :   the groupType
    - #### setGroupType

      ```
      public void setGroupType​(String groupType)
      ```

      Atribui valor para groupType

      Parameters:
      :   `groupType` - the groupType to set
    - #### getExtData

      ```
      public HashMap<String,​String> getExtData()
      ```

      Recupera valor do extData

      Returns:
      :   the extData
    - #### setExtData

      ```
      public void setExtData​(HashMap<String,​String> extData)
      ```

      Atribui valor para extData

      Parameters:
      :   `extData` - the extData to set
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
