---
content_hash: 2740e3617f86c3258621481fc417c78bb7c456763aea0aac8aedfd9784d59548
fetched_at: '2026-11-03T14:35:03.573924+00:00'
page_id: com/fluig/sdk/api/alert/AlertConfigVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.alert.AlertConfigVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/AlertConfigVO.html
version: 1
---

Package [com.fluig.sdk.api.alert](https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/package-summary.html)

## Class AlertConfigVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.alert.AlertConfigVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AlertConfigVO
  extends Object
  implements Serializable
  ```

  Vo que representa a configuração de recebimento de um evento de alerta.

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.alert.AlertConfigVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AlertConfigVO()` |  |
    | `AlertConfigVO​(String login, String eventKey, String applicationKey, String wantReceive)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getApplicationKey()` |  |
    | `String` | `getEventKey()` |  |
    | `String` | `getLogin()` |  |
    | `String` | `getWantReceive()` |  |
    | `void` | `setApplicationKey​(String applicationKey)` |  |
    | `void` | `setEventKey​(String eventKey)` |  |
    | `void` | `setLogin​(String login)` |  |
    | `void` | `setWantReceive​(String wantReceive)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AlertConfigVO

      ```
      public AlertConfigVO()
      ```
    - #### AlertConfigVO

      ```
      public AlertConfigVO​(String login,
                           String eventKey,
                           String applicationKey,
                           String wantReceive)
      ```

  + ### Method Detail

    - #### getLogin

      ```
      public String getLogin()
      ```
    - #### setLogin

      ```
      public void setLogin​(String login)
      ```
    - #### getEventKey

      ```
      public String getEventKey()
      ```
    - #### setEventKey

      ```
      public void setEventKey​(String eventKey)
      ```
    - #### getApplicationKey

      ```
      public String getApplicationKey()
      ```
    - #### setApplicationKey

      ```
      public void setApplicationKey​(String applicationKey)
      ```
    - #### getWantReceive

      ```
      public String getWantReceive()
      ```
    - #### setWantReceive

      ```
      public void setWantReceive​(String wantReceive)
      ```
