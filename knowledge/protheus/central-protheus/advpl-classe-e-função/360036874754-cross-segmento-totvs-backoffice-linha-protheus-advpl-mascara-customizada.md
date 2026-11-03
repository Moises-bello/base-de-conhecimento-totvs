---
article_id: 360036874754
category: ADVPL - Classe e Função
content_hash: 46671b86d084401b86a307de1cb47714792ec98f82f50226b58fe734087ac1ba
fetched_at: '2026-06-28T22:40:14.258686+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL  - Mascara customizada
type: support-article
updated_at: '2021-12-28T19:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036874754-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mascara-customizada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como criar uma mascara customizada em um campo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - Todas as versões  
  
**Solução**Segue um exemplo de criação de um campo para placa de veículo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049044933/mceclip0.png)

No campo form. Variável informe o nome da função compilada em seu RPO que onde será feito a personalização da mascara conforme o exemplo abaixo:

```
#Include "protheus.ch"  
  
function u_MASKA()  
  
local cRet    AS CHARACTER  
local cRot    AS CHARACTER  
  
cRet    := ""  
cRot    := allTrim(funName())  
  
if cRot == "MATA103"  
 cRet    := "AAA-999"  
else  
 cRet    := "@!"  
endIf  
  
cRet := cRet + "%C"  
  
return cret
```

**Saiba mais**[X3Picture - Máscara do campo](https://tdn.totvs.com/pages/releaseview.action?pageId=6815019)  
[Picture dos Campos - Dicionário de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=22479526)
