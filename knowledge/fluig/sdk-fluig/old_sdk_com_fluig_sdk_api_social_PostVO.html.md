---
content_hash: 081f2b2eb081ef6fcb1e777853a7bec15a08aac92fe2b0a9fa8a11d991bd0f24
fetched_at: '2026-11-03T14:35:04.877347+00:00'
page_id: com/fluig/sdk/api/social/PostVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.PostVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/PostVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class PostVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.PostVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class PostVO
  extends Object
  implements Serializable
  ```

  Value Object para Post

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.PostVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `PostVO()` |  |
    | `PostVO​(String text, String visibility, String alias, List<Long> customUsers, Long sociableObjectId)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAlias()` | Recupera valor do alias |
    | `List<Long>` | `getCustomUsers()` | Recupera valor do customUsers |
    | `Long` | `getId()` | Recupera valor do id |
    | `MediaVO` | `getMediaVO()` | Recupera o valor do |
    | `Long` | `getSociableObjectId()` | Recupera valor do sociableObjectId |
    | `String` | `getText()` | Recupera valor do text |
    | `String` | `getVisibility()` | Recupera valor do visibility |
    | `void` | `setAlias​(String alias)` | Atribui valor para alias |
    | `void` | `setCustomUsers​(List<Long> customUsers)` | Atribui valor para customUsers |
    | `void` | `setId​(Long id)` | Atribui valor para id |
    | `void` | `setMediaVO​(MediaVO mediaVO)` | \* Atribui valor para mediaVO |
    | `void` | `setSociableObjectId​(Long sociableObjectId)` | Atribui valor para sociableObjectId |
    | `void` | `setText​(String text)` | Atribui valor para text |
    | `void` | `setVisibility​(String visibility)` | Atribui valor para visibility |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### PostVO

      ```
      public PostVO()
      ```
    - #### PostVO

      ```
      public PostVO​(String text,
                    String visibility,
                    String alias,
                    List<Long> customUsers,
                    Long sociableObjectId)
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
    - #### getText

      ```
      public String getText()
      ```

      Recupera valor do text

      Returns:
      :   the text
    - #### setText

      ```
      public void setText​(String text)
      ```

      Atribui valor para text

      Parameters:
      :   `text` - the text to set
    - #### getVisibility

      ```
      public String getVisibility()
      ```

      Recupera valor do visibility

      Returns:
      :   the visibility
    - #### setVisibility

      ```
      public void setVisibility​(String visibility)
      ```

      Atribui valor para visibility

      Parameters:
      :   `visibility` - the visibility to set
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
    - #### getCustomUsers

      ```
      public List<Long> getCustomUsers()
      ```

      Recupera valor do customUsers

      Returns:
      :   the customUsers
    - #### setCustomUsers

      ```
      public void setCustomUsers​(List<Long> customUsers)
      ```

      Atribui valor para customUsers

      Parameters:
      :   `customUsers` - the customUsers to set
    - #### getSociableObjectId

      ```
      public Long getSociableObjectId()
      ```

      Recupera valor do sociableObjectId

      Returns:
      :   the sociableObjectId
    - #### setSociableObjectId

      ```
      public void setSociableObjectId​(Long sociableObjectId)
      ```

      Atribui valor para sociableObjectId

      Parameters:
      :   `sociableObjectId` - the sociableObjectId to set
    - #### getMediaVO

      ```
      public MediaVO getMediaVO()
      ```

      Recupera o valor do

      Returns:
      :   the mediaVO
    - #### setMediaVO

      ```
      public void setMediaVO​(MediaVO mediaVO)
      ```

      \* Atribui valor para mediaVO

      Parameters:
      :   `mediaVO` - the mediaVO to set
