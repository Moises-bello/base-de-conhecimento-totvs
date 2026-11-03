---
content_hash: e797fc1dc61c703044f74433585aa93eb0ac69c638312336de45032291fe4905
fetched_at: '2026-11-03T14:35:07.422457+00:00'
page_id: com/fluig/sdk/user/UserVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.user.UserVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/user/UserVO.html
version: 1
---

Package [com.fluig.sdk.user](https://api.fluig.com/old/sdk/com/fluig/sdk/user/package-summary.html)

## Class UserVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.user.UserVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class UserVO
  extends Object
  implements Serializable
  ```

  Value Object para usuário

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.user.UserVO)

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `protected static String` | `EXTATTR_birthDay` | Constante birthDay String - EXTATTR\_birthDay |
    | `protected static String` | `EXTATTR_consumerKey` | Constante consumerKey String - EXTATTR\_consumerKey |
    | `protected static String` | `EXTATTR_firstAccess` | Constante firstAccess String - EXTATTR\_firstAccess |
    | `protected static String` | `EXTATTR_groups` | Constante groups String - EXTATTR\_groups |
    | `protected static String` | `EXTATTR_idpId` | Constante idpId String - EXTATTR\_idpId |
    | `protected static String` | `EXTATTR_locationId` | Constante locationid String - EXTATTR\_locationId |
    | `protected static String` | `EXTATTR_passwordType` | Constante passwordType String - EXTATTR\_passwordType |
    | `protected static String` | `EXTATTR_roles` | Constante roles String - EXTATTR\_roles |
    | `protected static String` | `EXTATTR_tenantCode` | Constante tenantCode String - EXTATTR\_tenantCode |
    | `protected static String` | `EXTATTR_tenantId` | Constante tenantId String - EXTATTR\_tenantId |
    | `protected static String` | `EXTATTR_userType` | Constante userType String - EXTATTR\_userType |

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `UserVO()` | Construtor default. |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `void` | `addExtData​(String key, Object value)` | Adicionar chave e valor no mapa. |
    | `String` | `getCode()` | Recupera valor do code |
    | `String` | `getEmail()` | Recupera valor do email |
    | `HashMap<String,​Object>` | `getExtData()` | Recupera mapa de extraData |
    | `Object` | `getExtraData​(String key)` | Recupera valor do extData |
    | `String` | `getFirstName()` | Recupera valor do firstName |
    | `String` | `getFullName()` | Recupera valor do fullName |
    | `List<String>` | `getGroups()` |  |
    | `Long` | `getId()` | Recupera valor do id |
    | `Boolean` | `getIsActive()` | Return user status |
    | `String` | `getLastName()` | Recupera valor do lastName |
    | `String` | `getLogin()` | Recupera valor do login |
    | `String` | `getPassword()` | Recupera valor do password |
    | `List<String>` | `getRoles()` |  |
    | `String` | `getTimezone()` | Atribui valor ao timezone |
    | `String` | `getTokenAccess()` | Retorna tokenAccess |
    | `String` | `getTokenSecret()` | Retorna token secret |
    | `String` | `getUserUUID()` | Recupera valor do userUUID |
    | `Object` | `getValueExtData​(String key)` | Retorna objeto no mapa |
    | `void` | `setCode​(String code)` | Atribui valor para code |
    | `void` | `setEmail​(String email)` | Atribui valor para email |
    | `void` | `setExtData​(HashMap<String,​Object> extData)` | Atribui valor ao map |
    | `void` | `setExtraData​(String key, Object value)` | Atribui valor para extData |
    | `void` | `setFirstName​(String firstName)` | Atribui valor para firstName |
    | `void` | `setFullName​(String fullName)` | Atribui valor para fullName |
    | `void` | `setGroups​(List<String> groups)` |  |
    | `void` | `setId​(Long id)` | Atribui valor para id |
    | `void` | `setIsActive​(Boolean isActive)` | Set user status |
    | `void` | `setLastName​(String lastName)` | Atribui valor para lastName |
    | `void` | `setLogin​(String login)` | Atribui valor para login |
    | `void` | `setPassword​(String password)` | Atribui valor para password |
    | `void` | `setRoles​(List<String> roles)` |  |
    | `void` | `setTimezone​(String timezone)` | Retorna o timezone |
    | `void` | `setTokenAccess​(String token)` | Atribui valor ao tokenAccess |
    | `void` | `setTokenSecret​(String tokenSecret)` | Atribui valor ao token secret |
    | `void` | `setUserUUID​(String userUUID)` | Atribui valor para userUUID |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Field Detail

    - #### EXTATTR\_idpId

      ```
      protected static final String EXTATTR_idpId
      ```

      Constante idpId
      String - EXTATTR\_idpId

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_idpId)
    - #### EXTATTR\_birthDay

      ```
      protected static final String EXTATTR_birthDay
      ```

      Constante birthDay
      String - EXTATTR\_birthDay

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_birthDay)
    - #### EXTATTR\_firstAccess

      ```
      protected static final String EXTATTR_firstAccess
      ```

      Constante firstAccess
      String - EXTATTR\_firstAccess

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_firstAccess)
    - #### EXTATTR\_roles

      ```
      protected static final String EXTATTR_roles
      ```

      Constante roles
      String - EXTATTR\_roles

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_roles)
    - #### EXTATTR\_groups

      ```
      protected static final String EXTATTR_groups
      ```

      Constante groups
      String - EXTATTR\_groups

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_groups)
    - #### EXTATTR\_locationId

      ```
      protected static final String EXTATTR_locationId
      ```

      Constante locationid
      String - EXTATTR\_locationId

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_locationId)
    - #### EXTATTR\_tenantCode

      ```
      protected static final String EXTATTR_tenantCode
      ```

      Constante tenantCode
      String - EXTATTR\_tenantCode

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_tenantCode)
    - #### EXTATTR\_tenantId

      ```
      protected static final String EXTATTR_tenantId
      ```

      Constante tenantId
      String - EXTATTR\_tenantId

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_tenantId)
    - #### EXTATTR\_userType

      ```
      protected static final String EXTATTR_userType
      ```

      Constante userType
      String - EXTATTR\_userType

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_userType)
    - #### EXTATTR\_passwordType

      ```
      protected static final String EXTATTR_passwordType
      ```

      Constante passwordType
      String - EXTATTR\_passwordType

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_passwordType)
    - #### EXTATTR\_consumerKey

      ```
      protected static final String EXTATTR_consumerKey
      ```

      Constante consumerKey
      String - EXTATTR\_consumerKey

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.user.UserVO.EXTATTR_consumerKey)

  + ### Constructor Detail

    - #### UserVO

      ```
      public UserVO()
      ```

      Construtor default.

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
    - #### getUserUUID

      ```
      public String getUserUUID()
      ```

      Recupera valor do userUUID

      Returns:
      :   the userUUID
    - #### setUserUUID

      ```
      public void setUserUUID​(String userUUID)
      ```

      Atribui valor para userUUID

      Parameters:
      :   `id` - the userUUID to set
    - #### getLogin

      ```
      public String getLogin()
      ```

      Recupera valor do login

      Returns:
      :   the login
    - #### setLogin

      ```
      public void setLogin​(String login)
      ```

      Atribui valor para login

      Parameters:
      :   `login` - the login to set
    - #### getEmail

      ```
      public String getEmail()
      ```

      Recupera valor do email

      Returns:
      :   the email
    - #### setEmail

      ```
      public void setEmail​(String email)
      ```

      Atribui valor para email

      Parameters:
      :   `email` - the email to set
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
    - #### getFirstName

      ```
      public String getFirstName()
      ```

      Recupera valor do firstName

      Returns:
      :   the firstName
    - #### setFirstName

      ```
      public void setFirstName​(String firstName)
      ```

      Atribui valor para firstName

      Parameters:
      :   `firstName` - the firstName to set
    - #### getLastName

      ```
      public String getLastName()
      ```

      Recupera valor do lastName

      Returns:
      :   the lastName
    - #### setLastName

      ```
      public void setLastName​(String lastName)
      ```

      Atribui valor para lastName

      Parameters:
      :   `lastName` - the lastName to set
    - #### getFullName

      ```
      public String getFullName()
      ```

      Recupera valor do fullName

      Returns:
      :   the fullName
    - #### setFullName

      ```
      public void setFullName​(String fullName)
      ```

      Atribui valor para fullName

      Parameters:
      :   `fullName` - the fullName to set
    - #### getPassword

      ```
      public String getPassword()
      ```

      Recupera valor do password

      Returns:
      :   the password
    - #### setPassword

      ```
      public void setPassword​(String password)
      ```

      Atribui valor para password

      Parameters:
      :   `password` - the password to set
    - #### getExtraData

      ```
      public Object getExtraData​(String key)
      ```

      Recupera valor do extData

      Returns:
      :   Object
    - #### addExtData

      ```
      public void addExtData​(String key,
                             Object value)
      ```

      Adicionar chave e valor no mapa.

      Parameters:
      :   `key` -
      :   `value` -
    - #### getValueExtData

      ```
      public Object getValueExtData​(String key)
      ```

      Retorna objeto no mapa

      Parameters:
      :   `key` -

      Returns:
      :   Object
    - #### setExtraData

      ```
      public void setExtraData​(String key,
                               Object value)
      ```

      Atribui valor para extData

      Parameters:
      :   `key` -
      :   `value` -
    - #### getExtData

      ```
      public HashMap<String,​Object> getExtData()
      ```

      Recupera mapa de extraData

      Returns:
      :   HashMap
    - #### setExtData

      ```
      public void setExtData​(HashMap<String,​Object> extData)
      ```

      Atribui valor ao map

      Parameters:
      :   `extData` -
    - #### getTokenAccess

      ```
      public String getTokenAccess()
      ```

      Retorna tokenAccess

      Returns:
      :   String
    - #### setTokenAccess

      ```
      public void setTokenAccess​(String token)
      ```

      Atribui valor ao tokenAccess

      Parameters:
      :   `token` -
    - #### getTokenSecret

      ```
      public String getTokenSecret()
      ```

      Retorna token secret

      Returns:
      :   String
    - #### setTokenSecret

      ```
      public void setTokenSecret​(String tokenSecret)
      ```

      Atribui valor ao token secret

      Parameters:
      :   `tokenSecret` -
    - #### getTimezone

      ```
      public String getTimezone()
      ```

      Atribui valor ao timezone

      Returns:
      :   timezone
    - #### setTimezone

      ```
      public void setTimezone​(String timezone)
      ```

      Retorna o timezone

      Parameters:
      :   `timezone` -
    - #### getRoles

      ```
      public List<String> getRoles()
      ```
    - #### setRoles

      ```
      public void setRoles​(List<String> roles)
      ```
    - #### getGroups

      ```
      public List<String> getGroups()
      ```
    - #### setGroups

      ```
      public void setGroups​(List<String> groups)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
    - #### getIsActive

      ```
      public Boolean getIsActive()
      ```

      Return user status

      Returns:
      :   Boolean
    - #### setIsActive

      ```
      public void setIsActive​(Boolean isActive)
      ```

      Set user status

      Parameters:
      :   `isActive` -
