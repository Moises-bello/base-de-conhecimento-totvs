---
article_id: 360022591872
category: ADVPL - Web Service
content_hash: 32d27ab7477a87433d9584eb27e3e333c5dd2de1d31e8ea3c06065bc746aa85a
fetched_at: '2026-06-28T22:40:10.458795+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: Host not
  found em consumo Rest'
type: support-article
updated_at: '2021-12-29T13:25:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022591872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Host-not-found-em-consumo-Rest
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao efetuar o consumo de um serviço REST utilizando a classe FwRest(), eu tenho sucesso, porém ao efetuar a segunda requisição, é exibido o erro abaixo quando utilizado o método GetLastError():

```
HOST NOT FOUND
```

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Causa**Este erro ocorre porque na primeira requisição é enviado implicitamente um (ou mais) *cookie*(s), no cabeçalho da requisição por meio do *MIME type* *Set-Cookie*.

Esta informação fica evidente quando efetuamos a requisição via ferramentas externas (ex: Postman), contudo na segunda requisição, o cookie não é enviado, porém é utilizado:  
  
IMG01: *Cookies* enviados (Primeira requisição)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020000291/mceclip0.png)  
  
IMG02: *Mime type* set - *cookie* (Primeira requisição)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020000651/mceclip2.png)  
  
IMG03: *Cookies* utilizados na aba *cookies*, porém não enviados (Segunda requisição)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020001211/mceclip3.png)  
  
**Solução**Na segunda requisição para a mesma URI (*Uniform Resource Identifier)*, realizar a adição dos *cookies* no vetor do cabeçalho que será enviado no método Post():

```
/** PRIMEIRA REQUISIÇÃO JÁ REALIZADA **/  
  
// INFORMA O RECURSO E ENVIA O JSON NO CORPO DA REQUISIÇÃO  
oRest:SetPath(cPath)  
oRest:SetPostParams(oJson:ToJson())  
  
// REALIZA O ENVIO DO USUÁRIO E SENHA NO CABEÇALHO  
AAdd(aHeader, aSession[1][1] ": "+ aSession[1][2])  
AAdd(aHeader, aSession[2][1] ": "+ aSession[2][2])  
  
// ENVIA O COOKIE QUE JÁ FOI MONTADO CONFIGURADO NA REQUISIÇÃO ANTERIOR  
If (Len(oRest:oResponseH:aHeaderFields) > 0)   
    AAdd(aHeader, "Cookie: " + oRest:oResponseH:aHeaderFields[AScan(oRest:oResponseH:aHeaderFields, {|x| Upper(AllTrim(x[1])) == "SET-COOKIE"})][2])  
      
    // REALIZA O ENVIO PELO VERBO HTTP POST  
    If (oRest:Post(aHeader)) // SE SUCESSO, GERA OBJETO JSON COM A RESPOSTA  
        oJson:FromJson(oRest:GetResult())  
    Else // SE ERRO, EXIBE A MENSAGEM NO CONSOLE DO SERVIDOR  
        ConOut(Repl("-", 80))  
        ConOut(PadC("Couldn't generate the application token", 80))  
        ConOut(Repl("-", 80))  
    EndIf  
EndIf  
  
/** DEMAIS PROCESSO PÓS REQUISIÇÃO **/
```

**Saiba mais**  
[Mdn - Cookies HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Cookies)  
[FWRest](http://tdn.totvs.com/display/framework/FWRest)
