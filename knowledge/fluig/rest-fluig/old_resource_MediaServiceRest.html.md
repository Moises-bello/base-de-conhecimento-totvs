---
content_hash: baeed973bc4cb0737a121004101ff227df6d86cfae9ad987451e22a1329c64d9
fetched_at: '2026-11-03T14:34:39.972630+00:00'
page_id: resource_MediaServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — MediaServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_MediaServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# MediaServiceRest Resource

Media

### POST /social/community/gallery

This method has been deprecated.

Creates a gallery in a given community. **Note:** If the parentId is
not given, the gallery will be created in the root folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GalleryVO](https://api.fluig.com/old/json_GalleryVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //community's alias  	"parentId" : "1",       //parent's gallery id. If it is 0, the gallery will be created in the root folder.  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal 001" //gallery's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //gallery's id  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal Desc",     //gallery's description  	"url" : "/fluig/gal01",     //gallery's URL  	"previousMediaId" : "null", //this is not applicable for galleries  	"nextMediaId" : "null", //this is not applicable for galleries  	"file" : "null",    //this is not applicable for galleries  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  	"numberMedias" : "0",       //number of medias inside the gallery  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  } ``` |

### POST /social/community/media

This method has been deprecated.

Creates a media (photo or video) in a given gallery.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"galleryId" : "1",  //the gallery's id where the media will be created inside  	"name" : "Media01",  //media's name  	"description" : "Media 001", //media's description  	"base64media" : "4747545", //media's content in base64 format  	"extension" : "PNG" //media's extension. It can be: "PNG", "JPG" or "JPEG" for photo and "MP4", "FLV", "MPEG" for videos  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response JSON (example):  ``` {  	"id" : "2",     //media's id  	"gallery" : {  		"id" : "1",     //gallery's id  		"name" : "Gallery 01",  //gallery's name  		"description" : "Gal Desc",     //gallery's description  		"url" : "/fluig/gal01",     //gallery's URL  		"previousMediaId" : "null", //this is not applicable for galleries  		"nextMediaId" : "null", //this is not applicable for galleries  		"file" : "null",    //this is not applicable for galleries  		"alias" : "community01",    //community's alias  		"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  		"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  		"numberMedias" : "0",       //number of medias inside the gallery  		"socialObjectId" : "1",     //social object id  		"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  	},  	"name" : "Media 01",    //media's name  	"description" : "Media Desc",       //media's description  	"url" : "/fluig/gal01/media01",     //media's URL  	"previousMediaId" : "1",    //previous media id  	"nextMediaId" : "3",    //next media id  	"file" : "/fluig/gal/media.png",    //phisical file  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the media has been created (in miliseconds)  	"numberMedias" : "0",       //this is not applicable for medias  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the media  } ``` |

### POST /social/community/gallery/new

Creates a gallery in a given community. **Note:** If the parentId is
not given, the gallery will be created in the root folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GalleryVO](https://api.fluig.com/old/json_GalleryVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //community's alias  	"parentId" : "1",       //parent's gallery id. If it is 0, the gallery will be created in the root folder.  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal 001" //gallery's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //gallery's id  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal Desc",     //gallery's description  	"url" : "/fluig/gal01",     //gallery's URL  	"previousMediaId" : "null", //this is not applicable for galleries  	"nextMediaId" : "null", //this is not applicable for galleries  	"file" : "null",    //this is not applicable for galleries  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  	"numberMedias" : "0",       //number of medias inside the gallery  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  } ``` |

### POST /social/community/gallery/remove

Removes a gallery in a given community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GalleryVO](https://api.fluig.com/old/json_GalleryVO.html) (JSON) | Request JSON (example):  ```  {  	"galleryId" : "1"       //gallery's id  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO"        //gallery's type. It can be "PHOTO" or "VIDEO"  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/community/gallery/update

Updates a gallery in a given community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GalleryVO](https://api.fluig.com/old/json_GalleryVO.html) (JSON) | Request JSON (example):  ```  {  	"galleryId" : "1"       //gallery's id  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal 001" //gallery's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/community/media/new

Creates a media (photo or video) in a given gallery.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"galleryId" : "1",  //the gallery's id where the media will be created inside  	"name" : "Media01",  //media's name  	"description" : "Media 001", //media's description  	"base64media" : "4747545", //media's content in base64 format  	"extension" : "PNG" //media's extension. It can be: "PNG", "JPG" or "JPEG" for photo and "MP4", "FLV", "MPEG" for videos  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "2",     //media's id  	"gallery" : {  		"id" : "1",     //gallery's id  		"name" : "Gallery 01",  //gallery's name  		"description" : "Gal Desc",     //gallery's description  		"url" : "/fluig/gal01",     //gallery's URL  		"previousMediaId" : "null", //this is not applicable for galleries  		"nextMediaId" : "null", //this is not applicable for galleries  		"file" : "null",    //this is not applicable for galleries  		"alias" : "community01",    //community's alias  		"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  		"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  		"numberMedias" : "0",       //number of medias inside the gallery  		"socialObjectId" : "1",     //social object id  		"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  	},  	"name" : "Media 01",    //media's name  	"description" : "Media Desc",       //media's description  	"url" : "/fluig/gal01/media01",     //media's URL  	"previousMediaId" : "1",    //previous media id  	"nextMediaId" : "3",    //next media id  	"file" : "/fluig/gal/media.png",    //phisical file  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the media has been created (in miliseconds)  	"numberMedias" : "0",       //this is not applicable for medias  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the media  } ``` |

### POST /social/community/media/remove

Removes a media (photo or video).

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):  ```  {  	"mediaId" : "1", //media's alias  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"galleryId" : "1"   //the gallery's id where the media is inside  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/community/media/update

Updates a media (photo or video).

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):  ```  {  	"mediaId" : "1", //media's alias  	"communityAlias" : "community01", //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"galleryId" : "1",  //the gallery's id where the media is inside  	"name" : "Media01",  //media's name  	"description" : "Media 001", //media's description  	"extension" : "PNG" //media's extension. It can be: "PNG", "JPG" or "JPEG" for photo and "MP4", "FLV", "MPEG" for videos  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /social/community/media/{galleryId}/{communityAlias}/{type}

Lists the medias from a given gallery.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityAlias | path | REQUIRED community's alias |  |
| galleryId | path | REQUIRED gallery's id | long |
| type | path | REQUIRED (PHOTO | VIDEO) | "GALLERY\_PHOTO" or "GALLERY\_VIDEO" or "PHOTO" or "VIDEO" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",     //media's id  	"gallery" : {  		"id" : "1",     //gallery's id  		"name" : "Gallery 01",  //gallery's name  		"description" : "Gal Desc",     //gallery's description  		"url" : "/fluig/gal01",     //gallery's URL  		"previousMediaId" : "null", //this is not applicable for galleries  		"nextMediaId" : "null", //this is not applicable for galleries  		"file" : "null",    //this is not applicable for galleries  		"alias" : "community01",    //community's alias  		"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  		"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  		"numberMedias" : "0",       //number of medias inside the gallery  		"socialObjectId" : "1",     //social object id  		"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  	},  	"name" : "Media 01",    //media's name  	"description" : "Media Desc",       //media's description  	"url" : "/fluig/gal01/media01",     //media's URL  	"previousMediaId" : "1",    //previous media id  	"nextMediaId" : "3",    //next media id  	"file" : "/fluig/gal/media.png",    //phisical file  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the media has been created (in miliseconds)  	"numberMedias" : "0",       //this is not applicable for medias  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the media  }] ``` |

