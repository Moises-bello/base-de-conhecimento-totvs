---
content_hash: 4fff8d33bcae84aa756295a3e457bf4bcd816797c49de7b1cd0458c27368fb73
fetched_at: '2026-11-03T14:35:04.763525+00:00'
page_id: com/fluig/sdk/api/social/ArticleVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.ArticleVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class ArticleVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.ArticleVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ArticleVO
  extends Object
  implements Serializable
  ```

  VO com informações utilizadas para criar Artigos

  Author:
  :   marcus.carvalho

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.ArticleVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ArticleVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object obj)` |  |
    | `Integer` | `getAccessCount()` | Recupera valor do campo accessCount |
    | `String` | `getAlias()` | Recupera o valor do field alias |
    | `ArticleCoverVO` | `getArticleCoverVO()` | Recupera o valor do field articleCoverVO |
    | `List<String>` | `getAttachments()` | Recupera o valor do field attachments |
    | `Long` | `getCategoryId()` | Recupera o valor do field categoryId |
    | `String` | `getContent()` | Recupera o valor do field content |
    | `Map<String,​String>` | `getCovers()` | Recupera o valor do field covers |
    | `String` | `getDescription()` | Recupera o valor do field description |
    | `Date` | `getExpirationDate()` | Recupera o valor do field expirationDate |
    | `Long` | `getId()` | Recupera o valor do field id |
    | `String` | `getKeyWord()` | Recupera o valor do field keyWord |
    | `long` | `getNumberWatchs()` | Recupera valor do campo numberWatchs |
    | `Date` | `getPublicationDate()` | Recupera o valor do field publicationDate |
    | `String` | `getPublisherId()` | Recupera o valor do field publisherId |
    | `String` | `getSecurityLevel()` | Recupera valor do campo securityLevel |
    | `SociableVO` | `getSociable()` | Recupera o valor do field sociableVO |
    | `Long` | `getSocialObjectId()` | Recupera o valor do field socialObjectId |
    | `Integer` | `getTopicId()` | Recupera o valor do field topicId |
    | `SocialVO` | `getUser()` | Recupera o valor do field user |
    | `Integer` | `getVersion()` | Recupera o valor do field version |
    | `int` | `hashCode()` |  |
    | `boolean` | `isApproved()` |  |
    | `boolean` | `isDraft()` | Recupera o valor do field draft |
    | `boolean` | `isExpires()` | Recupera o valor do field expires |
    | `boolean` | `isUserNotify()` | Recupera o valor do field userNotify |
    | `boolean` | `isViewedDocument()` | Recupera valor do campo viewedDocument |
    | `void` | `setAccessCount​(Integer accessCount)` | Atribui valor do campo accessCount |
    | `void` | `setAlias​(String alias)` | Setado o valor do field alias |
    | `void` | `setApproved​(boolean approved)` |  |
    | `void` | `setArticleCoverVO​(ArticleCoverVO articleCoverVO)` | Setado o valor do field articleCoverVO |
    | `void` | `setAttachments​(List<String> attachments)` | Setado o valor do field attachments |
    | `void` | `setCategoryId​(Long categoryId)` | Setado o valor do field categoryId |
    | `void` | `setContent​(String content)` | Setado o valor do field content |
    | `void` | `setCovers​(Map<String,​String> covers)` | Setado o valor do field covers |
    | `void` | `setDescription​(String description)` | Setado o valor do field description |
    | `void` | `setDraft​(boolean draft)` | Setado o valor do field draft |
    | `void` | `setExpirationDate​(Date expirationDate)` | Setado o valor do field expirationDate |
    | `void` | `setExpires​(boolean expires)` | Setado o valor do field expires |
    | `void` | `setId​(Long id)` | Setado o valor do field id |
    | `void` | `setKeyWord​(String keyWord)` | Setado o valor do field keyWord |
    | `void` | `setNumberWatchs​(long numberWatchs)` | Atribui valor do campo numberWatchs |
    | `void` | `setPublicationDate​(Date publicationDate)` | Setado o valor do field publicationDate |
    | `void` | `setPublisherId​(String publisherId)` | Setado o valor do field publisherId |
    | `void` | `setSecurityLevel​(String securityLevel)` | Atribui valor do campo securityLevel |
    | `void` | `setSociable​(SociableVO sociable)` | Setado o valor do field sociableVO |
    | `void` | `setSocialObjectId​(Long socialObjectId)` | Setado o valor do field socialObjectId |
    | `void` | `setTopicId​(Integer topicId)` | Setado o valor do field topicId |
    | `void` | `setUser​(SocialVO user)` | Setado o valor do field user |
    | `void` | `setUserNotify​(boolean userNotify)` | Setado o valor do field userNotify |
    | `void` | `setVersion​(Integer version)` | Setado o valor do field version |
    | `void` | `setViewedDocument​(boolean viewedDocument)` | Atribui valor do campo viewedDocument |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### ArticleVO

      ```
      public ArticleVO()
      ```

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```

      Recupera o valor do field id

      Returns:
      :   the id
    - #### setId

      ```
      public void setId​(Long id)
      ```

      Setado o valor do field id

      Parameters:
      :   `id` - o id que será setado
    - #### getCategoryId

      ```
      public Long getCategoryId()
      ```

      Recupera o valor do field categoryId

      Returns:
      :   the categoryId
    - #### setCategoryId

      ```
      public void setCategoryId​(Long categoryId)
      ```

      Setado o valor do field categoryId

      Parameters:
      :   `categoryId` - o categoryId que será setado
    - #### getAlias

      ```
      public String getAlias()
      ```

      Recupera o valor do field alias

      Returns:
      :   the alias
    - #### setAlias

      ```
      public void setAlias​(String alias)
      ```

      Setado o valor do field alias

      Parameters:
      :   `alias` - o alias que será setado
    - #### getContent

      ```
      public String getContent()
      ```

      Recupera o valor do field content

      Returns:
      :   the content
    - #### setContent

      ```
      public void setContent​(String content)
      ```

      Setado o valor do field content

      Parameters:
      :   `content` - o content que será setado
    - #### getTopicId

      ```
      public Integer getTopicId()
      ```

      Recupera o valor do field topicId

      Returns:
      :   the topicId
    - #### setTopicId

      ```
      public void setTopicId​(Integer topicId)
      ```

      Setado o valor do field topicId

      Parameters:
      :   `topicId` - o topicId que será setado
    - #### isDraft

      ```
      public boolean isDraft()
      ```

      Recupera o valor do field draft

      Returns:
      :   the draft
    - #### setDraft

      ```
      public void setDraft​(boolean draft)
      ```

      Setado o valor do field draft

      Parameters:
      :   `draft` - o draft que será setado
    - #### getKeyWord

      ```
      public String getKeyWord()
      ```

      Recupera o valor do field keyWord

      Returns:
      :   the keyWord
    - #### setKeyWord

      ```
      public void setKeyWord​(String keyWord)
      ```

      Setado o valor do field keyWord

      Parameters:
      :   `keyWord` - o keyWord que será setado
    - #### isExpires

      ```
      public boolean isExpires()
      ```

      Recupera o valor do field expires

      Returns:
      :   the expires
    - #### setExpires

      ```
      public void setExpires​(boolean expires)
      ```

      Setado o valor do field expires

      Parameters:
      :   `expires` - o expires que será setado
    - #### getDescription

      ```
      public String getDescription()
      ```

      Recupera o valor do field description

      Returns:
      :   the description
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```

      Setado o valor do field description

      Parameters:
      :   `description` - o description que será setado
    - #### getVersion

      ```
      public Integer getVersion()
      ```

      Recupera o valor do field version

      Returns:
      :   the version
    - #### setVersion

      ```
      public void setVersion​(Integer version)
      ```

      Setado o valor do field version

      Parameters:
      :   `version` - o version que será setado
    - #### getPublicationDate

      ```
      public Date getPublicationDate()
      ```

      Recupera o valor do field publicationDate

      Returns:
      :   the publicationDate
    - #### setPublicationDate

      ```
      public void setPublicationDate​(Date publicationDate)
      ```

      Setado o valor do field publicationDate

      Parameters:
      :   `publicationDate` - o publicationDate que será setado
    - #### getExpirationDate

      ```
      public Date getExpirationDate()
      ```

      Recupera o valor do field expirationDate

      Returns:
      :   the expirationDate
    - #### setExpirationDate

      ```
      public void setExpirationDate​(Date expirationDate)
      ```

      Setado o valor do field expirationDate

      Parameters:
      :   `expirationDate` - o expirationDate que será setado
    - #### getPublisherId

      ```
      public String getPublisherId()
      ```

      Recupera o valor do field publisherId

      Returns:
      :   the publisherId
    - #### setPublisherId

      ```
      public void setPublisherId​(String publisherId)
      ```

      Setado o valor do field publisherId

      Parameters:
      :   `publisherId` - o publisherId que será setado
    - #### getAttachments

      ```
      public List<String> getAttachments()
      ```

      Recupera o valor do field attachments

      Returns:
      :   the attachments
    - #### setAttachments

      ```
      public void setAttachments​(List<String> attachments)
      ```

      Setado o valor do field attachments

      Parameters:
      :   `attachments` - o attachments que será setado
    - #### getCovers

      ```
      public Map<String,​String> getCovers()
      ```

      Recupera o valor do field covers

      Returns:
      :   the covers
    - #### setCovers

      ```
      public void setCovers​(Map<String,​String> covers)
      ```

      Setado o valor do field covers

      Parameters:
      :   `covers` - o covers que será setado
    - #### getUser

      ```
      public SocialVO getUser()
      ```

      Recupera o valor do field user

      Returns:
      :   the user
    - #### setUser

      ```
      public void setUser​(SocialVO user)
      ```

      Setado o valor do field user

      Parameters:
      :   `user` - o user que será setado
    - #### getArticleCoverVO

      ```
      public ArticleCoverVO getArticleCoverVO()
      ```

      Recupera o valor do field articleCoverVO

      Returns:
      :   the articleCoverVO
    - #### setArticleCoverVO

      ```
      public void setArticleCoverVO​(ArticleCoverVO articleCoverVO)
      ```

      Setado o valor do field articleCoverVO

      Parameters:
      :   `articleCoverVO` - o articleCoverVO que será setado
    - #### isUserNotify

      ```
      public boolean isUserNotify()
      ```

      Recupera o valor do field userNotify

      Returns:
      :   the userNotify
    - #### setUserNotify

      ```
      public void setUserNotify​(boolean userNotify)
      ```

      Setado o valor do field userNotify

      Parameters:
      :   `userNotify` - o userNotify que será setado
    - #### getSocialObjectId

      ```
      public Long getSocialObjectId()
      ```

      Recupera o valor do field socialObjectId

      Returns:
      :   the socialObjectId
    - #### setSocialObjectId

      ```
      public void setSocialObjectId​(Long socialObjectId)
      ```

      Setado o valor do field socialObjectId

      Parameters:
      :   `socialObjectId` - o socialObjectId que será setado
    - #### getSociable

      ```
      public SociableVO getSociable()
      ```

      Recupera o valor do field sociableVO

      Returns:
      :   the sociableVO
    - #### setSociable

      ```
      public void setSociable​(SociableVO sociable)
      ```

      Setado o valor do field sociableVO

      Parameters:
      :   `sociableVO` - o sociableVO que será setado
    - #### isViewedDocument

      ```
      public boolean isViewedDocument()
      ```

      Recupera valor do campo viewedDocument

      Returns:
      :   usuario viu o artigo
    - #### setViewedDocument

      ```
      public void setViewedDocument​(boolean viewedDocument)
      ```

      Atribui valor do campo viewedDocument

      Parameters:
      :   `viewedDocument` -
    - #### getSecurityLevel

      ```
      public String getSecurityLevel()
      ```

      Recupera valor do campo securityLevel

      Returns:
    - #### setSecurityLevel

      ```
      public void setSecurityLevel​(String securityLevel)
      ```

      Atribui valor do campo securityLevel

      Parameters:
      :   `securityLevel` -
    - #### getAccessCount

      ```
      public Integer getAccessCount()
      ```

      Recupera valor do campo accessCount

      Returns:
    - #### setAccessCount

      ```
      public void setAccessCount​(Integer accessCount)
      ```

      Atribui valor do campo accessCount

      Parameters:
      :   `accessCount` -
    - #### getNumberWatchs

      ```
      public long getNumberWatchs()
      ```

      Recupera valor do campo numberWatchs

      Returns:
    - #### setNumberWatchs

      ```
      public void setNumberWatchs​(long numberWatchs)
      ```

      Atribui valor do campo numberWatchs

      Parameters:
      :   `numberWatchs` -
    - #### isApproved

      ```
      public boolean isApproved()
      ```
    - #### setApproved

      ```
      public void setApproved​(boolean approved)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `Object`
    - #### equals

      ```
      public boolean equals​(Object obj)
      ```

      Overrides:
      :   `equals` in class `Object`
