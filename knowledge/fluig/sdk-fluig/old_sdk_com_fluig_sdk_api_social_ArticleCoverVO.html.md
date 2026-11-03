---
content_hash: ed835512c2f4fb23d17259625acac0f78c79d455d190a57c73a26162defa553e
fetched_at: '2026-11-03T14:35:04.702746+00:00'
page_id: com/fluig/sdk/api/social/ArticleCoverVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.social.ArticleCoverVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleCoverVO.html
version: 1
---

Package [com.fluig.sdk.api.social](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/package-summary.html)

## Class ArticleCoverVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.social.ArticleCoverVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ArticleCoverVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.social.ArticleCoverVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ArticleCoverVO()` |  |
    | `ArticleCoverVO​(byte[] image, int width, int height, int x, int y)` |  |
    | `ArticleCoverVO​(String pictureName, byte[] image)` |  |
    | `ArticleCoverVO​(String pictureName, byte[] image, int width, int height)` |  |
    | `ArticleCoverVO​(String pictureName, byte[] image, int width, int height, int x, int y)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `void` | `convertMediaData()` |  |
    | `String` | `getBase64media()` |  |
    | `CropVO` | `getBoxData()` |  |
    | `CropVO` | `getCanvasData()` |  |
    | `int` | `getCoordinateX()` |  |
    | `int` | `getCoordinateY()` |  |
    | `int` | `getHeight()` |  |
    | `byte[]` | `getImage()` |  |
    | `String` | `getPath()` |  |
    | `String` | `getPictureId()` |  |
    | `String` | `getPictureName()` |  |
    | `int` | `getWidth()` |  |
    | `int` | `getWindowHeight()` | Recupera o valor do field windowHeight |
    | `int` | `getWindowWidth()` | Recupera o valor do field windowWidth |
    | `void` | `setBase64media​(String base64media)` |  |
    | `void` | `setBoxData​(CropVO boxData)` |  |
    | `void` | `setCanvasData​(CropVO canvasData)` |  |
    | `void` | `setCoordinateX​(int coordinateX)` |  |
    | `void` | `setCoordinateY​(int coordinateY)` |  |
    | `void` | `setHeight​(int height)` |  |
    | `void` | `setImage​(byte[] image)` |  |
    | `void` | `setPath​(String path)` |  |
    | `void` | `setPictureId​(String pictureId)` |  |
    | `void` | `setPictureName​(String pictureName)` |  |
    | `void` | `setWidth​(int width)` |  |
    | `void` | `setWindowHeight​(int windowHeight)` | Setado o valor do field windowHeight |
    | `void` | `setWindowWidth​(int windowWidth)` | Setado o valor do field windowWidth |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### ArticleCoverVO

      ```
      public ArticleCoverVO()
      ```
    - #### ArticleCoverVO

      ```
      public ArticleCoverVO​(String pictureName,
                            byte[] image,
                            int width,
                            int height)
      ```
    - #### ArticleCoverVO

      ```
      public ArticleCoverVO​(String pictureName,
                            byte[] image)
      ```
    - #### ArticleCoverVO

      ```
      public ArticleCoverVO​(String pictureName,
                            byte[] image,
                            int width,
                            int height,
                            int x,
                            int y)
      ```
    - #### ArticleCoverVO

      ```
      public ArticleCoverVO​(byte[] image,
                            int width,
                            int height,
                            int x,
                            int y)
      ```

  + ### Method Detail

    - #### getPath

      ```
      public String getPath()
      ```
    - #### setPath

      ```
      public void setPath​(String path)
      ```
    - #### getPictureName

      ```
      public String getPictureName()
      ```
    - #### setPictureName

      ```
      public void setPictureName​(String pictureName)
      ```
    - #### getImage

      ```
      public byte[] getImage()
      ```
    - #### setImage

      ```
      public void setImage​(byte[] image)
      ```
    - #### getCoordinateX

      ```
      public int getCoordinateX()
      ```
    - #### setCoordinateX

      ```
      public void setCoordinateX​(int coordinateX)
      ```
    - #### getCoordinateY

      ```
      public int getCoordinateY()
      ```
    - #### setCoordinateY

      ```
      public void setCoordinateY​(int coordinateY)
      ```
    - #### getWidth

      ```
      public int getWidth()
      ```
    - #### setWidth

      ```
      public void setWidth​(int width)
      ```
    - #### getHeight

      ```
      public int getHeight()
      ```
    - #### setHeight

      ```
      public void setHeight​(int height)
      ```
    - #### getBase64media

      ```
      public String getBase64media()
      ```
    - #### setBase64media

      ```
      public void setBase64media​(String base64media)
      ```
    - #### convertMediaData

      ```
      public void convertMediaData()
      ```
    - #### getCanvasData

      ```
      public CropVO getCanvasData()
      ```
    - #### setCanvasData

      ```
      public void setCanvasData​(CropVO canvasData)
      ```
    - #### getBoxData

      ```
      public CropVO getBoxData()
      ```
    - #### setBoxData

      ```
      public void setBoxData​(CropVO boxData)
      ```
    - #### getPictureId

      ```
      public String getPictureId()
      ```
    - #### setPictureId

      ```
      public void setPictureId​(String pictureId)
      ```
    - #### getWindowHeight

      ```
      public int getWindowHeight()
      ```

      Recupera o valor do field windowHeight

      Returns:
      :   the windowHeight
    - #### setWindowHeight

      ```
      public void setWindowHeight​(int windowHeight)
      ```

      Setado o valor do field windowHeight

      Parameters:
      :   `windowHeight` - o windowHeight que será setado
    - #### getWindowWidth

      ```
      public int getWindowWidth()
      ```

      Recupera o valor do field windowWidth

      Returns:
      :   the windowWidth
    - #### setWindowWidth

      ```
      public void setWindowWidth​(int windowWidth)
      ```

      Setado o valor do field windowWidth

      Parameters:
      :   `windowWidth` - o windowWidth que será setado
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