### GET /social/community/gallery/byid/{galleryId}/{communityAlias}/{type}

Finds a gallery by its id.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityAlias | path | REQUIRED community's alias |  |
| galleryId | path | REQUIRED gallery's id | long |
| type | path | REQUIRED (PHOTO | VIDEO) | "GALLERY\_PHOTO" or "GALLERY\_VIDEO" or "PHOTO" or "VIDEO" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //gallery's id  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal Desc",     //gallery's description  	"url" : "/fluig/gal01",     //gallery's URL  	"previousMediaId" : "null", //this is not applicable for galleries  	"nextMediaId" : "null", //this is not applicable for galleries  	"file" : "null",    //this is not applicable for galleries  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  	"numberMedias" : "0",       //number of medias inside the gallery  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  } ``` |

### GET /social/community/gallery/byname/{galleryName}/{communityAlias}/{type}

Finds a gallery by its name.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityAlias | path | REQUIRED community's alias |  |
| galleryName | path |  |  |
| type | path | REQUIRED (PHOTO | VIDEO) | "GALLERY\_PHOTO" or "GALLERY\_VIDEO" or "PHOTO" or "VIDEO" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //gallery's id  	"name" : "Gallery 01",  //gallery's name  	"description" : "Gal Desc",     //gallery's description  	"url" : "/fluig/gal01",     //gallery's URL  	"previousMediaId" : "null", //this is not applicable for galleries  	"nextMediaId" : "null", //this is not applicable for galleries  	"file" : "null",    //this is not applicable for galleries  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  	"numberMedias" : "0",       //number of medias inside the gallery  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  	"canWrite" : "true"          //indicates if the current user has permission to write on gallery  } ``` |

### GET /social/community/media/{mediaId}/{galleryId}/{communityAlias}/{type}

Finds a media.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityAlias | path | REQUIRED community's alias |  |
| galleryId | path | REQUIRED gallery's id | long |
| mediaId | path | REQUIRED media's id | long |
| type | path | REQUIRED (PHOTO | VIDEO) | "GALLERY\_PHOTO" or "GALLERY\_VIDEO" or "PHOTO" or "VIDEO" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "2",     //media's id  	"gallery" : {  		"id" : "1",     //gallery's id  		"name" : "Gallery 01",  //gallery's name  		"description" : "Gal Desc",     //gallery's description  		"url" : "/fluig/gal01",     //gallery's URL  		"previousMediaId" : "null", //this is not applicable for galleries  		"nextMediaId" : "null", //this is not applicable for galleries  		"file" : "null",    //this is not applicable for galleries  		"alias" : "community01",    //community's alias  		"type" : "PHOTO",       //gallery's type. It can be "PHOTO" or "VIDEO"  		"creationDate" : "14470506", //date the gallery has been created (in miliseconds)  		"numberMedias" : "0",       //number of medias inside the gallery  		"socialObjectId" : "1",     //social object id  		"canEdit" : "true"          //indicates if the current user has permission to edit the gallery  	},  	"name" : "Media 01",    //media's name  	"description" : "Media Desc",       //media's description  	"url" : "/fluig/gal01/media01",     //media's URL  	"previousMediaId" : "1",    //previous media id  	"nextMediaId" : "3",    //next media id  	"file" : "/fluig/gal/media.png",    //phisical file  	"alias" : "community01",    //community's alias  	"type" : "PHOTO",       //media's type. It can be "PHOTO" or "VIDEO"  	"creationDate" : "14470506", //date the media has been created (in miliseconds)  	"numberMedias" : "0",       //this is not applicable for medias  	"socialObjectId" : "1",     //social object id  	"canEdit" : "true"          //indicates if the current user has permission to edit the media  } ``` |
