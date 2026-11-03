---
article_id: 10438922558487
category: ADVPL - Classe e Função
content_hash: a41d571bccc9b66fa4a72b3f7d7c807c6bf5b91bffaabdb345e48f8d8cb74e5c
fetched_at: '2026-06-28T22:40:20.656527+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  É possível trazer
  informações de qualquer servidor pela função GetPvProfileInt?
type: support-article
updated_at: '2024-01-29T17:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10438922558487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-trazer-informa%C3%A7%C3%B5es-de-qualquer-servidor-pela-fun%C3%A7%C3%A3o-GetPvProfileInt
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**É possível trazer informações de qualquer servidor pela função GetPvProfileInt?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as versões  
  
**Solução**A premissa para trazer determinada informação do servidor é que esteja conectado.

**Localização do arquivo de configuração a ser pesquisado:**

* Se <cNomeArqCfg> for informado sem caminho, o arquivo será procurado na pasta de instalação do TOTVS Application Server.
* Se <cNomeArqCfg> for informado com caminho, o arquivo será procurado na estação que executou a função.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10438787113111)

```
user function ExGetPvProfInt()  
  
  localret,ret1  
  localserverIni := "appserver.ini"// for informado sem caminho, o arquivo será procurado na pasta de instalação do TOTVS Application Server.                                       
  localremoteIni := "C:\Totvs\Protheus33\Protheus\smartclient\smartclient.ini"//for informado com caminho, o arquivo será procurado na estação que executou a função.                 
  localsecao := "TCP"  
  localchave := "port"  
  
  ret1 := GetPvProfileInt(secao,chave,0,serverIni)  
  
  Conout("Valor server ini Retornado " + cValToChar(ret1))  
  
  ret := GetPvProfileInt(secao,chave,0,remoteIni)  
  
  Conout("Valor remote ini Retornado " + cValToChar(ret))  
  
return
```

**Saiba mais**[GetPvProfileInt](https://tdn.totvs.com/display/tec/GetPvProfileInt)
