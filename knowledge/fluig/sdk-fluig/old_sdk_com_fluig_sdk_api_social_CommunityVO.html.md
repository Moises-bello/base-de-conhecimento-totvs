---
content_hash: f588070f3d4c505a9013b4c5ad850cc8237de6ff483cda3ee1a94e4014de566d
fetched_at: '2026-11-03T14:35:04.830652+00:00'
page_id: com/fluig/sdk/api/social/CommunityVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.CommunityVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/CommunityVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class CommunityVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.CommunityVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CommunityVO
  extends Object
  implements Serializable
  ```

  Value Object para Community

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.CommunityVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CommunityVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAdminAlias()` | Recupera valor do adminAlias |
    | `String` | `getAlias()` | Recupera valor do alias |
    | `Boolean` | `getApprovalRequired()` | Recupera valor do approvalRequired |
    | `Boolean` | `getCreateForum()` |  |
    | `String` | `getDescription()` | Recupera valor do description |
    | `Map<String,​Object>` | `getEcmInfo()` | Recupera valor do ecmInfo |
    | `Boolean` | `getHidden()` | Recupera valor do hidden |
    | `Long` | `getId()` | Recupera valor do id |
    | `String` | `getName()` | Recupera valor do name |
    | `Boolean` | `getPrivateContent()` | Recupera valor do privateContent |
    | `void` | `setAdminAlias​(String adminAlias)` | Atribui valor para adminAlias |
    | `void` | `setAlias​(String alias)` | Atribui valor para alias |
    | `void` | `setApprovalRequired​(Boolean approvalRequired)` | Atribui valor para approvalRequired |
    | `void` | `setCreateForum​(Boolean createForum)` |  |
    | `void` | `setDescription​(String description)` | Atribui valor para description |
    | `void` | `setEcmInfo​(Map<String,​Object> ecmInfo)` | Atribui valor para ecmInfo |
    | `void` | `setHidden​(Boolean hidden)` | Atribui valor para hidden |
    | `void` | `setId​(Long id)` | Atribui valor para id |
    | `void` | `setName​(String name)` | Atribui valor para name |
    | `void` | `setPrivateContent​(Boolean privateContent)` | Atribui valor para privateContent |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### CommunityVO

      ```
      public CommunityVO()
      ```

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
    - #### getAlias

      ```
      public String getAlias()
      ```

      Recupera valor do alias

      Returns:
      :   the alias
    - #### setAlias

      ```
      public void setAlias​(String alias)
      ```

      Atribui valor para alias

      Parameters:
      :   `alias` - the alias to set
    - #### getName

      ```
      public String getName()
      ```

      Recupera valor do name

      Returns:
      :   the name
    - #### setName

      ```
      public void setName​(String name)
      ```

      Atribui valor para name

      Parameters:
      :   `name` - the name to set
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
    - #### getAdminAlias

      ```
      public String getAdminAlias()
      ```

      Recupera valor do adminAlias

      Returns:
      :   the adminAlias
    - #### setAdminAlias

      ```
      public void setAdminAlias​(String adminAlias)
      ```

      Atribui valor para adminAlias

      Parameters:
      :   `adminAlias` - the adminAlias to set
    - #### getHidden

      ```
      public Boolean getHidden()
      ```

      Recupera valor do hidden

      Returns:
      :   the hidden
    - #### setHidden

      ```
      public void setHidden​(Boolean hidden)
      ```

      Atribui valor para hidden

      Parameters:
      :   `hidden` - the hidden to set
    - #### getPrivateContent

      ```
      public Boolean getPrivateContent()
      ```

      Recupera valor do privateContent

      Returns:
      :   the privateContent
    - #### setPrivateContent

      ```
      public void setPrivateContent​(Boolean privateContent)
      ```

      Atribui valor para privateContent

      Parameters:
      :   `privateContent` - the privateContent to set
    - #### getApprovalRequired

      ```
      public Boolean getApprovalRequired()
      ```

      Recupera valor do approvalRequired

      Returns:
      :   the approvalRequired
    - #### setApprovalRequired

      ```
      public void setApprovalRequired​(Boolean approvalRequired)
      ```

      Atribui valor para approvalRequired

      Parameters:
      :   `approvalRequired` - the approvalRequired to set
    - #### getEcmInfo

      ```
      public Map<String,​Object> getEcmInfo()
      ```

      Recupera valor do ecmInfo

      Returns:
      :   the ecmInfo
    - #### setEcmInfo

      ```
      public void setEcmInfo​(Map<String,​Object> ecmInfo)
      ```

      Atribui valor para ecmInfo

      Parameters:
      :   `ecmInfo` - the ecmInfo to set
    - #### getCreateForum

      ```
      public Boolean getCreateForum()
      ```
    - #### setCreateForum

      ```
      public void setCreateForum​(Boolean createForum)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
