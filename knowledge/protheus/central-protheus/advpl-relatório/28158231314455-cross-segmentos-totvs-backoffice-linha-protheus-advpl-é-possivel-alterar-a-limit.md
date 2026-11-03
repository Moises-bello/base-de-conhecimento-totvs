---
article_id: 28158231314455
category: ADVPL - Relatório
content_hash: c4cdaf65bf6a86f7c59c40c08ec196c1558427aef4abb2b7916da8e7369997aa
fetched_at: '2026-06-28T22:40:22.976318+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - É possivel alterar
  a limitação de 8 decimais da Classe JsonObject?
type: support-article
updated_at: '2024-12-02T18:52:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28158231314455-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-possivel-alterar-a-limita%C3%A7%C3%A3o-de-8-decimais-da-Classe-JsonObject
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28158231295639)*Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
É possivel alterar a limitação de 8 decimais da Classe JsonObject?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Para isso, a solução seria utilizando as funções **DEC\_CREATE** que indica a quantidade total de dígitos do número, e a escala indica a quantidade reservada para as casas decimais do número e a função **cValToChar** para transformar este número em String para passar no JSON.

**Observação**Reforçamos que campos do Protheus continuarão recebendo por padrão no máximo 8 casas decimais.  
  
**Exemplo**:

```
#include "protheus.ch"  
  
  
user function FJDEC()  
local oJson  
local ret  
local nCoord1 := DEC_CREATE(-49.354684361, 10, 9)  
local nCoord2 := DEC_CREATE(-23.353524586, 10, 9)  
local nCoord1Str := cValToChar(nCoord1)  
local nCoord2Str := cValToChar(nCoord2)  
local cJson := '{"coordenada" : "' + nCoord1Str + '" , "coordenada2" : "' + nCoord2Str + '"}'  
Alert(cJson)  
  
oJson := JsonObject():new()  
  
ret := oJson:FromJson(cJson)  
  
if ValType(ret) == "U"  
Alert("JsonObject populado com sucesso")  
else  
Conout("Falha ao popular JsonObject. Erro: " + ret)  
endif  
FreeObj(oJson)  
return  
  
  
/*  
Impressão ao executar o u_FJSucesso():  
   
JsonObject populado com sucesso  
*/
```

**Saiba mais**  
- [**Classe JsonObject**](https://tdn.totvs.com/display/public/FRAMJOI/JSONObject)

**- [Função DEC\_CREATE](https://tdn.totvs.com/display/tec/DEC_CREATE)**

**- [Função cValToChar](https://tdn.totvs.com/display/tec/cValToChar)**
