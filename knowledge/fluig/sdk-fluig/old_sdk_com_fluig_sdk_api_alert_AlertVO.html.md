---
content_hash: c70d2e13c6d0711017bb8de08463def44c9b5eaa968a3f8eb123e16ee499d9d6
fetched_at: '2026-11-03T14:35:03.695856+00:00'
page_id: com/fluig/sdk/api/alert/AlertVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.alert.AlertVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/AlertVO.html
version: 1
---

Package [com.fluig.sdk.api.alert](https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/package-summary.html)

## Class AlertVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.alert.AlertVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AlertVO
  extends Object
  implements Serializable
  ```

  Author:
  :   luis.junior

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.alert.AlertVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AlertVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<AlertActionVO>` | `getActions()` |  |
    | `Boolean` | `getCanRemove()` |  |
    | `Date` | `getCreationDate()` |  |
    | `Long` | `getCreationDateTime()` |  |
    | `Date` | `getCurrentDate()` |  |
    | `AlertEventVO` | `getEvent()` |  |
    | `Long` | `getId()` |  |
    | `AlertObjectVO` | `getObject()` |  |
    | `AlertObjectVO` | `getPlace()` |  |
    | `String` | `getPriority()` |  |
    | `Boolean` | `getRead()` |  |
    | `AlertUserVO` | `getReceiver()` |  |
    | `List<AlertSenderVO>` | `getSenders()` |  |
    | `void` | `setActions​(List<AlertActionVO> actions)` |  |
    | `void` | `setCanRemove​(Boolean canRemove)` |  |
    | `void` | `setCreationDate​(Date creationDate)` |  |
    | `void` | `setCreationDateTime​(Long creationDateTime)` |  |
    | `void` | `setCurrentDate​(Date currentDate)` |  |
    | `void` | `setEvent​(AlertEventVO event)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setObject​(AlertObjectVO object)` |  |
    | `void` | `setPlace​(AlertObjectVO place)` |  |
    | `void` | `setPriority​(String priority)` |  |
    | `void` | `setRead​(Boolean read)` |  |
    | `void` | `setReceiver​(AlertUserVO receiver)` |  |
    | `void` | `setSenders​(List<AlertSenderVO> senders)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AlertVO

      ```
      public AlertVO()
      ```

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getSenders

      ```
      public List<AlertSenderVO> getSenders()
      ```
    - #### setSenders

      ```
      public void setSenders​(List<AlertSenderVO> senders)
      ```
    - #### getReceiver

      ```
      public AlertUserVO getReceiver()
      ```
    - #### setReceiver

      ```
      public void setReceiver​(AlertUserVO receiver)
      ```
    - #### getEvent

      ```
      public AlertEventVO getEvent()
      ```
    - #### setEvent

      ```
      public void setEvent​(AlertEventVO event)
      ```
    - #### getObject

      ```
      public AlertObjectVO getObject()
      ```
    - #### setObject

      ```
      public void setObject​(AlertObjectVO object)
      ```
    - #### getPlace

      ```
      public AlertObjectVO getPlace()
      ```
    - #### setPlace

      ```
      public void setPlace​(AlertObjectVO place)
      ```
    - #### getRead

      ```
      public Boolean getRead()
      ```
    - #### setRead

      ```
      public void setRead​(Boolean read)
      ```
    - #### getCreationDate

      ```
      public Date getCreationDate()
      ```
    - #### setCreationDate

      ```
      public void setCreationDate​(Date creationDate)
      ```
    - #### getActions

      ```
      public List<AlertActionVO> getActions()
      ```
    - #### setActions

      ```
      public void setActions​(List<AlertActionVO> actions)
      ```
    - #### getCurrentDate

      ```
      public Date getCurrentDate()
      ```
    - #### setCurrentDate

      ```
      public void setCurrentDate​(Date currentDate)
      ```
    - #### getCanRemove

      ```
      public Boolean getCanRemove()
      ```
    - #### setCanRemove

      ```
      public void setCanRemove​(Boolean canRemove)
      ```
    - #### getPriority

      ```
      public String getPriority()
      ```
    - #### setPriority

      ```
      public void setPriority​(String priority)
      ```
    - #### getCreationDateTime

      ```
      public Long getCreationDateTime()
      ```
    - #### setCreationDateTime

      ```
      public void setCreationDateTime​(Long creationDateTime)
      ```
