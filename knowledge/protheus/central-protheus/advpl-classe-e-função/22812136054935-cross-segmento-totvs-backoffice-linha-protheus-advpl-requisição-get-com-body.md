---
article_id: 22812136054935
category: ADVPL - Classe e Função
content_hash: 43ab2b9e9f86be32f5f76c82f7fc51bcdaab3b9ca9ec079c0c555effe1e32536
fetched_at: '2026-06-28T22:40:17.145053+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Requisição GET com
  body
type: support-article
updated_at: '2024-04-15T14:14:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22812136054935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Requisi%C3%A7%C3%A3o-GET-com-body
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22812144099991) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Existe alguma função para consumo de API GET com Body?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Soluções**

Para esses casos de consumir uma API Get onde é necessário informar um Body em json, pode se utilizar as funções *HTTPQuote* ou *HTTPsQuote*.

**Exemplo**

```
user function gettst()   
  
Local   cUrl        := 'link da api'   
Local   aHeader     := {}   
Local   cHeaderRet  :=""   
Local   cRest1       :='{"Seu_json":"Seu json"}'   
Local   cRest       :=""   
  
aAdd(aHeader, "content-type: application/json" )   
aAdd(aHeader, "Accept: */*" )   
  
cRest  := HTTPQuote( cUrl, "GET", "", cRest1, 10, aHeader, @cHeaderRet)   
  
If !empty(cRest )   
conOut("VERBO: GET ", EncodeUTF8(cRest) )   
nErro := HttpGetStatus(@cHeaderRet)   
EndIf   
  
RETURN
```

**Saiba Mais**

[HTTPQuote](https://tdn.totvs.com/display/tec/HTTPQuote)

[HTTPsQuote](https://tdn.totvs.com/display/tec/HTTPsQuote)
