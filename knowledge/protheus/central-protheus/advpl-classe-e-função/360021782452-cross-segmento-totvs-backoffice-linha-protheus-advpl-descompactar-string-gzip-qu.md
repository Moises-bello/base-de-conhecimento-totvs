---
article_id: 360021782452
category: ADVPL - Classe e Função
content_hash: 82d38117b08abfa2e49d2b1839e3185a7828714a219d6d1d60b6eac83d69cd05
fetched_at: '2026-06-28T22:40:15.767296+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Descompactar string
  .gZip que está em base64Binary
type: support-article
updated_at: '2022-01-05T15:30:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021782452-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Descompactar-string-gZip-que-est%C3%A1-em-base64Binary
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Preciso descompactar uma string .**gZip** em *base64Binary*, e gerar o resultado em um arquivo texto.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Utilize a função **GzStrDecomp**juntamente com a função **Decode64**.  
  
![KCS_gZip.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360018731751/KCS_gZip.gif)

**Exemplo:**

```
user function TGzStrDecomp()  
  
Local lRet :=.F.  
Local cComp :="", cUncomp :=""  
Local nLenComp :=0, nLenUncomp :=0  
  
cComp := MemoRead( "\testdir\string.gz" )  
cDecode64 := Decode64(cComp)  
nLenComp := Len( cComp )  
  
cUncomp := ""  
nLenUncomp := 0  
  
lRet := GzStrDecomp( cDecode64, nLenComp, @cUncomp )  
  
nLenUncomp := Len( cUncomp )  
nHandle := FCreate( "\testdir\string.txt" )  
FWrite( nHandle, cUncomp, nLenUncomp )  
FClose( nHandle )  
  
return
```

**Saiba mais**[GzStrDecomp](http://tdn.totvs.com/display/tec/GzStrDecomp)[Decode64](http://tdn.totvs.com/display/tec/Decode64)
