---
article_id: 360051658134
category: ADVPL - Classe e Função
content_hash: f27c517d0a3632f3bd8b854896750ef30a9232aa72da22cd861c6462ef13c039
fetched_at: '2026-06-28T22:40:15.693556+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Converter PDF para
  Array de Bytes
type: support-article
updated_at: '2023-12-20T22:07:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051658134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Converter-PDF-para-Array-de-Bytes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
  **Dúvida**Existe alguma forma de converter PDF para array de bytes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**O binário não trabalha bem com alguns arquivos de texto, pois a leitura e verificação de tamanho acabam falhando.  
Um possível implementação, é a leitura do arquivo byte a byte para então gerar a conversão e o array, porém isso é um processo que gera grande lentidão, por conta do IO gerado.  
Veja um exemplo:

```
#include "protheus.ch"  
#include "fileio.ch"  
//Função para testes das demais funções de conversão de arquivo para  
array (byte e binário)  
  
user function testBytesFile()  
local cFile as char  
local aBytes as array  
local nHandle as numeric  
cFile := "mypdf.pdf"  
aBytes := u_file2ArraryByte(cFile)  
nHandle := FCreate("advpl-bytes.txt")  
AEval(aBytes,{|cValue| FWrite(nHandle, cValue)})  
FClose(nHandle)  
aSize(aBytes, 0)  
aBytes := nil  
return  
//Converte o arquivo recebido para um array de bytes  
  
user function file2ArraryByte(cFile)  
local cByte as char  
local aBytes as array  
local nLoop as numeric  
local nLength as numeric  
local nHandle as numeric  
nHandle := FOpen(cFile, FO_READ+FO_SHARED)  
nLength := FSeek(nHandle, 0, FS_END)  
FSeek(nHandle, 0)  
aBytes := {}  
for nLoop := 1 to nLength  
cByte := FReadStr(nHandle, 1)  
cByte := cValToChar(Asc(cByte))  
aAdd(aBytes, cByte)  
  
next  
FClose(nHandle)  
return aBytes
```

Observação: Os resultados obtidos foram comparados com outra linguagem e ficaram iguais, ainda sim recomendamos a utilização da base64 nesse cenário.
