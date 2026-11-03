---
article_id: 360019176971
category: ADVPL - Classe e Função
content_hash: d0eb395f60b3843845620987a1ec84baf43bb7d946998f96b78c282a22e22c52
fetched_at: '2026-06-28T22:40:15.784383+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Encode64 não funciona
  com imagem
type: support-article
updated_at: '2021-10-25T14:04:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019176971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Encode64-n%C3%A3o-funciona-com-imagem
---

**Ocorrência**Ao tentar converter uma imagem para a base 64 p/ enviar via API, poderia me passar uma forma de converter uma imagem do tipo .jpeg para base 64?

A função Encode 64 está com problema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Esse recurso de conversão de um arquivo, não esta disponível, conforme a documentação

**[ENCODE64](http://tdn.totvs.com/display/tec/Encode64)**

```
Os parâmetros marcados com (*) só estão disponíveis para versões superiores a apenas nas versões 17.1.0.0 ou 17.2.1.0 ou superior.
```

**Solução**Segue exemplo para converter uma imagem para BASE64 utilizando funções de manipulação de arquivos.

[Manipulação de arquivos, discos e IO](http://tdn.totvs.com/pages/viewpage.action?pageId=6063692)

```
#Include 'Protheus.ch'  
#include "Fileio.ch"  
  
User Function tGzip()  
Local cTexto := ""  
Local aFiles := {} // O array receberá os nomes dos arquivos e do diretório  
Local aSizes := {} // O array receberá os tamanhos dos arquivos e do diretorio  
  
ADir("C:\tmp\img.jpg", aFiles, aSizes)//Verifica o tamanho do arquivo, parâmetro exigido na FRead.  
  
nHandle := fopen('C:\tmp\img.jpg' , FO_READWRITE + FO_SHARED )  
cString := ""  
FRead( nHandle, cString, aSizes[1] ) //Carrega na variável cString, a string ASCII do arquivo.  
  
cTexto := Encode64(cString) //Converte o arquivo para BASE64  
  
fclose(nHandle)  
  
//Cria uma cópia do arquivo utilizando cTexto em um processo inverso(Decode64) para validar a conversão.      
nHandle := fcreate("C:\tmp\img2.jpg")  
FWrite(nHandle, Decode64(cTexto))  
fclose(nHandle)  
  
Return
```
