---
article_id: 39577428668951
category: ADVPL - Classe e Função
content_hash: aae75dec51d91c54eb2889e3614a171a6b78606038ae95b735975cee085f0eeb
fetched_at: '2026-06-28T22:40:19.362123+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções e classes
  para consumo de API
type: support-article
updated_at: '2026-05-05T19:57:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39577428668951-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%B5es-e-classes-para-consumo-de-API
---

As principais funções e classes ADVPL para consumo de APIs são:

FWRest.

HTTPGet/HTTPSGet.

HTTPPost/HTTPSPost.

HTTPQuote/HTTPSQuote ( para métodos HTTP variados, ideal para PATCH).

Endereços HTTPS requer certificados em formato PEM, podendo usar configuração centralizada no appserver.ini para segurança.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39580950258327)Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais as principais funções e classes ADVPL que podem ser utilizadas para realizar o consumo de APIs?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – Todas as versões.

**Solução**  
Para o consumo de APIs e requisições Web via AdvPL, existem diversas funções e classes nativas que permitem a comunicação HTTP e HTTPS. A escolha correta depende do protocolo, da necessidade de certificados e do método HTTP exigido pela integração:

**FWRest:** É a classe Client de REST padrão, que simplifica as requisições e fornece métodos diretos para os principais verbos HTTP, como Get, Post, Put e Delete. A classe não oferece suporte nativo ao método PATCH. .

Exemplo de código com a **FWRest** com método GET:

```
User Function TstFwRest()
    Local oRestClient := FWRest():New("https://seusite.com.br")  // Instancia informando o Host 
    Local aHeader := {}
    
    AAdd(aHeader, "Content-Type: application/json; charset=UTF-8") //exemplo de header
    oRestClient:SetHeader(aHeader)
    oRestClient:setPath("/p/json-path/") // Informa o path da requisição 
    
    // Efetua o Comando Get no Host e Path informados 
    if oRestClient:Get()
		ConOut(oRestClient:GetResult())
	else
		ConOut(oRestClient:GetLastError())
	endif
Return
```

Exemplo de código com a **FWRest** com método POST:

```
User Function TstFwRestPost()
    Local oRestClient := FWRest():New("https://seusite.com.br") // Instancia informando o Host 
    Local aHeader := {"Content-Type: application/json"} //exemplo de header
    Local cPayload := '{"teste":"123"}'
    
    oRestClient:SetPath("/api/endpoint") 
    oRestClient:SetPostParams(cPayload) // Seta a string de parâmetro do Post 
    
    If oRestClient:Post(aHeader)
        ConOut(oRestClient:GetResult())
    Else
        ConOut(oRestClient:GetLastError())
    EndIf
Return
```

Exemplo de código com a **FWRest** com método PUT:

```
User Function TstFwRestPut()
    Local oRestClient := FWRest():New("https://seusite.com.br") // Instancia informando o Host 
    Local aHeader := {"Content-Type: application/json"} //exemplo de header
    Local cPayload := '{"status":"atualizado"}' // Corresponde à StringList de parâmetros a serem enviados ao servidor HTTP 
    
    oRestClient:SetPath("/api/endpoint/1")
    
    If oRestClient:Put(aHeader, cPayload, "")
        ConOut(oRestClient:GetResult())
    Else
        ConOut(oRestClient:GetLastError())
    EndIf
Return
```

Exemplo de código com a **FWRest** com método DELETE:

```
User Function TstFwRestDel()
    Local oRestClient := FWRest():New("https://seusite.com.br") // Instancia informando o Host 
    Local aHeader := {"Content-Type: application/json"} //exemplo de header
    
    oRestClient:SetPath("/api/endpoint/1")
    
    If oRestClient:Delete(aHeader, "", "")
        ConOut(oRestClient:GetResult())
    Else
        ConOut(oRestClient:GetLastError())
    EndIf
Return
```

**HTTPGet e HTTPSGet:** Funções que permitem emular um client para acessar um documento ou endpoint utilizando exclusivamente com o método GET. A versão HTTPS realiza a requisição utilizando protocolo de segurança, necessitando a passagem de certificados.  
  
Exemplo de código com o HTTPGet:

```
User Function TstHttpGet()
    Local cHtmlPage
    
    // Chamada direta passando a URL 
    cHtmlPage := HttpGet('http://www.servidor.com.br/pageteste.htm') 
    
    ConOut("Retorno WebPage", cHtmlPage) 
Return
```

Exemplo de código com o HTTPSGet:

```
User Function TstHttpsGet()
    Local cURL := "https://api.exemplo.com/dados" // Instancia informando o Host 
    Local cHeadRet := ""
    Local cGetRet := ""
    
    // Exige a passagem dos caminhos do certificado (.pem) e chave privada 
    cGetRet := HTTPSGet( cURL, "\certs\cert.pem", "\certs\privkey.pem", "senha_chave", "", 120, {}, @cHeadRet ) 
    
    ConOut("Retorno: ", cGetRet) 
Return
```

**HTTPPost e HTTPSPost:** Funções que emulam um client HTTP/HTTPS para enviar (postar) um bloco de informações para uma determinada URL utilizando exclusivamente o método POST.

Exemplo de código com o HTTPPost :

