---
content_hash: b5e29dd17817c3a9283c5afbd90b763d92d8b9281d0bf16c4bb8f80497af809d
fetched_at: '2026-11-03T14:35:04.631242+00:00'
page_id: com/fluig/sdk/api/permission/PermissionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.permission.PermissionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/permission/PermissionVO.html
version: 1
---

Package [com.fluig.sdk.api.permission](https://api.fluig.com/old/sdk/com/fluig/sdk/api/permission/package-summary.html)

## Class PermissionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.permission.PermissionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class PermissionVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.permission.PermissionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `PermissionVO()` |  |
    | `PermissionVO​(String permission, String permissionDescription, Boolean isSelected)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getCategory()` |  |
    | `String` | `getCategoryCode()` |  |
    | `Boolean` | `getIsSelected()` |  |
    | `String` | `getPermission()` |  |
    | `String` | `getPermissionDescription()` |  |
    | `void` | `setCategory​(String category)` |  |
    | `void` | `setCategoryCode​(String categoryCode)` |  |
    | `void` | `setIsSelected​(Boolean isSelected)` |  |
    | `void` | `setPermission​(String permission)` |  |
    | `void` | `setPermissionDescription​(String permissionDescription)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### PermissionVO

      ```
      public PermissionVO​(String permission,
                          String permissionDescription,
                          Boolean isSelected)
      ```
    - #### PermissionVO

      ```
      public PermissionVO()
      ```

  + ### Method Detail

    - #### getPermission

      ```
      public String getPermission()
      ```
    - #### setPermission

      ```
      public void setPermission​(String permission)
      ```
    - #### getPermissionDescription

      ```
      public String getPermissionDescription()
      ```
    - #### setPermissionDescription

      ```
      public void setPermissionDescription​(String permissionDescription)
      ```
    - #### getIsSelected

      ```
      public Boolean getIsSelected()
      ```
    - #### setIsSelected

      ```
      public void setIsSelected​(Boolean isSelected)
      ```
    - #### getCategory

      ```
      public String getCategory()
      ```
    - #### setCategory

      ```
      public void setCategory​(String category)
      ```
    - #### getCategoryCode

      ```
      public String getCategoryCode()
      ```
    - #### setCategoryCode

      ```
      public void setCategoryCode​(String categoryCode)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
