---
content_hash: 6bc5f992fde73cbaca88f27ab7128b68f2284dbfe52ef3e99b4dca972ae2bb31
fetched_at: '2026-11-03T14:35:04.970857+00:00'
page_id: com/fluig/sdk/api/social/SocialVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.SocialVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/SocialVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class SocialVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.SocialVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class SocialVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.SocialVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `SocialVO()` | Default constructor. |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object obj)` |  |
    | `String` | `getAlias()` |  |
    | `Date` | `getCreateDate()` |  |
    | `Boolean` | `getCustomPage()` |  |
    | `String` | `getDescription()` |  |
    | `String` | `getEmail()` |  |
    | `Boolean` | `getFavorite()` |  |
    | `String` | `getFullName()` |  |
    | `Long` | `getId()` |  |
    | `Boolean` | `getIsAdmin()` |  |
    | `Boolean` | `getIsCommunityAdmin()` |  |
    | `Boolean` | `getIsModerator()` |  |
    | `String` | `getLastName()` |  |
    | `Date` | `getLastUpdate()` |  |
    | `String` | `getName()` |  |
    | `Integer` | `getNumberFollowers()` |  |
    | `Integer` | `getNumberFollowing()` |  |
    | `Integer` | `getNumberFriends()` |  |
    | `Integer` | `getNumberModerations()` |  |
    | `Integer` | `getNumberParticipations()` |  |
    | `Long` | `getTenantId()` |  |
    | `Map<String,​String>` | `getUserData()` |  |
    | `int` | `hashCode()` |  |
    | `Boolean` | `isApprovalRequired()` |  |
    | `Boolean` | `isHidden()` |  |
    | `Boolean` | `isPrivateContent()` |  |
    | `Boolean` | `isTenantAdmin()` |  |
    | `void` | `setAlias​(String alias)` |  |
    | `void` | `setApprovalRequired​(Boolean approvalRequired)` |  |
    | `void` | `setCreateDate​(Date createDate)` |  |
    | `void` | `setCustomPage​(Boolean customPage)` |  |
    | `void` | `setDescription​(String description)` |  |
    | `void` | `setEmail​(String email)` |  |
    | `void` | `setFavorite​(Boolean favorite)` |  |
    | `void` | `setFullName​(String fullName)` |  |
    | `void` | `setHidden​(Boolean hidden)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setIsAdmin​(Boolean isAdmin)` |  |
    | `void` | `setIsCommunityAdmin​(Boolean isCommunityAdmin)` |  |
    | `void` | `setIsModerator​(Boolean isModerator)` |  |
    | `void` | `setLastName​(String lastName)` |  |
    | `void` | `setLastUpdate​(Date lastUpdate)` |  |
    | `void` | `setName​(String name)` |  |
    | `void` | `setNumberFollowers​(Integer numberFollowers)` |  |
    | `void` | `setNumberFollowing​(Integer numberFollowing)` |  |
    | `void` | `setNumberFriends​(Integer numberFriends)` |  |
    | `void` | `setNumberModerations​(Integer numberModerations)` |  |
    | `void` | `setNumberParticipations​(Integer numberParticipations)` |  |
    | `void` | `setPrivateContent​(Boolean privateContent)` |  |
    | `void` | `setTenantAdmin​(Boolean tenantAdmin)` |  |
    | `void` | `setTenantId​(Long tenantId)` |  |
    | `void` | `setUserData​(Map<String,​String> userData)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### SocialVO

      ```
      public SocialVO()
      ```

      Default constructor.

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getName

      ```
      public String getName()
      ```
    - #### setName

      ```
      public void setName​(String name)
      ```
    - #### getDescription

      ```
      public String getDescription()
      ```
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```
    - #### getAlias

      ```
      public String getAlias()
      ```
    - #### setAlias

      ```
      public void setAlias​(String alias)
      ```
    - #### getNumberFriends

      ```
      public Integer getNumberFriends()
      ```
    - #### setNumberFriends

      ```
      public void setNumberFriends​(Integer numberFriends)
      ```
    - #### getNumberParticipations

      ```
      public Integer getNumberParticipations()
      ```
    - #### setNumberParticipations

      ```
      public void setNumberParticipations​(Integer numberParticipations)
      ```
    - #### getNumberFollowing

      ```
      public Integer getNumberFollowing()
      ```
    - #### setNumberFollowing

      ```
      public void setNumberFollowing​(Integer numberFollowing)
      ```
    - #### getNumberFollowers

      ```
      public Integer getNumberFollowers()
      ```
    - #### setNumberFollowers

      ```
      public void setNumberFollowers​(Integer numberFollowers)
      ```
    - #### getNumberModerations

      ```
      public Integer getNumberModerations()
      ```

      Returns:
      :   the numberModerations
    - #### setNumberModerations

      ```
      public void setNumberModerations​(Integer numberModerations)
      ```

      Parameters:
      :   `numberModerations` - the numberModerations to set
    - #### isHidden

      ```
      public Boolean isHidden()
      ```

      Returns:
      :   the hidden
    - #### setHidden

      ```
      public void setHidden​(Boolean hidden)
      ```

      Parameters:
      :   `hidden` - the hidden to set
    - #### isPrivateContent

      ```
      public Boolean isPrivateContent()
      ```

      Returns:
      :   the privateContent
    - #### setPrivateContent

      ```
      public void setPrivateContent​(Boolean privateContent)
      ```

      Parameters:
      :   `privateContent` - the privateContent to set
    - #### isApprovalRequired

      ```
      public Boolean isApprovalRequired()
      ```

      Returns:
      :   the approvalRequired
    - #### setApprovalRequired

      ```
      public void setApprovalRequired​(Boolean approvalRequired)
      ```

      Parameters:
      :   `approvalRequired` - the approvalRequired to set
    - #### getIsModerator

      ```
      public Boolean getIsModerator()
      ```
    - #### setIsModerator

      ```
      public void setIsModerator​(Boolean isModerator)
      ```
    - #### getIsAdmin

      ```
      public Boolean getIsAdmin()
      ```
    - #### setIsAdmin

      ```
      public void setIsAdmin​(Boolean isAdmin)
      ```
    - #### getIsCommunityAdmin

      ```
      public Boolean getIsCommunityAdmin()
      ```
    - #### setIsCommunityAdmin

      ```
      public void setIsCommunityAdmin​(Boolean isCommunityAdmin)
      ```
    - #### setTenantId

      ```
      public void setTenantId​(Long tenantId)
      ```
    - #### getTenantId

      ```
      public Long getTenantId()
      ```
    - #### getLastUpdate

      ```
      public Date getLastUpdate()
      ```
    - #### setLastUpdate

      ```
      public void setLastUpdate​(Date lastUpdate)
      ```
    - #### getCreateDate

      ```
      public Date getCreateDate()
      ```

      Returns:
      :   the createDate
    - #### setCreateDate

      ```
      public void setCreateDate​(Date createDate)
      ```

      Parameters:
      :   `createDate` - the createDate to set
    - #### getCustomPage

      ```
      public Boolean getCustomPage()
      ```
    - #### setCustomPage

      ```
      public void setCustomPage​(Boolean customPage)
      ```
    - #### getFavorite

      ```
      public Boolean getFavorite()
      ```
    - #### setFavorite

      ```
      public void setFavorite​(Boolean favorite)
      ```
    - #### isTenantAdmin

      ```
      public Boolean isTenantAdmin()
      ```
    - #### setTenantAdmin

      ```
      public void setTenantAdmin​(Boolean tenantAdmin)
      ```
    - #### getUserData

      ```
      public Map<String,​String> getUserData()
      ```
    - #### setUserData

      ```
      public void setUserData​(Map<String,​String> userData)
      ```
    - #### getEmail

      ```
      public String getEmail()
      ```
    - #### setEmail

      ```
      public void setEmail​(String email)
      ```
    - #### getLastName

      ```
      public String getLastName()
      ```
    - #### getFullName

      ```
      public String getFullName()
      ```
    - #### setLastName

      ```
      public void setLastName​(String lastName)
      ```
    - #### setFullName

      ```
      public void setFullName​(String fullName)
      ```
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
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
