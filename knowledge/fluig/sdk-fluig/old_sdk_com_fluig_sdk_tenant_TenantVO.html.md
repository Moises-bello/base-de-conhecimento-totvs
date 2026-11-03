---
content_hash: b908d9acb4fcd8a3d4e7e832c57908c52ac42d1937bde9ce79b1a91d1e556bf3
fetched_at: '2026-11-03T14:35:07.336137+00:00'
page_id: com/fluig/sdk/tenant/TenantVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.tenant.TenantVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/tenant/TenantVO.html
version: 1
---

Package [com.fluig.sdk.tenant](https://api.fluig.com/old/sdk/com/fluig/sdk/tenant/package-summary.html)

## Class TenantVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.tenant.TenantVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class TenantVO
  extends Object
  implements Serializable
  ```

  Value Object para Tenant

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.tenant.TenantVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `TenantVO()` | Nova instância para TenantVO.java |
    | `TenantVO​(Long id, String code)` | Nova instância para TenantVO.java |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `AdminUserVO` | `getAdminUser()` | Recupera valor do adminUser |
    | `String` | `getCode()` | Recupera valor do code |
    | `Map<String,​String>` | `getData()` | Recupera valor do data |
    | `String` | `getDescription()` | Recupera valor do description |
    | `String` | `getFederalId()` | Recupera valor do federalId |
    | `Long` | `getId()` | Recupera valor do id |
    | `String` | `getIdpId()` | Recupera valor do idpId |
    | `Boolean` | `getIdpLogOff()` | Recupera valor do idpLogOff |
    | `String` | `getOrganizationUrl()` | Recupera valor do organizationUrl |
    | `Boolean` | `getRemoveVolume()` | Recupera valor do removeVolume |
    | `Boolean` | `getTenantActive()` | Recupera o valor para tenantActive |
    | `Boolean` | `getThumbnailEnabled()` | Recupera valor do thumbnailEnabled |
    | `String` | `getVolumeDir()` | Recupera valor do volumeDir |
    | `void` | `setAdminUser​(AdminUserVO adminUser)` | Atribui valor para adminUser |
    | `void` | `setCode​(String code)` | Atribui valor para code |
    | `void` | `setData​(Map<String,​String> data)` | Atribui valor para data |
    | `void` | `setDescription​(String description)` | Atribui valor para description |
    | `void` | `setFederalId​(String federalId)` | Atribui valor para federalId |
    | `void` | `setId​(Long id)` | Atribui valor para id |
    | `void` | `setIdpId​(String idpId)` | Atribui valor para idpId |
    | `void` | `setIdpLogOff​(Boolean idpLogOff)` | Atribui valor para idpLogOff |
    | `void` | `setOrganizationUrl​(String organizationUrl)` | Atribui valor para organizationUrl |
    | `void` | `setRemoveVolume​(Boolean removeVolume)` | Atribui valor para removeVolume |
    | `void` | `setTenantActive​(Boolean tenantActive)` | Atribui valor para tenantActive |
    | `void` | `setThumbnailEnabled​(Boolean thumbnailEnabled)` | Atribui valor para thumbnailEnabled |
    | `void` | `setVolumeDir​(String volumeDir)` | Atribui valor para volumeDir |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### TenantVO

      ```
      public TenantVO()
      ```

      Nova instância para TenantVO.java
    - #### TenantVO

      ```
      public TenantVO​(Long id,
                      String code)
      ```

      Nova instância para TenantVO.java

      Parameters:
      :   `id` -
      :   `code` -

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
    - #### getFederalId

      ```
      public String getFederalId()
      ```

      Recupera valor do federalId

      Returns:
      :   the federalId
    - #### setFederalId

      ```
      public void setFederalId​(String federalId)
      ```

      Atribui valor para federalId

      Parameters:
      :   `federalId` - the federalId to set
    - #### getIdpId

      ```
      public String getIdpId()
      ```

      Recupera valor do idpId

      Returns:
      :   the idpId
    - #### setIdpId

      ```
      public void setIdpId​(String idpId)
      ```

      Atribui valor para idpId

      Parameters:
      :   `idpId` - the idpId to set
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
    - #### getOrganizationUrl

      ```
      public String getOrganizationUrl()
      ```

      Recupera valor do organizationUrl

      Returns:
      :   the organizationUrl
    - #### setOrganizationUrl

      ```
      public void setOrganizationUrl​(String organizationUrl)
      ```

      Atribui valor para organizationUrl

      Parameters:
      :   `organizationUrl` - the organizationUrl to set
    - #### getVolumeDir

      ```
      public String getVolumeDir()
      ```

      Recupera valor do volumeDir

      Returns:
      :   the volumeDir
    - #### setVolumeDir

      ```
      public void setVolumeDir​(String volumeDir)
      ```

      Atribui valor para volumeDir

      Parameters:
      :   `volumeDir` - the volumeDir to set
    - #### getIdpLogOff

      ```
      public Boolean getIdpLogOff()
      ```

      Recupera valor do idpLogOff

      Returns:
      :   the idpLogOff
    - #### setIdpLogOff

      ```
      public void setIdpLogOff​(Boolean idpLogOff)
      ```

      Atribui valor para idpLogOff

      Parameters:
      :   `idpLogOff` - the idpLogOff to set
    - #### getThumbnailEnabled

      ```
      public Boolean getThumbnailEnabled()
      ```

      Recupera valor do thumbnailEnabled

      Returns:
      :   the thumbnailEnabled
    - #### setThumbnailEnabled

      ```
      public void setThumbnailEnabled​(Boolean thumbnailEnabled)
      ```

      Atribui valor para thumbnailEnabled

      Parameters:
      :   `thumbnailEnabled` - the thumbnailEnabled to set
    - #### getRemoveVolume

      ```
      public Boolean getRemoveVolume()
      ```

      Recupera valor do removeVolume

      Returns:
      :   the removeVolume
    - #### setRemoveVolume

      ```
      public void setRemoveVolume​(Boolean removeVolume)
      ```

      Atribui valor para removeVolume

      Parameters:
      :   `removeVolume` - the removeVolume to set
    - #### getData

      ```
      public Map<String,​String> getData()
      ```

      Recupera valor do data

      Returns:
      :   the data
    - #### setData

      ```
      public void setData​(Map<String,​String> data)
      ```

      Atribui valor para data

      Parameters:
      :   `data` - the data to set
    - #### getAdminUser

      ```
      public AdminUserVO getAdminUser()
      ```

      Recupera valor do adminUser

      Returns:
      :   the adminUser
    - #### setAdminUser

      ```
      public void setAdminUser​(AdminUserVO adminUser)
      ```

      Atribui valor para adminUser

      Parameters:
      :   `adminUser` - the adminUser to set
    - #### getTenantActive

      ```
      public Boolean getTenantActive()
      ```

      Recupera o valor para tenantActive

      Returns:
      :   the tenantActive
    - #### setTenantActive

      ```
      public void setTenantActive​(Boolean tenantActive)
      ```

      Atribui valor para tenantActive

      Parameters:
      :   `tenantActive` - the tenantActive to set
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`

      See Also:
      :   [`Object.toString()`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")
