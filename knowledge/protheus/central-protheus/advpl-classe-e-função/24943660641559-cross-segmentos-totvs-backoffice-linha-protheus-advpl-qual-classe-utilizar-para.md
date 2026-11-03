---
article_id: 24943660641559
category: ADVPL - Classe e Função
content_hash: 1940ac143b5b5a53dae8f0d6d2f8c6276f7d3361471a1a3b8e9dcd46c05b7093
fetched_at: '2026-06-28T22:40:21.649532+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Qual classe utilizar
  para substituir a TMediaPlayer?
type: support-article
updated_at: '2024-07-16T19:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24943660641559-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-classe-utilizar-para-substituir-a-TMediaPlayer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24943660621591) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual classe utilizar para substituir a TMediaPlayer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**A melhor substituição do TMediaPlayer seria utilizar diretamente o TWebEngine para renderizar o vídeo. Segue exemplo de código:

```
user function video()  
  
Local cHtml  
  
oModal := MSDialog():New(180,180,550,700, "Página HTML (WebAPP)",,,,,,,,,.T./lPixel/)  
  
//Cria o componente que irá carregar o arquivo local  
oWebEngine := TWebEngine():New(oModal, 0, 0, 100, 100,/cUrl/, )  
  
cRet := cpyf2web("C:\Users\lucas.bonfim\Downloads\webapp.mp4", .T., .T., .T., .F.)  
  
cHtml := '<!DOCTYPE html>'   
cHtml += '<html lang="pt-BR">'  
cHtml += '<body>'  
cHtml += ' <div>'  
cHtml += ' <div>'  
cHtml += ' <video width="320" height="240" autoplay>'  
cHtml += ' <source src="webapp.mp4" type="video/mp4">'  
cHtml += ' </div>'  
cHtml += ' </div>'  
cHtml += '</body>'  
cHtml += '</html>'  
  
nHnd := fcreate("c:\teste\video.html")  
fWrite(nHnd, cHtml)  
fclose(nHnd)  
  
curl := cpyf2web("c:\teste\video.html", .T.,.T.,.T.,.F.)  
oWebEngine:navigate(curl)  
oWebEngine:Align := 5  
oModal:Activate()  
  
  
return
```

**Saiba mais:**

[TWebEngine](https://tdn.totvs.com/display/tec/TWebEngine)
