---
content_hash: 73d77bc5a621dac2d8fee40bc9db2c60f07728c03d8a89e21404fefd807fc473
fetched_at: '2026-11-03T14:35:04.031725+00:00'
page_id: com/fluig/sdk/api/document/DocumentSecurityVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.DocumentSecurityVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/DocumentSecurityVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class DocumentSecurityVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.DocumentSecurityVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DocumentSecurityVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.DocumentSecurityVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DocumentSecurityVO()` |  |
    | `DocumentSecurityVO​(Long companyId, String userCode, Integer documentId, List<DocumentSecurityConfigVO> documentSecurityConfigVOs)` |  |
    | `DocumentSecurityVO​(Long companyId, List<DocumentPermissionVO> documentPermissionVO, List<DocumentApproverVO> documentApproverVO)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<DocumentApproverVO>` | `getDocumentApproverVO()` |  |
    | `List<DocumentPermissionVO>` | `getDocumentPermissionVO()` |  |
    | `List<DocumentSecurityConfigVO>` | `getDocumentSecurityConfigVOs()` |  |
    | `void` | `setDocumentApproverVO​(List<DocumentApproverVO> documentApproverVO)` |  |
    | `void` | `setDocumentPermissionVO​(List<DocumentPermissionVO> documentPermissionVO)` |  |
    | `void` | `setDocumentSecurityConfigVOs​(List<DocumentSecurityConfigVO> documentSecurityConfigVOs)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DocumentSecurityVO

      ```
      public DocumentSecurityVO()
      ```
    - #### DocumentSecurityVO

      ```
      public DocumentSecurityVO​(Long companyId,
                                String userCode,
                                Integer documentId,
                                List<DocumentSecurityConfigVO> documentSecurityConfigVOs)
      ```
    - #### DocumentSecurityVO

      ```
      public DocumentSecurityVO​(Long companyId,
                                List<DocumentPermissionVO> documentPermissionVO,
                                List<DocumentApproverVO> documentApproverVO)
      ```

  + ### Method Detail

    - #### getDocumentSecurityConfigVOs

      ```
      public List<DocumentSecurityConfigVO> getDocumentSecurityConfigVOs()
      ```
    - #### setDocumentSecurityConfigVOs

      ```
      public void setDocumentSecurityConfigVOs​(List<DocumentSecurityConfigVO> documentSecurityConfigVOs)
      ```
    - #### getDocumentPermissionVO

      ```
      public List<DocumentPermissionVO> getDocumentPermissionVO()
      ```
    - #### setDocumentPermissionVO

      ```
      public void setDocumentPermissionVO​(List<DocumentPermissionVO> documentPermissionVO)
      ```
    - #### getDocumentApproverVO

      ```
      public List<DocumentApproverVO> getDocumentApproverVO()
      ```
    - #### setDocumentApproverVO

      ```
      public void setDocumentApproverVO​(List<DocumentApproverVO> documentApproverVO)
      ```
