---
content_hash: 7c418235ff4af1fb88e07bcac3f5a94006c4b831fcc3e486e387f62aa74d1913
fetched_at: '2026-11-03T14:35:06.862692+00:00'
page_id: com/fluig/sdk/service/MentionService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.MentionService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/MentionService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface MentionService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface MentionService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de menções.

  Since:
  :   1.5.13

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `String` | `formatText​(Long objectId, String objectClass, String text, String formatPattern)` | Formats a text with mentions acording to the given pattern. |
    | `String` | `formatText​(String text, String formatPattern)` | Formats a text with mentions acording to the given pattern. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.MentionService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.MentionService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### formatText

      ```
      String formatText​(String text,
                        String formatPattern)
                 throws NamingException
      ```

      Formats a text with mentions acording to the given pattern.
      Type @[alias] in the formatPattern to replace with the mentioned's alias.
      Type @[name] in the formatPattern to replace with the mentioned's name.

      Parameters:
      :   `text` - text with mentions
      :   `formatPattern` - pattern to format the mentions inside the text

      Throws:
      :   `NamingException`
    - #### formatText

      ```
      String formatText​(Long objectId,
                        String objectClass,
                        String text,
                        String formatPattern)
                 throws NamingException
      ```

      Formats a text with mentions acording to the given pattern.
      Type @[alias] in the formatPattern to replace with the mentioned's alias.
      Type @[name] in the formatPattern to replace with the mentioned's name.

      Parameters:
      :   `objectId` - id of the object that has made the mentions
      :   `objectClass` - class of the object that has made the mentions
      :   `text` - text with mentions
      :   `formatPattern` - pattern to format the mentions inside the text

      Throws:
      :   `NamingException`
