---
content_hash: ad574ad776609208d73583f34bec0ced9be10a46d19bd7c0f19ac859e33dcd7b
fetched_at: '2026-11-03T14:35:04.790330+00:00'
page_id: com/fluig/sdk/api/social/CommentVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.CommentVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/CommentVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class CommentVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.CommentVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CommentVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.CommentVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CommentVO()` |  |
    | `CommentVO​(Long sociableId, Long sociableParentId, String comment, Date creationDate, Date updateDate, String commentWithoutMention, boolean mention, Map<String,​String> mentions, Map<String,​String> customData, String userName, String userAlias)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object obj)` |  |
    | `String` | `getComment()` |  |
    | `String` | `getCommentWithoutMention()` |  |
    | `Date` | `getCreationDate()` |  |
    | `Map<String,​String>` | `getCustomData()` |  |
    | `Map<String,​String>` | `getMentions()` |  |
    | `Long` | `getSociableId()` |  |
    | `Long` | `getSociableParentId()` |  |
    | `Date` | `getUpdateDate()` |  |
    | `String` | `getUserAlias()` |  |
    | `String` | `getUserName()` |  |
    | `int` | `hashCode()` |  |
    | `boolean` | `isMention()` |  |
    | `void` | `setComment​(String comment)` |  |
    | `void` | `setCommentWithoutMention​(String commentWithoutMention)` |  |
    | `void` | `setCreationDate​(Date creationDate)` |  |
    | `void` | `setCustomData​(Map<String,​String> customData)` |  |
    | `void` | `setMention​(boolean mention)` |  |
    | `void` | `setMentions​(Map<String,​String> mentions)` |  |
    | `void` | `setSociableId​(Long sociableId)` |  |
    | `void` | `setSociableParentId​(Long sociableParentId)` |  |
    | `void` | `setUpdateDate​(Date updateDate)` |  |
    | `void` | `setUserAlias​(String userAlias)` |  |
    | `void` | `setUserName​(String userName)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### CommentVO

      ```
      public CommentVO()
      ```
    - #### CommentVO

      ```
      public CommentVO​(Long sociableId,
                       Long sociableParentId,
                       String comment,
                       Date creationDate,
                       Date updateDate,
                       String commentWithoutMention,
                       boolean mention,
                       Map<String,​String> mentions,
                       Map<String,​String> customData,
                       String userName,
                       String userAlias)
      ```

  + ### Method Detail

    - #### getSociableId

      ```
      public Long getSociableId()
      ```
    - #### setSociableId

      ```
      public void setSociableId​(Long sociableId)
      ```
    - #### getComment

      ```
      public String getComment()
      ```
    - #### setComment

      ```
      public void setComment​(String comment)
      ```
    - #### getCreationDate

      ```
      public Date getCreationDate()
      ```
    - #### setCreationDate

      ```
      public void setCreationDate​(Date creationDate)
      ```
    - #### getUpdateDate

      ```
      public Date getUpdateDate()
      ```
    - #### setUpdateDate

      ```
      public void setUpdateDate​(Date updateDate)
      ```
    - #### getCommentWithoutMention

      ```
      public String getCommentWithoutMention()
      ```
    - #### setCommentWithoutMention

      ```
      public void setCommentWithoutMention​(String commentWithoutMention)
      ```
    - #### isMention

      ```
      public boolean isMention()
      ```
    - #### setMention

      ```
      public void setMention​(boolean mention)
      ```
    - #### getMentions

      ```
      public Map<String,​String> getMentions()
      ```
    - #### setMentions

      ```
      public void setMentions​(Map<String,​String> mentions)
      ```
    - #### getCustomData

      ```
      public Map<String,​String> getCustomData()
      ```
    - #### setCustomData

      ```
      public void setCustomData​(Map<String,​String> customData)
      ```
    - #### getUserName

      ```
      public String getUserName()
      ```
    - #### setUserName

      ```
      public void setUserName​(String userName)
      ```
    - #### getUserAlias

      ```
      public String getUserAlias()
      ```
    - #### setUserAlias

      ```
      public void setUserAlias​(String userAlias)
      ```
    - #### getSociableParentId

      ```
      public Long getSociableParentId()
      ```
    - #### setSociableParentId

      ```
      public void setSociableParentId​(Long sociableParentId)
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
