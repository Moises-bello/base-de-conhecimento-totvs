---
article_id: 360019402932
category: ADVPL - Classe e Função
content_hash: 2f463e8acf1b0f516449552a85661e617f8838876ba54db007ecb75914508070
fetched_at: '2026-06-28T22:40:19.493423+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FWFileReader não
  faz a leitura de todas as linhas corretamente
type: support-article
updated_at: '2026-06-15T11:20:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019402932-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWFileReader-n%C3%A3o-faz-a-leitura-de-todas-as-linhas-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**FWFileReader não faz a leitura de todas as linhas corretamente  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Esse erro pode ocorre quando utilizado o métodos GetLine(.T.) , exemplo de customização:

```
#Include 'Protheus.ch'  
#include 'TOPCONN.ch'  
#include 'TBICONN.ch'  
#DEFINE ENTER Chr(13)+Chr(10)  
  
User Function MyFWFile()  
local oFile   
Local cLine :=""  
local nlinha:= 1  
  
oFile:= FWFileReader():new("C:\logleitura.txt")  
   
 If oFile:Open()  
 Do While oFile:Hasline()  
 cLine := oFile:GetLine()  
 Alert("cLine " + cvaltochar(nlinha) + "" +cLine)  
 nlinha++  
 End Do  
   
 oFile:Close()  
   
 EndIF  
  
  
Return
```
