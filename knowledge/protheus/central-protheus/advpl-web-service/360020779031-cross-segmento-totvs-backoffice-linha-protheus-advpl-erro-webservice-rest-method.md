---
article_id: 360020779031
category: ADVPL - Web Service
content_hash: e60e115882720d85d1ed41c4c270c096c5867118982a132c7ddc7dd626f8e993
fetched_at: '2026-06-28T22:40:10.454045+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro Webservice:
  Rest Method for Resource[URL]Not Found,Please make sure the Content-Type or Accept
  of Request Header or Request Parameters is correct'
type: support-article
updated_at: '2021-12-29T13:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020779031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Webservice-Rest-Method-for-Resource-URL-Not-Found-Please-make-sure-the-Content-Type-or-Accept-of-Request-Header-or-Request-Parameters-is-correct
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Após as últimas atualizações, o sistema apresenta erro ao utilizar a função HTTPSPOST.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Em análise ao seguinte incidente reportado:  
WebPage -> C (  377) [REST Method for Resource[https://tpall2.2wglobal.com/WWLRestService]Not Found,Please make sure the Content-Type or Accept of Request Header or Request Parameters is correct!The Request should be like:  
===============Request Method[POST]================  
Parameters:  
Message\_Identifier  query  Required[true]  
Message\_Type  query  Required[true]  
Headers:  
Accept:application/json  
  
]  
"  
Isso ocorre por conta de não estar passando no cabeçalho HTTP (aHeadOut) "Accept:application/json", pois da mesma forma, para determinar que tipo de representação é desejado no lado do cliente, o cabeçalho HTTP `ACCEPT` é usado. Ele terá um dos valores mencionados `Content-Type`. Da mesma forma o APPSERVER espera  a informação no cabeçalho.

Passando a informação " Accept:application/json " no cabeçalho HTTP na variável aHeadOut, gera a seguinte questão:  
  
"WebPage -> C (  113) [Request Media Type[application/json] Error or Server setting Error for Content-Type! Actually it is not JSON Data]"  
  
Ou seja o serviço não esta reconhecendo como Dados em formato JSON e isso ocorre também no Postman->  
![](https://totvssuporte.zendesk.com/attachments/token/hvt7DYlJKiRsDUUgfyCod82IX/?name=inline-1370403721.png)​  
  
  
  
Para solução deve-se passar " Accept: \*/\* "   
  
Postman:  
![](https://totvssuporte.zendesk.com/attachments/token/P0kD5JlVFul1QYRblCHJU9TOa/?name=inline-2033276627.png)  
  
No protheus->

Segue fonte de exemplo contendo as modificações necessárias:

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#Include "totvs.ch"  
  
user function tstpost2()   
  
Local cPostUrl      := "https://tpall2.2wglobal.com:6443/WWLRestService"  
Local nTimeOut      := 120  
Local aHeadOut      := {}  
Local cHeaderRet  := ""  
Local sPostRet      := ""  
Local cPostData  :=""  
Local cMens      := 'Message_Identifier=JD&Message_Type=TruckPostion'  
  
Aadd(aHeadOut,'Accept: */*')   
Aadd(aHeadOut,'Content-Type: application/json')  
  
// formatado em JSON pelo link https://jsonformatter.curiousconcept.com/  
cPostData := '{'    
cPostData +=  ' "truckLocation":{'    
cPostData +=      '"header":{'    
cPostData +=          '"partner":"JD",'  
cPostData +=          '"carrier":"TRAN",'  
cPostData +=          '"ediControlNo":"267753039",'  
cPostData +=          '"timestamp":"201804170905210"'  
cPostData +=      '},'  
cPostData +=      '"eventDetail":['    
cPostData +=          '{'    
cPostData +=            '"licensePlate":"HKE5865",'  
cPostData +=            '"latitude":"14.143777913430046",'  
cPostData +=            '"longitude":"100.91526948374563",'  
cPostData +=            '"updateDate":"201804170905210"'  
cPostData +=          '}'  
cPostData +=      ']'  
cPostData +=    '}'  
cPostData += '}'  
  
 _cPostData := EncodeUTF8(cPostData)  
  
 sPostRet := HttpPost(cPostUrl,cMens,_cPostData,nTimeOut,aHeadOut,@cHeaderRet)  
  
if !empty(sPostRet)  
  conout("HttpPost Ok")  
  varinfo("WebPage", sPostRet)  
else  
  conout("HttpPost Failed.")  
  varinfo("Header", cHeaderRet)  
Endif  
  
Return
```

Resultado esperado em build atualizada:

![](https://totvssuporte.zendesk.com/attachments/token/dw5sY5QO5KSAxjTy6BQZ0YSeV/?name=inline279833392.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/J7O79jMvJYIAyUoYlXsgjfalv/?name=inline1921450881.png)​  
**Obs.** No teste foi utilizada a função [HttpPost](http://tdn.totvs.com/display/tec/HTTPPost). Para o serviço acima testado, não se faz necessária a utilização da função [HTTPSPost](http://tdn.totvs.com/display/tec/HTTPSPost), pois o serviço em questão não exige certificado.
