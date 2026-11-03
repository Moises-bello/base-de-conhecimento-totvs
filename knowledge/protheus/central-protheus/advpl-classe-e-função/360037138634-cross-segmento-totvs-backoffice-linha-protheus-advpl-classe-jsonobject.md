---
article_id: 360037138634
category: ADVPL - Classe e Função
content_hash: e31f284959a1105ae8334643388efcaf2489ec5c8f7ddab2f413c0f404587347
fetched_at: '2026-06-28T22:40:15.424529+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe JsonObject '
type: support-article
updated_at: '2022-01-10T17:11:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037138634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-JsonObject
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao utilizar a classe JsonObject o método fromJson  com a expressão abaixo funciona.

'{"name":"John", "age":31, "city":"New York"}'  
Mas no Formato a frente não retorna o objeto corretamente, retorna somente a expressão DATA   
'{"DATA": [{"ID\_COMPANY\_FK": "5022","COD\_ESTAB\_PK": "01"}]}'  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.25  
  
**Solução**O retorno do objeto traz a propriedade DATA pois ocorre que o Json enviado é recursivo e neste caso deve tratar e utilizar o método [GetJsonObject](https://tdn.totvs.com/display/public/FRAMJOI/JSONObject%3AgetJSONObject) que retorna um objeto JSON que seja o conteúdo de uma propriedade em outro objeto JSON.  
Exemplo funcional

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#Include 'Totvs.ch'  
  
User Function JSONTST2()  
  
Local oJsonA := Nil  
Local oJsonB := Nil  
Local cParseRes := ''  
Local cJsonStr := ''  
Local array := {}  
Local array1 := {}  
Local array2 := {}  
Local nl := 0  
  
cJsonStr:= '{"DATA": [{"ID_COMPANY_FK": "5022","COD_ESTAB_PK": "01"}]}'  
  
  
oJsonA := JsonObject():new()  
cParseRes := oJsonA:fromJson(cJsonStr)  
  
array:= oJsonA:GetNames()  
Varinfo("Conteudo oJsonA:GetNames", array)  
  
  
oJsonB := JsonObject():new()  
oJsonB := oJsonA:GetJsonObject(ARRAY[1])  
  
oJsonB[1]:toJSON()  
oJsonB[2]:toJSON()  
  
array1:= oJsonB[1]:GetNames()  
Varinfo("Conteudo oJsonB[1]:GetNames", array1)  
  
array2:= oJsonB[2]:GetNames()  
Varinfo("Conteudo oJsonB[2]:GetNames", array2)  
  
For nL := 1 to len( array1 )  
 ConOut ( array1[nL] )  
 Conout ( oJsonB[1]:GetJsonText( array1[nL] ) )  
 Next nL  
  
For nL := 1 to len( array2 )  
 ConOut ( array2[nL] )  
 Conout ( oJsonB[2]:GetJsonText( array2[nL] ) )  
 Next nL  
  
FreeObj(oJsonA)  
FreeObj(oJsonB)  
  
return  
  
Obs.: Caso esse exemplo não lhe atenda utilize o exemplo da Classe JsonObject
```

**Saiba Mais**[JSON](https://tdn.totvs.com/display/public/FRAMJOI/JSON)