```
User Function TstHttpPost()
    Local cUrl := "http://www.exemplo.com/api" // Instancia informando o Host 
    Local aHeadOut := {'Content-Type: application/x-www-form-urlencoded'} //exemplo de header
    Local cHeadRet := ""
    Local sPostRet := ""
    
    // Envio de parâmetros no corpo (POST) e captura do Header de retorno na variável cHeadRet 
    sPostRet := HttpPost( cUrl, "", "CAMPO=VALOR&TESTE=123", 120, aHeadOut, @cHeadRet ) 
Return
```

Exemplo de código com o HTTPsPost :

```
User Function TstHttpsPost()
    Local cUrl := "http://www.exemplo.com/api" // Instancia informando o Host https
    Local aHeadOut := {'Content-Type: application/x-www-form-urlencoded'}  //exemplo de header
    Local cHeadRet := ""
    Local sPostRet := ""
    Local nTimeOut := 120
    Local cPostParms := "CAMPO=VALOR&TESTE=123"
    
    // Envio de parâmetros no corpo (POST) e captura do Header de retorno na variável cHeadRet 
    cPostRet := HTTPSPost( cURL, "\certs\cert.pem", "\certs\privkey.pem", "senha_certificado", "", cPostParms, nTimeOut, aHeadOut, @cHeadRet )  
Return
```

**HTTPQuote e HTTPSQuote:** Permitem emular um client HTTP ou HTTPS onde o método HTTP a ser utilizado é informado de forma explícita na chamada da função através do parâmetro cMethod. Como permitem a definição livre do verbo HTTP que será enviado ao servidor (permitindo outros além de GET/POST), **são as funções ideais e indicadas para o envio de requisições utilizando o método PATCH**.

Exemplo de código com o HTTPQuote método PATCH:

```
User Function TstHttpQuotePatch()
    Local cUrl := "http://api.exemplo.com/recurso/1" // Instancia informando o Host 
    Local aHeadOut := {'Content-Type: application/json'} //exemplo de header
    Local cHeadRet := ""
    Local cResponse := ""
    Local cPayload := '{"status": "atualizado"}' // Dados para o PATCH
    
    // Observe o segundo parâmetro informando "PATCH" explicitamente como o cMethod 
    cResponse := HTTPQuote( cUrl, "PATCH", "", cPayload, 120, aHeadOut, @cHeadRet ) 
    
    ConOut("Retorno PATCH: ", cResponse)
Return
```

Exemplo de código com o HTTPSQuote com método PATCH:

```
User Function TstHttpsQuotePatch()
     Local cUrl := "https://api.exemplo.com/recurso/1" // Instancia informando o Host https
    Local aHeadOut := {'Content-Type: application/json'} //exemplo de header
    Local cHeadRet := ""
    Local cResponse := ""
    Local cPayload := '{"status": "atualizado"}' // Dados para o PATCH
    
    // O quinto parâmetro define o método HTTP ("PATCH"), permitindo outros além de POST/GET 
    cResponse:= HTTPSQuote( cURL, "\certs\cert.pem", "\certs\privkey.pem", "senha", "PATCH", "", cPayload, 120, {}, @cHeadRet ) 
    
    ConOut("Retorno PATCH: ", cResponse)
    
Return
```

**Observações**:

* Ao configurar a seção [**SSLConfigure**] no appserver.ini, o Protheus estabelece uma identidade global de segurança que é automaticamente herdada pela classe **FWRest** ao processar hosts via HTTPS. Em releases recentes do AppServer, as funções **HTTPSGet**, **HTTPSPost** e **HTTPSQuote** permitem que os parâmetros de caminho físico do certificado e da chave privada sejam passados como strings vazias (""), uma vez que o binário prioriza a parametrização centralizada do servidor, eliminando a necessidade de referências locais no código-fonte ADVPL.
* As funções **HTTPSGet**, **HTTPSPost** e **HTTPSQuote** exigem certificado no formato PEM. Caso o mesmo seja extensão .PFX, segue as documentações das funções de conversão para formato .PEM  
  [PFX2PEM](https://tdn.totvs.com/display/tec/PFX2PEM)  
  [PFXCA2PEM](http://tdn.totvs.com/display/tec/PFXCA2PEM)  
  [PFXCert2PEM](https://tdn.totvs.com/display/tec/PFXCert2PEM)  
  [PFXKey2PEM](http://tdn.totvs.com/display/tec/PFXKey2PEM)

**Saiba mais**  
[FWRest](https://tdn.totvs.com/display/public/framework/FWRest)  
[HttpGet](https://tdn.totvs.com/display/tec/HTTPGet)  
[HTTPSGet](https://tdn.totvs.com/display/tec/HTTPSGet)  
[HttpPost](https://tdn.totvs.com/display/tec/HTTPPost)  
[HTTPSPost](https://tdn.totvs.com/display/tec/HTTPSPost)  
[HTTPQuote](https://tdn.totvs.com/display/tec/HTTPQuote)  
[HTTPSQuote](https://tdn.totvs.com/display/tec/HTTPSQuote)  
[Seção [SSLConfigure]](https://tdn.totvs.com/pages/viewpage.action?pageId=6064865)  
[Requisição REST com método PATCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418380554775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Requisi%C3%A7%C3%A3o-REST-com-m%C3%A9todo-PATCH)
