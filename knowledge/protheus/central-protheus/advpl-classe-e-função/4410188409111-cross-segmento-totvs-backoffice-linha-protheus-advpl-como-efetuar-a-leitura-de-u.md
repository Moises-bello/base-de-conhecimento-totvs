---
article_id: 4410188409111
category: ADVPL - Classe e Função
content_hash: 24b7de169ca0907603aa6116297eb643c279e45a8e6e9f3fbfc56aac8b48940c
fetched_at: '2026-06-28T22:40:20.685013+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como efetuar a leitura
  de um arquivo Json com array através da classe JsonObject?
type: support-article
updated_at: '2021-10-06T17:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410188409111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-efetuar-a-leitura-de-um-arquivo-Json-com-array-atrav%C3%A9s-da-classe-JsonObject
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como efetuar a leitura de um arquivo Json com array através da classe JsonObject?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**A leitura do arquivo Json , pode ser realizada conforme exemplo:

```
#include "protheus.ch"  
  
User Function Exemplo1()  
  
Local cFile := '\teste\exemplo2.json'  
Local cJsonStr,oJson  
Local nId, cNome, cNomer  
  
// Le a string JSON do arquivo do disco   
cJsonStr := readfile(cFile)  
  
// Cria o objeto JSON e popula ele a partir da string  
oJson := JSonObject():New()  
cErr  := oJSon:fromJson(cJsonStr)  
  
If !empty(cErr)  
  MsgStop(cErr,"JSON PARSE ERROR")  
  Return  
Endif  
  
// Agora vamos ler as propriedades com GetJSonObject()  
nId := oJson:GetJSonObject('a1_cod')  
cNome := oJson:GetJSonObject('a1_nome')  
cNomer := oJson:GetJSonObject('a1_nreduz')  
FreeObj(oJson)  
  
Return  
  
STATIC Function ReadFile(cFile)  
Local cBuffer := ''  
Local nH , nTam  
nH := Fopen(cFile)  
IF nH != -1  
    nTam := fSeek(nH,0,2)  
    fSeek(nH,0)  
    cBuffer := space(nTam)  
    fRead(nH,@cBuffer,nTam)  
    fClose(nH)  
Else  
    MsgStop("Falha na abertura do arquivo ["+cFile+"]","FERROR "+cValToChar(Ferror()))  
Endif  
  
Return cBuffer
```

**Saiba mais**  
[JsonObject - GetJsonObject](https://tdn.totvs.com/display/tec/JsonObject%3AGetJsonObject)
